# Plano de Combate à Malária 2027 para a ibradep. Páginas 1080x1350.
import json
FLAG = open('bandeira-amapa.svg').read().replace('height="700" width="1000"', 'viewBox="0 0 1000 700" preserveAspectRatio="xMidYMid slice" style="width:100%; height:100%; display:block"')
brl = lambda v: 'R$ ' + f'{v:,.0f}'.replace(',', '.')
fmt = lambda v: f'{v:,.0f}'.replace(',', '.')

# ---------------- ORÇAMENTO (12 meses, cenário padrão) ----------------
ORC = [
 ('Pessoal', [
   ('Coordenação geral', 1, 12, 9000, 'pessoa/mês'),
   ('Coordenação técnica (enfermagem ou epidemiologia)', 1, 12, 8000, 'pessoa/mês'),
   ('Supervisores de polo', 3, 12, 5500, 'pessoa/mês'),
   ('Agentes de campo e mobilizadores', 12, 12, 3200, 'pessoa/mês'),
   ('Comunicação (redes e design)', 2, 12, 4500, 'pessoa/mês'),
   ('Analista de dados', 1, 12, 6000, 'pessoa/mês'),
   ('Administrativo-financeiro', 1, 12, 4500, 'pessoa/mês'),
   ('Piloteiros e motoristas', 3, 12, 3000, 'pessoa/mês'),
 ]),
 ('Logística', [
   ('Aluguel de caminhonetes 4x4', 2, 12, 9000, 'veículo/mês'),
   ('Combustível dos veículos', 2, 12, 2500, 'veículo/mês'),
   ('Voadeira com motor 40 hp (compra)', 2, 1, 45000, 'unidade'),
   ('Combustível dos barcos', 2, 12, 3000, 'barco/mês'),
   ('Diárias de campo (8 por pessoa ao mês)', 15, 96, 120, 'diária'),
 ]),
 ('Prevenção', [
   ('Mosquiteiros impregnados de longa duração', 5000, 1, 45, 'unidade'),
   ('Kits de repelente para trabalhadores', 3000, 1, 25, 'kit'),
   ('Telas em casas de maior risco', 500, 1, 300, 'casa'),
 ]),
 ('Comunicação', [
   ('Rádios comunitárias (pacote mensal)', 6, 12, 1500, 'rádio/mês'),
   ('Material impresso bilíngue', 1, 1, 40000, 'lote'),
   ('Vídeos e áudios, inclusive em línguas indígenas', 1, 1, 35000, 'lote'),
   ('Impulsionamento nas redes', 1, 12, 2000, 'mês'),
   ('Carro de som', 1, 1, 20000, 'lote'),
 ]),
 ('Capacitação e eventos', [
   ('Formação de agentes e 60 multiplicadores', 1, 1, 45000, 'lote'),
   ('Oficinas em aldeias e garimpos', 1, 1, 30000, 'lote'),
   ('Lançamento (25 de abril) e seminário final', 1, 1, 25000, 'lote'),
 ]),
 ('Tecnologia e dados', [
   ('Celulares e tablets resistentes', 15, 1, 2000, 'unidade'),
   ('Internet via satélite: equipamento', 3, 1, 2500, 'polo'),
   ('Internet via satélite: mensalidade', 3, 12, 500, 'polo/mês'),
   ('App offline e painel de dados', 1, 1, 60000, 'lote'),
 ]),
 ('Administração', [
   ('Bases de apoio nos polos (aluguel)', 3, 12, 2000, 'base/mês'),
   ('Contabilidade, auditoria e seguros', 1, 1, 48000, 'ano'),
 ]),
]
cat_tot = {c: sum(q*m*u for _,q,m,u,_ in it) for c,it in ORC}
direto = sum(cat_tot.values())
reserva = round(direto*0.05)
TOTAL = direto + reserva
CORES = {'Pessoal':'#2B2B2B','Logística':'#E8692C','Prevenção':'#3F8A2E','Comunicação':'#C2C930','Capacitação e eventos':'#5AA0D6','Tecnologia e dados':'#002580','Administração':'#9A9A92'}
PESSOAS = 40000
print('total', TOTAL, cat_tot)

