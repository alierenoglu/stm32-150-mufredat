#!/usr/bin/env python3
"""gorevler.json'daki görevleri GitHub reposuna issue olarak açar.

Yaptıkları:
  1. Etiketleri oluşturur (varsa günceller).
  2. Her modül için bir milestone açar (varsa atlar).
  3. Her görev için bir issue açar (aynı görev numarasında issue varsa atlar).

Gereken: GitHub CLI (gh) kurulu ve `gh auth login` yapılmış olmalı.

Kullanım (reponun kök klasöründen):
    python3 scripts/issue_olustur.py --dry-run          # önce ne yapacağını gör
    python3 scripts/issue_olustur.py                    # bu klasörün GitHub reposuna aç
    python3 scripts/issue_olustur.py --repo kullanici/stm32-150
    python3 scripts/issue_olustur.py --sadece 1-15      # yalnızca bu görevler

Tekrar çalıştırmak güvenlidir: var olanları atlar.
"""
import argparse
import json
import re
import shutil
import subprocess
import sys
import time

from _ortak import (veriyi_yukle, issue_basligi, issue_govdesi, etiketler,
                    modul_bul, milestone_basligi)

ETIKET_RENKLERI = {
    "ana": "1f6feb", "mini-uygulama": "8250df", "bitirme": "d1242f",
    "pekistirme": "bf8700", "ileri": "0e8a16",
    "wokwi:evet": "2da44e", "wokwi:kismen": "d4a72c", "wokwi:dene": "a371f7",
    "wokwi:hayir": "cf222e", "wokwi:pc": "6e7781",
}
PARCA_RENGI = "bfdadc"


def gh(args, girdi=None, kontrol=True):
    sonuc = subprocess.run(["gh"] + args, input=girdi, capture_output=True, text=True, encoding="utf-8")
    if kontrol and sonuc.returncode != 0:
        raise RuntimeError(f"gh {' '.join(args[:3])} ... başarısız:\n{sonuc.stderr.strip()}")
    return sonuc


def gh_tekrarli(args, girdi=None, deneme=3):
    """GitHub'ın ikincil hız sınırına takılırsa bekleyip yeniden dener."""
    for i in range(deneme):
        try:
            return gh(args, girdi)
        except RuntimeError as e:
            metin = str(e).lower()
            if i < deneme - 1 and ("rate limit" in metin or "abuse" in metin or "502" in metin):
                bekle = 60 * (i + 1)
                print(f"  hız sınırı, {bekle} sn bekleniyor...")
                time.sleep(bekle)
                continue
            raise


def aralik_coz(metin):
    secilen = set()
    for parca in metin.split(","):
        parca = parca.strip()
        if "-" in parca:
            a, b = parca.split("-")
            secilen.update(range(int(a), int(b) + 1))
        elif parca:
            secilen.add(int(parca))
    return secilen


