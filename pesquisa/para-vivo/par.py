# "Pará Vivo": plano integrado de água limpa e combate à malária. Padrão do plano do Amapá, 1080x1350.
import json, re
raw = open('../pa-dl/flag.svg').read()
raw = raw[raw.index('<svg'):]
FLAG = re.sub(r'height="600\.00000"\s+width="900\.00000"', 'viewBox="0 0 900 600" preserveAspectRatio="xMidYMid slice" style="width:100%; height:100%; display:block"', raw, count=1)
brl = lambda v: 'R$ ' + f'{v:,.0f}'.replace(',', '.')
mi = lambda v: 'R$ ' + f'{v/1e6:,.1f}'.replace('.', ',') + ' mi'
fmt = lambda v: f'{v:,.0f}'.replace(',', '.')

ORC = [
 ('Pessoal', [('Coordenação geral',1,12,10000,'pessoa/mês'),('Coordenação de saúde (malária)',1,12,9000,'pessoa/mês'),('Coordenação de água e ambiente',1,12,9000,'pessoa/mês'),
   ('Supervisores de polo',5,12,6000,'pessoa/mês'),('Agentes de campo de malária',20,12,3300,'pessoa/mês'),('Técnicos ambientais',5,12,4500,'pessoa/mês'),
   ('Comunicação',2,12,4500,'pessoa/mês'),('Analista de dados',1,12,6500,'pessoa/mês'),('Administrativo-financeiro',2,12,4500,'pessoa/mês'),('Piloteiros e motoristas',6,12,3000,'pessoa/mês')]),
 ('Logística', [('Caminhonetes 4x4 (aluguel)',3,12,9500,'veículo/mês'),('Combustível dos veículos',3,12,2800,'veículo/mês'),('Voadeiras com motor (compra)',4,1,45000,'unidade'),
   ('Combustível dos barcos',4,12,3500,'barco/mês'),('Diárias de campo',30,96,130,'diária'),('Horas de voo para áreas isoladas',40,1,4500,'hora')]),
 ('Malária: prevenção', [('Mosquiteiros impregnados',10000,1,45,'unidade'),('Kits de repelente para trabalhadores',5000,1,25,'kit')]),
 ('Água: monitorar e limpar', [('Estações automáticas de monitoramento',10,1,80000,'unidade'),('Manutenção das estações',10,12,1500,'estação/mês'),
   ('Análises de mercúrio em peixes e cabelo',3000,1,150,'amostra'),('Ecobarreiras nos canais de Belém',10,1,30000,'unidade'),('Operação das ecobarreiras',10,12,3000,'barreira/mês'),
   ('Filtros e cloração para comunidades',1000,1,350,'família'),('Banheiros com biodigestor em palafitas',300,1,4000,'casa')]),
 ('Comunicação', [('Rádios comunitárias',10,12,1500,'rádio/mês'),('Material impresso',1,1,60000,'lote'),('Vídeos e áudios em português e línguas indígenas',1,1,50000,'lote'),
   ('Impulsionamento nas redes',1,12,2500,'mês'),('Barco e carro de som',1,1,30000,'lote')]),
 ('Capacitação', [('Formação de agentes e multiplicadores',1,1,80000,'lote'),('Oficinas em aldeias, garimpos e comunidades',1,1,50000,'lote'),('Lançamento e seminário final',1,1,30000,'lote')]),
 ('Tecnologia', [('Celulares e tablets resistentes',30,1,2000,'unidade'),('Internet via satélite: equipamento',5,1,2500,'polo'),('Internet via satélite: mensalidade',5,12,600,'polo/mês'),('App offline e painel de dados',1,1,80000,'lote')]),
 ('Administração', [('Bases nos polos (aluguel)',5,12,2200,'base/mês'),('Contabilidade, auditoria e seguros',1,1,60000,'ano')]),
]
CT = {c: sum(q*m*u for _,q,m,u,_ in it) for c,it in ORC}
DIR = sum(CT.values()); RES = round(DIR*0.05); TOTAL = DIR + RES
COR = {'Pessoal':'#1E2230','Logística':'#E8692C','Malária: prevenção':'#2E7D4F','Água: monitorar e limpar':'#0071CE','Comunicação':'#C9A227','Capacitação':'#7FB77E','Tecnologia':'#6B5B95','Administração':'#9A9A92'}
PESSOAS = 80000
print(TOTAL, CT)

