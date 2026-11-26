# Apresentação "Rios Vivos de Minas" para lideranças: 6 rios, custo de cada um, como usar e impactos. Slides 1280x720.
import json
FLAG = open('../mg-dl/flag.svg').read()
FLAG = FLAG.replace('width="600" height="420" style="', 'viewBox="0 0 600 420" preserveAspectRatio="xMidYMid meet" style="width:100%; height:100%; display:block; ')
brl = lambda v: 'R$ ' + f'{v:,.0f}'.replace(',', '.')
mi = lambda v: ('R$ ' + f'{v/1e6:,.1f}'.replace('.', ',') + ' mi')
fmt = lambda v: f'{v:,.0f}'.replace(',', '.')

# ---------- Kit limpador: custo unitário (estimativas 2026) ----------
KIT = [
 ('est', 'Estação automática de monitoramento', 'unidade', 80000, 'Mede oxigênio, turbidez, pH e temperatura a cada 15 min'),
 ('estm','Manutenção das estações (24 meses)', 'estação/mês', 1500, ''),
 ('eco', 'Ecobarreira: limpador de lixo flutuante', 'unidade', 30000, 'Barreira que segura garrafas e plásticos para coleta'),
 ('ecom','Coleta e operação das ecobarreiras (24 meses)', 'barreira/mês', 3000, ''),
 ('mata','Restauração de mata ciliar', 'hectare', 18000, 'Plantio e 2 anos de manutenção'),
 ('nasc','Proteção de nascente', 'nascente', 6000, 'Cerca, plantio e placa'),
 ('caca','Caça-esgoto: vistoria de ligações', 'imóvel', 40, 'Acha esgoto ligado na rede de chuva'),
 ('bio', 'Fossa séptica biodigestora rural', 'unidade', 2500, 'Modelo Embrapa, para casas sem rede'),
 ('edu', 'Educação e mobilização', 'ano', 300000, 'Escolas, rádio, mutirões'),
 ('ges', 'Equipe e gestão do programa', 'ano', 600000, 'Coordenação, técnicos e dados'),
]
U = {k: c for k, _, _, c, _ in KIT}
RIOS = [
 # nome, cidade-símbolo, lat, lon, cor, problema, quantidades (2 anos)
 ('Rio das Velhas','Belo Horizonte',-19.92,-43.94,'#1B6CA8','Esgoto da Grande BH pelos ribeirões Arrudas e Onça',
   dict(est=10, eco=12, mata=300, nasc=200, caca=60000, bio=300)),
 ('Rio Paraopeba','Brumadinho',-20.14,-44.20,'#C0392B','Rejeito de 2019 e esgoto de Betim e Ibirité',
   dict(est=8, eco=8, mata=250, nasc=200, caca=30000, bio=300)),
 ('Rio Doce','Gov. Valadares',-18.85,-41.95,'#B5652A','Lama de Mariana (2015), erosão e esgoto',
   dict(est=10, eco=6, mata=400, nasc=300, caca=25000, bio=400)),
 ('Rio Piracicaba','Ipatinga',-19.47,-42.54,'#6B5B95','Siderurgia, mineração e esgoto do Vale do Aço',
   dict(est=6, eco=6, mata=150, nasc=120, caca=30000, bio=150)),
 ('Rio Paraibuna','Juiz de Fora',-21.76,-43.35,'#2E7D4F','Esgoto urbano de Juiz de Fora',
   dict(est=5, eco=6, mata=120, nasc=100, caca=35000, bio=150)),
 ('Rio Pará','Divinópolis',-20.14,-44.89,'#C9A227','Esgoto e efluente industrial do Centro-Oeste',
   dict(est=5, eco=4, mata=150, nasc=150, caca=20000, bio=250)),
]
def custo(q):
    linhas = [
      ('Estações de monitoramento', q['est']*U['est'] + q['est']*24*U['estm']),
      ('Ecobarreiras (limpadores)', q['eco']*U['eco'] + q['eco']*24*U['ecom']),
      ('Mata ciliar', q['mata']*U['mata']),
      ('Nascentes', q['nasc']*U['nasc']),
      ('Caça-esgoto', q['caca']*U['caca']),
      ('Biodigestores rurais', q['bio']*U['bio']),
      ('Educação e mobilização', 2*U['edu']),
      ('Equipe e gestão', 2*U['ges']),
    ]
    return linhas, sum(v for _, v in linhas)