def tum_etiketler(veri):
    e = {}
    for t in veri["turler"].values():
        e[t["etiket"]] = f"Görev türü: {t['ad']}"
    for w in veri["wokwi"].values():
        e[w["etiket"]] = w["ad"]
    for p in veri["parcalar"].values():
        if p["etiket"]:
            e[p["etiket"]] = f"Gerekli parça: {p['ad']}"[:100]
    return e


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--repo", help="sahip/repo (verilmezse bulunulan klasörün reposu)")
    ap.add_argument("--dry-run", action="store_true", help="GitHub'a dokunmadan ne yapılacağını yazdır")
    ap.add_argument("--sadece", default="1-15", help="yalnızca bu görevler, ör. 1-15 ya da 1,5,10-20")
    ap.add_argument("--bekleme", type=float, default=1.0, help="issue'lar arası bekleme (sn), varsayılan 1")
    args = ap.parse_args()

    veri = veriyi_yukle()
    gorevler = veri["gorevler"]
    if args.sadece:
        secilen = aralik_coz(args.sadece)
        gecerli = {t["no"] for t in gorevler}
        if not secilen or secilen - gecerli:
            sys.exit("Geçerli görev aralığı 1–150 olmalı.")
        gorevler = [t for t in gorevler if t["no"] in secilen]
    if args.bekleme < 0:
        sys.exit("Bekleme negatif olamaz.")

    if args.dry_run:
        print(f"[dry-run] {len(tum_etiketler(veri))} etiket, {len(veri['moduller'])} milestone, "
              f"{len(gorevler)} issue oluşturulacak.\n")
        for t in gorevler[:3]:
            m = modul_bul(veri, t["modul"])
            print("=" * 70)
            print("Başlık   :", issue_basligi(t))
            print("Milestone:", milestone_basligi(m))
            print("Etiketler:", ", ".join(etiketler(veri, t)))
            print("-" * 70)
            print(issue_govdesi(veri, t))
        if len(gorevler) > 3:
            print("=" * 70)
            print(f"... ve {len(gorevler) - 3} issue daha.")
        return

    if not shutil.which("gh"):
        sys.exit("GitHub CLI (gh) bulunamadı. https://cli.github.com adresinden kur, sonra `gh auth login` yap.")
    if gh(["auth", "status"], kontrol=False).returncode != 0:
        sys.exit("gh oturumu yok. Önce `gh auth login` çalıştır.")

    repo = args.repo or gh(["repo", "view", "--json", "nameWithOwner", "-q", ".nameWithOwner"]).stdout.strip()
    print("Repo:", repo)

    # 1) Etiketler
    print("\nEtiketler...")
    for ad, aciklama in tum_etiketler(veri).items():
        renk = ETIKET_RENKLERI.get(ad, PARCA_RENGI)
        gh_tekrarli(["label", "create", ad, "--repo", repo, "--color", renk,
                     "--description", aciklama, "--force"])
        print("  ✓", ad)

    # 2) Milestone'lar
    print("\nMilestone'lar...")
    mevcut = json.loads(gh(["api", f"repos/{repo}/milestones?state=all&per_page=100"]).stdout)
    mevcut_basliklar = {m["title"] for m in mevcut}
    for m in veri["moduller"]:
        baslik = milestone_basligi(m)
        if baslik in mevcut_basliklar:
            print("  = var:", baslik)
            continue
        gh_tekrarli(["api", f"repos/{repo}/milestones", "-f", f"title={baslik}",
                     "-f", f"description={m['aciklama'][:250]}"])
        print("  ✓", baslik)

    # 3) Issue'lar
    print("\nIssue'lar...")
    var_olan = json.loads(gh(["issue", "list", "--repo", repo, "--state", "all", "--limit", "1000",
                              "--json", "title"]).stdout)
    var_olan = {int(m[1]) for i in var_olan if (m := re.match(r"^\[(\d{3})\]", i["title"]))}
    acilan, atlanan, hatali = 0, 0, []
    for t in gorevler:
        baslik = issue_basligi(t)
        if t["no"] in var_olan:
            atlanan += 1
            continue
        m = modul_bul(veri, t["modul"])
        komut = ["issue", "create", "--repo", repo, "--title", baslik, "--body-file", "-",
                 "--milestone", milestone_basligi(m)]
        for e in etiketler(veri, t):
            komut += ["--label", e]
        try:
            gh_tekrarli(komut, girdi=issue_govdesi(veri, t))
            acilan += 1
            var_olan.add(t["no"])
            print("  ✓", baslik)
        except RuntimeError as e:
            hatali.append(t["no"])
            print("  ✗", baslik, "\n   ", e)
        time.sleep(args.bekleme)

    print(f"\nBitti: {acilan} açıldı, {atlanan} zaten vardı, {len(hatali)} hata.")
    if hatali:
        print("Hatalı görevleri tekrar denemek için:",
              f"python3 scripts/issue_olustur.py --sadece {','.join(map(str, hatali))}")
        sys.exit(1)


if __name__ == "__main__":
    main()