CSS = '''
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Anton&family=Poppins:ital,wght@0,400;0,500;0,600;0,700;0,800;1,700;1,800&family=IBM+Plex+Mono:wght@500&display=swap">
<style>
/* Plano operacional: papel quadriculado claro, cartões brancos com sombra suave, faixa das cores do Amapá, títulos condensados. */
:root{
  --paper:#FAFAF6; --grid:rgba(30,40,30,.05); --ink:#232523; --muted:#5E615C; --line:rgba(30,40,30,.12);
  --lima:#B7BE22; --lima-bg:#F2F4C8; --laranja:#E8692C; --lar-bg:#FCE7DC; --verde:#2F7D32; --verde-bg:#E1F0DE;
  --ap-azul:#002580; --ap-verde:#00994C; --ap-amarelo:#F3E718; --card:#FFFFFF;
  --fh:"Anton", "Impact", "Arial Narrow", sans-serif; --fb:"Poppins", "Segoe UI", Arial, sans-serif; --fm:"IBM Plex Mono", monospace;
}
@page{ size:1080px 1350px; margin:0 }
*{box-sizing:border-box; margin:0; padding:0}
body{font-family:var(--fb); color:var(--ink); -webkit-print-color-adjust:exact; print-color-adjust:exact; background:var(--paper)}
.p{width:1080px; height:1350px; position:relative; overflow:hidden; page-break-after:always; break-after:page;
   background-color:var(--paper);
   background-image:linear-gradient(var(--grid) 1px, transparent 1px), linear-gradient(90deg, var(--grid) 1px, transparent 1px);
   background-size:36px 36px; padding:110px 90px 0}
.p:last-child{page-break-after:auto}
.H{font-family:var(--fh); font-weight:400; text-transform:uppercase; letter-spacing:-.005em}
.H > span{display:block; line-height:1.0} .H > br{display:none}
.lima{color:var(--lima)} .lar{color:var(--laranja)} .ink{color:var(--ink)} .verde{color:var(--verde)} .azul{color:var(--ap-azul)}
p{font-size:23px; line-height:1.48}
.card{background:var(--card); border-radius:18px; padding:28px 32px; box-shadow:0 1px 0 rgba(30,40,30,.06), 0 10px 30px -18px rgba(30,40,30,.35); border:1px solid rgba(30,40,30,.06)}
.dark{background:var(--ink); color:#fff; border:0}
.num{font-family:var(--fh); font-weight:400; line-height:.95; font-variant-numeric:tabular-nums}
.small{font-size:18px; color:var(--muted); line-height:1.4}
.eyebrow{font-family:var(--fm); font-size:17px; letter-spacing:.12em; text-transform:uppercase; color:var(--laranja)}
.top{position:absolute; left:90px; right:90px; top:44px; display:flex; justify-content:space-between; align-items:center; font-size:17px; color:var(--muted)}
.top b{color:var(--ink); font-weight:800}
.stripe{position:absolute; left:0; top:0; bottom:0; width:14px; display:flex; flex-direction:column}
.stripe i{flex:1}
.foot{position:absolute; left:90px; right:90px; bottom:44px; display:flex; justify-content:space-between; font-size:16px; color:var(--muted)}
ul.dot{list-style:none; display:grid; gap:12px}
ul.dot li{position:relative; padding-left:30px; font-size:22px; line-height:1.4}
ul.dot li::before{content:""; position:absolute; left:3px; top:.55em; width:11px; height:11px; background:var(--laranja); transform:rotate(45deg)}
table{border-collapse:collapse; width:100%; font-size:17.5px}
th{font-family:var(--fm); font-weight:500; font-size:14px; letter-spacing:.08em; text-transform:uppercase; color:var(--muted); text-align:left; padding:10px 10px; border-bottom:2px solid var(--ink)}
td{padding:6px 10px; border-bottom:1px solid var(--line); vertical-align:top}
td.r, th.r{text-align:right; font-variant-numeric:tabular-nums; white-space:nowrap}
tr.cat td{font-weight:800; background:rgba(30,40,30,.04); border-bottom:1px solid var(--line)}
.pill{display:inline-block; font-weight:700; font-size:15px; padding:5px 12px; border-radius:999px}
</style>'''

STRIPE = '<div class="stripe"><i style="background:var(--ap-azul)"></i><i style="background:var(--ap-verde)"></i><i style="background:var(--ap-amarelo)"></i></div>'
N = [0]
def pg(inner, secao, fonte=''):
    N[0] += 1
    return (f'<section class="p">{STRIPE}<div class="top"><span><b>ibradep</b> · Plano de Combate à Malária 2027</span><span>{secao}</span></div>'
            f'{inner}<div class="foot"><span>{fonte}</span><span>{N[0]:02d}</span></div></section>')
def head(eye, l1, l2, c1='ink', c2='lar', size=96):
    return f'<p class="eyebrow">{eye}</p><h2 class="H" style="font-size:{size}px; margin-top:14px"><span class="{c1}">{l1}</span><span class="{c2}">{l2}</span></h2>'

P = []

# 1 CAPA
N[0] += 1
P.append(f'''<section class="p" style="padding:0">
  <div style="position:absolute; left:0; right:0; top:0; height:560px">{FLAG}</div>
  <div style="position:absolute; left:0; right:0; top:560px; height:10px; background:var(--ink)"></div>
  <div style="position:absolute; left:90px; right:90px; top:630px">
    <p class="eyebrow">Para a ibradep · plano operacional</p>
    <h1 class="H" style="font-size:112px; margin-top:16px"><span class="ink">Plano de combate</span><span class="lar">à malária</span><span class="lima" style="font-size:84px; margin-top:8px">Amapá 2027</span></h1>
    <div style="display:flex; gap:14px; margin-top:34px; flex-wrap:wrap">
      <span class="pill" style="background:var(--ink); color:#fff">12 meses</span>
      <span class="pill" style="background:var(--lar-bg); color:var(--laranja)">7 municípios prioritários</span>
      <span class="pill" style="background:var(--verde-bg); color:var(--verde)">{brl(TOTAL)}</span>
    </div>
  </div>
  <p style="position:absolute; left:90px; bottom:56px; font-size:18px; color:var(--muted)">#AmapáNoCombateÀMalária · novembro de 2026</p>
</section>''')

