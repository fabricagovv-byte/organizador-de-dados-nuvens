import json, collections
D = '../mgterr-dl'
mun = json.load(open(f'{D}/mun.json'))
pop = {s['localidade']['id']: int(s['serie']['2022']) for s in json.load(open(f'{D}/pop.json'))[0]['resultados'][0]['series']}
pib = {}
for v in json.load(open(f'{D}/pib.json')):
    for s in v['resultados'][0]['series']:
        val = list(s['serie'].values())[0]
        pib.setdefault(s['localidade']['id'], {})[v['id']] = float(val) * 1000 if val not in ('-', '...', 'X', None) else 0.0
for v in json.load(open(f'{D}/set22.json')):
    for s_ in v['resultados'][0]['series']:
        val = list(s_['serie'].values())[0]
        pib.setdefault(s_['localidade']['id'], {})[v['id']] = float(val) * 1000 if val not in ('-', '...', 'X', None) else 0.0
M = []
for m in mun:
    i = str(m['id']); ri = m['regiao-imediata']; rt = ri['regiao-intermediaria']
    p = pib.get(i, {})
    M.append(dict(id=i, nome=m['nome'], imediata=ri['nome'], inter=rt['nome'], pop=pop.get(i, 0), pib=p.get('37', 0), agro=p.get('513', 0), ind=p.get('517', 0), serv=p.get('6575', 0), adm=p.get('525', 0)))
T = collections.OrderedDict()
for m in M:
    t = T.setdefault(m['inter'], dict(nome=m['inter'], mun=0, pop=0, pib=0, agro=0, ind=0, serv=0, adm=0, imediatas=set(), cidades=[]))
    t['mun'] += 1
    for k in ('pop','pib','agro','ind','serv','adm'): t[k] += m[k]
    t['imediatas'].add(m['imediata']); t['cidades'].append(m)
for t in T.values():
    t['imediatas'] = sorted(t['imediatas']); t['cidades'].sort(key=lambda c: -c['pop'])
    t['percap'] = t['pib'] / t['pop']; vab = t['agro'] + t['ind'] + t['serv'] + t['adm']
    t['sh'] = {k: t[k] / vab for k in ('agro','ind','serv','adm')}
    t['ate20'] = sum(1 for c in t['cidades'] if c['pop'] <= 20000)
TOT = dict(pop=sum(m['pop'] for m in M), pib=sum(m['pib'] for m in M), mun=len(M))
if __name__ == '__main__':
    print(TOT)
    for t in sorted(T.values(), key=lambda t: -t['pib']):
        print(f"{t['nome']:28s} mun {t['mun']:3d} pop {t['pop']/1e6:5.2f} mi pib {t['pib']/1e9:6.1f} bi percap {t['percap']/1000:5.1f} mil  agro {t['sh']['agro']*100:4.1f} ind {t['sh']['ind']*100:4.1f} serv {t['sh']['serv']*100:4.1f} adm {t['sh']['adm']*100:4.1f} | {', '.join(c['nome'] for c in t['cidades'][:3])}")