CSS = '''
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Anton&family=Poppins:ital,wght@0,400;0,500;0,600;0,700;0,800;1,700&family=IBM+Plex+Mono:wght@500&display=swap">
<style>
/* Padrão do plano do Amapá com as cores do Pará: vermelho, branco e o azul da estrela. */
:root{
  --paper:#FAFAF8; --grid:rgba(30,35,45,.05); --ink:#1E2230; --muted:#5C6170; --line:rgba(30,35,45,.12);
  --verm:#D9202F; --verm-bg:#FBE1E3; --azul:#0071CE; --azul-bg:#DDEBF8; --mata:#2E7D4F; --mata-bg:#E0F0E6; --lar:#E8692C; --lar-bg:#FCE7DC; --ouro:#B8902A; --ouro-bg:#F5EDD6; --card:#FFFFFF;
  --fh:"Anton", "Impact", "Arial Narrow", sans-serif; --fb:"Poppins", "Segoe UI", Arial, sans-serif; --fm:"IBM Plex Mono", monospace;
}
@page{ size:1080px 1350px; margin:0 }
*{box-sizing:border-box; margin:0; padding:0}
body{font-family:var(--fb); color:var(--ink); -webkit-print-color-adjust:exact; print-color-adjust:exact; background:var(--paper)}
.p{width:1080px; height:1350px; position:relative; overflow:hidden; page-break-after:always; break-after:page; background-color:var(--paper);
   background-image:linear-gradient(var(--grid) 1px, transparent 1px), linear-gradient(90deg, var(--grid) 1px, transparent 1px); background-size:36px 36px; padding:110px 90px 0}
.p:last-child{page-break-after:auto}
.H{font-family:var(--fh); font-weight:400; text-transform:uppercase}
.H > span{display:block; line-height:1.0}
.verm{color:var(--verm)} .azul{color:var(--azul)} .mata{color:var(--mata)} .ink{color:var(--ink)} .lar{color:var(--lar)} .ouro{color:var(--ouro)}
p{font-size:21px; line-height:1.46}
.card{background:var(--card); border-radius:18px; padding:24px 28px; box-shadow:0 1px 0 rgba(30,35,45,.06), 0 10px 30px -18px rgba(30,35,45,.35); border:1px solid rgba(30,35,45,.06)}
.dark{background:var(--ink); color:#fff; border:0}
.num{font-family:var(--fh); font-weight:400; line-height:.95; font-variant-numeric:tabular-nums}
.small{font-size:16px; color:var(--muted); line-height:1.4}
.eyebrow{font-family:var(--fm); font-size:16px; letter-spacing:.12em; text-transform:uppercase; color:var(--verm)}
.top{position:absolute; left:90px; right:90px; top:44px; display:flex; justify-content:space-between; font-size:16px; color:var(--muted)}
.top b{color:var(--ink); font-weight:800}
.stripe{position:absolute; left:0; top:0; bottom:0; width:14px; display:flex; flex-direction:column}
.stripe i{flex:1}
.foot{position:absolute; left:90px; right:90px; bottom:42px; display:flex; justify-content:space-between; font-size:15px; color:var(--muted)}
ul.dot{list-style:none; display:grid; gap:10px}
ul.dot li{position:relative; padding-left:28px; font-size:20px; line-height:1.4}
ul.dot li::before{content:"★"; position:absolute; left:0; top:-1px; color:var(--azul); font-size:17px}
table{border-collapse:collapse; width:100%; font-size:17px}
th{font-family:var(--fm); font-weight:500; font-size:13px; letter-spacing:.08em; text-transform:uppercase; color:var(--muted); text-align:left; padding:9px 10px; border-bottom:2px solid var(--ink)}
td{padding:7px 10px; border-bottom:1px solid var(--line); vertical-align:top}
td.r, th.r{text-align:right; font-variant-numeric:tabular-nums; white-space:nowrap}
tr.cat td{font-weight:800; background:rgba(30,35,45,.04)}
.pill{display:inline-block; font-weight:700; font-size:15px; padding:5px 12px; border-radius:999px}
.part{display:inline-block; font-family:var(--fm); font-size:14px; letter-spacing:.1em; padding:6px 12px; border-radius:6px; color:#fff}
</style>'''
STRIPE = '<div class="stripe"><i style="background:var(--verm)"></i><i style="background:#fff; border-right:1px solid var(--line)"></i><i style="background:var(--azul)"></i></div>'
N = [0]
def pg(inner, secao, fonte=''):
    N[0] += 1
    return (f'<section class="p">{STRIPE}<div class="top"><span><b>Pará Vivo</b> · água limpa e malária zero</span><span>{secao}</span></div>'
            f'{inner}<div class="foot"><span>{fonte}</span><span>{N[0]:02d}</span></div></section>')
def head(eye, l1, l2, c1='ink', c2='verm', size=92):
    return f'<p class="eyebrow">{eye}</p><h2 class="H" style="font-size:{size}px; margin-top:12px"><span class="{c1}">{l1}</span><span class="{c2}">{l2}</span></h2>'
def parte(txt, cor):
    N[0] += 1
    return f'''<section class="p" style="padding:0; background:{cor}; background-image:none">
  <div style="position:absolute; left:90px; right:90px; top:420px; color:#fff">
    <p style="font-family:var(--fm); font-size:20px; letter-spacing:.14em">{txt[0]}</p>
    <h2 class="H" style="font-size:150px; margin-top:20px"><span>{txt[1]}</span><span style="opacity:.75">{txt[2]}</span></h2>
    <p style="font-size:26px; margin-top:30px; max-width:820px">{txt[3]}</p>
  </div>
  <p style="position:absolute; right:90px; bottom:50px; color:#fff; font-size:16px">{N[0]:02d}</p>
</section>'''
P = []

# 1 CAPA
N[0] += 1
P.append(f'''<section class="p" style="padding:0">
  <div style="position:absolute; left:0; right:0; top:0; height:600px">{FLAG}</div>
  <div style="position:absolute; left:0; right:0; top:600px; height:10px; background:var(--ink)"></div>
  <div style="position:absolute; left:90px; right:90px; top:668px">
    <p class="eyebrow">Plano integrado · Estado do Pará</p>
    <h1 class="H" style="font-size:136px; margin-top:12px"><span class="ink">Pará vivo</span><span class="azul" style="font-size:72px; margin-top:6px">Água limpa</span><span class="verm" style="font-size:72px">e malária zero</span></h1>
    <div style="display:flex; gap:12px; margin-top:28px; flex-wrap:wrap">
      <span class="pill" style="background:var(--ink); color:#fff">12 meses</span>
      <span class="pill" style="background:var(--azul-bg); color:var(--azul)">5 polos</span>
      <span class="pill" style="background:var(--verm-bg); color:var(--verm)">{brl(TOTAL)}</span>
    </div>
  </div>
  <p style="position:absolute; left:90px; bottom:50px; font-size:16px; color:var(--muted)">Pesquisa e plano · novembro de 2026</p>
</section>''')

# 2 RESUMO
P.append(pg(f'''{head('Resumo executivo','Duas crises,','uma causa comum')}
  <p style="margin-top:22px; font-size:23px; max-width:880px">No Pará, o <b>garimpo ilegal</b> espalha malária e mercúrio ao mesmo tempo, e a falta de <b>esgoto tratado</b> adoece as cidades. Este plano ataca as duas frentes juntas, nos mesmos territórios, com a mesma equipe de campo.</p>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-top:26px">
    <div class="card" style="border-top:8px solid var(--azul)"><p class="eyebrow" style="color:var(--azul)">Frente 1 · Água limpa</p><ul class="dot" style="margin-top:12px"><li>10 estações medindo a água</li><li>3.000 análises de mercúrio</li><li>10 ecobarreiras em Belém</li><li>1.000 famílias com água segura</li><li>300 banheiros em palafitas</li></ul></div>
    <div class="card" style="border-top:8px solid var(--verm)"><p class="eyebrow">Frente 2 · Malária zero</p><ul class="dot" style="margin-top:12px"><li>−30% de casos nos polos</li><li>20 agentes em busca ativa</li><li>10.000 mosquiteiros</li><li>Tratamento acompanhado até o fim</li><li>Ação nas terras indígenas</li></ul></div>
  </div>
  <div class="card dark" style="margin-top:16px; display:grid; grid-template-columns:1fr auto; gap:20px; align-items:center">
    <div><p class="eyebrow" style="color:#F6B9BF">Investimento total · 12 meses</p><p class="num" style="font-size:76px; margin-top:8px">{brl(TOTAL)}</p></div>
    <div style="text-align:right"><p style="font-size:18px; color:#C9CDD6">cerca de</p><p class="num" style="font-size:52px; color:#F6B9BF">{brl(TOTAL/PESSOAS)}</p><p style="font-size:18px; color:#C9CDD6">por pessoa alcançada</p></div>
  </div>''', 'Resumo', 'Valores estimados para planejamento'))

