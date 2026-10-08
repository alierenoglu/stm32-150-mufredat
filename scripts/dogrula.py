#!/usr/bin/env python3
"""Müfredat kimliklerini, önkoşulları, bağlantıları ve üretilebilirliği doğrular."""
import re
import sys
from _ortak import KOK, veriyi_yukle
from md_uret import ozet_uret, modul_uret, modul_dosyasi

def main():
    v=veriyi_yukle();ts=v['gorevler'];ids=[t['no'] for t in ts]
    assert sorted(ids)==list(range(1,151)), '150 benzersiz görev gerekli'
    graph={t['no']:t['onkosul'] for t in ts}
    visiting=set();done=set()
    def visit(n):
        assert n in graph,f'Geçersiz önkoşul {n}'
        assert n not in visiting,f'Önkoşul döngüsü {n}'
        if n in done:return
        visiting.add(n)
        for p in graph[n]:visit(p)
        visiting.remove(n);done.add(n)
    for n in graph:visit(n)
    for t in ts:
        assert t['wokwi'] in v['wokwi']
        assert t['tur'] in v['turler']
        for x in t['gerekenler']:
            assert all(k in v['parcalar'] for k in x.split('/'))
        ms=[m for m in v['moduller'] if m['aralik'][0]<=t['no']<=m['aralik'][1]]
        assert len(ms)==1 and ms[0]['no']==t['modul']
    outputs={'GOREVLER.md':ozet_uret(v)}
    outputs.update({f"gorevler/{modul_dosyasi(m)}":modul_uret(v,m) for m in v['moduller']})
    for name,expected in outputs.items():assert (KOK/name).read_text(encoding='utf-8')==expected,f'Yeniden üret: {name}'
    for f in KOK.rglob('*.md'):
        for link in re.findall(r'\]\(([^)]+)\)',f.read_text(encoding='utf-8')):
            if '://' in link or link.startswith('#'):continue
            path=link.split('#')[0]
            if path:assert (f.parent/path).exists(),f'Kırık bağlantı {f}: {link}'
    print('150 görev, önkoşullar, modüller, üretilen dosyalar ve bağlantılar doğrulandı.')

if __name__=='__main__':main()
