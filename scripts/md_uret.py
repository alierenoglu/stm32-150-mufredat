#!/usr/bin/env python3
"""gorevler.json'dan okunur dosyaları üretir:

  GOREVLER.md            bütün görevlerin özet tablosu
  gorevler/Mxx-*.md      her modülün ayrıntılı görev açıklamaları
  docs/malzeme.md        parça listesi ve hangi görevde gerektiği

Görevleri değiştirmek için gorevler.json'u düzenle ve bu scripti çalıştır:
    python3 scripts/md_uret.py
"""
from collections import OrderedDict

from _ortak import (KOK, veriyi_yukle, slug, gerekenler_metni, gerekenler_kisa,
                    onkosul_metni, wokwi_metni)

UYARI = "<!-- Bu dosya scripts/md_uret.py ile üretildi. Elle düzenleme; gorevler.json'u düzenle. -->\n"


def modul_dosyasi(m):
    return f"{m['kod']}-{slug(m['ad'])}.md"


def gorevler_modulde(veri, m):
    a, b = m["aralik"]
    return [t for t in veri["gorevler"] if a <= t["no"] <= b]


def lejant(veri):
    s = ["**Simülasyon (Wokwi, Blue Pill F103):** "]
    s.append(" · ".join(f"{w['kisa']} {w['ad']}" for w in veri["wokwi"].values()))
    s.append("  \nAyrıntı: [docs/simulasyon.md](docs/simulasyon.md)")
    return "".join(s)


def ozet_uret(veri):
    L = [UYARI, "# Görev Listesi", ""]
    L.append("100 ana görev sırayla ilerler; her beşinci görev önceki görevleri birleştiren bir mini uygulamadır. "
             "96–100 bitirme projesidir. 101–125 pekiştirme ve 126–150 ileri görevler zorunlu değildir; "
             "önkoşulunu bitirdiğin anda yapabilirsin.")
    L.append("")
    L.append(lejant(veri))
    L.append("")
    L.append("| Modül | Görevler | Konu |")
    L.append("|---|---|---|")
    for m in veri["moduller"]:
        a, b = m["aralik"]
        L.append(f"| [{m['kod']}](gorevler/{modul_dosyasi(m)}) | {a:03d}–{b:03d} | {m['ad']} |")
    L.append("")
    for m in veri["moduller"]:
        L.append(f"## {m['kod']} · {m['ad']}")
        L.append("")
        L.append(m["aciklama"])
        L.append("")
        L.append("| No | Görev | Tür | Gerekenler | Wokwi |")
        L.append("|---|---|---|---|---|")
        for t in gorevler_modulde(veri, m):
            tur = veri["turler"][t["tur"]]["ad"]
            link = f"gorevler/{modul_dosyasi(m)}#g{t['no']:03d}"
            L.append(f"| {t['no']:03d} | [{t['baslik']}]({link}) | {tur} | {gerekenler_kisa(veri, t)} | "
                     f"{veri['wokwi'][t['wokwi']]['kisa']} |")
        L.append("")
    return "\n".join(L)


def modul_uret(veri, m):
    a, b = m["aralik"]
    L = [UYARI, f"# {m['kod']} · {m['ad']}", ""]
    L.append(f"Görevler {a:03d}–{b:03d} · [Tüm görevler](../GOREVLER.md) · "
             f"[Simülasyon rehberi](../docs/simulasyon.md)")
    L.append("")
    L.append(m["aciklama"])
    for t in gorevler_modulde(veri, m):
        tur = veri["turler"][t["tur"]]["ad"]
        L.append("")
        L.append("---")
        L.append("")
        L.append(f'<a id="g{t["no"]:03d}"></a>')
        L.append("")
        L.append(f"## {t['no']:03d} · {t['baslik']}")
        L.append("")
        L.append(f"`{tur}` · Önkoşul: {onkosul_metni(t)}")
        L.append("")
        L.append(f"**Amaç.** {t['amac']}")
        L.append("")
        L.append("**Araştır:** " + " · ".join(t["arastir"]))
        L.append("")
        g = gerekenler_metni(veri, t)
        L.append("**Gerekenler:** " + ("; ".join(g) if g else "Kart gerekmez"))
        L.append("")
        L.append("**Başarı ölçütü**")
        L.append("")
        L += [f"- {x}" for x in t["basari"]]
        L.append("")
        L.append(f"**Simülasyon:** {wokwi_metni(veri, t)}")
        if t.get("not"):
            L.append("")
            L.append(f"> {t['not']}")
    L.append("")
    return "\n".join(L)


def malzeme_uret(veri):
    kullanim = OrderedDict((k, {"zorunlu": [], "alternatifli": []}) for k in veri["parcalar"])
    for t in veri["gorevler"]:
        for tok in t["gerekenler"]:
            kodlar = tok.split("/")
            anahtar = "alternatifli" if len(kodlar) > 1 else "zorunlu"
            for k in kodlar:
                kullanim[k][anahtar].append(t["no"])
    L = [UYARI, "# Malzeme Listesi", ""]
    L.append("Her parçanın ilk gerektiği görev ve kaç görevde kullanıldığı. "
             "“Alternatifli” görevlerde parça yerine başka bir seçenek de kullanılabilir "
             "(ör. motor yerine 069'daki sanal motor).")
    L.append("")
    L.append("| Kod | Parça | İlk görev | Zorunlu olduğu görev sayısı | Alternatifli görev sayısı |")
    L.append("|---|---|---|---|---|")
    for k, p in veri["parcalar"].items():
        z, alt = kullanim[k]["zorunlu"], kullanim[k]["alternatifli"]
        hepsi = sorted(z + alt)
        ilk = f"{hepsi[0]:03d}" if hepsi else "—"
        L.append(f"| {k} | {p['ad']} | {ilk} | {len(z)} | {len(alt)} |")
    L.append("")
    L.append("## Hangi görev hangi parçayı istiyor")
    L.append("")
    for k, p in veri["parcalar"].items():
        z, alt = kullanim[k]["zorunlu"], kullanim[k]["alternatifli"]
        if (not z and not alt) or k == "KART":
            continue
        L.append(f"- **{p['kisa']}** — zorunlu: {', '.join(f'{n:03d}' for n in z) or '—'}"
                 + (f"; alternatifli: {', '.join(f'{n:03d}' for n in alt)}" if alt else ""))
    L.append("")
    return "\n".join(L)


def yaz(yol, icerik):
    yol.parent.mkdir(parents=True, exist_ok=True)
    yol.write_text(icerik, encoding="utf-8")
    print("yazıldı:", yol.relative_to(KOK))


def main():
    veri = veriyi_yukle()
    yaz(KOK / "GOREVLER.md", ozet_uret(veri))
    for m in veri["moduller"]:
        yaz(KOK / "gorevler" / modul_dosyasi(m), modul_uret(veri, m))
    yaz(KOK / "docs" / "malzeme.md", malzeme_uret(veri))


if __name__ == "__main__":
    main()