# 3 PARÁ EM NÚMEROS
P.append(pg(f'''{head('Contexto','O Pará','em números','ink','azul')}
  <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:14px; margin-top:28px">
    <div class="card"><p class="num azul" style="font-size:60px">8,1 mi</p><p style="font-size:17px; margin-top:6px">habitantes (Censo 2022), o estado mais populoso da Amazônia</p></div>
    <div class="card"><p class="num azul" style="font-size:60px">144</p><p style="font-size:17px; margin-top:6px">municípios, muitos acessíveis só por rio ou avião</p></div>
    <div class="card"><p class="num verm" style="font-size:60px">2.098 km²</p><p style="font-size:17px; margin-top:6px">desmatados em 2025, o maior valor entre os estados (PRODES)</p></div>
  </div>
  <div class="card" style="margin-top:16px">
    <p class="eyebrow" style="color:var(--muted)">Os grandes rios</p>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px 28px; margin-top:12px">
      <p style="font-size:18px"><b>Amazonas</b> · corta o estado de oeste a leste até o Marajó</p>
      <p style="font-size:18px"><b>Tapajós</b> · Santarém, Itaituba e terras Munduruku</p>
      <p style="font-size:18px"><b>Xingu</b> · Altamira e a usina de Belo Monte</p>
      <p style="font-size:18px"><b>Tocantins</b> · Marabá, Tucuruí e a baía do Marajó</p>
      <p style="font-size:18px"><b>Rio Pará e Guamá</b> · Belém e Barcarena</p>
      <p style="font-size:18px"><b>Trombetas</b> · Oriximiná e a mineração de bauxita</p>
    </div>
  </div>
  <div class="card dark" style="margin-top:16px"><p style="font-size:20px"><b style="color:#F6B9BF">Belém sediou a COP30</b> em 2025. O mundo olhou para o Pará. Agora é a hora de mostrar resultado em água e saúde.</p></div>''',
  'Contexto', 'IBGE (Censo 2022); INPE/PRODES 2025'))

# PARTE A
P.append(parte(('PARTE A','Água','limpa','Saneamento, mercúrio e poluição dos rios paraenses.'), '#0071CE'))

# 5 SANEAMENTO
P.append(pg(f'''{head('Saneamento','Cidades que','despejam no rio','ink','azul')}
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-top:28px">
    <div class="card"><p class="num verm" style="font-size:78px">25%</p><p style="font-size:18px; margin-top:6px">da população de Belém tem esgotamento adequado (Ranking do Saneamento 2026, Trata Brasil)</p></div>
    <div class="card"><p class="num verm" style="font-size:78px">29 de 50</p><p style="font-size:18px; margin-top:6px">piores municípios do país em saneamento ficam na Amazônia Legal (ranking de 2025)</p></div>
  </div>
  <div class="card" style="margin-top:16px">
    <p class="eyebrow" style="color:var(--muted)">O que isso causa</p>
    <ul class="dot" style="margin-top:12px"><li>Esgoto direto nos canais de Belém e na baía do Guajará</li><li>Diarreia, hepatite A e verminoses, sobretudo em crianças</li><li>Alagamentos com água contaminada nas baixadas</li><li>Santarém, Ananindeua e Belém aparecem entre os piores do país nos rankings recentes do Trata Brasil</li></ul>
  </div>
  <div class="card" style="margin-top:16px; background:var(--azul-bg); border:0"><p style="font-size:19px"><b class="azul">Desafio amazônico:</b> casas sobre palafitas e áreas alagáveis não recebem rede comum. É preciso soluções descentralizadas, como banheiros com biodigestor e tratamento por bairro.</p></div>''',
  'Saneamento', 'Instituto Trata Brasil (rankings 2025 e 2026), via O Liberal e InfoMoney'))

# 6 MERCÚRIO
P.append(pg(f'''{head('Garimpo e mercúrio','Veneno','no Tapajós','ink','verm')}
  <p style="margin-top:20px; font-size:21px; max-width:880px">O garimpo de ouro usa mercúrio, que vai para o rio, entra nos peixes e chega às pessoas. Estudo da Fiocruz com o WWF-Brasil em três aldeias Munduruku do médio Tapajós (2019):</p>
  <div style="display:grid; grid-template-columns:repeat(3,1fr); gap:14px; margin-top:22px">
    <div class="card"><p class="num verm" style="font-size:66px">88 de 88</p><p style="font-size:16px; margin-top:6px">peixes analisados tinham mercúrio</p></div>
    <div class="card"><p class="num verm" style="font-size:66px">200</p><p style="font-size:16px; margin-top:6px">indígenas avaliados, todos com mercúrio no corpo; mais da metade acima do limite seguro</p></div>
    <div class="card"><p class="num verm" style="font-size:66px">4 a 18×</p><p style="font-size:16px; margin-top:6px">acima do limite de ingestão diária recomendado nos EUA</p></div>
  </div>
  <div class="card" style="margin-top:16px"><p style="font-size:19px"><b>Novo alerta (2026):</b> resultados preliminares da Fiocruz indicam gestantes Munduruku com mercúrio cerca de 4,5 vezes acima do limite seguro da OMS. O mercúrio afeta o cérebro dos bebês em formação.</p></div>
  <div class="card dark" style="margin-top:16px"><p style="font-size:20px"><b style="color:#F6B9BF">O que fazer já:</b> analisar peixes e pessoas, orientar o consumo (preferir peixes que não comem outros peixes), acompanhar gestantes e crianças e combater o garimpo ilegal com o Estado e a União.</p></div>''',
  'Mercúrio', 'Fiocruz e WWF-Brasil (2020); Agência Brasil (jun/2026)'))