TOT = {r[0]: custo(r[6]) for r in RIOS}
GERAL = sum(t for _, t in TOT.values())
print({k: v[1] for k, v in TOT.items()}, GERAL)

CSS = '''
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=Poppins:wght@400;500;600;700;800&family=IBM+Plex+Mono:wght@500&display=swap">
<style>
/* Identidade mineira: branco e vermelho da bandeira, serifa de título com ar de igreja barroca, ouro só em detalhes, azul de rio e verde de mata para os dados. */
:root{
  --bg:#FBFAF8; --ink:#1A1F2B; --muted:#5B6170; --line:rgba(26,31,43,.12);
  --verm:#D7141F; --verm-bg:#FBE3E4; --ouro:#B8902A; --rio:#1B6CA8; --rio-bg:#E1EEF8; --mata:#2E7D4F; --mata-bg:#E2F1E7; --card:#FFFFFF;
  --fh:"DM Serif Display", Georgia, serif; --fb:"Poppins", "Segoe UI", Arial, sans-serif; --fm:"IBM Plex Mono", monospace;
}
@page{ size:1280px 720px; margin:0 }
*{box-sizing:border-box; margin:0; padding:0}
body{font-family:var(--fb); color:var(--ink); -webkit-print-color-adjust:exact; print-color-adjust:exact; background:var(--bg)}
.s{width:1280px; height:720px; position:relative; overflow:hidden; page-break-after:always; break-after:page; background:var(--bg); padding:64px 72px}
.s:last-child{page-break-after:auto}
h1,h2,h3{font-family:var(--fh); font-weight:400; letter-spacing:-.01em; line-height:1.02}
h2{font-size:52px}
.eyebrow{font-family:var(--fm); font-size:13px; letter-spacing:.14em; text-transform:uppercase; color:var(--verm)}
p{font-size:17px; line-height:1.5}
.muted{color:var(--muted)}
.card{background:var(--card); border-radius:14px; padding:20px 22px; border:1px solid rgba(26,31,43,.07); box-shadow:0 10px 28px -20px rgba(26,31,43,.45)}
.dark{background:var(--ink); color:#fff; border:0}
.num{font-family:var(--fh); font-variant-numeric:tabular-nums; line-height:1}
.tri{position:absolute; right:72px; top:58px; width:0; height:0; border-left:13px solid transparent; border-right:13px solid transparent; border-bottom:22px solid var(--verm)}
.foot{position:absolute; left:72px; right:72px; bottom:26px; display:flex; justify-content:space-between; font-size:12px; color:var(--muted); font-family:var(--fm); letter-spacing:.06em}
table{border-collapse:collapse; width:100%; font-size:14px}
th{font-family:var(--fm); font-weight:500; font-size:11.5px; letter-spacing:.08em; text-transform:uppercase; color:var(--muted); text-align:left; padding:8px 9px; border-bottom:2px solid var(--ink)}
td{padding:7px 9px; border-bottom:1px solid var(--line); vertical-align:top}
td.r, th.r{text-align:right; font-variant-numeric:tabular-nums; white-space:nowrap}
ul.l{list-style:none; display:grid; gap:9px}
ul.l li{position:relative; padding-left:22px; font-size:16.5px; line-height:1.42}
ul.l li::before{content:""; position:absolute; left:2px; top:.45em; width:0; height:0; border-left:6px solid transparent; border-right:6px solid transparent; border-bottom:10px solid var(--verm)}
</style>'''
N = [0]
def s(inner, rod='Rios Vivos de Minas'):
    N[0] += 1
    return f'<section class="s"><span class="tri"></span>{inner}<div class="foot"><span>{rod.upper()}</span><span>{N[0]:02d}</span></div></section>'
def tit(eye, t):
    return f'<p class="eyebrow">{eye}</p><h2 style="margin-top:10px; width:1000px">{t}</h2>'

