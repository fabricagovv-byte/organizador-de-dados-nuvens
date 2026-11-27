# "Territórios de Minas e consórcios": documento A4 para impressão em preto e branco, com páginas de ligação.
import json, base64, html as H, datetime
import territorios as TT
T = TT.T; TOT = TT.TOT
for t in T.values(): t['nome'] = t['nome'].replace('Juíz de Fora', 'Juiz de Fora')
CONS = json.load(open('../mgterr-dl/consorcios_contatos.json'))
LOGO = 'data:image/png;base64,' + base64.b64encode(open('logo_pb.png','rb').read()).decode()
fmt = lambda v: f'{v:,.0f}'.replace(',', '.')
bi = lambda v: 'R$ ' + f'{v/1e9:,.1f}'.replace('.', ',') + ' bi'
mil = lambda v: 'R$ ' + f'{v/1000:,.1f}'.replace('.', ',') + ' mil'
pct = lambda v: f'{v*100:.0f}%'
def tel(t):
    t = ''.join(ch for ch in (t or '') if ch.isdigit())
    if len(t) == 10: return f'({t[:2]}) {t[2:6]}-{t[6:]}'
    if len(t) == 11: return f'({t[:2]}) {t[2:7]}-{t[7:]}'
    return t or '—'
import re
def short(c, n=48):
    f = (c.get('fantasia') or '').strip()
    if f: return f[:n]
    x = re.sub(r'^(CONSORCIO|CONSÓRCIO)\s+(PUBLICO\s+|PÚBLICO\s+)?(INTERMUNICIPAL\s+|REGIONAL\s+|INTERFEDERATIVO\s+)?(DE\s+|DO\s+|DA\s+|DOS\s+|DAS\s+)?', '', c['nome'].upper()).strip()
    return (x or c['nome']).title()[:n]
import os as _os, re
COMP = json.load(open('../mgterr-dl/cons_compras.json')) if _os.path.exists('../mgterr-dl/cons_compras.json') else []
PCA = json.load(open('../mgterr-dl/cons_pca.json')) if _os.path.exists('../mgterr-dl/cons_pca.json') else {'feitos': [], 'pcas': [], 'itens': []}
import unicodedata as _ud
def _n(x): return _ud.normalize('NFKD', (x or '').lower()).encode('ascii','ignore').decode()
COMP = [x for x in COMP if not (re.search(r'impress|outsourcing|reprograf', _n(x['objeto'])) and not re.search(r'gestao documental|gestao eletronica de document|\bged\b', _n(x['objeto'])))]
COMP = [x for x in COMP if not re.search(r'valor que se empenha', _n(x['objeto']))]
comp_by = {}
for x in sorted(COMP, key=lambda x: x['data'], reverse=True): comp_by.setdefault(x['cnpj'], []).append(x)
plan_by = {}
for x in PCA['itens']: plan_by.setdefault(x['cnpj'], []).append(x)
pca_pub = {}
for x in PCA['pcas']: pca_pub.setdefault(x['cnpj'], []).append(x['ano'])
pca_lidos = {k[:-4] for k in PCA['feitos']}
def marca(c):
    m = ''
    if c['cnpj'] in comp_by: m += '<b>●</b> '
    if c['cnpj'] in plan_by: m += '<b>◆</b> '
    return m
# consórcios por território (pela cidade-sede)
id2inter = {m['id']: m['inter'].replace('Juíz de Fora','Juiz de Fora') for m in TT.M}
porT = {}
for c in CONS:
    ti = id2inter.get(str(c.get('ibge') or '')) or 'Sem território identificado'
    porT.setdefault(ti, []).append(c)
for v in porT.values(): v.sort(key=lambda c: (-c.get('editais', 0), c['nome']))