# 7 CAUSAS
causas = [('Esgoto urbano','Belém, Ananindeua, Santarém e cidades do interior sem tratamento.','#D9202F'),
          ('Garimpo','Mercúrio e lama no Tapajós, Jamanxim e afluentes.','#E8692C'),
          ('Mineração e indústria','Bauxita, alumina e ferro no Trombetas, em Barcarena e no Sudeste.','#6B5B95'),
          ('Desmatamento','Solo exposto vira lama no rio e esquenta a água.','#B8902A'),
          ('Lixo','Canais de Belém entupidos e lixões nas cidades do interior.','#0071CE'),
          ('Navegação','Óleo e esgoto de barcos nos portos e rios de grande tráfego.','#1E2230')]
cc = ''.join(f'<div class="card" style="padding:20px 24px; border-left:8px solid {c}"><p class="H" style="font-size:32px">{a}</p><p style="font-size:18px; color:var(--muted); margin-top:4px">{b}</p></div>' for a,b,c in causas)
P.append(pg(f'''{head('De onde vem','Seis fontes','de poluição','ink','azul')}
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px; margin-top:28px">{cc}</div>
  <div class="card" style="margin-top:14px; background:var(--lar-bg); border:0"><p style="font-size:19px"><b class="lar">Barcarena:</b> em 2018, depois de chuvas fortes, a refinaria Hydro Alunorte foi alvo de denúncias de contaminação e reconheceu lançamentos de água não licenciados. O caso mostra a importância de monitorar a água o tempo todo.</p></div>''', 'Causas'))

# 8 SOLUÇÕES ÁGUA
sol = [('Banheiro com biodigestor','Palafitas e áreas alagáveis','Trata o esgoto na própria casa','#0071CE'),
       ('Tratamento por bairro','Baixadas de Belém e Ananindeua','Pequenas estações e jardins filtrantes','#0071CE'),
       ('Ecobarreiras nos canais','Belém','Retêm o lixo antes da baía','#0071CE'),
       ('Água segura em casa','Ribeirinhos e aldeias','Filtro e cloração simples','#2E7D4F'),
       ('Monitorar mercúrio','Tapajós e afluentes','Análise de peixes, cabelo e água','#D9202F'),
       ('Guia de consumo de peixe','Comunidades do Tapajós','Quais peixes comer e com que frequência','#D9202F'),
       ('Sensores nos rios','5 polos','Oxigênio, turbidez e temperatura a cada 15 min','#6B5B95')]
stb = ''.join(f'<tr><td><span style="display:inline-block; width:12px; height:12px; border-radius:3px; background:{c}; margin-right:8px"></span><b>{a}</b></td><td>{b}</td><td style="color:var(--muted)">{d}</td></tr>' for a,b,d,c in sol)
P.append(pg(f'''{head('Soluções','Como limpar','as águas do Pará','ink','azul')}
  <div class="card" style="margin-top:26px; padding:14px 22px"><table style="font-size:17.5px"><thead><tr><th>Solução</th><th>Onde</th><th>O que faz</th></tr></thead><tbody>{stb}</tbody></table></div>
  <div class="card dark" style="margin-top:16px"><p style="font-size:20px"><b style="color:#F6B9BF">As grandes obras de esgoto</b> são da companhia de saneamento e das prefeituras. Este plano faz o que a obra não alcança: palafitas, comunidades, lixo e vigilância da água.</p></div>''', 'Soluções'))

# PARTE B
P.append(parte(('PARTE B','Malária','zero','Casos, garimpo, calendário e o que fazer.'), '#D9202F'))

# 10 MALÁRIA NÚMEROS
anos = [('2024',24297,'#9A9A92'),('2025',17514,'#D9202F')]
mxv = 24297
bars = ''.join(f'<div style="display:grid; grid-template-columns:90px 1fr 150px; gap:14px; align-items:center; padding:8px 0"><span class="num" style="font-size:34px">{a}</span><span style="height:46px; background:rgba(30,35,45,.06); border-radius:0 8px 8px 0; overflow:hidden"><span style="display:block; height:100%; width:{v/mxv*100:.1f}%; background:{c}; border-radius:0 8px 8px 0"></span></span><span class="num" style="font-size:40px; text-align:right">{fmt(v)}</span></div>' for a,v,c in anos)
P.append(pg(f'''{head('Malária no Pará','Caiu, mas','segue alta','ink','verm')}
  <div class="card" style="margin-top:26px"><p class="eyebrow" style="color:var(--muted)">Casos confirmados no ano · Sespa</p>{bars}</div>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:14px; margin-top:16px">
    <div class="card"><p class="num verm" style="font-size:60px">77%</p><p style="font-size:17px; margin-top:6px">dos casos de janeiro a julho de 2025 vieram de Jacareacanga (6.127) e Itaituba (2.589)</p></div>
    <div class="card"><p class="num mata" style="font-size:60px">−34,2%</p><p style="font-size:17px; margin-top:6px">no 1º trimestre de 2025: 4.467 casos (Ministério da Saúde)</p></div>
  </div>
  <div class="card" style="margin-top:14px"><p style="font-size:19px"><b>Municípios prioritários:</b> Jacareacanga, Itaituba, Bagre, Anajás e Oriximiná. A maioria das infecções vem de áreas de garimpo e zonas rurais.</p></div>
  <p class="small" style="margin-top:10px">As fontes divergem sobre o percentual de queda entre 2024 e 2025. Confira o boletim mais recente da Sespa antes de citar.</p>''',
  'Malária', 'Sespa, boletins de malária 2025; Ministério da Saúde'))

