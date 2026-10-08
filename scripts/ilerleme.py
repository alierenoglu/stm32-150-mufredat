#!/usr/bin/env python3
"""GitHub issue'larından benzersiz ve completed görev sayısını okur. Salt okunur."""
import argparse
import json
import re
import subprocess
import sys
from _ortak import veriyi_yukle


def say(veri, issues):
    gecerli = {t['no'] for t in veri['gorevler']}
    acilan, biten = set(), set()
    for i in issues:
        if 'pull_request' in i:
            continue
        m = re.match(r'^\[(\d{3})\]', i.get('title', ''))
        if not m or int(m[1]) not in gecerli:
            continue
        n = int(m[1])
        acilan.add(n)
        if i.get('state') == 'closed' and i.get('state_reason') == 'completed':
            biten.add(n)
    return [f"{len(biten & set(range(m['aralik'][0], m['aralik'][1]+1)))}/{m['aralik'][1]-m['aralik'][0]+1}" for m in veri['moduller']] + [f'{len(biten & set(range(1,101)))}/100', str(len(acilan))]


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('repolar',nargs='*');ap.add_argument('--dosya');ap.add_argument('--markdown',action='store_true')
    a=ap.parse_args();repolar=list(a.repolar)
    if a.dosya:
        with open(a.dosya,encoding='utf-8') as f:
            repolar.extend(s.strip() for s in f if s.strip() and not s.lstrip().startswith('#'))
    repolar=list(dict.fromkeys(repolar))
    if not repolar:sys.exit('ekip.txt içine kullanici/repo ekle veya komutta repo belirt.')
    v=veriyi_yukle();rows=[];failed=False
    for repo in repolar:
        if not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+',repo):sys.exit('Geçersiz sahip/repo: '+repo)
        try:
            p=subprocess.run(['gh','api',f'repos/{repo}/issues?state=all&per_page=100','--paginate','--slurp'],capture_output=True,text=True,check=True)
            pages=json.loads(p.stdout);issues=[i for page in pages for i in page]
            rows.append([repo]+say(v,issues))
        except (OSError,subprocess.CalledProcessError,ValueError) as e:
            print(f'{repo}: okunamadı ({type(e).__name__})',file=sys.stderr);failed=True
            rows.append([repo]+['?']*(len(v['moduller'])+2))
    head=['Repo']+[m['kod'] for m in v['moduller']]+['Ana tamamlanan','Açılmış görev']
    if a.markdown:
        print('| '+' | '.join(head)+' |');print('|'+'---|'*len(head))
        for row in rows:print('| '+' | '.join(row)+' |')
    else:
        for row in [head]+rows:print('\t'.join(row))
    if failed:sys.exit(1)

if __name__=='__main__':main()
