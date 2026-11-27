# Cards de oportunidades DigitalGov: licitações abertas (propostas a partir de 30/11/2026) em digitalização e software.
import json, re, unicodedata, base64, os, csv, datetime, html as H
D = '../opp'
def norm(s): return unicodedata.normalize('NFKD', (s or '').lower()).encode('ascii','ignore').decode()
def b64(p, mime='image/png'): return f'data:{mime};base64,' + base64.b64encode(open(p,'rb').read()).decode()
LOGO = b64('logo.png')
ops = json.load(open(f'{D}/oportunidades.json')); det = json.load(open(f'{D}/detalhes.json'))
if os.path.exists(f'{D}/detalhes2.json'): det.update(json.load(open(f'{D}/detalhes2.json')))
HOJE = datetime.date(2026, 11, 27); INICIO = '2026-11-30'
DIAS = ['seg','ter','qua','qui','sex','sáb','dom']
SW_IT = r'software|sistema|licen|desenvolv|plataforma|aplicativo|implant|hospedagem|nuvem|ged\b|gestao eletronica|banco de dados|modulo'
DG_IT = r'digitaliz|indexa|gestao documental|gestao eletronica de document|ged\b|arquiv|higieniz|microfilm|organizacao de document|tratamento documental'
EQUIP = r'scanner|computador|notebook|impressora|monitor|nobreak|toner|cartucho|mouse|teclado|tablet|smartphone|servidor rack|switch'
OUT = []
for o in ops:
    c = det.get(o['link'])
    if not c or not c.get('det'): continue
    d = c['det']; its = c.get('itens') or []
    fim = (d.get('dataEncerramentoProposta') or '')[:10]
    if not fim or fim < INICIO: continue
    sit = norm(d.get('situacaoCompraNome'))
    if re.search(r'revog|anulad|suspens|deserta|fracassad', sit): continue
    obj = (d.get('objetoCompra') or o['objeto'] or '').strip()
    txt = norm(obj + ' ' + ' '.join((i.get('desc') or '') for i in its))
    it_txt = [norm(i.get('desc')) for i in its]
    servicos = [i for i in its if norm(i.get('me')).startswith('serv')]
    if o['cat'].startswith('Digit'):
        rel = [i for i, t in zip(its, it_txt) if re.search(DG_IT, t) and not re.search(EQUIP, t)]
        if not rel and not (re.search(DG_IT, norm(obj)) and servicos): continue
    else:
        rel = [i for i, t in zip(its, it_txt) if re.search(SW_IT, t) and not re.search(EQUIP, t)]
        if not rel and not (re.search(SW_IT, norm(obj)) and servicos and not re.search(EQUIP, norm(obj))): continue
    if re.search(r'curso|capacitacao|treinamento de servidores', norm(obj)) and not rel: continue
    imp = sum(1 for t in it_txt if re.search(r'impress|copia|reprograf|outsourcing', t))
    if imp and imp >= len(it_txt) / 2 and not any(re.search(r'digitaliz|indexa|software|sistema', t) for t in it_txt): continue
    if re.search(r'outsourcing de impress|locacao de (impressoras|equipamentos de impress)', norm(obj)) and not rel: continue
    rel = rel or its
    u = d.get('unidadeOrgao') or {}
    val = d.get('valorTotalEstimado') or sum((i.get('vt') or 0) for i in its) or 0
    OUT.append(dict(cat=o['cat'], orgao=(d.get('orgaoEntidade') or {}).get('razaoSocial') or o['orgao'], unidade=u.get('nomeUnidade') or o['unidade'],
        cidade=u.get('municipioNome') or o['cidade'], uf=u.get('ufSigla') or o['uf'], ibge=str(u.get('codigoIbge') or o['ibge'] or ''),
        modalidade=d.get('modalidadeNome') or o['modalidade'], disputa=d.get('modoDisputaNome'), fim=d.get('dataEncerramentoProposta'), abertura=d.get('dataAberturaProposta'),
        valor=val, sigiloso=bool(d.get('orcamentoSigilosoCodigo') and d.get('orcamentoSigilosoCodigo') != 1) and not val, objeto=obj, srp=d.get('srp'),
        link=o['link'], origem=d.get('linkSistemaOrigem') or o.get('origem'), numero=d.get('numeroCompra'), processo=d.get('processo'),
        itens=[dict(desc=(i.get('desc') or '').strip(), qtd=i.get('qtd'), un=i.get('un'), vt=i.get('vt')) for i in rel[:4]], n_itens=len(its)))