# 11 GARIMPO LIGA AS CRISES
P.append(pg(f'''{head('O elo','O garimpo liga','as duas crises','ink','lar')}
  <div class="card" style="margin-top:28px; padding:24px">
    <svg viewBox="0 0 880 330" style="width:100%; display:block"><g font-family="Poppins" text-anchor="middle">
      <rect x="320" y="10" width="240" height="80" rx="14" fill="#E8692C"/><text x="440" y="45" fill="#fff" font-size="22" font-weight="800">Garimpo ilegal</text><text x="440" y="72" fill="#fff" font-size="14">Tapajós · Jamanxim · Munduruku</text>
      <path d="M380 90 C 300 140, 230 150, 190 190" stroke="#1E2230" stroke-width="2.5" fill="none"/><path d="M500 90 C 580 140, 650 150, 690 190" stroke="#1E2230" stroke-width="2.5" fill="none"/>
      <rect x="40" y="190" width="300" height="120" rx="14" fill="#D9202F"/><text x="190" y="232" fill="#fff" font-size="22" font-weight="800">Malária</text><text x="190" y="260" fill="#fff" font-size="14">Cavas e poças viram criadouro</text><text x="190" y="282" fill="#fff" font-size="14">Migração espalha o parasita</text>
      <rect x="540" y="190" width="300" height="120" rx="14" fill="#0071CE"/><text x="690" y="232" fill="#fff" font-size="22" font-weight="800">Mercúrio</text><text x="690" y="260" fill="#fff" font-size="14">Rio contaminado e peixe com veneno</text><text x="690" y="282" fill="#fff" font-size="14">Risco para gestantes e bebês</text>
    </g></svg>
  </div>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:14px; margin-top:16px">
    <div class="card"><p class="H" style="font-size:30px">Mesmo território</p><p style="font-size:18px; color:var(--muted); margin-top:6px">Jacareacanga e Itaituba concentram tanto os casos de malária quanto o garimpo no Tapajós.</p></div>
    <div class="card"><p class="H" style="font-size:30px">Mesma equipe</p><p style="font-size:18px; color:var(--muted); margin-top:6px">O agente que faz o teste de malária coleta a amostra de cabelo para mercúrio e orienta sobre o peixe.</p></div>
  </div>
  <div class="card dark" style="margin-top:14px"><p style="font-size:20px">Atacar o garimpo ilegal reduz as duas crises de uma vez. É por isso que este plano junta água e saúde.</p></div>''', 'Elo', 'Casa Civil e Secom (dez/2024); Sespa; Fiocruz'))

# 12 CALENDÁRIO E O QUE FAZER
meses = ['JAN','FEV','MAR','ABR','MAI','JUN','JUL','AGO','SET','OUT','NOV','DEZ']
chuva = [5,5,5,5,4,3,2,1,1,1,2,3]; risco = [1,1,1,1,2,3,3,3,3,2,1,1]
cr = {1:'#DADAD3',2:'#F6B9BF',3:'#D9202F'}
cal = ''.join(f'<div style="display:grid; gap:6px; justify-items:center"><span style="width:40px; height:{chuva[i]*20}px; background:#5AA0D6; border-radius:4px 4px 0 0; align-self:end"></span><span style="width:52px; height:52px; border-radius:10px; background:{cr[risco[i]]}"></span><span style="font-weight:700; font-size:15px">{m}</span></div>' for i,m in enumerate(meses))
P.append(pg(f'''{head('Quando e como','Calendário','e prevenção','ink','verm')}
  <div class="card" style="margin-top:26px">
    <div style="display:grid; grid-template-columns:repeat(12,1fr); align-items:end; height:200px">{cal}</div>
    <p class="small" style="margin-top:12px">Barras azuis: chuva. Quadrados: risco de malária (vermelho = maior). Padrão amazônico; confirme com os dados mensais da Sespa por município.</p>
  </div>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:14px; margin-top:14px">
    <div class="card"><p class="eyebrow">Para a população</p><ul class="dot" style="margin-top:10px"><li style="font-size:18px">Febre? Teste no mesmo dia, de graça no SUS</li><li style="font-size:18px">Tome o remédio até o fim</li><li style="font-size:18px">Mosquiteiro e repelente ao entardecer e ao amanhecer</li><li style="font-size:18px">Prefira peixes que não comem outros peixes</li></ul></div>
    <div class="card"><p class="eyebrow" style="color:var(--azul)">Para os gestores</p><ul class="dot" style="margin-top:10px"><li style="font-size:18px">Busca ativa em garimpos e aldeias</li><li style="font-size:18px">Tratamento supervisionado e tafenoquina com teste de G6PD</li><li style="font-size:18px">Mosquiteiros antes de junho</li><li style="font-size:18px">Mercúrio no pré-natal das áreas de garimpo</li></ul></div>
  </div>''', 'Calendário'))

# PARTE C
P.append(parte(('PARTE C','Plano','integrado','Onde, quem, quando, quanto custa e como financiar.'), '#1E2230'))

# 14 MAPA POLOS
geo = json.load(open('../dados/uf.json'))
g = [f for f in geo['features'] if f['properties']['sigla']=='PA'][0]['geometry']
rings = [p[0] for p in g['coordinates']] if g['type']=='MultiPolygon' else [g['coordinates'][0]]
X0,X1,Y0,Y1 = -59.2,-45.8,-10.1,2.8
W=860; H=int(W*(Y1-Y0)/(X1-X0))
px=lambda x:(x-X0)/(X1-X0)*W; py=lambda y:(Y1-y)/(Y1-Y0)*H
path=''.join('M'+' L'.join(f'{px(a):.1f},{py(b):.1f}' for a,b in r[::2])+'Z' for r in rings)
POLOS = [('Tapajós','Itaituba e Jacareacanga','Malária, garimpo e mercúrio','#E8692C',[('Itaituba',-4.28,-55.98),('Jacareacanga',-6.22,-57.75)]),
         ('Marajó','Anajás e Bagre','Malária e água segura','#2E7D4F',[('Anajás',-0.98,-49.94),('Bagre',-1.90,-50.20)]),
         ('Grande Belém','Belém, Ananindeua e Barcarena','Esgoto, lixo e indústria','#0071CE',[('Belém',-1.46,-48.49),('Barcarena',-1.51,-48.62)]),
         ('Baixo Amazonas','Santarém e Oriximiná','Saneamento e malária','#6B5B95',[('Santarém',-2.44,-54.71),('Oriximiná',-1.77,-55.86)]),
         ('Xingu e Sudeste','Altamira e Marabá','Rios, mineração e água','#B8902A',[('Altamira',-3.20,-52.21),('Marabá',-5.37,-49.12)])]
pins=''
for i,(n,c,d,cor,cs) in enumerate(POLOS):
    for (cn,la,lo) in cs:
        pins += f'<circle cx="{px(lo):.1f}" cy="{py(la):.1f}" r="13" fill="{cor}" stroke="#fff" stroke-width="3"/><text x="{px(lo):.1f}" y="{py(la)+5:.1f}" text-anchor="middle" font-family="Poppins" font-size="13" font-weight="800" fill="#fff">{i+1}</text>'
lb = {'Itaituba':(18,6,'start'),'Jacareacanga':(18,6,'start'),'Anajás':(-18,-4,'end'),'Bagre':(-18,8,'end'),'Belém':(18,-6,'start'),'Barcarena':(4,30,'middle'),'Santarém':(18,-4,'start'),'Oriximiná':(-18,-4,'end'),'Altamira':(18,6,'start'),'Marabá':(18,6,'start')}
for i,(n,c,d,cor,cs) in enumerate(POLOS):
    for (cn,la,lo) in cs:
        dx,dy,an = lb[cn]
        pins += f'<text x="{px(lo)+dx:.1f}" y="{py(la)+dy:.1f}" text-anchor="{an}" font-family="Poppins" font-size="18" font-weight="700" fill="#1E2230">{cn}</text>'