CSS = '''
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo+Narrow:wght@500;600;700&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
/* Feito para impressão em preto e branco: só tons de cinza, linhas finas, contraste alto, nada depende de cor. */
:root{ --k:#111; --g7:#3A3A3A; --g5:#6B6B6B; --g3:#B8B8B8; --g2:#D9D9D9; --g1:#EFEFEF; --w:#FFF;
  --fh:"Archivo Narrow", "Arial Narrow", Arial, sans-serif; --fb:"Source Serif 4", Georgia, serif; --fm:"IBM Plex Mono", monospace; }
@page{ size:A4; margin:0 }
*{box-sizing:border-box; margin:0; padding:0}
body{font-family:var(--fb); color:var(--k); background:var(--w); -webkit-print-color-adjust:exact; print-color-adjust:exact}
.p{width:210mm; height:297mm; position:relative; overflow:hidden; page-break-after:always; break-after:page; padding:22mm 16mm 18mm}
.p:last-child{page-break-after:auto}
h1,h2,h3{font-family:var(--fh); font-weight:700; letter-spacing:-.01em; line-height:1.02}
.eb{font-family:var(--fm); font-size:8.5pt; letter-spacing:.12em; text-transform:uppercase; color:var(--g5)}
p{font-size:10.5pt; line-height:1.45}
.top{position:absolute; left:16mm; right:16mm; top:8mm; display:flex; justify-content:space-between; align-items:center; border-bottom:.6pt solid var(--k); padding-bottom:2.5mm}
.top img{height:9mm}
.top span{font-family:var(--fm); font-size:8pt; letter-spacing:.08em; color:var(--g7); text-transform:uppercase}
.foot{position:absolute; left:16mm; right:16mm; bottom:8mm; display:flex; justify-content:space-between; font-family:var(--fm); font-size:7.5pt; color:var(--g5); border-top:.4pt solid var(--g3); padding-top:2mm}
.box{border:.6pt solid var(--k); padding:4mm 5mm}
.kpis{display:grid; grid-template-columns:repeat(4,1fr); border:.6pt solid var(--k)}
.kpis div{padding:3.5mm 4mm; border-right:.4pt solid var(--g3)}
.kpis div:last-child{border-right:0}
.kpis b{display:block; font-family:var(--fh); font-size:20pt; line-height:1}
.kpis span{font-size:8.5pt; color:var(--g7)}
table{border-collapse:collapse; width:100%; font-size:9pt}
th{font-family:var(--fm); font-weight:500; font-size:7.5pt; letter-spacing:.06em; text-transform:uppercase; text-align:left; padding:2mm 2mm; border-bottom:.9pt solid var(--k)}
td{padding:1.8mm 2mm; border-bottom:.4pt solid var(--g3); vertical-align:top}
td.r, th.r{text-align:right; font-variant-numeric:tabular-nums; white-space:nowrap}
.bar{height:3.2mm; background:var(--g1); border:.3pt solid var(--g5)}
.bar i{display:block; height:100%; background:var(--g7)}
.call td{height:13mm}
.blank{border-bottom:.4pt solid var(--g5); border-left:.4pt solid var(--g3)}
.chk{display:inline-block; width:3mm; height:3mm; border:.6pt solid var(--k); margin-right:1.2mm; vertical-align:-.4mm}
.patt-agro{background:repeating-linear-gradient(45deg, #fff 0 1.2mm, #555 1.2mm 1.6mm)}
.patt-ind{background:#222}
.patt-serv{background:#8A8A8A}
.patt-adm{background:repeating-linear-gradient(0deg, #fff 0 1mm, #444 1mm 1.4mm)}
</style>'''
N = [0]
def pg(inner, rot):
    N[0] += 1
    return f'<section class="p"><div class="top"><img src="{LOGO}" alt="DigitalGov"><span>{rot}</span></div>{inner}<div class="foot"><span>Territórios de Minas e consórcios · DigitalGov · novembro de 2026</span><span>{N[0]:02d}</span></div></section>'
def setores(t, w=100):
    segs = ''.join(f'<span class="patt-{k}" style="display:block; width:{t["sh"][k]*100:.1f}%; height:100%; border-right:.6pt solid #fff"></span>' for k in ('agro','ind','serv','adm'))
    return f'<div style="display:flex; height:7mm; border:.6pt solid var(--k)">{segs}</div>'