FORA = r'servicos de impressao|aquisicao de acervo bibliografico|telessaude|reconhecimento facial|dispositivos de reconhecimento|antivirus|windows server|sql server|microsoft|adobe|autocad|licencas de uso da ferramenta|pacote corporativo de ferramentas'
vistos = set(); LIMPO = []
for o in sorted(OUT, key=lambda x: x['fim']):
    if re.search(FORA, norm(o['objeto'])): continue
    if o['valor'] and o['valor'] < 100: o['valor'] = 0
    k = (norm(o['orgao']), round(o['valor'])) if o['valor'] else (norm(o['orgao']), re.sub(r'^\[[^\]]*\]\s*-?\s*', '', norm(o['objeto']))[:80])
    if k in vistos: continue
    vistos.add(k); LIMPO.append(o)
OUT = LIMPO
print('oportunidades', len(OUT))

brl = lambda v: 'R$ ' + f'{v:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')
def brlk(v):
    if v >= 1e6: return 'R$ ' + f'{v/1e6:,.2f}'.replace('.', ',') + ' mi'
    return 'R$ ' + f'{v:,.0f}'.replace(',', '.')
fmtq = lambda v: (f'{v:,.0f}'.replace(',', '.') if float(v or 0).is_integer() else f'{v:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')) if v else '—'
def dt(s):
    d = datetime.date.fromisoformat(s[:10]); return d, f'{d.day:02d}/{d.month:02d}', DIAS[d.weekday()], s[11:16]
def bras(o):
    p = f'../brasoes/png/{o["ibge"]}.png'
    if o['ibge'] and os.path.exists(p): return f'<img src="{b64(p)}" alt="Brasão de {H.escape(o["cidade"])}" style="width:84px; height:96px; object-fit:contain">'
    return f'<div style="width:84px; height:96px; border-radius:12px; background:var(--soft); display:grid; place-items:center; text-align:center"><span class="H" style="font-size:30px; color:var(--navy)">{o["uf"]}</span></div>'

# planilha
with open('Oportunidades-DigitalGov.csv', 'w', newline='', encoding='utf-8-sig') as f:
    w = csv.writer(f, delimiter=';')
    w.writerow(['Prazo da proposta','Categoria','Órgão','Unidade','Cidade','UF','Modalidade','Valor estimado (R$)','Objeto','Itens principais','Link PNCP','Sistema de origem'])
    for o in OUT:
        w.writerow([o['fim'][:16].replace('T',' '), o['cat'], o['orgao'], o['unidade'], o['cidade'], o['uf'], o['modalidade'], f"{o['valor']:.2f}".replace('.',','), o['objeto'],
                    ' | '.join(f"{i['desc'][:80]} ({fmtq(i['qtd'])} {i['un'] or ''})" for i in o['itens']), o['link'], o['origem'] or ''])