# 2 RESUMO
P.append(pg(f'''{head('Resumo executivo','O plano','em uma página')}
  <p style="margin-top:26px; font-size:25px; max-width:880px">A ibradep atua como braço de campo e de comunicação do SUS: leva teste, tratamento acompanhado e prevenção aonde o posto não chega, em parceria com o Estado, os municípios e as lideranças locais.</p>
  <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:18px; margin-top:34px">
    <div class="card"><p class="num lar" style="font-size:64px">−30%</p><p style="font-size:19px; margin-top:6px">de casos nos polos atendidos em 12 meses</p></div>
    <div class="card"><p class="num ink" style="font-size:64px">{fmt(PESSOAS)}</p><p style="font-size:19px; margin-top:6px">pessoas alcançadas</p></div>
    <div class="card"><p class="num verde" style="font-size:64px">15 mil</p><p style="font-size:19px; margin-top:6px">testes em busca ativa</p></div>
  </div>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:18px; margin-top:18px">
    <div class="card"><p class="eyebrow" style="color:var(--muted)">Onde</p><p style="font-size:21px; margin-top:8px">3 polos: <b>Calçoene</b> (garimpo), <b>Oiapoque e Pedra Branca</b> (fronteira e aldeias) e <b>Mazagão, Santana, Porto Grande e Macapá</b> (várzea e periferia).</p></div>
    <div class="card"><p class="eyebrow" style="color:var(--muted)">Como</p><p style="font-size:21px; margin-top:8px">5 eixos: busca ativa, tratamento até o fim, prevenção, comunicação e dados.</p></div>
  </div>
  <div class="card dark" style="margin-top:18px; display:grid; grid-template-columns:1fr auto; align-items:center; gap:20px">
    <div><p class="eyebrow" style="color:var(--lima)">Investimento total</p><p class="num" style="font-size:78px; margin-top:8px">{brl(TOTAL)}</p></div>
    <div style="text-align:right"><p style="font-size:19px; color:#D7D9D2">cerca de</p><p class="num" style="font-size:52px; color:var(--lima)">{brl(TOTAL/PESSOAS)}</p><p style="font-size:19px; color:#D7D9D2">por pessoa alcançada</p></div>
  </div>''', 'Resumo', 'Valores estimados para 12 meses, cenário padrão'))

# 3 DIAGNÓSTICO
P.append(pg(f'''{head('Ponto de partida','Por que agir','agora')}
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:18px; margin-top:34px">
    <div class="card"><p class="num lar" style="font-size:78px">6.413</p><p style="font-size:20px; margin-top:6px">casos em 2024, o dobro de 2022</p></div>
    <div class="card"><p class="num ink" style="font-size:78px">91%</p><p style="font-size:20px; margin-top:6px">vivax: volta se o tratamento parar no meio</p></div>
    <div class="card"><p class="num ink" style="font-size:78px">88%</p><p style="font-size:20px; margin-top:6px">dos casos só aparecem quando a pessoa vai ao posto</p></div>
    <div class="card"><p class="num verde" style="font-size:78px">−82%</p><p style="font-size:20px; margin-top:6px">em Macapá de 2024 para 2025: ação organizada funciona</p></div>
  </div>
  <div class="card" style="margin-top:18px">
    <p class="eyebrow" style="color:var(--muted)">O que os dados mostram</p>
    <ul class="dot" style="margin-top:14px">
      <li>Calçoene, Mazagão e Santana somam 44% dos casos de 2014 a 2024.</li>
      <li>30% dos doentes trabalham na roça ou no garimpo, longe do posto.</li>
      <li>Indígenas são 8,6% dos casos, bem acima do peso deles na população.</li>
      <li>O risco sobe de junho a setembro, quando os rios baixam.</li>
    </ul>
  </div>''', 'Diagnóstico', 'SIVEP-Malária via Oliveira et al. (2025); Ministério da Saúde; Prefeitura de Macapá'))

# 4 METAS
metas = [('Reduzir casos','30% a menos de casos nos polos atendidos, comparado a 2026','lar'),
         ('Diagnosticar rápido','70% dos casos testados em até 48 horas após a febre','ink'),
         ('Tratar até o fim','100% dos casos de vivax acompanhados até a última dose','verde'),
         ('Proteger casas','5.000 mosquiteiros entregues e instalados, com visita de retorno','ink'),
         ('Informar','40.000 pessoas alcançadas por rádio, visitas, escolas e redes','lar'),
         ('Formar gente local','12 agentes e 60 multiplicadores comunitários capacitados','verde')]