LEG = '<div style="display:flex; gap:5mm; font-size:8.5pt; margin-top:2mm; flex-wrap:wrap">' + ''.join(f'<span><i class="patt-{k}" style="display:inline-block; width:5mm; height:3mm; border:.4pt solid #000; vertical-align:-.5mm; margin-right:1.2mm"></i>{n}</span>' for k, n in (('agro','Agropecuária'),('ind','Indústria'),('serv','Serviços'),('adm','Administração pública'))) + '</div>'

P = []
TS = sorted(T.values(), key=lambda t: -t['pib'])
nc = len(CONS)
# CAPA
N[0] += 1
P.append(f'''<section class="p" style="padding:30mm 18mm">
  <img src="{LOGO}" alt="DigitalGov" style="height:22mm">
  <div style="margin-top:40mm; border-top:2pt solid var(--k); padding-top:8mm">
    <p class="eb">Pesquisa · Minas Gerais · novembro de 2026</p>
    <h1 style="font-size:54pt; margin-top:4mm">Territórios de Minas<br>e consórcios</h1>
    <p style="font-size:13pt; margin-top:6mm; max-width:150mm">Economia de cada território, quanto cada um produz, os consórcios intermunicipais com telefone e as folhas de ligação para a equipe comercial.</p>
  </div>
  <div class="kpis" style="margin-top:22mm">
    <div><b>{len(T)}</b><span>territórios (regiões intermediárias do IBGE)</span></div>
    <div><b>{TOT["mun"]}</b><span>municípios</span></div>
    <div><b>{bi(TOT["pib"])}</b><span>PIB de Minas em 2023</span></div>
    <div><b>{nc}</b><span>consórcios com contato</span></div>
  </div>
  <p style="position:absolute; left:18mm; right:18mm; bottom:18mm; font-size:9pt; color:var(--g5)">Impressão recomendada: A4, preto e branco, frente e verso. As folhas de ligação têm espaço para anotar à mão.</p>
</section>''')

# SUMÁRIO / COMO USAR
P.append(pg(f'''<p class="eb">Como usar</p><h2 style="font-size:28pt; margin-top:2mm">Roteiro deste caderno</h2>
  <div class="box" style="margin-top:7mm">
    <p><b>1. Visão geral</b> · ranking dos {len(T)} territórios por PIB, população e renda por pessoa.</p>
    <p style="margin-top:2mm"><b>2. Uma página por território</b> · economia por setor, maiores cidades, quantos municípios têm até 20 mil habitantes e quais consórcios estão lá.</p>
    <p style="margin-top:2mm"><b>3. Folhas de ligação</b> · consórcios por território com telefone, e-mail e espaço para anotar data, contato, resultado e retorno.</p>
    <p style="margin-top:2mm"><b>4. Roteiro de ligação</b> · o que falar em 2 minutos e as perguntas que qualificam o cliente.</p>
  </div>
  <div class="box" style="margin-top:6mm">
    <p class="eb">Por que consórcios</p>
    <p style="margin-top:2mm">Um consórcio intermunicipal compra em nome de vários municípios de uma vez, por meio de um único processo e de uma ata de registro de preços. Uma venda pode chegar a dezenas de prefeituras. Minas é o estado com mais consórcios públicos do país.</p>
  </div>
  <div class="box" style="margin-top:6mm">
    <p class="eb">Sobre os territórios</p>
    <p style="margin-top:2mm">Usamos as 13 Regiões Geográficas Intermediárias do IBGE, que têm dados oficiais por município. Os 17 Territórios de Desenvolvimento do governo de Minas não têm base pública de municípios disponível para esta pesquisa.</p>
  </div>''', 'Roteiro'))