S = []
# 1 CAPA
N[0] += 1
S.append(f'''<section class="s" style="padding:0">
  <div style="position:absolute; right:0; top:0; bottom:0; width:560px; background:#fff; border-left:1px solid var(--line); display:grid; place-items:center"><div style="width:460px; height:322px; box-shadow:0 20px 50px -30px rgba(26,31,43,.6)">{FLAG}</div></div>
  <p class="eyebrow" style="position:absolute; left:72px; top:80px">Apresentação para lideranças · Minas Gerais</p>
  <h1 style="position:absolute; left:72px; top:130px; font-size:96px; width:620px">Rios Vivos<br><i style="color:var(--verm)">de Minas</i></h1>
  <p style="position:absolute; left:72px; top:390px; width:560px; font-size:21px">Plano para limpar 6 rios mineiros em 2 anos: quanto custa cada um, como executar e o que Minas ganha com isso.</p>
  <div style="position:absolute; left:72px; top:540px; display:flex; gap:12px">
    <div class="card" style="padding:14px 18px"><p class="num" style="font-size:34px; color:var(--verm)">6</p><p style="font-size:13px" class="muted">rios</p></div>
    <div class="card" style="padding:14px 18px"><p class="num" style="font-size:34px; color:var(--verm)">{mi(GERAL)}</p><p style="font-size:13px" class="muted">em 2 anos</p></div>
    <div class="card" style="padding:14px 18px"><p class="num" style="font-size:34px; color:var(--verm)">24</p><p style="font-size:13px" class="muted">meses</p></div>
  </div>
  <p style="position:absolute; left:72px; bottom:30px; font-family:var(--fm); font-size:12px; letter-spacing:.1em; color:var(--muted)">LIBERTAS QUÆ SERA TAMEN · NOVEMBRO DE 2026</p>
</section>''')

# 2 PROBLEMA
S.append(s(f'''{tit('Onde estamos','Minas coleta o esgoto, mas ainda devolve muito dele sujo aos rios')}
  <div style="display:grid; grid-template-columns:repeat(4,1fr); gap:14px; margin-top:40px">
    <div class="card"><p class="num" style="font-size:52px; color:var(--verm)">17%</p><p style="font-size:15px; margin-top:8px">dos pontos medidos pelo IGAM com água ruim em 2023</p></div>
    <div class="card"><p class="num" style="font-size:52px; color:var(--verm)">54%</p><p style="font-size:15px; margin-top:8px">das amostras fora do limite legal em 2020</p></div>
    <div class="card"><p class="num" style="font-size:52px; color:var(--rio)">87,6%</p><p style="font-size:15px; margin-top:8px">de coleta de esgoto em 2021</p></div>
    <div class="card"><p class="num" style="font-size:52px; color:var(--rio)">53,7%</p><p style="font-size:15px; margin-top:8px">da população com esgoto tratado no mesmo ano</p></div>
  </div>
  <div class="card dark" style="margin-top:22px; display:grid; grid-template-columns:1fr 1fr; gap:30px">
    <div><p class="eyebrow" style="color:#F3B9BC">A ferida</p><p style="font-size:17px; margin-top:8px">Mariana (2015) e Brumadinho (2019) mostraram ao mundo o custo de um rio morto: 289 vidas e bacias inteiras atingidas.</p></div>
    <div><p class="eyebrow" style="color:#F3B9BC">A oportunidade</p><p style="font-size:17px; margin-top:8px">Os acordos de reparação somam mais de R$ 200 bilhões e a lei exige 90% de esgoto tratado até 2033. O dinheiro e o prazo existem.</p></div>
  </div>''', 'IGAM; Governo de Minas; Lei 14.026/2020'))

# 3 EVOLUIR
ev = [('Monitoramento','Relatório anual do IGAM','Rio medido a cada 15 minutos, com alerta no celular'),
      ('Lixo no rio','Mutirões de vez em quando','Ecobarreiras fixas recolhendo lixo toda semana'),
      ('Esgoto','Rede existe, mas há ligações erradas','Caça-esgoto casa por casa e fossas no campo'),
      ('Margens','Pasto até a beira do rio','Mata ciliar e nascentes cercadas'),
      ('População','Assiste de longe','Escolas, comitês e denúncias pelo celular'),
      ('Transparência','Dados espalhados','Painel público por rio e por cidade')]