mt = ''.join(f'<div class="card" style="display:grid; grid-template-columns:70px 1fr; gap:18px; align-items:start; padding:20px 28px"><p class="num {c}" style="font-size:58px">{i+1}</p><div><p class="H" style="font-size:36px">{t}</p><p style="font-size:20px; margin-top:4px; color:var(--muted)">{d}</p></div></div>' for i,(t,d,c) in enumerate(metas))
P.append(pg(f'''{head('Objetivos','Seis metas','para 2027','ink','lima')}
  <div style="display:grid; gap:12px; margin-top:26px">{mt}</div>''', 'Metas'))

# 5 MAPA
geo = json.load(open('../dados/uf.json'))
ap = [f for f in geo['features'] if f['properties']['sigla']=='AP'][0]['geometry']
rings = [p[0] for p in ap['coordinates']] if ap['type']=='MultiPolygon' else [ap['coordinates'][0]]
X0,X1,Y0,Y1 = -54.95,-49.75,-1.35,4.55
W=600; H=int(W*(Y1-Y0)/(X1-X0))
px=lambda x:(x-X0)/(X1-X0)*W; py=lambda y:(Y1-y)/(Y1-Y0)*H
path=''.join('M'+' L'.join(f'{px(a):.1f},{py(b):.1f}' for a,b in r)+'Z' for r in rings)
cid = [('Calçoene',2.50,-50.95,17911,1),('Mazagão',-0.12,-51.29,15864,3),('Santana',-0.06,-51.17,15467,3),('Pedra Branca',0.78,-51.95,14390,2),
       ('Porto Grande',0.71,-51.41,12965,3),('Oiapoque',3.84,-51.83,11355,2),('Macapá',0.03,-51.07,10374,3),('Serra do Navio',0.90,-52.00,6510,0),
       ('Tartarugalzinho',1.51,-50.91,3449,0),('Laranjal do Jari',-0.83,-52.45,1748,0)]
polo_cor = {1:'#E8692C',2:'#002580',3:'#2F7D32',0:'#9A9A92'}
dots=''
for n,la,lo,v,pl in cid:
    r = 7 + (v/17911)**.5*20
    dots += f'<circle cx="{px(lo):.1f}" cy="{py(la):.1f}" r="{r:.1f}" fill="{polo_cor[pl]}" fill-opacity=".85" stroke="#fff" stroke-width="3"/>'
lab = {'Calçoene':(14,-6,'start'),'Mazagão':(-14,26,'end'),'Santana':(16,30,'start'),'Pedra Branca':(-16,6,'end'),'Porto Grande':(18,4,'start'),'Oiapoque':(-16,-14,'end'),'Macapá':(22,-8,'start'),'Serra do Navio':(-14,-12,'end'),'Tartarugalzinho':(14,6,'start'),'Laranjal do Jari':(14,24,'start')}
for n,la,lo,v,pl in cid:
    dx,dy,an = lab[n]
    dots += f'<text x="{px(lo)+dx:.1f}" y="{py(la)+dy:.1f}" text-anchor="{an}" font-family="Poppins" font-weight="{700 if pl else 500}" font-size="17" fill="#232523">{n}</text>'
mapa = f'<svg viewBox="-40 -10 {W+80} {H+20}" style="width:100%; display:block"><path d="{path}" fill="#E9EDE3" stroke="#232523" stroke-width="1.5"/>{dots}</svg>'
polos = [('#E8692C','Polo 1 · Garimpo','Calçoene e garimpo do Lourenço. Busca ativa no barranco, teste rápido e tratamento supervisionado.'),
         ('#002580','Polo 2 · Fronteira e aldeias','Oiapoque e Pedra Branca do Amapari. Ação com DSEI, lideranças e agentes indígenas; material bilíngue.'),
         ('#2F7D32','Polo 3 · Várzea e cidade','Mazagão, Santana, Porto Grande e Macapá. Criadouros, mosquiteiros, telas e escolas.')]
pl = ''.join(f'<div class="card" style="padding:20px 24px; border-left:8px solid {c}"><p class="H" style="font-size:30px">{t}</p><p style="font-size:18px; margin-top:4px; color:var(--muted)">{d}</p></div>' for c,t,d in polos)
P.append(pg(f'''{head('Onde atuar','Três polos,','sete municípios')}
  <div style="display:grid; grid-template-columns:520px 1fr; gap:26px; margin-top:26px; align-items:start">
    <div class="card" style="padding:14px">{mapa}<p class="small" style="padding:4px 10px 6px; font-size:15px">Círculo proporcional aos casos de 2014 a 2024. Localização aproximada das sedes.</p></div>
    <div style="display:grid; gap:14px">{pl}</div>
  </div>''', 'Território', 'Contorno: base pública de limites estaduais; casos: SIVEP-Malária'))