# RANKING
mx = TS[0]['pib']
rows = ''.join(f'<tr><td><b>{i+1}. {H.escape(t["nome"])}</b></td><td class="r">{t["mun"]}</td><td class="r">{fmt(t["pop"])}</td><td class="r">{bi(t["pib"])}</td><td style="width:34mm"><div class="bar"><i style="width:{t["pib"]/mx*100:.1f}%"></i></div></td><td class="r">{t["pib"]/TOT["pib"]*100:.1f}%</td><td class="r">{mil(t["percap"])}</td></tr>' for i, t in enumerate(TS))
P.append(pg(f'''<p class="eb">Visão geral</p><h2 style="font-size:28pt; margin-top:2mm">Quanto cada território produz</h2>
  <p style="margin-top:3mm">PIB de 2023 a preços correntes e população do Censo 2022. Ordenado do maior para o menor PIB.</p>
  <table style="margin-top:6mm"><thead><tr><th>Território</th><th class="r">Munic.</th><th class="r">População</th><th class="r">PIB 2023</th><th></th><th class="r">% MG</th><th class="r">PIB por pessoa</th></tr></thead><tbody>{rows}
  <tr><td style="border-top:.9pt solid var(--k)"><b>Minas Gerais</b></td><td class="r" style="border-top:.9pt solid var(--k)"><b>{TOT["mun"]}</b></td><td class="r" style="border-top:.9pt solid var(--k)"><b>{fmt(TOT["pop"])}</b></td><td class="r" style="border-top:.9pt solid var(--k)"><b>{bi(TOT["pib"])}</b></td><td style="border-top:.9pt solid var(--k)"></td><td class="r" style="border-top:.9pt solid var(--k)">100%</td><td class="r" style="border-top:.9pt solid var(--k)"><b>{mil(TOT["pib"]/TOT["pop"])}</b></td></tr></tbody></table>
  <div class="box" style="margin-top:7mm"><p><b>Leitura:</b> a região de Belo Horizonte gera {TS[0]["pib"]/TOT["pib"]*100:.0f}% do PIB do estado. O Triângulo (Uberlândia e Uberaba) e o Sul (Pouso Alegre e Varginha) têm a maior renda por pessoa. O Norte e o Nordeste (Montes Claros, Teófilo Otoni, Governador Valadares) têm a menor renda e dependem mais do setor público.</p></div>''', 'Visão geral'))

# ESTRUTURA ECONÔMICA
er = ''.join(f'<tr><td style="width:46mm"><b>{H.escape(t["nome"])}</b></td><td>{setores(t)}</td><td class="r" style="font-size:8pt">{pct(t["sh"]["agro"])} · {pct(t["sh"]["ind"])} · {pct(t["sh"]["serv"])} · {pct(t["sh"]["adm"])}</td></tr>' for t in TS)
P.append(pg(f'''<p class="eb">Economia</p><h2 style="font-size:28pt; margin-top:2mm">Do que vive cada território</h2>
  <p style="margin-top:3mm">Participação de cada setor no valor adicionado (IBGE, 2021, último ano com setores por município).</p>
  {LEG}
  <table style="margin-top:5mm"><thead><tr><th>Território</th><th>Setores</th><th class="r">Agro · Ind. · Serv. · Adm.</th></tr></thead><tbody>{er}</tbody></table>
  <div class="box" style="margin-top:6mm"><p><b>Para vender:</b> onde a administração pública pesa mais (Teófilo Otoni, Governador Valadares, Montes Claros), as prefeituras são os grandes compradores da região. Onde a indústria pesa mais (Ipatinga, Barbacena, Belo Horizonte), há receita própria para investir em tecnologia.</p></div>''', 'Economia'))