mapa = f'<svg viewBox="-20 -10 {W+40} {H+20}" style="height:610px; width:auto; max-width:100%; display:block; margin:0 auto"><path d="{path}" fill="#EFEDE8" stroke="#1E2230" stroke-width="1.5"/>{pins}</svg>'
pl = ''.join(f'<div style="display:grid; grid-template-columns:30px 1fr; gap:10px; align-items:start"><span style="width:30px; height:30px; border-radius:50%; background:{cor}; color:#fff; font-weight:800; display:grid; place-items:center">{i+1}</span><div><p style="font-size:17px"><b>{n}</b> · {c}</p><p style="font-size:15px; color:var(--muted)">{d}</p></div></div>' for i,(n,c,d,cor,cs) in enumerate(POLOS))
P.append(pg(f'''{head('Onde atuar','Cinco polos','de ação','ink','azul')}
  <div class="card" style="margin-top:22px; padding:12px">{mapa}</div>
  <div class="card" style="margin-top:14px; display:grid; grid-template-columns:1fr 1fr; gap:12px 24px">{pl}</div>''', 'Polos', 'Localização aproximada das sedes'))

# 15 EIXOS
eixos = [('01','Busca ativa e tratamento','Teste de malária no garimpo, na aldeia e no rio; tratamento acompanhado até a cura.','#D9202F'),
         ('02','Mercúrio sob vigilância','Análises de peixe, cabelo e água; acompanhamento de gestantes e crianças.','#E8692C'),
         ('03','Água segura e saneamento','Filtros, cloração, banheiros com biodigestor e tratamento por bairro.','#0071CE'),
         ('04','Rios sem lixo','Ecobarreiras nos canais de Belém e mutirões nas cidades.','#6B5B95'),
         ('05','Comunicação em várias línguas','Rádio, barco de som, redes e agentes indígenas.','#B8902A'),
         ('06','Dados abertos','Estações nos rios, app offline e painel público por polo.','#1E2230')]
ex = ''.join(f'<div class="card" style="display:grid; grid-template-columns:86px 1fr; gap:18px; padding:20px 24px"><div style="background:{c}; border-radius:14px; display:grid; place-items:center; height:86px"><p class="num" style="font-size:40px; color:#fff">{n}</p></div><div><p class="H" style="font-size:31px">{t}</p><p style="font-size:18px; color:var(--muted); margin-top:4px">{d}</p></div></div>' for n,t,d,c in eixos)
P.append(pg(f'''{head('Como agir','Seis eixos','de ação')}
  <div style="display:grid; gap:12px; margin-top:26px">{ex}</div>''', 'Eixos'))

# 16 EQUIPE
eq = [('Coordenação geral','1'),('Coordenação de saúde','1'),('Coordenação de água e ambiente','1'),('Supervisores de polo','5'),('Agentes de campo de malária','20'),
      ('Técnicos ambientais','5'),('Comunicação','2'),('Analista de dados','1'),('Administrativo-financeiro','2'),('Piloteiros e motoristas','6')]
tot = sum(int(b) for a,b in eq)
et = ''.join(f'<tr><td><b>{a}</b></td><td class="r">{b}</td></tr>' for a,b in eq)
P.append(pg(f'''{head('Quem faz','Equipe de',f'{tot} pessoas','ink','mata')}
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-top:26px; align-items:start">
    <div class="card" style="padding:14px 22px"><table style="font-size:17.5px"><thead><tr><th>Função</th><th class="r">Qtd.</th></tr></thead><tbody>{et}</tbody></table></div>
    <div style="display:grid; gap:14px">
      <div class="card"><p class="H" style="font-size:30px">Por polo</p><p style="font-size:18px; color:var(--muted); margin-top:6px">1 supervisor, 4 agentes de malária, 1 técnico ambiental e 1 piloteiro ou motorista.</p></div>
      <div class="card"><p class="H" style="font-size:30px">Gente do lugar</p><p style="font-size:18px; color:var(--muted); margin-top:6px">Prioridade para moradores dos polos e agentes indígenas indicados pelas lideranças.</p></div>
      <div class="card dark"><p style="font-size:18px"><b style="color:#F6B9BF">Diagnóstico e remédio</b> seguem com o SUS. A equipe leva, acompanha e registra.</p></div>
    </div>
  </div>''', 'Equipe'))

# 17 CRONOGRAMA
tar = [('Contratar e formar a equipe',0,2,'#1E2230'),('Acordos com Estado, municípios, DSEI e lideranças',0,2,'#1E2230'),('Instalar estações nos rios',2,4,'#0071CE'),
       ('Ecobarreiras nos canais de Belém',2,4,'#0071CE'),('Mosquiteiros e repelentes',3,6,'#2E7D4F'),('Busca ativa de malária',3,10,'#D9202F'),
       ('Coleta de amostras de mercúrio',3,9,'#E8692C'),('Filtros e banheiros com biodigestor',4,11,'#0071CE'),('Campanha de rádio, barco e redes',3,10,'#B8902A'),
       ('Tratamento supervisionado',2,12,'#D9202F'),('Painel público e relatórios',2,12,'#6B5B95'),('Avaliação e seminário final',10,12,'#1E2230')]
M = ['JAN','FEV','MAR','ABR','MAI','JUN','JUL','AGO','SET','OUT','NOV','DEZ']; cw=46
hdr = ''.join(f'<div style="width:{cw}px; text-align:center; font-family:var(--fm); font-size:11px; color:{"#D9202F" if 5<=i<=8 else "#5C6170"}">{m}</div>' for i,m in enumerate(M))
gl = ''.join(f'<div style="display:grid; grid-template-columns:290px {cw*12}px; align-items:center; padding:7px 0; border-bottom:1px solid var(--line)"><span style="font-size:15.5px; font-weight:600">{t}</span><div style="position:relative; height:20px; background:repeating-linear-gradient(90deg, transparent 0 {cw-1}px, rgba(30,35,45,.08) {cw-1}px {cw}px)"><span style="position:absolute; left:{a*cw+3}px; width:{(b-a)*cw-6}px; top:2px; bottom:2px; border-radius:6px; background:{c}"></span></div></div>' for t,a,b,c in tar)
P.append(pg(f'''{head('Quando','Cronograma','de 12 meses','ink','verm')}
  <div class="card" style="margin-top:26px; padding:20px 24px">
    <div style="display:grid; grid-template-columns:290px {cw*12}px; padding-bottom:8px; border-bottom:2px solid var(--ink)"><span class="eyebrow" style="color:var(--muted); font-size:12px">Atividade</span><div style="display:flex">{hdr}</div></div>
    {gl}
  </div>
  <div class="card dark" style="margin-top:16px"><p style="font-size:19px"><b style="color:#F6B9BF">Meses em vermelho:</b> pico esperado de malária. Prevenção no campo antes de junho.</p></div>''', 'Cronograma'))