CSS = '''
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Anton&family=Poppins:wght@400;500;600;700;800&family=IBM+Plex+Mono:wght@500&display=swap">
<style>
/* Identidade do logo DigitalGov: azul-marinho do nome, mosaico colorido do D (ciano, magenta, laranja, verde). */
:root{ --paper:#F7F8FC; --grid:rgba(36,48,94,.05); --navy:#2F3C60; --ink:#1C2440; --muted:#5D6580; --line:rgba(36,48,94,.12); --soft:#E8ECF6;
  --ciano:#1BA6E0; --ciano-bg:#DDF2FB; --mag:#E6197F; --mag-bg:#FCE0EE; --lar:#F7941D; --lar-bg:#FEEDD8; --verde:#7CB342; --verde-bg:#E9F4DC; --card:#FFFFFF;
  --fh:"Anton", "Impact", "Arial Narrow", sans-serif; --fb:"Poppins", "Segoe UI", Arial, sans-serif; --fm:"IBM Plex Mono", monospace; }
@page{ size:1080px 1350px; margin:0 }
*{box-sizing:border-box; margin:0; padding:0}
body{font-family:var(--fb); color:var(--ink); -webkit-print-color-adjust:exact; print-color-adjust:exact; background:var(--paper)}
.p{width:1080px; height:1350px; position:relative; overflow:hidden; page-break-after:always; break-after:page; background-color:var(--paper);
   background-image:linear-gradient(var(--grid) 1px, transparent 1px), linear-gradient(90deg, var(--grid) 1px, transparent 1px); background-size:36px 36px; padding:120px 70px 0}
.p:last-child{page-break-after:auto}
.H{font-family:var(--fh); font-weight:400; text-transform:uppercase}
.H > span{display:block; line-height:1.0}
.top{position:absolute; left:70px; right:70px; top:34px; display:flex; justify-content:space-between; align-items:center}
.top img{height:54px}
.top span{font-family:var(--fm); font-size:14px; letter-spacing:.1em; color:var(--muted); text-transform:uppercase}
.mosaic{position:absolute; left:0; right:0; top:0; height:10px; display:flex}
.mosaic i{flex:1}
.foot{position:absolute; left:70px; right:70px; bottom:34px; display:flex; justify-content:space-between; font-size:14px; color:var(--muted)}
.card{background:var(--card); border-radius:18px; box-shadow:0 1px 0 rgba(36,48,94,.06), 0 12px 30px -20px rgba(36,48,94,.45); border:1px solid rgba(36,48,94,.07)}
.num{font-family:var(--fh); line-height:.95; font-variant-numeric:tabular-nums}
.op{display:grid; grid-template-columns:96px 1fr 220px; gap:18px; padding:18px 22px; position:relative; overflow:hidden}
.op .bar{position:absolute; left:0; top:0; bottom:0; width:8px}
.tag{display:inline-block; font-weight:700; font-size:12.5px; padding:4px 10px; border-radius:999px; letter-spacing:.02em}
.obj{font-size:15px; line-height:1.4; color:var(--ink); margin-top:8px; display:-webkit-box; -webkit-line-clamp:2; -webkit-box-orient:vertical; overflow:hidden}
.it{font-size:13px; color:var(--muted); margin-top:3px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis}
.lnk{display:inline-block; margin-top:10px; font-family:var(--fm); font-size:12px; color:var(--navy); text-decoration:none; background:var(--soft); padding:6px 10px; border-radius:8px}
.side{border-left:1px dashed var(--line); padding-left:18px; display:grid; align-content:start; gap:10px}
.lab{font-family:var(--fm); font-size:11.5px; letter-spacing:.08em; text-transform:uppercase; color:var(--muted)}
</style>'''
MOS = '<div class="mosaic">' + ''.join(f'<i style="background:{c}"></i>' for c in ['#1BA6E0','#2F3C60','#E6197F','#F7941D','#7CB342','#8E44AD','#E53935','#1BA6E0','#F7941D','#E6197F']) + '</div>'
N = [0]
def page(inner, rot):
    N[0] += 1
    return f'<section class="p">{MOS}<div class="top"><img src="{LOGO}" alt="DigitalGov"><span>{rot}</span></div>{inner}<div class="foot"><span>Fonte: PNCP · consulta em 27/11/2026 · confira o edital antes de participar</span><span>{N[0]:02d}</span></div></section>'