et = ''.join(f'<tr><td><b>{a}</b></td><td class="muted">{b}</td><td style="color:var(--rio); font-weight:600">{c}</td></tr>' for a,b,c in ev)
S.append(s(f'''{tit('Como podemos evoluir','De onde partimos e aonde queremos chegar')}
  <div class="card" style="margin-top:32px; padding:14px 22px"><table style="font-size:16px"><thead><tr><th style="width:200px">Tema</th><th>Hoje</th><th>Em 2 anos</th></tr></thead><tbody>{et}</tbody></table></div>'''))

# 4 MAPA DOS 6 RIOS
geo = json.load(open('../dados/uf.json'))
g = [f for f in geo['features'] if f['properties']['sigla']=='MG'][0]['geometry']
rings = [p[0] for p in g['coordinates']] if g['type']=='MultiPolygon' else [g['coordinates'][0]]
X0,X1,Y0,Y1 = -51.2,-39.7,-23.0,-14.1
W=520; H=int(W*(Y1-Y0)/(X1-X0)*1.04)
px=lambda x:(x-X0)/(X1-X0)*W; py=lambda y:(Y1-y)/(Y1-Y0)*H
path=''.join('M'+' L'.join(f'{px(a):.1f},{py(b):.1f}' for a,b in r[::2])+'Z' for r in rings)
pins=''
off = {'Belo Horizonte':(12,-10,'start'),'Brumadinho':(4,26,'middle'),'Gov. Valadares':(12,-6,'start'),'Ipatinga':(-12,-10,'end'),'Juiz de Fora':(12,6,'start'),'Divinópolis':(-12,-12,'end')}
for i,(n,c,la,lo,cor,_,_) in enumerate(RIOS):
    pins += f'<circle cx="{px(lo):.1f}" cy="{py(la):.1f}" r="13" fill="{cor}" stroke="#fff" stroke-width="3"/><text x="{px(lo):.1f}" y="{py(la)+5:.1f}" text-anchor="middle" font-family="Poppins" font-size="14" font-weight="800" fill="#fff">{i+1}</text>'
mapa = f'<svg viewBox="-10 -10 {W+20} {H+20}" style="width:100%; display:block"><path d="{path}" fill="#F1EEEA" stroke="#1A1F2B" stroke-width="1.3"/>{pins}</svg>'
lst = ''.join(f'<div style="display:grid; grid-template-columns:26px 1fr; gap:12px; padding:9px 0; border-bottom:1px solid var(--line)"><span style="width:26px; height:26px; border-radius:50%; background:{cor}; color:#fff; font-weight:800; font-size:14px; display:grid; place-items:center">{i+1}</span><div><p style="font-size:17px; font-weight:700">{n} <span class="muted" style="font-weight:500; font-size:14px">· {c}</span></p><p style="font-size:14.5px" class="muted">{pb}</p></div></div>' for i,(n,c,la,lo,cor,pb,_) in enumerate(RIOS))
S.append(s(f'''{tit('Os 6 rios','Seis rios, seis regiões, um plano')}
  <div style="display:grid; grid-template-columns:470px 1fr; gap:30px; margin-top:22px; align-items:start">
    <div class="card" style="padding:10px">{mapa}</div>
    <div class="card" style="padding:8px 22px">{lst}</div>
  </div>''', 'Localização aproximada da cidade de referência de cada rio'))