# 18-19 ORÇAMENTO
def tabela(cats):
    out=''
    for c in cats:
        out += f'<tr class="cat"><td colspan="3"><span style="display:inline-block; width:12px; height:12px; border-radius:3px; background:{COR[c]}; margin-right:10px"></span>{c}</td><td class="r">{brl(CT[c])}</td></tr>'
        for n,q,m,u,un in dict(ORC)[c]:
            out += f'<tr><td>{n}</td><td class="r">{fmt(q)}{" × "+str(m) if m>1 else ""}</td><td class="r">{brl(u)}<span style="color:var(--muted); font-size:13px"> /{un}</span></td><td class="r">{brl(q*m*u)}</td></tr>'
    return f'<table style="font-size:15.5px"><thead><tr><th>Item</th><th class="r">Qtd.</th><th class="r">Custo unitário</th><th class="r">Total</th></tr></thead><tbody>{out}</tbody></table>'
P.append(pg(f'''{head('Custos de operação','Orçamento','detalhado · 1/2','ink','verm', 74)}
  <div class="card" style="margin-top:22px; padding:14px 20px">{tabela(['Pessoal','Logística','Malária: prevenção'])}</div>''', 'Orçamento', 'Valores estimados em reais de 2026'))
P.append(pg(f'''{head('Custos de operação','Orçamento','detalhado · 2/2','ink','verm', 74)}
  <div class="card" style="margin-top:22px; padding:14px 20px">{tabela(['Água: monitorar e limpar','Comunicação','Capacitação','Tecnologia','Administração'])}
    <table style="margin-top:6px; font-size:16px"><tbody><tr><td><b>Subtotal</b></td><td class="r"><b>{brl(DIR)}</b></td></tr><tr><td>Reserva para imprevistos (5%)</td><td class="r">{brl(RES)}</td></tr>
    <tr style="background:var(--ink); color:#fff"><td style="font-weight:800; font-size:19px; border:0">TOTAL EM 12 MESES</td><td class="r" style="font-weight:800; font-size:19px; border:0">{brl(TOTAL)}</td></tr></tbody></table></div>''', 'Orçamento', 'Testes, remédios e exames oficiais são fornecidos pelo SUS'))

# 20 RESUMO + CENÁRIOS
seg = ''.join(f'<span style="width:{v/DIR*100:.2f}%; background:{COR[c]}; height:100%; display:block; border-right:3px solid #fff"></span>' for c,v in sorted(CT.items(), key=lambda kv:-kv[1]))
leg = ''.join(f'<div style="display:grid; grid-template-columns:16px 1fr auto auto; gap:10px; align-items:center; font-size:17px; padding:6px 0; border-bottom:1px solid var(--line)"><span style="width:14px; height:14px; border-radius:3px; background:{COR[c]}"></span><span>{c}</span><span style="color:var(--muted)">{v/DIR*100:.0f}%</span><b style="font-variant-numeric:tabular-nums">{brl(v)}</b></div>' for c,v in sorted(CT.items(), key=lambda kv:-kv[1]))
enx = round(TOTAL*0.45/1000)*1000; amp = round(TOTAL*1.6/1000)*1000
P.append(pg(f'''{head('Para onde vai o dinheiro','Resumo e','cenários','ink','verm')}
  <div class="card" style="margin-top:24px"><div style="display:flex; height:42px; border-radius:10px; overflow:hidden">{seg}</div><div style="margin-top:12px">{leg}</div></div>
  <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:14px; margin-top:16px">
    <div class="card"><p class="eyebrow" style="color:var(--muted)">Enxuto</p><p class="num" style="font-size:40px; margin-top:6px">{brl(enx)}</p><p style="font-size:15px; margin-top:6px; color:var(--muted)">Só os polos Tapajós e Marajó</p></div>
    <div class="card dark"><p class="eyebrow" style="color:#F6B9BF">Padrão · recomendado</p><p class="num" style="font-size:40px; margin-top:6px">{brl(TOTAL)}</p><p style="font-size:15px; margin-top:6px; color:#C9CDD6">5 polos, água e malária</p></div>
    <div class="card"><p class="eyebrow" style="color:var(--muted)">Ampliado</p><p class="num" style="font-size:40px; margin-top:6px">{brl(amp)}</p><p style="font-size:15px; margin-top:6px; color:var(--muted)">8 polos e 2º ano de obras</p></div>
  </div>''', 'Orçamento', 'Cenários estimados a partir do padrão'))

# 21 FINANCIAMENTO E PARCEIROS
fin = [('Governo do Pará (Sespa e Semas)','Termo de colaboração; testes, remédios, mosquiteiros e licenças'),
       ('Ministério da Saúde e SESAI','Insumos de malária e ações nas terras indígenas'),
       ('Fundo Amazônia e fundos de clima','Projetos de água, floresta e comunidades'),
       ('Emendas parlamentares','Recurso rápido para os polos prioritários'),
       ('Empresas de mineração, energia e alumínio','Compensação ambiental e programas sociais'),
       ('Universidades (UFPA, UFOPA) e Fiocruz','Análises de mercúrio, pesquisa e avaliação'),
       ('Prefeituras e empresa de saneamento','Postos, agentes, obras e ligações de esgoto')]
ftb = ''.join(f'<tr><td><b>{a}</b></td><td style="color:var(--muted)">{b}</td></tr>' for a,b in fin)
P.append(pg(f'''{head('Quem paga e quem ajuda','Financiamento','e parcerias','ink','ouro')}
  <div class="card" style="margin-top:26px; padding:14px 22px"><table style="font-size:17.5px"><thead><tr><th>Fonte ou parceiro</th><th>O que entra</th></tr></thead><tbody>{ftb}</tbody></table></div>
  <div class="card" style="margin-top:16px; background:var(--ouro-bg); border:0"><p style="font-size:19px"><b class="ouro">Sugestão:</b> equipe e malária com o Estado e o Ministério da Saúde; água e mercúrio com Fundo Amazônia, universidades e empresas.</p></div>''', 'Financiamento'))

