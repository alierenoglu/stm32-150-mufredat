#!/usr/bin/env python3
"""gorevler.json'dan okunur dosyaları üretir:

  GOREVLER.md            bütün görevlerin özet tablosu
  gorevler/Mxx-*.md      her modülün ayrıntılı görev açıklamaları

Görevleri değiştirmek için gorevler.json'u düzenle ve bu scripti çalıştır:
    python3 scripts/md_uret.py
"""

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
    L.append(f"Görevler {a:03d}–{b:03d} · [Tüm görevler](../GOREVLER.md)")
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


def yaz(yol, icerik):
    yol.parent.mkdir(parents=True, exist_ok=True)
    yol.write_text(icerik, encoding="utf-8")
    print("yazıldı:", yol.relative_to(KOK))


def main():
    veri = veriyi_yukle()
    yaz(KOK / "GOREVLER.md", ozet_uret(veri))
    for m in veri["moduller"]:
        yaz(KOK / "gorevler" / modul_dosyasi(m), modul_uret(veri, m))


if __name__ == "__main__":
    main()