# 5 KIT LIMPADOR
kt = ''.join(f'<tr><td style="padding:5px 9px"><b>{n}</b> <span class="muted" style="font-size:12.5px">· {d}</span></td><td class="r" style="padding:5px 9px">{brl(c)}</td><td class="muted" style="padding:5px 9px; white-space:nowrap">por {un}</td></tr>' for k,n,un,c,d in KIT if d)
S.append(s(f'''{tit('O kit limpador','O que vai em cada rio e quanto custa')}
  <div style="display:grid; grid-template-columns:1fr 360px; gap:24px; margin-top:24px">
    <div class="card" style="padding:10px 18px"><table style="font-size:14px"><thead><tr><th>Ação</th><th class="r">Custo</th><th>Unidade</th></tr></thead><tbody>{kt}</tbody></table></div>
    <div style="display:grid; gap:14px; align-content:start">
      <div class="card" style="background:var(--rio-bg); border:0"><p class="eyebrow" style="color:var(--rio)">O "limpador"</p><p style="font-size:16px; margin-top:8px">A <b>ecobarreira</b> é uma barreira flutuante instalada de margem a margem. Ela segura garrafas, sacolas e isopor, e uma equipe recolhe o lixo toda semana.</p></div>
      <div class="card"><p class="eyebrow">Não entra no kit</p><p style="font-size:15px; margin-top:8px">As grandes estações de tratamento de esgoto. Elas são obra da Copasa e das prefeituras. O plano acelera e fiscaliza essas obras.</p></div>
    </div>
  </div>''', 'Custos unitários estimados, valores de 2026'))

# 6 CUSTO POR RIO
mx = max(t for _,t in TOT.values())
bars = ''.join(f'<div style="display:grid; grid-template-columns:170px 1fr 120px; gap:14px; align-items:center; padding:7px 0"><span style="font-size:16px; font-weight:600">{n}</span><span style="height:28px; background:rgba(26,31,43,.06); border-radius:0 6px 6px 0; overflow:hidden"><span style="display:block; height:100%; width:{TOT[n][1]/mx*100:.1f}%; background:{cor}; border-radius:0 6px 6px 0"></span></span><span class="num" style="font-size:24px; text-align:right">{mi(TOT[n][1])}</span></div>' for n,c,la,lo,cor,pb,q in RIOS)
S.append(s(f'''{tit('Quanto custa','Custo de cada rio em 2 anos')}
  <div style="display:grid; grid-template-columns:1fr 330px; gap:26px; margin-top:28px; align-items:start">
    <div class="card" style="padding:16px 24px">{bars}</div>
    <div class="card dark" style="padding:28px"><p class="eyebrow" style="color:#F3B9BC">Total dos 6 rios</p><p class="num" style="font-size:50px; margin-top:12px">{mi(GERAL)}</p><p style="font-size:15px; margin-top:12px; color:#C9CDD6">em 24 meses. É menos de 0,5% do novo acordo de Mariana.</p></div>
  </div>''', 'Estimativas para planejamento; detalhe por rio nos próximos slides'))

# 7-8 FICHAS POR RIO
def ficha(r):
    n,c,la,lo,cor,pb,q = r
    linhas, t = TOT[n]
    rows = ''.join(f'<tr><td>{a}</td><td class="r">{brl(v)}</td></tr>' for a,v in linhas)
    return (f'<div class="card" style="padding:16px 18px; border-top:6px solid {cor}"><p style="font-family:var(--fh); font-size:26px">{n}</p><p class="muted" style="font-size:13px">{c} · {pb}</p>'
            f'<p style="font-size:13px; margin-top:8px"><b>{q["est"]}</b> estações · <b>{q["eco"]}</b> ecobarreiras · <b>{q["mata"]}</b> ha de mata · <b>{q["nasc"]}</b> nascentes · <b>{fmt(q["caca"])}</b> imóveis vistoriados · <b>{q["bio"]}</b> biodigestores</p>'
            f'<table style="font-size:12.5px; margin-top:8px"><tbody>{rows}<tr><td style="font-weight:800; border-bottom:0">Total</td><td class="r" style="font-weight:800; border-bottom:0; color:{cor}">{brl(t)}</td></tr></tbody></table></div>')
for k in (0, 3):
    S.append(s(f'''{tit('Ficha de cada rio', 'Rios ' + ('1 a 3' if k==0 else '4 a 6'))}
  <div style="display:grid; grid-template-columns:repeat(3,1fr); gap:16px; margin-top:22px">{''.join(ficha(r) for r in RIOS[k:k+3])}</div>''', 'Quantidades e custos estimados para 24 meses'))