def card(o):
    d, dm, wd, hh = dt(o['fim']); faltam = (d - HOJE).days
    dig = o['cat'].startswith('Digit'); cor = '#1BA6E0' if dig else '#E6197F'; bg = 'var(--ciano-bg)' if dig else 'var(--mag-bg)'
    urg = faltam <= 7
    its = ''.join(f'<p class="it">• {H.escape(i["desc"][:90])} — {fmtq(i["qtd"])} {H.escape(i["un"] or "")}</p>' for i in o['itens'][:1])
    val = brl(o['valor']) if o['valor'] else 'Sigiloso ou não informado'
    return f'''<div class="card op"><span class="bar" style="background:{cor}"></span>
  <div style="display:grid; justify-items:center; gap:8px">{bras(o)}<span class="tag" style="background:var(--soft); color:var(--navy)">{H.escape(o["uf"])}</span></div>
  <div style="min-width:0">
    <span class="tag" style="background:{bg}; color:{cor}">{"Digitalização de documentos" if dig else "Software"}</span> <span class="tag" style="background:var(--soft); color:var(--navy)">{H.escape(o["modalidade"] or "")}{" · registro de preço" if o["srp"] else ""}</span>
    <p style="font-size:21px; font-weight:800; margin-top:8px; line-height:1.15">{H.escape(o["cidade"])} <span style="font-weight:500; color:var(--muted)">· {H.escape(o["uf"])}</span></p>
    <p style="font-size:14px; color:var(--muted); margin-top:2px">{H.escape(o["orgao"].title())}</p>
    <p class="obj">{H.escape(o["objeto"][:330])}</p>
    {its}
    <a class="lnk" href="{o["link"]}">{o["link"].replace("https://","")}</a>
  </div>
  <div class="side">
    <div><p class="lab">Valor estimado</p><p class="num" style="font-size:{30 if o["valor"] else 18}px; color:var(--navy); margin-top:4px">{val}</p></div>
    <div><p class="lab">Prazo da proposta</p><p class="num" style="font-size:34px; color:{"#E53935" if urg else "var(--ink)"}; margin-top:4px">{dm} <span style="font-size:20px">{wd}</span></p><p style="font-size:13px; color:var(--muted)">até {hh} · faltam {faltam} dias</p></div>
    <div><p class="lab">Itens</p><p style="font-size:15px; font-weight:700">{o["n_itens"]} no edital</p></div>
  </div>
</div>'''

P = []
# CAPA
tot = sum(o['valor'] for o in OUT); nd = sum(1 for o in OUT if o['cat'].startswith('Digit')); ns = len(OUT) - nd
vd = sum(o['valor'] for o in OUT if o['cat'].startswith('Digit')); vs = tot - vd
from collections import Counter
uf = Counter(o['uf'] for o in OUT).most_common(8)
sem = Counter()
for o in OUT:
    d = datetime.date.fromisoformat(o['fim'][:10]); seg = d - datetime.timedelta(days=d.weekday()); sem[seg] += 1