# 6 EIXOS
eixos = [('01','Busca ativa e diagnóstico','Equipes com teste rápido em garimpos, roças, ramais, aldeias e comunidades ribeirinhas. Febre = teste no mesmo dia.','#E8692C'),
         ('02','Tratamento até o fim','Cada caso positivo ganha um "padrinho" na equipe, que acompanha as doses e confere a cura. Encaminhamento ao SUS para tafenoquina com teste de G6PD.','#232523'),
         ('03','Prevenção','Mosquiteiros impregnados, repelente para trabalhadores, telas em casas de risco e mutirões contra criadouros com a comunidade.','#2F7D32'),
         ('04','Comunicação','Rádio comunitária, carro de som, WhatsApp, Instagram, escolas e igrejas. Mensagens em português, francês e línguas indígenas.','#B7BE22'),
         ('05','Dados e monitoramento','App offline para o campo, painel semanal por localidade e relatório mensal para a ibradep, o Estado e os parceiros.','#002580')]
ex = ''.join(f'<div class="card" style="display:grid; grid-template-columns:96px 1fr; gap:20px; padding:24px 28px"><div style="background:{c}; border-radius:14px; display:grid; place-items:center; height:96px"><p class="num" style="font-size:46px; color:#fff">{n}</p></div><div><p class="H" style="font-size:34px">{t}</p><p style="font-size:19.5px; margin-top:4px; color:var(--muted)">{d}</p></div></div>' for n,t,d,c in eixos)
P.append(pg(f'''{head('Como agir','Cinco eixos','de ação')}
  <div style="display:grid; gap:14px; margin-top:30px">{ex}</div>''', 'Eixos'))

# 7 EQUIPE
equipe = [('Coordenação geral','1','Responde à diretoria da ibradep e aos parceiros'),
          ('Coordenação técnica','1','Enfermagem ou epidemiologia; protocolos com o SUS'),
          ('Supervisores de polo','3','Um por polo; organizam rotas e equipes'),
          ('Agentes de campo','12','Quatro por polo; busca ativa, visitas e acompanhamento'),
          ('Comunicação','2','Redes, rádio, materiais e relação com a imprensa'),
          ('Dados','1','App, painel e relatórios'),
          ('Administrativo-financeiro','1','Compras, contratos e prestação de contas'),
          ('Piloteiros e motoristas','3','Barcos e caminhonetes')]
org = f'''<svg viewBox="0 0 900 300" style="width:100%; display:block">
  <g font-family="Poppins" text-anchor="middle">
  <rect x="330" y="10" width="240" height="64" rx="12" fill="#232523"/><text x="450" y="50" fill="#fff" font-size="19" font-weight="700">Coordenação geral</text>
  <line x1="450" y1="74" x2="450" y2="104" stroke="#232523" stroke-width="2"/><line x1="120" y1="104" x2="780" y2="104" stroke="#232523" stroke-width="2"/>
  {''.join(f'<line x1="{x}" y1="104" x2="{x}" y2="130" stroke="#232523" stroke-width="2"/><rect x="{x-100}" y="130" width="200" height="60" rx="12" fill="{c}"/><text x="{x}" y="166" fill="{t}" font-size="17" font-weight="700">{n}</text>' for x,n,c,t in [(120,'Técnica','#E8692C','#fff'),(340,'Comunicação','#B7BE22','#232523'),(560,'Dados','#002580','#fff'),(780,'Adm.-financeiro','#9A9A92','#fff')])}
  <line x1="120" y1="190" x2="120" y2="220" stroke="#232523" stroke-width="2"/><line x1="60" y1="220" x2="300" y2="220" stroke="#232523" stroke-width="2"/>
  {''.join(f'<line x1="{x}" y1="220" x2="{x}" y2="236" stroke="#232523" stroke-width="2"/><rect x="{x-56}" y="236" width="112" height="56" rx="10" fill="#FCE7DC" stroke="#E8692C"/><text x="{x}" y="260" fill="#232523" font-size="14" font-weight="700">Polo {i+1}</text><text x="{x}" y="280" fill="#5E615C" font-size="13">4 agentes</text>' for i,x in enumerate([60,180,300]))}
  </g></svg>'''
rows = ''.join(f'<tr><td><b>{a}</b></td><td class="r">{b}</td><td>{c}</td></tr>' for a,b,c in equipe)
P.append(pg(f'''{head('Quem faz','Equipe de','24 pessoas','ink','verde')}
  <div class="card" style="margin-top:28px; padding:22px 26px">{org}</div>
  <div class="card" style="margin-top:18px; padding:16px 24px"><table><thead><tr><th>Função</th><th class="r">Qtd.</th><th>Papel</th></tr></thead><tbody>{rows}</tbody></table></div>
  <p class="small" style="margin-top:14px">Prioridade de contratação para pessoas dos próprios municípios, inclusive agentes indígenas indicados pelas lideranças.</p>''', 'Equipe'))

# 8 CRONOGRAMA
M = ['JAN','FEV','MAR','ABR','MAI','JUN','JUL','AGO','SET','OUT','NOV','DEZ']
tarefas = [('Contratar e formar a equipe',0,2,'#232523'),('Acordos com Estado, municípios e DSEI',0,2,'#232523'),('Mapear localidades e criadouros',1,3,'#002580'),
           ('Lançamento · 25 de abril',3,4,'#B7BE22'),('Entrega de mosquiteiros e telas',3,6,'#2F7D32'),('Busca ativa intensiva',4,9,'#E8692C'),
           ('Campanha de rádio e redes',3,10,'#B7BE22'),('Tratamento supervisionado',2,12,'#E8692C'),('Painel e relatórios mensais',2,12,'#002580'),('Avaliação e seminário final',10,12,'#232523')]