# 22 INDICADORES E RISCOS
ind = [('Casos de malária nos polos','Mensal','−30% no ano'),('Tempo da febre até o teste','Semanal','70% em até 48 h'),('Tratamentos concluídos','Semanal','100%'),
       ('Amostras de mercúrio analisadas','Mensal','3.000'),('Famílias com água segura','Trimestral','1.000'),('Lixo retirado dos canais de Belém','Mensal','Toneladas por mês'),
       ('Pessoas alcançadas','Mensal',fmt(PESSOAS))]
il = ''.join(f'<tr><td><b>{a}</b></td><td>{b}</td><td class="r">{c}</td></tr>' for a,b,c in ind)
ris = [('Violência em áreas de garimpo','Entrar com o Estado, a SESAI e as lideranças; nunca sozinhos'),('Falta de insumos do SUS','Pedido trimestral e estoque nos polos'),
       ('Acesso difícil','Barco, avião e calendário flexível'),('Resultados de mercúrio assustarem','Devolver com orientação e acompanhamento de saúde')]
rl = ''.join(f'<tr><td><b>{a}</b></td><td>{b}</td></tr>' for a,b in ris)
P.append(pg(f'''{head('Acompanhar','Indicadores','e riscos','ink','verm')}
  <div class="card" style="margin-top:24px; padding:14px 22px"><table style="font-size:16.5px"><thead><tr><th>Indicador</th><th>Frequência</th><th class="r">Meta</th></tr></thead><tbody>{il}</tbody></table></div>
  <div class="card" style="margin-top:14px; padding:14px 22px"><table style="font-size:16.5px"><thead><tr><th>Risco</th><th>Como evitar</th></tr></thead><tbody>{rl}</tbody></table></div>''', 'Monitoramento'))

# 23 CAMPANHAS
pub = [('Garimpeiros','Teste rápido no barranco, áudio de WhatsApp e rádio'),('Povos indígenas','Com lideranças e agentes indígenas, nas línguas locais'),
       ('Ribeirinhos','Barco de som, rádio comunitária e aviso nos portos'),('Baixadas de Belém','Agentes de bairro, igrejas e redes sociais'),
       ('Gestantes','Pré-natal com orientação sobre peixe e malária'),('Escolas','Alunos levam o recado: febre = teste; água filtrada')]
pt = ''.join(f'<div style="display:grid; grid-template-columns:240px 1fr; gap:20px; padding:12px 0; border-bottom:1px solid var(--line)"><b class="H verm" style="font-size:28px">{a}</b><span style="font-size:19px">{b}</span></div>' for a,b in pub)
P.append(pg(f'''{head('Comunicação','Campanhas','por público','ink','verm')}
  <div class="card" style="margin-top:26px; padding:10px 28px">{pt}</div>
  <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:12px; margin-top:16px">
    <div class="card" style="background:var(--verm-bg); border:0"><p class="H verm" style="font-size:28px">Febre?</p><p style="font-size:16px">Faça o teste hoje.</p></div>
    <div class="card" style="background:var(--azul-bg); border:0"><p class="H azul" style="font-size:28px">Água filtrada</p><p style="font-size:16px">Saúde para a família.</p></div>
    <div class="card" style="background:var(--lar-bg); border:0"><p class="H lar" style="font-size:28px">Peixe seguro</p><p style="font-size:16px">Saiba qual comer.</p></div>
  </div>''', 'Campanhas'))

# 24 FONTES
P.append(pg(f'''{head('Referências','Fontes','e notas','ink','azul', 80)}
  <div class="card" style="margin-top:26px"><ul class="dot" style="gap:11px">
    <li style="font-size:17.5px">Sespa: boletins epidemiológicos de malária nº 01/2025 e nº 12/2025; "Casos de malária estão em redução no Pará".</li>
    <li style="font-size:17.5px">Ministério da Saúde: "Pará reduz 34,2% dos casos de malária no primeiro trimestre de 2025".</li>
    <li style="font-size:17.5px">Casa Civil e Secom (dez/2024): malária e garimpo ilegal na Terra Indígena Munduruku.</li>
    <li style="font-size:17.5px">Fiocruz e WWF-Brasil (2020): mercúrio nos Munduruku do médio Tapajós; Agência Brasil (jun/2026): gestantes.</li>
    <li style="font-size:17.5px">Instituto Trata Brasil: Ranking do Saneamento 2025 e 2026, via O Liberal e InfoMoney.</li>
    <li style="font-size:17.5px">IBGE, Censo 2022; INPE, PRODES 2025.</li>
    <li style="font-size:17.5px">Bandeira do Pará: Wikimedia Commons. Contorno do estado: base pública de limites estaduais.</li>
  </ul></div>
  <div class="card" style="margin-top:14px"><p style="font-size:17.5px">Custos são estimativas para planejamento, sem cotação. Fontes de malária divergem sobre o percentual de queda de 2024 para 2025. O calendário de risco segue o padrão amazônico e deve ser confirmado com dados mensais.</p></div>''', 'Fontes'))

# 25 ENCERRAMENTO
N[0] += 1
P.append(f'''<section class="p" style="padding:0; background:var(--ink); background-image:none">
  <div style="position:absolute; left:0; right:0; top:0; height:480px">{FLAG}</div>
  <div style="position:absolute; left:0; right:0; top:480px; height:10px; background:var(--azul)"></div>
  <div style="position:absolute; left:90px; right:90px; top:580px; color:#fff">
    <p class="eyebrow" style="color:#F6B9BF">Pará Vivo</p>
    <h2 class="H" style="font-size:112px; margin-top:16px"><span>Rio limpo.</span><span>Febre tratada.</span><span style="color:#8EC5F0">Floresta de pé.</span></h2>
    <p style="font-size:22px; margin-top:28px; color:#C9CDD6">{brl(TOTAL)} em 12 meses · novembro de 2026</p>
  </div>
</section>''')

html = '<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Pará Vivo</title>' + CSS + '</head><body>' + ''.join(P) + '</body></html>'
open('para-vivo.html','w').write(html)
print('ok', len(P))