N[0] += 1
P.append(f'''<section class="p" style="padding:0; background:#fff; background-image:none">{MOS}
  <div style="position:absolute; left:70px; top:90px"><img src="{LOGO}" alt="DigitalGov" style="height:150px"></div>
  <div style="position:absolute; left:70px; right:70px; top:330px">
    <p style="font-family:var(--fm); font-size:16px; letter-spacing:.12em; color:var(--mag)">OPORTUNIDADES · PROPOSTAS A PARTIR DE 30/11/2026</p>
    <h1 class="H" style="font-size:118px; margin-top:34px; color:var(--navy)"><span>Licitações</span><span style="color:var(--ciano)">abertas</span></h1>
    <p style="font-size:24px; margin-top:16px; max-width:860px">Digitalização de documentos e software para órgãos públicos de todo o Brasil, com órgão, cidade, itens, valor, prazo e link.</p>
  </div>
  <div style="position:absolute; left:70px; right:70px; top:760px; display:grid; grid-template-columns:repeat(3,1fr); gap:16px">
    <div class="card" style="padding:24px"><p class="num" style="font-size:64px; color:var(--navy)">{len(OUT)}</p><p style="font-size:16px">oportunidades abertas</p></div>
    <div class="card" style="padding:24px; border-top:6px solid var(--ciano)"><p class="num" style="font-size:64px; color:var(--ciano)">{nd}</p><p style="font-size:16px">digitalização · {brlk(vd)}</p></div>
    <div class="card" style="padding:24px; border-top:6px solid var(--mag)"><p class="num" style="font-size:64px; color:var(--mag)">{ns}</p><p style="font-size:16px">software · {brlk(vs)}</p></div>
  </div>
  <div class="card" style="position:absolute; left:70px; right:70px; top:960px; padding:22px 26px">
    <p class="lab">Valor estimado somado</p><p class="num" style="font-size:72px; color:var(--navy); margin-top:6px">{brlk(tot)}</p>
    <p style="font-size:15px; color:var(--muted); margin-top:6px">Estados com mais oportunidades: {", ".join(f"{u} ({n})" for u, n in uf)}</p>
  </div>
  <p style="position:absolute; left:70px; bottom:40px; font-size:14px; color:var(--muted)">Consulta ao Portal Nacional de Contratações Públicas em 27/11/2026 · cards ordenados pelo prazo da proposta</p>
</section>''')
# COMO LER
semr = ''.join(f'<div style="display:grid; grid-template-columns:220px 1fr 50px; gap:12px; align-items:center; padding:6px 0"><span style="font-size:16px; font-weight:600">Semana de {s.day:02d}/{s.month:02d}</span><span style="height:20px; background:var(--soft); border-radius:0 5px 5px 0; overflow:hidden"><span style="display:block; height:100%; width:{n/max(sem.values())*100:.0f}%; background:var(--ciano)"></span></span><b style="text-align:right">{n}</b></div>' for s, n in sorted(sem.items()))
P.append(page(f'''<h2 class="H" style="font-size:80px; color:var(--navy)"><span>Como usar</span><span style="color:var(--mag)">os cards</span></h2>
  <div class="card" style="margin-top:28px; padding:24px 28px"><p class="lab">Quando vencem as propostas</p><div style="margin-top:10px">{semr}</div></div>
  <div class="card" style="margin-top:16px; padding:24px 28px">
    <p class="lab">Como foram filtradas</p>
    <p style="font-size:17px; margin-top:10px; line-height:1.5">Busca no PNCP de editais com propostas abertas por "digitalização de documentos", "digitalização de acervo", "gestão eletrônica de documentos", "gestão documental", "desenvolvimento de software" e "licenciamento de software de gestão". Ficaram só os que têm prazo de proposta a partir de 30/11/2026, não estão suspensos ou revogados e têm itens de serviço de digitalização ou de software. Compras só de equipamentos (scanner, computador, impressora) e cursos foram retiradas.</p>
  </div>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:14px; margin-top:16px">
    <div class="card" style="padding:20px 24px; border-left:8px solid var(--ciano)"><p style="font-size:17px"><b>Azul</b> = digitalização de documentos</p></div>
    <div class="card" style="padding:20px 24px; border-left:8px solid var(--mag)"><p style="font-size:17px"><b>Magenta</b> = software</p></div>
  </div>
  <div class="card" style="margin-top:14px; padding:20px 24px; background:var(--lar-bg); border:0"><p style="font-size:16px"><b>Prazo em vermelho</b> = vence em até 7 dias. Os brasões vêm do Wikidata; onde não há brasão aparece a sigla do estado. Sempre confira o edital completo no link: prazos podem mudar.</p></div>''', 'Guia'))
# CARDS: 4 por página
for k in range(0, len(OUT), 4):
    grp = OUT[k:k+4]
    d0 = dt(grp[0]['fim'])[1]; d1 = dt(grp[-1]['fim'])[1]
    P.append(page(f'<div style="display:grid; gap:14px">{"".join(card(o) for o in grp)}</div>', f'Propostas de {d0} a {d1}'))
html = '<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Oportunidades DigitalGov</title>' + CSS + '</head><body>' + ''.join(P) + '</body></html>'
open('cards.html', 'w').write(html)
print('paginas', len(P), 'total', tot, nd, ns)
