"""Scriptlerin ortak kullandığı yardımcılar: görev verisini okuma ve metin üretme."""
import json
import re
from pathlib import Path

KOK = Path(__file__).resolve().parent.parent
VERI_DOSYASI = KOK / "gorevler.json"

_TR = str.maketrans("çğıöşüÇĞİÖŞÜ²³", "cgiosuCGIOSU23")


def veriyi_yukle(yol=VERI_DOSYASI):
    with open(yol, encoding="utf-8") as f:
        return json.load(f)


def slug(metin, uzunluk=48):
    s = metin.translate(_TR).lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s[:uzunluk].rstrip("-")


def klasor_adi(gorev):
    return f"{gorev['no']:03d}-{slug(gorev['baslik'])}"


def issue_basligi(gorev):
    return f"[{gorev['no']:03d}] {gorev['baslik']}"


def modul_bul(veri, no):
    for m in veri["moduller"]:
        if m["no"] == no:
            return m
    raise KeyError(no)


def milestone_basligi(modul):
    return f"{modul['kod']} - {modul['ad']}"


def gerekenler_metni(veri, gorev):
    """Her gereksinim satırını okunur metne çevirir. 'A/B' -> 'A veya B'."""
    satirlar = []
    for tok in gorev["gerekenler"]:
        adlar = [veri["parcalar"][kod]["ad"] for kod in tok.split("/")]
        satirlar.append(" veya ".join(adlar))
    return satirlar


def gerekenler_kisa(veri, gorev):
    p = veri["parcalar"]
    parcalar = [" veya ".join(p[k]["kisa"] for k in tok.split("/")) for tok in gorev["gerekenler"]]
    return ", ".join(parcalar) or "—"


def onkosul_metni(gorev):
    if not gorev["onkosul"]:
        return "—"
    return ", ".join(f"{n:03d}" for n in gorev["onkosul"])


def etiketler(veri, gorev):
    e = [veri["turler"][gorev["tur"]]["etiket"], veri["wokwi"][gorev["wokwi"]]["etiket"]]
    for tok in gorev["gerekenler"]:
        if "/" in tok:  # alternatifi olan parça zorunlu sayılmaz
            continue
        et = veri["parcalar"][tok]["etiket"]
        if et and et not in e:
            e.append(et)
    return e


def wokwi_metni(veri, gorev):
    w = veri["wokwi"][gorev["wokwi"]]
    s = f"{w['kisa']} {w['ad']}"
    if gorev.get("wokwi_not"):
        s += f". {gorev['wokwi_not']}"
    return s


def issue_govdesi(veri, gorev):
    modul = modul_bul(veri, gorev["modul"])
    tur = veri["turler"][gorev["tur"]]["ad"]
    satir = []
    satir.append(f"**{modul['kod']} · {modul['ad']}** · {tur}")
    satir.append(f"**Önkoşul:** {onkosul_metni(gorev)}")
    satir.append(f"**Simülasyon:** {wokwi_metni(veri, gorev)}")
    satir.append("")
    satir.append("### Amaç")
    satir.append(gorev["amac"])
    satir.append("")
    satir.append("### Araştır")
    satir += [f"- {a}" for a in gorev["arastir"]]
    satir.append("")
    satir.append("### Gerekenler")
    g = gerekenler_metni(veri, gorev)
    satir += [f"- {x}" for x in g] if g else ["- Kart gerekmez"]
    satir.append("")
    satir.append("### Başarı ölçütü")
    satir += [f"- [ ] {b}" for b in gorev["basari"]]
    if gorev.get("not"):
        satir += ["", f"> {gorev['not']}"]
    satir.append("")
    satir.append("### Teslim")
    satir.append(f"- [ ] Kod ve rapor `cozumler/{klasor_adi(gorev)}/` klasöründe (şablon: `cozumler/_sablon/README.md`)")
    satir.append("- [ ] Raporda kanıt var: ekran görüntüsü, video, log ya da grafik")
    satir.append("- [ ] Raporda “Öğrendiklerim” bölümü dolu")
    satir.append("- [ ] PR açıklamasında `Closes #<bu issue'nun numarası>` yazıyor")
    return "\n".join(satir)