cw = 52
hdr = ''.join(f'<div style="width:{cw}px; text-align:center; font-family:var(--fm); font-size:13px; color:{"#E8692C" if 5<=i<=8 else "#5E615C"}">{m}</div>' for i,m in enumerate(M))
gl = ''
for t,a,b,c in tarefas:
    gl += (f'<div style="display:grid; grid-template-columns:270px {cw*12}px; align-items:center; padding:9px 0; border-bottom:1px solid var(--line)">'
           f'<span style="font-size:17px; font-weight:600">{t}</span><div style="position:relative; height:22px; background:repeating-linear-gradient(90deg, transparent 0 {cw-1}px, rgba(30,40,30,.08) {cw-1}px {cw}px)">'
           f'<span style="position:absolute; left:{a*cw+3}px; width:{(b-a)*cw-6}px; top:2px; bottom:2px; border-radius:6px; background:{c}"></span></div></div>')
P.append(pg(f'''{head('Quando','Cronograma','2027','ink','lar')}
  <div class="card" style="margin-top:30px; padding:22px 26px">
    <div style="display:grid; grid-template-columns:270px {cw*12}px; padding-bottom:8px; border-bottom:2px solid var(--ink)"><span class="eyebrow" style="color:var(--muted); font-size:13px">Atividade</span><div style="display:flex">{hdr}</div></div>
    {gl}
    <div style="display:grid; grid-template-columns:270px {cw*12}px; margin-top:10px"><span></span><div style="position:relative; height:30px"><span style="position:absolute; left:{5*cw}px; width:{4*cw}px; top:0; bottom:0; background:var(--lar-bg); border-radius:6px; display:grid; place-items:center; font-size:14px; font-weight:700; color:var(--laranja)">Pico de risco</span></div></div>
  </div>
  <div class="card dark" style="margin-top:18px"><p style="font-size:21px"><b style="color:var(--lima)">Ponto-chave:</b> tudo o que é prevenção precisa estar no campo antes de junho. A busca ativa mais forte acontece de maio a setembro.</p></div>''', 'Cronograma'))

# 9-10 ORÇAMENTO DETALHADO
def tabela(cats):
    out = ''
    for c in cats:
        it = dict(ORC)[c]
        out += f'<tr class="cat"><td colspan="3"><span style="display:inline-block; width:12px; height:12px; border-radius:3px; background:{CORES[c]}; margin-right:10px"></span>{c}</td><td class="r">{brl(cat_tot[c])}</td></tr>'
        for n,q,m,u,un in it:
            qtd = f'{fmt(q)}' + (f' × {m}' if m>1 else '')
            out += f'<tr><td>{n}</td><td class="r">{qtd}</td><td class="r">{brl(u)}<span style="color:var(--muted); font-size:14px"> /{un}</span></td><td class="r">{brl(q*m*u)}</td></tr>'
    return f'<table style="font-size:16.5px"><thead><tr><th>Item</th><th class="r">Qtd.</th><th class="r">Custo unitário</th><th class="r">Total</th></tr></thead><tbody>{out}</tbody></table>'
P.append(pg(f'''{head('Custos de operação','Orçamento','detalhado · 1/2','ink','lar', 74)}
  <div class="card" style="margin-top:26px; padding:16px 22px">{tabela(['Pessoal','Logística','Prevenção'])}</div>
  <p class="small" style="margin-top:10px; font-size:16px">Pessoal: custo total mensal com encargos. Diárias: 15 pessoas × 8 diárias por mês × 12 meses.</p>  <div class="card" style="margin-top:10px; padding:14px 24px; background:var(--verde-bg); border:0"><p style="font-size:18px"><b class="verde">Fora do orçamento</b> (o SUS fornece): testes, exames, remédios e borrifação.</p>''', 'Orçamento', 'Valores estimados em reais de 2026'))
P.append(pg(f'''{head('Custos de operação','Orçamento','detalhado · 2/2','ink','lar', 74)}
  <div class="card" style="margin-top:26px; padding:16px 22px">{tabela(['Comunicação','Capacitação e eventos','Tecnologia e dados','Administração'])}
    <table style="margin-top:8px"><tbody>
      <tr><td><b>Subtotal dos custos diretos</b></td><td class="r"><b>{brl(direto)}</b></td></tr>
      <tr><td>Reserva para imprevistos (5%)</td><td class="r">{brl(reserva)}</td></tr>
      <tr style="background:var(--ink); color:#fff"><td style="font-weight:800; font-size:20px; border:0">TOTAL EM 12 MESES</td><td class="r" style="font-weight:800; font-size:20px; border:0">{brl(TOTAL)}</td></tr>
    </tbody></table>
  </div>
</div>''', 'Orçamento', 'Valores estimados em reais de 2026'))