# PÁGINA POR TERRITÓRIO
for t in TS:
    cs = porT.get(t['nome'], [])
    cid = ''.join(f'<tr><td>{H.escape(c["nome"])}</td><td class="r">{fmt(c["pop"])}</td><td class="r">{bi(c["pib"]) if c["pib"] >= 1e9 else mil(c["pib"]/1000) + " mi"}</td></tr>' for c in t['cidades'][:8])
    crow = ''.join(f'<tr><td>{H.escape(short(c, 40))}</td><td>{H.escape((c.get("municipio") or c.get("cidade") or "").title())}</td><td class="r">{c.get("editais",0)}</td></tr>' for c in cs[:8])
    P.append(pg(f'''<p class="eb">Território</p><h2 style="font-size:30pt; margin-top:2mm">{H.escape(t["nome"])}</h2>
  <div class="kpis" style="margin-top:6mm">
    <div><b>{bi(t["pib"])}</b><span>PIB 2023 · {t["pib"]/TOT["pib"]*100:.1f}% de MG</span></div>
    <div><b>{fmt(t["pop"])}</b><span>habitantes</span></div>
    <div><b>{mil(t["percap"])}</b><span>PIB por pessoa</span></div>
    <div><b>{t["mun"]}</b><span>municípios · {t["ate20"]} com até 20 mil hab.</span></div>
  </div>
  <p class="eb" style="margin-top:6mm">Economia por setor</p>{setores(t)}{LEG}
  <p style="font-size:9pt; margin-top:1.5mm">Agro {pct(t["sh"]["agro"])} · Indústria {pct(t["sh"]["ind"])} · Serviços {pct(t["sh"]["serv"])} · Administração pública {pct(t["sh"]["adm"])}</p>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:6mm; margin-top:6mm">
    <div><p class="eb">Maiores cidades</p><table style="margin-top:2mm"><thead><tr><th>Cidade</th><th class="r">População</th><th class="r">PIB</th></tr></thead><tbody>{cid}</tbody></table></div>
    <div><p class="eb">Consórcios com sede aqui ({len(cs)})</p><table style="margin-top:2mm"><thead><tr><th>Consórcio</th><th>Sede</th><th class="r">Editais</th></tr></thead><tbody>{crow or '<tr><td colspan="3">Nenhum encontrado no PNCP</td></tr>'}</tbody></table></div>
  </div>
  <div class="box" style="margin-top:6mm"><p><b>Regiões imediatas:</b> {", ".join(H.escape(x) for x in t["imediatas"])}.</p>
  <p style="margin-top:2mm"><b>Oportunidade:</b> {t["ate20"]} municípios com até 20 mil habitantes precisam cumprir as regras de divulgação da Lei 14.133 até 1º de abril de 2027.</p></div>''', t['nome']))

# ROTEIRO DE LIGAÇÃO
P.append(pg(f'''<p class="eb">Antes de ligar</p><h2 style="font-size:28pt; margin-top:2mm">Roteiro de ligação (2 minutos)</h2>
  <div class="box" style="margin-top:6mm"><p><b>1. Abertura.</b> "Bom dia, aqui é ____, da DigitalGov, empresa mineira de tecnologia para o setor público. Com quem eu falo sobre compras e projetos do consórcio?"</p>
  <p style="margin-top:3mm"><b>2. Motivo.</b> "Atendemos prefeituras como Araçuaí, Ibiá e Cordisburgo com digitalização de documentos e software de gestão. Um consórcio pode contratar uma vez e levar a solução a todos os municípios."</p>
  <p style="margin-top:3mm"><b>3. Pergunta-chave.</b> "Os municípios do consórcio já organizaram o arquivo e o envio ao PNCP? O prazo dos menores é abril de 2027."</p>
  <p style="margin-top:3mm"><b>4. Próximo passo.</b> "Posso mandar uma proposta de ata de registro de preços e marcar uma reunião de 20 minutos?"</p></div>
  <div class="box" style="margin-top:6mm"><p class="eb">Perguntas para qualificar</p>
  <p style="margin-top:2mm"><span class="chk"></span>Quantos municípios fazem parte do consórcio?</p>
  <p style="margin-top:1.5mm"><span class="chk"></span>O consórcio já compra por registro de preços para os municípios?</p>
  <p style="margin-top:1.5mm"><span class="chk"></span>Existe demanda de digitalização, arquivo ou software de gestão?</p>
  <p style="margin-top:1.5mm"><span class="chk"></span>Quem decide: secretário-executivo, presidente (prefeito) ou assembleia?</p>
  <p style="margin-top:1.5mm"><span class="chk"></span>Quando é a próxima assembleia dos prefeitos?</p></div>
  <div class="box" style="margin-top:6mm"><p class="eb">Códigos de resultado para as folhas</p>
  <p style="margin-top:2mm"><b>A</b> agendou reunião · <b>P</b> pediu proposta · <b>R</b> retornar depois · <b>S</b> sem interesse agora · <b>N</b> não atendeu · <b>X</b> número errado</p></div>''', 'Roteiro de ligação'))