# 9 FINANCIAMENTO
fin = [('Acordos de Mariana e Brumadinho','Recursos para recuperar as bacias do Doce e do Paraopeba'),
       ('Comitês de bacia','Dinheiro da cobrança pelo uso da água, aplicado na própria bacia'),
       ('Copasa e prefeituras','Obras de esgoto previstas nos contratos e no Marco do Saneamento'),
       ('Emendas parlamentares','Deputados e senadores podem destinar recursos ao programa'),
       ('Empresas','Mineradoras, siderúrgicas e indústrias que precisam compensar impactos'),
       ('Fundos e editais','Bancos de desenvolvimento e fundos de clima e água')]
ft = ''.join(f'<div class="card" style="padding:16px 18px"><p style="font-family:var(--fh); font-size:22px">{a}</p><p class="muted" style="font-size:14.5px; margin-top:4px">{b}</p></div>' for a,b in fin)
S.append(s(f'''{tit('Quem paga','O dinheiro já existe em várias fontes')}
  <div style="display:grid; grid-template-columns:repeat(3,1fr); gap:14px; margin-top:28px">{ft}</div>
  <div class="card" style="margin-top:16px; background:var(--mata-bg); border:0"><p style="font-size:17px"><b style="color:var(--mata)">Proposta:</b> um fundo do programa por rio, com conta separada e painel público de gastos.</p></div>'''))

# 10 COMO USAR
passos = [('Mês 1–2','Pacto','Assinatura com Estado, prefeituras, Copasa e comitês. Escolha do coordenador de cada rio.'),
          ('Mês 3–4','Diagnóstico','Mapa de pontos de lixo, esgoto e nascentes; definição dos locais das ecobarreiras e estações.'),
          ('Mês 5–12','Instalação','Ecobarreiras, estações, início do plantio e do caça-esgoto.'),
          ('Mês 13–24','Escala','Plantio completo, biodigestores no campo, painel público e relatório a cada 3 meses.')]
pt = ''.join(f'<div class="card" style="padding:18px; border-top:5px solid {c}"><p class="eyebrow" style="color:{c}">{a}</p><p style="font-family:var(--fh); font-size:28px; margin-top:8px">{b}</p><p class="muted" style="font-size:14.5px; margin-top:6px">{d}</p></div>' for (a,b,d),c in zip(passos,['#D7141F','#B8902A','#1B6CA8','#2E7D4F']))
S.append(s(f'''{tit('Como usar o plano','Passo a passo em 24 meses')}
  <div style="display:grid; grid-template-columns:repeat(4,1fr); gap:14px; margin-top:30px">{pt}</div>
  <div class="card dark" style="margin-top:18px"><p style="font-size:17px"><b style="color:#F3B9BC">Comece pequeno:</b> um rio piloto (sugestão: rio das Velhas ou Paraibuna) prova o modelo em 6 meses e abre caminho para os outros cinco.</p></div>'''))

# 11 IMPACTO POSITIVO
imp = [('Saúde','Menos diarreia, verminose e internações ligadas à água suja.','#D7141F'),
       ('Água mais barata','Rio limpo custa menos para tratar e virar água de torneira.','#1B6CA8'),
       ('Empregos','Viveiros, plantio, coleta, sensores e obras em cada região.','#B8902A'),
       ('Turismo e lazer','Pesca, esportes e orla de rio voltam a atrair gente.','#2E7D4F'),
       ('Natureza','Peixes e mata voltam; nascentes protegidas garantem água na seca.','#2E7D4F'),
       ('Imagem de Minas','De estado dos desastres a referência em rios vivos.','#D7141F')]
it = ''.join(f'<div class="card" style="padding:18px 20px; border-left:6px solid {c}"><p style="font-family:var(--fh); font-size:26px">{a}</p><p class="muted" style="font-size:15px; margin-top:4px">{b}</p></div>' for a,b,c in imp)
S.append(s(f'''{tit('Como pode vir positivamente','O que Minas ganha com rios vivos')}
  <div style="display:grid; grid-template-columns:repeat(3,1fr); gap:14px; margin-top:28px">{it}</div>
  <div class="card" style="margin-top:16px; background:var(--rio-bg); border:0"><p style="font-size:17px"><b style="color:var(--rio)">Retorno:</b> a Organização Mundial da Saúde estima que cada dólar investido em água e saneamento devolve cerca de quatro em saúde e produtividade.</p></div>''', 'OMS (2012), estudo global de custo-benefício em água e saneamento'))