# 11 RESUMO DO ORÇAMENTO + CENÁRIOS
seg = ''; acc = 0
for c,v in sorted(cat_tot.items(), key=lambda kv:-kv[1]):
    w = v/direto*100
    seg += f'<span style="width:{w:.2f}%; background:{CORES[c]}; height:100%; display:block; border-right:3px solid #fff"></span>'
leg = ''.join(f'<div style="display:grid; grid-template-columns:18px 1fr auto auto; gap:12px; align-items:center; font-size:19px; padding:7px 0; border-bottom:1px solid var(--line)"><span style="width:16px; height:16px; border-radius:4px; background:{CORES[c]}"></span><span>{c}</span><span style="color:var(--muted)">{v/direto*100:.0f}%</span><b style="font-variant-numeric:tabular-nums">{brl(v)}</b></div>' for c,v in sorted(cat_tot.items(), key=lambda kv:-kv[1]))
enx = round(TOTAL*0.42/1000)*1000; amp = round(TOTAL*1.62/1000)*1000
P.append(pg(f'''{head('Para onde vai o dinheiro','Resumo e','cenários','ink','lar')}
  <div class="card" style="margin-top:26px">
    <div style="display:flex; height:46px; border-radius:10px; overflow:hidden">{seg}</div>
    <div style="margin-top:16px">{leg}</div>
  </div>
  <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:14px; margin-top:18px">
    <div class="card"><p class="eyebrow" style="color:var(--muted)">Enxuto</p><p class="num" style="font-size:44px; margin-top:6px">{brl(enx)}</p><p style="font-size:17px; margin-top:6px; color:var(--muted)">Só o Polo 1 e o Polo 2, 6 agentes, sem telas</p></div>
    <div class="card dark"><p class="eyebrow" style="color:var(--lima)">Padrão · recomendado</p><p class="num" style="font-size:44px; margin-top:6px">{brl(TOTAL)}</p><p style="font-size:17px; margin-top:6px; color:#D7D9D2">3 polos, 7 municípios, 12 agentes</p></div>
    <div class="card"><p class="eyebrow" style="color:var(--muted)">Ampliado</p><p class="num" style="font-size:44px; margin-top:6px">{brl(amp)}</p><p style="font-size:17px; margin-top:6px; color:var(--muted)">10 municípios, 24 agentes, 2º ano de telas</p></div>
  </div>''', 'Orçamento', 'Cenários enxuto e ampliado estimados a partir do padrão'))

# 12 PARCERIAS
parc = [('Governo do Amapá (vigilância em saúde)','Testes, remédios, mosquiteiros, notificação e protocolos'),
        ('Prefeituras e secretarias de saúde','Postos, agentes comunitários, escolas e apoio logístico'),
        ('DSEI e lideranças indígenas','Entrada nas aldeias, tradução e agentes indígenas'),
        ('Cooperativas e associações de garimpeiros','Acesso aos barrancos e adesão dos trabalhadores'),
        ('Rádios comunitárias e igrejas','Mensagens diárias e confiança da população'),
        ('UNIFAP, IFAP e IEPA','Pesquisa, avaliação e estudantes voluntários'),
        ('Saúde da Guiana Francesa','Troca de informações na fronteira de Oiapoque')]
pr = ''.join(f'<tr><td><b>{a}</b></td><td>{b}</td></tr>' for a,b in parc)
P.append(pg(f'''{head('Com quem','Parcerias','e papéis','ink','verde')}
  <div class="card" style="margin-top:30px; padding:16px 24px"><table style="font-size:19px"><thead><tr><th>Parceiro</th><th>O que entra</th></tr></thead><tbody>{pr}</tbody></table></div>
  <div class="card dark" style="margin-top:18px"><p style="font-size:21px"><b style="color:var(--lima)">Papel da ibradep:</b> organizar, contratar, levar a equipe ao campo, comunicar e prestar contas. O diagnóstico oficial, o remédio e a notificação continuam com o SUS.</p></div>''', 'Parcerias'))

# 13 FINANCIAMENTO
fin = [('Termo de colaboração ou fomento','Parceria formal com Estado ou municípios pela Lei 13.019/2014 (marco das organizações da sociedade civil).'),
       ('Emendas parlamentares','Deputados e senadores do Amapá podem destinar recursos de saúde a projetos de entidades parceiras.'),
       ('Empresas da região','Mineradoras, energia, petróleo e varejo, por meio de programas sociais e ESG.'),
       ('Editais e fundações','Editais de saúde, Amazônia e clima de fundações nacionais e internacionais.'),
       ('Doação de insumos','Mosquiteiros e repelentes doados por empresas reduzem o custo de prevenção.')]