# COMPRAS E PLANOS DE DIGITALIZAÇÃO
alvo = [c for c in CONS if c['cnpj'] in comp_by or c['cnpj'] in plan_by]
alvo.sort(key=lambda c: (-(len(comp_by.get(c['cnpj'], [])) + len(plan_by.get(c['cnpj'], []))), short(c)))
def bloco(c):
    ti = id2inter.get(str(c.get('ibge') or ''), '')
    lin = ''
    for x in comp_by.get(c['cnpj'], [])[:4]:
        lin += f'<tr><td style="width:20mm">● {"Edital" if x["tipo"] == "edital" else "Ata"}</td><td style="width:18mm">{x["data"][8:10]}/{x["data"][5:7]}/{x["data"][:4]}</td><td>{H.escape(x["objeto"][:150])}</td><td style="width:22mm; font-size:7.5pt">{H.escape(x.get("situacao") or "")}</td></tr>'
    for x in plan_by.get(c['cnpj'], [])[:4]:
        q = f'{fmt(x["qtd"])} {x["un"] if x.get("un") and x["un"] != "-" else ""}'.strip() if x.get('qtd') else ''
        lin += f'<tr><td>◆ Plano {x["ano"]}</td><td>{(x.get("data") or "")[8:10]}/{(x.get("data") or "")[5:7]}</td><td>{H.escape((x.get("desc") or "")[:150])}{" · " + q if q else ""}</td><td class="r">{("R$ " + fmt(x["valor"])) if x.get("valor") else ""}</td></tr>'
    return f'<div style="break-inside:avoid; margin-top:4mm"><p style="font-family:var(--fh); font-size:12pt; font-weight:700">{H.escape(short(c, 60))} <span style="font-weight:500; font-size:9pt; color:var(--g5)">· {H.escape((c.get("municipio") or c.get("cidade") or "").title())} · {H.escape(ti)} · {tel(c.get("tel1"))}</span></p><table style="margin-top:1mm; font-size:8.5pt"><tbody>{lin}</tbody></table></div>'
com_pca = len({k for k in pca_pub})
resumo = f'''<p class="eb">Compras de digitalização</p><h2 style="font-size:26pt; margin-top:2mm">Quem já compra ou planeja comprar</h2>
  <p style="margin-top:3mm">Editais e atas de digitalização, gestão documental e GED publicados pelos consórcios no PNCP, e itens desses temas nos Planos de Contratações Anuais de 2026 e 2027.</p>
  <div class="kpis" style="margin-top:5mm">
    <div><b>{len(CONS)}</b><span>consórcios consultados</span></div>
    <div><b>{len(comp_by)}</b><span>com edital ou ata do tema (●)</span></div>
    <div><b>{com_pca}</b><span>publicaram plano 2026 ou 2027</span></div>
    <div><b>{len(plan_by)}</b><span>com o tema no plano (◆)</span></div>
  </div>
  <div class="box" style="margin-top:5mm"><p><b>Como usar:</b> ligue primeiro para os consórcios marcados. Quem já comprou conhece o serviço e pode renovar ou ampliar; quem planejou tem verba prevista e ainda vai abrir a licitação. Os mesmos símbolos aparecem nas folhas de ligação.</p></div>'''