# 12 INDICADORES
ind = [('Lixo retirado pelas ecobarreiras','toneladas por mês'),('Oxigênio e turbidez nas estações','média mensal por rio'),
       ('Ligações de esgoto corrigidas','número de imóveis'),('Mata ciliar plantada e viva','hectares'),
       ('Nascentes protegidas','número'),('Pontos com IQA bom ou excelente','% no relatório do IGAM')]
il = ''.join(f'<tr><td><b>{a}</b></td><td class="muted">{b}</td></tr>' for a,b in ind)
S.append(s(f'''{tit('Como medir','Indicadores no painel público')}
  <div style="display:grid; grid-template-columns:1fr 380px; gap:24px; margin-top:28px">
    <div class="card" style="padding:12px 22px"><table style="font-size:16px"><thead><tr><th>Indicador</th><th>Medida</th></tr></thead><tbody>{il}</tbody></table></div>
    <div class="card dark"><p class="eyebrow" style="color:#F3B9BC">Meta em 2 anos</p><p style="font-family:var(--fh); font-size:30px; margin-top:10px; line-height:1.15">Mais pontos com água boa em cada um dos 6 rios, medidos pelo próprio IGAM.</p></div>
  </div>'''))

# 13 PEDIDO
S.append(s(f'''{tit('O que precisamos de você','Três decisões para começar')}
  <div style="display:grid; grid-template-columns:repeat(3,1fr); gap:16px; margin-top:34px">
    <div class="card" style="padding:26px; border-top:6px solid var(--verm)"><p class="num" style="font-size:56px; color:var(--verm)">1</p><p style="font-family:var(--fh); font-size:26px; margin-top:10px">Apoio político</p><p class="muted" style="font-size:15px; margin-top:6px">Reunir Estado, prefeituras, Copasa e comitês no pacto do primeiro rio.</p></div>
    <div class="card" style="padding:26px; border-top:6px solid var(--ouro)"><p class="num" style="font-size:56px; color:var(--ouro)">2</p><p style="font-family:var(--fh); font-size:26px; margin-top:10px">Recurso inicial</p><p class="muted" style="font-size:15px; margin-top:6px">Emenda ou parceria para o rio piloto, cerca de {mi(min(t for _,t in TOT.values()))}.</p></div>
    <div class="card" style="padding:26px; border-top:6px solid var(--rio)"><p class="num" style="font-size:56px; color:var(--rio)">3</p><p style="font-family:var(--fh); font-size:26px; margin-top:10px">Padrinho do programa</p><p class="muted" style="font-size:15px; margin-top:6px">Uma liderança que acompanhe os resultados e preste contas à população.</p></div>
  </div>
  <p style="font-family:var(--fh); font-size:34px; margin-top:40px; text-align:center"><i>Rios vivos são o futuro de Minas.</i></p>'''))

# 14 ENCERRAMENTO
N[0] += 1
S.append(f'''<section class="s" style="padding:0; background:#fff">
  <div style="position:absolute; left:440px; top:120px; width:400px; height:280px">{FLAG}</div>
  <h2 style="position:absolute; left:0; right:0; top:440px; text-align:center; font-size:58px">Rios Vivos <i style="color:var(--verm)">de Minas</i></h2>
  <p style="position:absolute; left:0; right:0; top:520px; text-align:center; font-size:19px" class="muted">Seis rios · dois anos · {mi(GERAL)}</p>
  <p style="position:absolute; left:0; right:0; bottom:40px; text-align:center; font-family:var(--fm); font-size:12px; letter-spacing:.12em; color:var(--muted)">CUSTOS ESTIMADOS PARA PLANEJAMENTO · CONFIRMAR COM COTAÇÕES LOCAIS</p>
</section>''')

html = '<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Rios Vivos de Minas</title>' + CSS + '</head><body>' + ''.join(S) + '</body></html>'
open('rios-vivos.html','w').write(html)
print('ok', len(S))