fn = ''.join(f'<div class="card" style="padding:22px 26px"><p class="H lar" style="font-size:32px">{a}</p><p style="font-size:19px; margin-top:4px; color:var(--muted)">{b}</p></div>' for a,b in fin)
P.append(pg(f'''{head('De onde vem o recurso','Como','financiar','ink','lar')}
  <div style="display:grid; gap:14px; margin-top:30px">{fn}</div>
  <div class="card" style="margin-top:16px; background:var(--lima-bg); border:0"><p style="font-size:20px"><b>Sugestão:</b> combinar um termo de colaboração com o Estado (base da equipe) com uma ou duas empresas patrocinadoras (prevenção e comunicação).</p></div>''', 'Financiamento'))

# 14 INDICADORES + RISCOS
ind = [('Casos nos polos atendidos','Mensal','−30% no ano'),('Tempo da febre até o teste','Semanal','70% em até 48 h'),('Tratamentos concluídos','Semanal','100%'),
       ('Testes em busca ativa','Mensal','15 mil no ano'),('Mosquiteiros em uso (visita de retorno)','Trimestral','80% em uso'),('Pessoas alcançadas','Mensal','40 mil no ano')]
ir = ''.join(f'<tr><td><b>{a}</b></td><td>{b}</td><td class="r">{c}</td></tr>' for a,b,c in ind)
riscos = [('Falta de testes ou remédio','Pedido trimestral ao Estado e estoque de segurança nos polos'),
          ('Recusa em garimpos','Entrar com a cooperativa e lideranças; atendimento sem fiscalização'),
          ('Chuva, rio baixo e acesso','Rotas alternativas, barco e calendário flexível'),
          ('Atraso no repasse','Cronograma de desembolso e reserva de 5%')]
rr = ''.join(f'<tr><td><b>{a}</b></td><td>{b}</td></tr>' for a,b in riscos)
P.append(pg(f'''{head('Acompanhar e prevenir problemas','Indicadores','e riscos','ink','lar')}
  <div class="card" style="margin-top:28px; padding:16px 24px"><table style="font-size:18.5px"><thead><tr><th>Indicador</th><th>Frequência</th><th class="r">Meta</th></tr></thead><tbody>{ir}</tbody></table></div>
  <div class="card" style="margin-top:18px; padding:16px 24px"><table style="font-size:18.5px"><thead><tr><th>Risco</th><th>Como evitar</th></tr></thead><tbody>{rr}</tbody></table></div>''', 'Monitoramento'))

# 15 PRÓXIMOS PASSOS
passos = [('Semana 1','Aprovar o plano e o cenário de orçamento na diretoria da ibradep'),
          ('Semana 2','Reunião com a vigilância em saúde do Estado e as 7 prefeituras'),
          ('Semana 3','Enviar propostas a parlamentares e a 3 empresas patrocinadoras'),
          ('Semana 4','Abrir seleção da equipe e encomendar os materiais da campanha')]
ps = ''.join(f'<div style="display:grid; grid-template-columns:200px 1fr; gap:22px; align-items:center"><div style="background:{c}; color:#fff; border-radius:14px; padding:20px; text-align:center"><p class="H" style="font-size:34px">{a}</p></div><div class="card" style="padding:22px 26px"><p style="font-size:22px">{b}</p></div></div>' for (a,b),c in zip(passos,['#002580','#00994C','#E8692C','#232523']))
P.append(pg(f'''{head('Começar agora','Próximos','30 dias','ink','lar')}
  <div style="display:grid; gap:18px; margin-top:36px">{ps}</div>
  <div class="card dark" style="margin-top:28px"><p style="font-size:22px">Começando em dezembro, a equipe estará formada em fevereiro e a prevenção chegará ao campo <b style="color:var(--lima)">antes do pico de junho</b>.</p></div>
  <p class="small" style="margin-top:24px">Todos os custos são estimativas para planejamento, com base em valores de mercado de 2026. Faça cotações locais antes de fechar o orçamento.</p>''', 'Próximos passos'))

# 16 DEDICATÓRIA
N[0] += 1
P.append(f'''<section class="p" style="padding:0; background:#1F5E2A; background-image:none">
  <div style="position:absolute; left:0; right:0; top:0; height:420px">{FLAG}</div>
  <div style="position:absolute; left:0; right:0; top:420px; height:10px; background:#232523"></div>
  <div style="position:absolute; left:90px; right:90px; top:520px; color:#fff">
    <p class="eyebrow" style="color:#E2F27A">#AmapáNoCombateÀMalária</p>
    <p style="font-size:28px; margin-top:44px; font-weight:500">Plano elaborado</p>
    <h2 class="H" style="font-size:140px; margin-top:12px"><span style="color:#fff">De Arthur Miguel</span><span style="color:#E2F27A">para a ibradep</span></h2>
    <p style="font-size:24px; margin-top:40px; max-width:820px; line-height:1.5">Para que nenhuma febre no Amapá fique sem teste, e nenhum tratamento fique pela metade.</p>
  </div>
  <p style="position:absolute; left:90px; bottom:60px; color:#D7E6D4; font-size:18px">Novembro de 2026</p>
</section>''')

html = '<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Plano de Combate à Malária</title>' + CSS + '</head><body>' + ''.join(P) + '</body></html>'
open('plano-malaria.html','w').write(html)
print('ok', len(P))