bl = [bloco(c) for c in alvo]
if not bl: bl = ['<div class="box" style="margin-top:6mm"><p>Nenhum consórcio da lista tem edital, ata ou plano com estes temas no PNCP.</p></div>']
pg_now = [resumo]; cnt = 3
for b_ in bl:
    if cnt >= 7: P.append(pg(''.join(pg_now), 'Compras')); pg_now = ['<p class="eb">Compras de digitalização (continuação)</p>']; cnt = 0
    pg_now.append(b_); cnt += 1
P.append(pg(''.join(pg_now), 'Compras'))

# FOLHAS DE LIGAÇÃO
ordem = [t['nome'] for t in TS] + (['Sem território identificado'] if 'Sem território identificado' in porT else [])
for nome in ordem:
    cs = porT.get(nome, [])
    for k in range(0, len(cs), 9):
        grp = cs[k:k+9]
        rows = ''.join(f'''<tr class="call"><td><b style="font-size:9pt">{marca(c)}{H.escape(short(c, 55))}</b><br><span style="font-size:7.5pt; color:var(--g5)">{H.escape(c["nome"][:70])}</span><br><span style="font-size:7.5pt">{H.escape((c.get("municipio") or c.get("cidade") or "").title())} · CNPJ {c["cnpj"]}</span></td>
  <td style="font-family:var(--fm); font-size:8.5pt">{tel(c.get("tel1"))}{"<br>" + tel(c.get("tel2")) if c.get("tel2") else ""}<br><span style="font-size:7pt">{H.escape((c.get("email") or "").lower())}</span></td>
  <td class="blank"></td><td class="blank"></td><td class="blank" style="width:12mm"></td><td class="blank"></td></tr>''' for c in grp)
        P.append(pg(f'''<p class="eb">Folha de ligação</p><h2 style="font-size:20pt; margin-top:1mm">{H.escape(nome)}{f" · {k//9+1}/{(len(cs)+8)//9}" if len(cs) > 9 else ""}</h2>
  <table style="margin-top:4mm"><thead><tr><th style="width:62mm">Consórcio <span style="text-transform:none">(● comprou · ◆ planeja)</span></th><th style="width:36mm">Telefone · e-mail</th><th>Data</th><th>Falou com</th><th>Res.</th><th>Anotações / retorno</th></tr></thead><tbody>{rows}</tbody></table>''', 'Ligações'))

# FONTES
P.append(pg(f'''<p class="eb">Fontes e limites</p><h2 style="font-size:28pt; margin-top:2mm">De onde vêm os dados</h2>
  <div class="box" style="margin-top:6mm">
  <p>• <b>População:</b> IBGE, Censo Demográfico 2022, por município.</p>
  <p style="margin-top:2mm">• <b>PIB:</b> IBGE, PIB dos Municípios 2023 (total) e 2021 (valor adicionado por setor).</p>
  <p style="margin-top:2mm">• <b>Territórios:</b> IBGE, Regiões Geográficas Intermediárias e Imediatas (divisão de 2017).</p>
  <p style="margin-top:2mm">• <b>Consórcios:</b> órgãos com nome de consórcio que publicaram editais em Minas no Portal Nacional de Contratações Públicas (PNCP), consulta de 27/11/2026.</p>
  <p style="margin-top:2mm">• <b>Telefones e e-mails:</b> cadastro público de CNPJ da Receita Federal (via BrasilAPI). Podem estar desatualizados.</p></div>
  <div class="box" style="margin-top:6mm"><p><b>Limites:</b> a lista traz só consórcios que publicaram editais no PNCP; consórcios que não usam o portal podem faltar. O território de cada consórcio é o da sua cidade-sede, mas ele pode atender municípios de outros territórios. Confira os contatos no site do consórcio antes de enviar proposta.</p></div>''', 'Fontes'))

html = '<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Territórios de Minas e Consórcios</title>' + CSS + '</head><body>' + ''.join(P) + '</body></html>'
open('territorios-minas.html', 'w').write(html)
print('ok', len(P), nc, {k: len(v) for k, v in porT.items()})
