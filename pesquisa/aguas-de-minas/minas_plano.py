# "Rios Vivos de Minas" no padrão do plano do Amapá: 1080x1350, papel quadriculado, títulos condensados, cartões.
import json
FLAG = open('../mg-dl/flag.svg').read().replace('width="600" height="420" style="', 'viewBox="0 0 600 420" preserveAspectRatio="xMidYMid meet" style="width:100%; height:100%; display:block; ')
brl = lambda v: 'R$ ' + f'{v:,.0f}'.replace(',', '.')
mi = lambda v: 'R$ ' + f'{v/1e6:,.1f}'.replace('.', ',') + ' mi'
fmt = lambda v: f'{v:,.0f}'.replace(',', '.')

# ---------------- custos unitários (estimativas 2026) ----------------
U = dict(est=80000, estm=1500, eco=30000, ecom=3000, mata=18000, nasc=6000, caca=40, bio=2500, edu=300000, ges=600000)
RIOS = [
 dict(n='Rio das Velhas', c='Belo Horizonte', la=-19.92, lo=-43.94, cor='#1B6CA8', bacia='São Francisco',
      sobre='Nasce em Ouro Preto e corre cerca de 800 km até o São Francisco. Abastece boa parte da Grande BH.',
      cid='Ouro Preto, Nova Lima, Belo Horizonte, Sabará, Santa Luzia, Lagoa Santa, Sete Lagoas (afluentes)',
      prob=['Esgoto dos ribeirões Arrudas e Onça, que cortam BH', 'Ligações de esgoto na rede de chuva', 'Lixo urbano e enchentes', 'Mineração no alto curso'],
      boa='O IGAM registra recuperação progressiva da qualidade da água.',
      q=dict(est=10, eco=12, mata=300, nasc=200, caca=60000, bio=300)),
 dict(n='Rio Paraopeba', c='Brumadinho', la=-20.14, lo=-44.20, cor='#C0392B', bacia='São Francisco',
      sobre='Afluente do São Francisco que deságua no lago de Três Marias. Foi atingido pelo rejeito de Brumadinho em 2019.',
      cid='Congonhas, Brumadinho, Betim, Ibirité, Juatuba, Pará de Minas (afluentes), Paraopeba',
      prob=['Rejeito da barragem B1 da mina Córrego do Feijão', 'Esgoto de Betim e Ibirité (ribeirão Ibirité entre os piores pontos de 2023)', 'Mineração e indústria', 'Erosão em pastagens'],
      boa='O acordo de Brumadinho financia projetos de recuperação da bacia.',
      q=dict(est=8, eco=8, mata=250, nasc=200, caca=30000, bio=300)),
 dict(n='Rio Doce', c='Gov. Valadares', la=-18.85, lo=-41.95, cor='#B5652A', bacia='Doce',
      sobre='Formado pelos rios Piranga e do Carmo, corre cerca de 850 km até o mar no Espírito Santo.',
      cid='Mariana (rio do Carmo), Ponte Nova, Ipatinga, Gov. Valadares, Resplendor, Aimorés',
      prob=['Lama da barragem de Fundão (2015) ainda no leito e nas margens', 'Erosão forte e assoreamento', 'Esgoto de dezenas de cidades', 'Seca e calor que baixam o rio'],
      boa='O novo acordo de Mariana (2024) destina R$ 170 bilhões à bacia em 20 anos.',
      q=dict(est=10, eco=6, mata=400, nasc=300, caca=25000, bio=400)),
 dict(n='Rio Piracicaba', c='Ipatinga', la=-19.47, lo=-42.54, cor='#6B5B95', bacia='Doce',
      sobre='Afluente do rio Doce que atravessa o Vale do Aço, um dos polos industriais de Minas.',
      cid='Itabira (afluentes), João Monlevade, Timóteo, Coronel Fabriciano, Ipatinga',
      prob=['Efluentes da siderurgia e da mineração de ferro', 'Esgoto das cidades do Vale do Aço', 'Poluição do ar que se deposita na água', 'Margens ocupadas'],
      boa='Grandes empresas na bacia podem patrocinar a recuperação como compensação.',
      q=dict(est=6, eco=6, mata=150, nasc=120, caca=30000, bio=150)),
 dict(n='Rio Paraibuna', c='Juiz de Fora', la=-21.76, lo=-43.35, cor='#2E7D4F', bacia='Paraíba do Sul',
      sobre='Nasce na Serra da Mantiqueira, atravessa Juiz de Fora e segue para o Paraíba do Sul, que abastece o Rio de Janeiro.',
      cid='Antônio Carlos, Juiz de Fora, Matias Barbosa, Simão Pereira',
      prob=['Esgoto urbano de Juiz de Fora', 'Lixo e drenagem nas áreas centrais', 'Indústria e ocupação das margens'],
      boa='A água limpa aqui melhora também a do Paraíba do Sul, rio interestadual.',
      q=dict(est=5, eco=6, mata=120, nasc=100, caca=35000, bio=150)),
 dict(n='Rio Pará', c='Divinópolis', la=-20.14, lo=-44.89, cor='#C9A227', bacia='São Francisco',
      sobre='Afluente do São Francisco que cruza o Centro-Oeste mineiro, região de indústria, siderurgia e confecção.',
      cid='Itaúna, Divinópolis, Carmo do Cajuru, Pará de Minas, Pitangui, Pompéu',
      prob=['Esgoto doméstico das cidades médias', 'Efluentes de fundições e indústrias', 'Desmatamento das margens', 'Agrotóxicos e erosão rural'],
      boa='Cidades médias decidem rápido: bom candidato a rio piloto.',
      q=dict(est=5, eco=4, mata=150, nasc=150, caca=20000, bio=250)),
]
def custo(q):
    L = [('Estações de monitoramento', q['est']*U['est'] + q['est']*24*U['estm']),
         ('Ecobarreiras (limpadores)', q['eco']*U['eco'] + q['eco']*24*U['ecom']),
         ('Mata ciliar', q['mata']*U['mata']), ('Nascentes', q['nasc']*U['nasc']),
         ('Caça-esgoto', q['caca']*U['caca']), ('Biodigestores rurais', q['bio']*U['bio']),
         ('Educação e mobilização', 2*U['edu']), ('Equipe e gestão', 2*U['ges'])]
    return L, sum(v for _, v in L)
for r in RIOS: r['L'], r['T'] = custo(r['q'])
GERAL = sum(r['T'] for r in RIOS)
SOMA = {k: sum(r['q'][k] for r in RIOS) for k in ('est','eco','mata','nasc','caca','bio')}
CATCOR = ['#1B6CA8','#D7141F','#2E7D4F','#7FB77E','#C9A227','#B5652A','#6B5B95','#232523']
CAT = {}
for r in RIOS:
    for (n, v) in r['L']: CAT[n] = CAT.get(n, 0) + v
LIXO = round(SOMA['eco'] * 0.5 * 18)  # 0,5 t por barreira por mês, 18 meses de operação plena (estimativa)
print(GERAL, SOMA, LIXO)

CSS = '''
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Anton&family=Poppins:ital,wght@0,400;0,500;0,600;0,700;0,800;1,700&family=IBM+Plex+Mono:wght@500&display=swap">
<style>
/* Mesmo padrão do plano do Amapá: papel quadriculado, títulos condensados, cartões com sombra; faixa lateral com as cores de Minas. */
:root{
  --paper:#FAFAF8; --grid:rgba(30,35,45,.05); --ink:#1E2230; --muted:#5C6170; --line:rgba(30,35,45,.12);
  --verm:#D7141F; --verm-bg:#FBE1E2; --rio:#1B6CA8; --rio-bg:#E0EDF7; --mata:#2E7D4F; --mata-bg:#E0F0E6; --ouro:#B8902A; --ouro-bg:#F5EDD6; --lama:#B5652A; --card:#FFFFFF;
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
.H{font-family:var(--fh); font-weight:400; text-transform:uppercase}
.H > span{display:block; line-height:1.0}
.verm{color:var(--verm)} .rio{color:var(--rio)} .mata{color:var(--mata)} .ink{color:var(--ink)} .ouro{color:var(--ouro)} .lama{color:var(--lama)}
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
ul.dot li::before{content:""; position:absolute; left:2px; top:.4em; width:0; height:0; border-left:7px solid transparent; border-right:7px solid transparent; border-bottom:12px solid var(--verm)}
table{border-collapse:collapse; width:100%; font-size:17px}
th{font-family:var(--fm); font-weight:500; font-size:13px; letter-spacing:.08em; text-transform:uppercase; color:var(--muted); text-align:left; padding:9px 10px; border-bottom:2px solid var(--ink)}
td{padding:7px 10px; border-bottom:1px solid var(--line); vertical-align:top}
td.r, th.r{text-align:right; font-variant-numeric:tabular-nums; white-space:nowrap}
.pill{display:inline-block; font-weight:700; font-size:15px; padding:5px 12px; border-radius:999px}
</style>'''
STRIPE = '<div class="stripe"><i style="background:var(--verm)"></i><i style="background:#fff; border-right:1px solid var(--line)"></i><i style="background:var(--ink)"></i></div>'
N = [0]
def pg(inner, secao, fonte=''):
    N[0] += 1
    return (f'<section class="p">{STRIPE}<div class="top"><span><b>Rios Vivos de Minas</b> · plano para lideranças</span><span>{secao}</span></div>'
            f'{inner}<div class="foot"><span>{fonte}</span><span>{N[0]:02d}</span></div></section>')
def head(eye, l1, l2, c1='ink', c2='verm', size=92):
    return f'<p class="eyebrow">{eye}</p><h2 class="H" style="font-size:{size}px; margin-top:12px"><span class="{c1}">{l1}</span><span class="{c2}">{l2}</span></h2>'
P = []

# 1 CAPA
N[0] += 1
P.append(f'''<section class="p" style="padding:0; background:#fff; background-image:none">
  <div style="position:absolute; left:0; right:0; top:0; height:600px; background:#fff; display:grid; place-items:center; border-bottom:10px solid var(--ink)"><div style="width:700px; height:490px">{FLAG}</div></div>
  <div style="position:absolute; left:90px; right:90px; top:660px">
    <p class="eyebrow">Plano para lideranças · Minas Gerais</p>
    <h1 class="H" style="font-size:124px; margin-top:14px"><span class="ink">Rios vivos</span><span class="verm">de Minas</span></h1>
    <p style="font-size:25px; margin-top:20px; max-width:860px">Como limpar seis rios mineiros em dois anos: diagnóstico, soluções, custo de cada rio, como executar e o que Minas ganha.</p>
    <div style="display:flex; gap:12px; margin-top:30px; flex-wrap:wrap">
      <span class="pill" style="background:var(--ink); color:#fff">6 rios</span>
      <span class="pill" style="background:var(--rio-bg); color:var(--rio)">24 meses</span>
      <span class="pill" style="background:var(--verm-bg); color:var(--verm)">{mi(GERAL)}</span>
    </div>
  </div>
  <p style="position:absolute; left:90px; bottom:50px; font-size:16px; color:var(--muted); font-family:var(--fm); letter-spacing:.1em">LIBERTAS QUÆ SERA TAMEN · NOVEMBRO DE 2026</p>
</section>''')

# 2 RESUMO
P.append(pg(f'''{head('Resumo executivo','O plano em','uma página')}
  <p style="margin-top:22px; font-size:23px; max-width:880px">Um programa de dois anos que coloca em cada rio um <b>kit limpador</b>: medição da água em tempo real, barreiras de lixo, caça-esgoto, mata ciliar, nascentes e fossas no campo. As grandes estações de esgoto seguem com a Copasa e as prefeituras; o programa acelera, cobra e mostra resultado.</p>
  <div style="display:grid; grid-template-columns:repeat(3,1fr); gap:16px; margin-top:28px">
    <div class="card"><p class="num verm" style="font-size:60px">{fmt(SOMA["caca"])}</p><p style="font-size:17px; margin-top:6px">imóveis vistoriados no caça-esgoto</p></div>
    <div class="card"><p class="num mata" style="font-size:60px">{fmt(SOMA["mata"])} ha</p><p style="font-size:17px; margin-top:6px">de mata ciliar plantada</p></div>
    <div class="card"><p class="num rio" style="font-size:60px">{SOMA["eco"]}</p><p style="font-size:17px; margin-top:6px">ecobarreiras retirando lixo</p></div>
    <div class="card"><p class="num rio" style="font-size:60px">{SOMA["est"]}</p><p style="font-size:17px; margin-top:6px">estações medindo a água a cada 15 min</p></div>
    <div class="card"><p class="num mata" style="font-size:60px">{fmt(SOMA["nasc"])}</p><p style="font-size:17px; margin-top:6px">nascentes protegidas</p></div>
    <div class="card"><p class="num verm" style="font-size:60px">{fmt(SOMA["bio"])}</p><p style="font-size:17px; margin-top:6px">fossas biodigestoras no campo</p></div>
  </div>
  <div class="card dark" style="margin-top:16px; display:grid; grid-template-columns:1fr auto; gap:20px; align-items:center">
    <div><p class="eyebrow" style="color:#F3B9BC">Investimento em 24 meses</p><p class="num" style="font-size:76px; margin-top:8px">{mi(GERAL)}</p></div>
    <p style="font-size:18px; color:#C9CDD6; width:330px">Menos de 0,5% do novo acordo de Mariana. Cada rio tem conta e painel próprios.</p>
  </div>''', 'Resumo', 'Valores estimados para planejamento'))

# 3 CAIXA D'ÁGUA
bacias = [('São Francisco','Nasce na Serra da Canastra, em São Roque de Minas'),('Doce','Formado em Minas, deságua no Espírito Santo'),
          ('Grande e Paranaíba','Formam o rio Paraná, que abastece o Sul e o Sudeste'),('Jequitinhonha','Atravessa o Vale do Jequitinhonha até a Bahia'),
          ('Paraíba do Sul','Recebe águas mineiras e abastece o Rio de Janeiro'),('Mucuri, Pardo e outras','Rios do Leste e do Norte do estado')]
bt = ''.join(f'<tr><td><b>{a}</b></td><td>{b}</td></tr>' for a,b in bacias)
P.append(pg(f'''{head('Por que Minas importa','A caixa-d’água','do Brasil','ink','rio')}
  <p style="margin-top:22px; font-size:22px; max-width:880px">Nascem em Minas rios das grandes bacias do país. A água que sai suja daqui chega a outros estados; a que sai limpa abastece milhões de pessoas fora de Minas.</p>
  <div class="card" style="margin-top:26px; padding:14px 24px"><table style="font-size:19px"><thead><tr><th>Bacia</th><th>Ligação com Minas</th></tr></thead><tbody>{bt}</tbody></table></div>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-top:16px">
    <div class="card" style="background:var(--rio-bg); border:0"><p style="font-size:19px"><b class="rio">853 municípios</b>, o maior número do país, dividem essas bacias. Cada prefeitura tem parte da solução.</p></div>
    <div class="card" style="background:var(--ouro-bg); border:0"><p style="font-size:19px"><b class="ouro">Comitês de bacia</b> reúnem governo, usuários e sociedade para planejar cada rio e aplicar a cobrança pelo uso da água.</p></div>
  </div>''', 'Bacias', 'IGAM; ANA'))

# 4 PANORAMA
iqa = [('Excelente',1.4,'#2E7D4F'),('Bom',37.4,'#7FB77E'),('Médio',44.1,'#E7C35A'),('Ruim',17.0,'#B5652A'),('Muito ruim',0.1,'#D7141F')]
bar = ''.join(f'<span style="width:{max(v,0.6)}%; background:{c}; display:block; height:100%; border-right:3px solid #fff"></span>' for n,v,c in iqa)
leg = ''.join(f'<div style="display:grid; grid-template-columns:18px 1fr auto; gap:12px; align-items:center; font-size:19px; padding:6px 0; border-bottom:1px solid var(--line)"><span style="width:16px; height:16px; border-radius:4px; background:{c}"></span><span>{n}</span><b>{str(v).replace(".",",")}%</b></div>' for n,v,c in iqa)
P.append(pg(f'''{head('Diagnóstico','Como estão','os rios hoje','ink','verm')}
  <div class="card" style="margin-top:26px">
    <p class="eyebrow" style="color:var(--muted)">Índice de Qualidade da Água · pontos do IGAM em 2023</p>
    <div style="display:flex; height:50px; border-radius:12px; overflow:hidden; margin-top:14px">{bar}</div>
    <div style="margin-top:12px">{leg}</div>
  </div>
  <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:14px; margin-top:16px">
    <div class="card"><p class="num verm" style="font-size:58px">54%</p><p style="font-size:16px; margin-top:6px">das amostras fora do limite legal (2020)</p></div>
    <div class="card"><p class="num rio" style="font-size:58px">87,6%</p><p style="font-size:16px; margin-top:6px">de esgoto coletado (2021)</p></div>
    <div class="card"><p class="num verm" style="font-size:58px">53,7%</p><p style="font-size:16px; margin-top:6px">da população com esgoto tratado (2021)</p></div>
  </div>
  <div class="card dark" style="margin-top:16px"><p style="font-size:20px"><b style="color:#F3B9BC">Leitura:</b> a principal causa de água muito ruim é o esgoto das cidades (IGAM). E nas regiões mais populosas, até o esgoto tratado ainda leva nutrientes demais: é preciso tratamento mais avançado.</p></div>''',
  'Diagnóstico', 'IGAM (2023 e 2020); Governo de Minas/SNIS (2021)'))

# 5 CAUSAS
causas = [('Esgoto doméstico','Coliformes e matéria orgânica que tiram o oxigênio dos peixes.','Maior causa','#D7141F'),
          ('Mineração','Rejeitos, sedimentos e metais; risco de rompimento de barragens.','Maior risco','#B5652A'),
          ('Indústria','Siderurgia, fundições, alimentos e curtumes com efluente fora do padrão.','Regional','#6B5B95'),
          ('Agropecuária','Agrotóxicos, adubo e esterco levados pela chuva.','Difusa','#C9A227'),
          ('Erosão','Pasto e estrada de terra sem proteção viram lama no rio.','Difusa','#7A6A4F'),
          ('Lixo e drenagem','Lixões, entulho e a água da chuva que lava as ruas.','Urbana','#1B6CA8')]
ct = ''.join(f'<div class="card" style="padding:20px 24px; border-left:8px solid {c}"><div style="display:flex; justify-content:space-between; align-items:baseline"><p class="H" style="font-size:32px">{a}</p><span class="pill" style="background:{c}; color:#fff; font-size:13px">{t}</span></div><p style="font-size:18px; margin-top:4px; color:var(--muted)">{b}</p></div>' for a,b,t,c in causas)
P.append(pg(f'''{head('De onde vem','Seis fontes','de poluição','ink','verm')}
  <div style="display:grid; gap:12px; margin-top:28px">{ct}</div>''', 'Causas', 'IGAM; SEMAD'))

# 6 MARIANA E BRUMADINHO linha do tempo
eventos = [('2015','Rompe a barragem de Fundão, em Mariana','19 mortes; lama no rio Doce até o mar','#B5652A'),
           ('2019','Rompe a barragem B1, em Brumadinho','270 mortes; rejeito no rio Paraopeba','#D7141F'),
           ('2019','Lei estadual "Mar de Lama Nunca Mais"','Proíbe barragens alteadas a montante e exige desmontá-las','#1E2230'),
           ('2021','Acordo de Brumadinho','R$ 37,7 bilhões para reparação','#1B6CA8'),
           ('2024','Novo acordo de Mariana','R$ 170 bilhões em 20 anos, maior acordo socioambiental do mundo','#2E7D4F')]
tl = ''.join(f'<div style="display:grid; grid-template-columns:120px 30px 1fr; gap:16px; align-items:start"><p class="num" style="font-size:44px; color:{c}">{a}</p><div style="display:grid; justify-items:center; height:100%"><span style="width:18px; height:18px; border-radius:50%; background:{c}; margin-top:12px"></span><span style="width:2px; flex:1; background:var(--line); min-height:70px"></span></div><div class="card" style="padding:18px 22px"><p style="font-size:20px; font-weight:700">{b}</p><p style="font-size:17px; color:var(--muted); margin-top:2px">{d}</p></div></div>' for a,b,d,c in eventos)
P.append(pg(f'''{head('Lições que viraram lei','Mariana e','Brumadinho','ink','lama')}
  <div style="display:grid; gap:12px; margin-top:28px">{tl}</div>
  <div class="card dark" style="margin-top:16px"><p style="font-size:20px"><b style="color:#F3B9BC">289 vidas</b> perdidas e duas bacias atingidas. Os acordos somam mais de <b style="color:#F3B9BC">R$ 200 bilhões</b>: o desafio agora é transformar esse dinheiro em rio limpo de verdade.</p></div>''',
  'Desastres', 'Governo de Minas; Agência Minas; Planalto'))

# 7 MAPA DOS 6 RIOS
geo = json.load(open('../dados/uf.json'))
g = [f for f in geo['features'] if f['properties']['sigla']=='MG'][0]['geometry']
rings = [p[0] for p in g['coordinates']] if g['type']=='MultiPolygon' else [g['coordinates'][0]]
X0,X1,Y0,Y1 = -51.2,-39.7,-23.0,-14.1
W=860; H=int(W*(Y1-Y0)/(X1-X0)*1.03)
px=lambda x:(x-X0)/(X1-X0)*W; py=lambda y:(Y1-y)/(Y1-Y0)*H
path=''.join('M'+' L'.join(f'{px(a):.1f},{py(b):.1f}' for a,b in r[::2])+'Z' for r in rings)
pins=''
lab = {0:(-24,-20,'end'),1:(4,40,'middle'),2:(22,6,'start'),3:(24,4,'start'),4:(22,8,'start'),5:(-22,8,'end')}
for i,r in enumerate(RIOS):
    x,y = px(r['lo']), py(r['la']); dx,dy,an = lab[i]
    pins += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="17" fill="{r["cor"]}" stroke="#fff" stroke-width="4"/><text x="{x:.1f}" y="{y+6:.1f}" text-anchor="middle" font-family="Poppins" font-size="17" font-weight="800" fill="#fff">{i+1}</text>'
    pins += f'<text x="{x+dx:.1f}" y="{y+dy:.1f}" text-anchor="{an}" font-family="Poppins" font-size="17" font-weight="700" fill="#1E2230">{r["c"]}</text>'
mapa = f'<svg viewBox="-20 -10 {W+40} {H+20}" style="width:100%; display:block"><path d="{path}" fill="#EFEDE8" stroke="#1E2230" stroke-width="1.6"/>{pins}</svg>'
lst = ''.join(f'<div style="display:grid; grid-template-columns:30px 1fr; gap:10px; align-items:center"><span style="width:30px; height:30px; border-radius:50%; background:{r["cor"]}; color:#fff; font-weight:800; display:grid; place-items:center">{i+1}</span><span style="font-size:18px"><b>{r["n"]}</b> <span style="color:var(--muted)">· bacia do {r["bacia"]}</span></span></div>' for i,r in enumerate(RIOS))
P.append(pg(f'''{head('Onde vamos atuar','Os seis','rios do plano','ink','rio')}
  <div class="card" style="margin-top:24px; padding:14px">{mapa}</div>
  <div class="card" style="margin-top:14px; display:grid; grid-template-columns:1fr 1fr; gap:12px 24px">{lst}</div>''', 'Mapa', 'Localização aproximada da cidade de referência de cada rio'))

# 8-13 PÁGINA DE CADA RIO
for i, r in enumerate(RIOS):
    q = r['q']
    mxv = max(v for _, v in r['L'])
    cb = ''.join(f'<div style="display:grid; grid-template-columns:230px 1fr 120px; gap:12px; align-items:center; font-size:16px; padding:4px 0"><span>{n}</span><span style="height:16px; background:rgba(30,35,45,.06); border-radius:0 4px 4px 0; overflow:hidden"><span style="display:block; height:100%; width:{v/mxv*100:.1f}%; background:{r["cor"]}; border-radius:0 4px 4px 0"></span></span><span style="text-align:right; font-variant-numeric:tabular-nums">{brl(v)}</span></div>' for n, v in r['L'])
    probs = ''.join(f'<li style="font-size:18px">{x}</li>' for x in r['prob'])
    kit = [(q['est'],'estações'),(q['eco'],'ecobarreiras'),(q['mata'],'ha de mata'),(q['nasc'],'nascentes'),(fmt(q['caca']),'imóveis'),(q['bio'],'biodigestores')]
    kt = ''.join(f'<div style="text-align:center"><p class="num" style="font-size:40px; color:{r["cor"]}">{a}</p><p style="font-size:14px; color:var(--muted)">{b}</p></div>' for a,b in kit)
    P.append(pg(f'''<p class="eyebrow" style="color:{r["cor"]}">Rio {i+1} de 6 · bacia do {r["bacia"]}</p>
  <h2 class="H" style="font-size:96px; margin-top:10px"><span class="ink">{r["n"]}</span></h2>
  <p style="font-size:20px; margin-top:10px; max-width:900px">{r["sobre"]}</p>
  <p class="small" style="margin-top:6px"><b style="color:var(--ink)">Cidades:</b> {r["cid"]}</p>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:14px; margin-top:20px">
    <div class="card" style="padding:20px 24px"><p class="eyebrow" style="color:var(--muted)">Problemas</p><ul class="dot" style="margin-top:10px; gap:7px">{probs}</ul></div>
    <div class="card" style="padding:20px 24px; background:var(--mata-bg); border:0"><p class="eyebrow" style="color:var(--mata)">A favor</p><p style="font-size:18px; margin-top:10px">{r["boa"]}</p></div>
  </div>
  <div class="card" style="margin-top:14px; padding:18px 24px"><p class="eyebrow" style="color:var(--muted)">Kit limpador em 24 meses</p><div style="display:grid; grid-template-columns:repeat(6,1fr); gap:8px; margin-top:10px">{kt}</div></div>
  <div class="card" style="margin-top:14px; padding:18px 24px">{cb}</div>
  <div class="card dark" style="margin-top:14px; display:flex; justify-content:space-between; align-items:center; padding:20px 28px"><p style="font-size:20px">Custo total do rio em 24 meses</p><p class="num" style="font-size:52px; color:#fff">{brl(r["T"])}</p></div>''',
  r['n'], 'Quantidades e custos estimados'))

# 14 SOLUÇÕES DE ESGOTO (técnico)
tec = [('Lodo ativado','Grandes cidades','85–95%','Alta eficiência; consome energia; pode remover nutrientes'),
       ('Reator anaeróbio + pós-tratamento','Cidades médias','75–90%','Barato de operar; muito usado em Minas'),
       ('Lagoas de estabilização','Cidades pequenas','70–85%','Simples; precisa de área'),
       ('Jardins filtrantes (wetlands)','Pequenas e distritos','80–90%','Usa plantas; baixo custo de operação'),
       ('Fossa séptica biodigestora','Zona rural','—','Trata o esgoto da casa e gera adubo (Embrapa)')]
tt = ''.join(f'<tr><td><b>{a}</b></td><td>{b}</td><td class="r">{c}</td><td style="color:var(--muted)">{d}</td></tr>' for a,b,c,d in tec)
P.append(pg(f'''{head('Solução técnica','Tratar esgoto','do jeito certo','ink','rio')}
  <div class="card" style="margin-top:26px; padding:14px 22px"><table style="font-size:17px"><thead><tr><th>Tecnologia</th><th>Para</th><th class="r">Remoção de matéria orgânica</th><th>Observação</th></tr></thead><tbody>{tt}</tbody></table></div>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:14px; margin-top:16px">
    <div class="card"><p class="H rio" style="font-size:32px">Caça-esgoto</p><p style="font-size:18px; margin-top:6px; color:var(--muted)">Teste com corante em cada casa mostra se o esgoto vai para a rede certa. Ligação errada leva esgoto direto ao córrego, mesmo em cidade com estação.</p></div>
    <div class="card"><p class="H rio" style="font-size:32px">Tratamento avançado</p><p style="font-size:18px; margin-top:6px; color:var(--muted)">Na Grande BH e no Vale do Aço, as estações precisam também remover nitrogênio e fósforo, como alerta o IGAM.</p></div>
  </div>
  <div class="card" style="margin-top:14px; background:var(--rio-bg); border:0"><p style="font-size:19px"><b class="rio">Meta legal:</b> 99% com água e 90% com coleta e tratamento de esgoto até 2033 (Lei 14.026/2020).</p></div>''',
  'Esgoto', 'Faixas típicas de eficiência da literatura técnica de saneamento; IGAM; Embrapa'))

# 15 KIT LIMPADOR (custos unitários)
kitu = [('Estação automática de monitoramento','Oxigênio, turbidez, pH e temperatura a cada 15 min',U['est'],'unidade'),
        ('Manutenção da estação','Calibração, peças e transmissão de dados',U['estm'],'mês'),
        ('Ecobarreira (limpador de lixo)','Barreira flutuante de margem a margem',U['eco'],'unidade'),
        ('Operação da ecobarreira','Coleta semanal e destinação do lixo',U['ecom'],'mês'),
        ('Mata ciliar','Mudas nativas, plantio e 2 anos de manutenção',U['mata'],'hectare'),
        ('Nascente protegida','Cerca, plantio e placa',U['nasc'],'nascente'),
        ('Caça-esgoto','Vistoria com teste de corante',U['caca'],'imóvel'),
        ('Fossa séptica biodigestora','Modelo Embrapa para casas rurais',U['bio'],'unidade'),
        ('Educação e mobilização','Escolas, rádio, mutirões e comitês',U['edu'],'rio/ano'),
        ('Equipe e gestão','Coordenador, técnicos, dados e prestação de contas',U['ges'],'rio/ano')]
ku = ''.join(f'<tr><td><b>{a}</b><br><span style="font-size:14px; color:var(--muted)">{b}</span></td><td class="r">{brl(c)}</td><td style="white-space:nowrap; color:var(--muted)">por {d}</td></tr>' for a,b,c,d in kitu)
P.append(pg(f'''{head('Custos de operação','O kit limpador','peça por peça','ink','verm', 84)}
  <div class="card" style="margin-top:24px; padding:12px 22px"><table style="font-size:17px"><thead><tr><th>Item</th><th class="r">Custo</th><th>Unidade</th></tr></thead><tbody>{ku}</tbody></table></div>
  <p class="small" style="margin-top:12px">Valores estimados de mercado em 2026. Não incluem obras de estações de tratamento, que são da Copasa e das prefeituras.</p>''', 'Custos', 'Estimativas para planejamento'))

# 16 ORÇAMENTO GERAL
mx = max(r['T'] for r in RIOS)
rb = ''.join(f'<div style="display:grid; grid-template-columns:200px 1fr 140px; gap:14px; align-items:center; padding:6px 0"><span style="font-size:18px; font-weight:700">{r["n"]}</span><span style="height:26px; background:rgba(30,35,45,.06); border-radius:0 6px 6px 0; overflow:hidden"><span style="display:block; height:100%; width:{r["T"]/mx*100:.1f}%; background:{r["cor"]}; border-radius:0 6px 6px 0"></span></span><span class="num" style="font-size:26px; text-align:right">{mi(r["T"])}</span></div>' for r in RIOS)
seg = ''.join(f'<span style="width:{v/GERAL*100:.2f}%; background:{c}; display:block; height:100%; border-right:3px solid #fff"></span>' for (n,v),c in zip(CAT.items(), CATCOR))
cl = ''.join(f'<div style="display:grid; grid-template-columns:16px 1fr auto auto; gap:10px; align-items:center; font-size:16px; padding:4px 0"><span style="width:14px; height:14px; border-radius:3px; background:{c}"></span><span>{n}</span><span style="color:var(--muted)">{v/GERAL*100:.0f}%</span><b style="font-variant-numeric:tabular-nums">{mi(v)}</b></div>' for (n,v),c in zip(CAT.items(), CATCOR))
P.append(pg(f'''{head('Orçamento','Quanto custa','cada rio','ink','verm')}
  <div class="card" style="margin-top:24px; padding:18px 24px">{rb}</div>
  <div class="card" style="margin-top:14px">
    <p class="eyebrow" style="color:var(--muted)">Para onde vai o dinheiro</p>
    <div style="display:flex; height:36px; border-radius:10px; overflow:hidden; margin-top:12px">{seg}</div>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:0 28px; margin-top:10px">{cl}</div>
  </div>
  <div class="card dark" style="margin-top:14px; display:flex; justify-content:space-between; align-items:center"><p style="font-size:21px">Total dos 6 rios · 24 meses</p><p class="num" style="font-size:60px">{brl(GERAL)}</p></div>''', 'Orçamento', 'Estimativas para planejamento'))

# 17 CRONOGRAMA
M = ['1-2','3-4','5-6','7-8','9-10','11-12','13-14','15-16','17-18','19-20','21-22','23-24']
tar = [('Pacto com Estado, prefeituras e comitês',0,1,'#1E2230'),('Diagnóstico de esgoto, lixo e nascentes',1,2,'#1E2230'),
       ('Instalação das estações',2,4,'#1B6CA8'),('Instalação das ecobarreiras',2,4,'#1B6CA8'),('Coleta de lixo nas barreiras',3,12,'#1B6CA8'),
       ('Caça-esgoto casa por casa',2,10,'#D7141F'),('Plantio de mata ciliar (época de chuva)',4,11,'#2E7D4F'),('Proteção de nascentes',3,9,'#2E7D4F'),
       ('Biodigestores no campo',5,11,'#C9A227'),('Educação nas escolas e rádio',1,12,'#C9A227'),('Painel público e relatórios',3,12,'#6B5B95'),('Avaliação final',11,12,'#1E2230')]
cw = 46
hdr = ''.join(f'<div style="width:{cw}px; text-align:center; font-family:var(--fm); font-size:10.5px; color:var(--muted)">{m}</div>' for m in M)
gl = ''.join(f'<div style="display:grid; grid-template-columns:290px {cw*12}px; align-items:center; padding:7px 0; border-bottom:1px solid var(--line)"><span style="font-size:15.5px; font-weight:600">{t}</span><div style="position:relative; height:20px; background:repeating-linear-gradient(90deg, transparent 0 {cw-1}px, rgba(30,35,45,.08) {cw-1}px {cw}px)"><span style="position:absolute; left:{a*cw+3}px; width:{(b-a)*cw-6}px; top:2px; bottom:2px; border-radius:6px; background:{c}"></span></div></div>' for t,a,b,c in tar)
P.append(pg(f'''{head('Quando','Cronograma','de 24 meses','ink','verm')}
  <div class="card" style="margin-top:26px; padding:20px 24px">
    <div style="display:grid; grid-template-columns:290px {cw*12}px; padding-bottom:8px; border-bottom:2px solid var(--ink)"><span class="eyebrow" style="color:var(--muted); font-size:12px">Atividade · meses</span><div style="display:flex">{hdr}</div></div>
    {gl}
  </div>
  <div class="card dark" style="margin-top:16px"><p style="font-size:19px"><b style="color:#F3B9BC">Atenção ao clima:</b> plantio de mata na época de chuva (outubro a março) e obras nas margens na seca.</p></div>''', 'Cronograma'))

# 18 GOVERNANÇA E EQUIPE
P.append(pg(f'''{head('Quem coordena','Governança','e equipe','ink','rio')}
  <div class="card" style="margin-top:26px; padding:22px">
    <svg viewBox="0 0 880 330" style="width:100%; display:block"><g font-family="Poppins" text-anchor="middle">
      <rect x="290" y="6" width="300" height="66" rx="12" fill="#1E2230"/><text x="440" y="36" fill="#fff" font-size="18" font-weight="700">Comitê gestor</text><text x="440" y="58" fill="#C9CDD6" font-size="13">Estado · prefeituras · Copasa · comitês · financiadores</text>
      <line x1="440" y1="72" x2="440" y2="102" stroke="#1E2230" stroke-width="2"/>
      <rect x="320" y="102" width="240" height="56" rx="12" fill="#D7141F"/><text x="440" y="136" fill="#fff" font-size="17" font-weight="700">Coordenação do programa</text>
      <line x1="440" y1="158" x2="440" y2="186" stroke="#1E2230" stroke-width="2"/><line x1="73" y1="186" x2="807" y2="186" stroke="#1E2230" stroke-width="2"/>
      {''.join(f'<line x1="{73+i*146.8:.0f}" y1="186" x2="{73+i*146.8:.0f}" y2="206" stroke="#1E2230" stroke-width="2"/><rect x="{73+i*146.8-66:.0f}" y="206" width="132" height="58" rx="10" fill="{r["cor"]}"/><text x="{73+i*146.8:.0f}" y="232" fill="#fff" font-size="14" font-weight="700">{r["n"].replace("Rio ","")}</text><text x="{73+i*146.8:.0f}" y="252" fill="#fff" font-size="12">coordenador</text>' for i,r in enumerate(RIOS))}
      <text x="440" y="300" fill="#5C6170" font-size="14">Cada rio: coordenador, 2 técnicos de campo, 1 mobilizador e equipes contratadas de plantio e coleta</text>
    </g></svg>
  </div>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:14px; margin-top:16px">
    <div class="card"><p class="H" style="font-size:30px">Transparência</p><p style="font-size:18px; color:var(--muted); margin-top:6px">Conta separada por rio, compras publicadas e painel aberto com gastos e resultados.</p></div>
    <div class="card"><p class="H" style="font-size:30px">Participação</p><p style="font-size:18px; color:var(--muted); margin-top:6px">Comitês de bacia aprovam o plano de cada rio; a comunidade acompanha nas reuniões abertas.</p></div>
  </div>''', 'Governança'))

# 19 FINANCIAMENTO
fin = [('Acordos de Mariana e Brumadinho','Rio Doce, Piracicaba e Paraopeba','Recursos de reparação já previstos para as bacias atingidas'),
       ('Cobrança pelo uso da água','Todos os rios','Aplicada pelos comitês de bacia (Lei 9.433/1997 e Lei estadual 13.199/1999)'),
       ('Copasa e prefeituras','Todos os rios','Obras de esgoto e ligações previstas nos contratos de saneamento'),
       ('Emendas parlamentares','Rio piloto','Recurso rápido para o primeiro rio provar o modelo'),
       ('Empresas da bacia','Vale do Aço, Centro-Oeste, Grande BH','Compensação ambiental, ESG e patrocínio de ecobarreiras'),
       ('Bancos e fundos','Todos os rios','Linhas de saneamento, clima e água')]
ftb = ''.join(f'<tr><td><b>{a}</b></td><td>{b}</td><td style="color:var(--muted)">{c}</td></tr>' for a,b,c in fin)
P.append(pg(f'''{head('Quem paga','Fontes de','financiamento','ink','ouro')}
  <div class="card" style="margin-top:26px; padding:14px 22px"><table style="font-size:17px"><thead><tr><th>Fonte</th><th>Onde</th><th>Como</th></tr></thead><tbody>{ftb}</tbody></table></div>
  <div class="card" style="margin-top:16px; background:var(--ouro-bg); border:0"><p style="font-size:19px"><b class="ouro">Sugestão de arranjo:</b> rio piloto com emenda parlamentar; Doce, Piracicaba e Paraopeba com recursos dos acordos; Velhas, Paraibuna e Pará com comitês, Copasa e empresas.</p></div>''', 'Financiamento'))

# 20 IMPACTOS POSITIVOS
imp = [('Saúde','Menos diarreia, verminose e internações ligadas à água suja.','#D7141F'),
       ('Água mais barata','Rio mais limpo custa menos para tratar e chegar à torneira.','#1B6CA8'),
       ('Empregos','Viveiros, plantio, coleta, sensores e obras em cada região.','#C9A227'),
       ('Turismo e lazer','Pesca, canoagem e orlas de rio voltam a atrair gente.','#2E7D4F'),
       ('Água na seca','Nascentes protegidas e mata ciliar seguram água no período seco.','#2E7D4F'),
       ('Imagem de Minas','De estado dos desastres a referência em rios vivos.','#D7141F')]
it = ''.join(f'<div class="card" style="padding:18px 22px; border-left:8px solid {c}"><p class="H" style="font-size:30px">{a}</p><p style="font-size:17px; color:var(--muted); margin-top:4px">{b}</p></div>' for a,b,c in imp)
P.append(pg(f'''{head('Como pode vir positivamente','O que Minas','ganha','ink','mata')}
  <div style="display:grid; grid-template-columns:repeat(4,1fr); gap:12px; margin-top:24px">
    <div class="card" style="padding:16px"><p class="num rio" style="font-size:40px">≈ {fmt(LIXO)} t</p><p style="font-size:14px; margin-top:4px">de lixo retirado dos rios</p></div>
    <div class="card" style="padding:16px"><p class="num mata" style="font-size:40px">{fmt(SOMA["mata"])} ha</p><p style="font-size:14px; margin-top:4px">de mata nas margens</p></div>
    <div class="card" style="padding:16px"><p class="num mata" style="font-size:40px">{fmt(SOMA["nasc"])}</p><p style="font-size:14px; margin-top:4px">nascentes protegidas</p></div>
    <div class="card" style="padding:16px"><p class="num verm" style="font-size:40px">{fmt(SOMA["caca"]//1000)} mil</p><p style="font-size:14px; margin-top:4px">casas vistoriadas</p></div>
  </div>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px; margin-top:14px">{it}</div>
  <div class="card dark" style="margin-top:14px"><p style="font-size:19px"><b style="color:#F3B9BC">Retorno:</b> a OMS estima que cada dólar investido em água e saneamento devolve cerca de quatro em saúde e produtividade.</p></div>''',
  'Impactos', 'Lixo: estimativa de 0,5 t por barreira por mês em 18 meses de operação; OMS (2012)'))

# 21 INDICADORES E RISCOS
ind = [('Pontos com IQA bom ou excelente','IGAM, anual','Aumentar em cada rio'),('Oxigênio dissolvido','Estações, a cada 15 min','Acima do mínimo legal'),
       ('Lixo retirado','Ecobarreiras, mensal',f'≈ {fmt(LIXO)} t'),('Ligações de esgoto corrigidas','Caça-esgoto, mensal','Todas as encontradas'),
       ('Mata ciliar viva','Vistoria e satélite',f'{fmt(SOMA["mata"])} ha'),('Nascentes protegidas','Cadastro',f'{fmt(SOMA["nasc"])}')]
il = ''.join(f'<tr><td><b>{a}</b></td><td>{b}</td><td class="r">{c}</td></tr>' for a,b,c in ind)
ris = [('Obras de esgoto atrasarem','Cobrar cronograma no comitê gestor e publicar o andamento'),('Mudas morrerem na seca','Plantar na chuva, regar e repor por 2 anos'),
       ('Furto ou dano de sensores','Instalação em locais seguros e parceria com a comunidade'),('Troca de gestão política','Pacto assinado por todas as instituições e metas públicas')]
rl = ''.join(f'<tr><td><b>{a}</b></td><td>{b}</td></tr>' for a,b in ris)
P.append(pg(f'''{head('Acompanhar','Indicadores','e riscos','ink','verm')}
  <div class="card" style="margin-top:26px; padding:14px 22px"><table style="font-size:17px"><thead><tr><th>Indicador</th><th>Fonte e frequência</th><th class="r">Meta</th></tr></thead><tbody>{il}</tbody></table></div>
  <div class="card" style="margin-top:16px; padding:14px 22px"><table style="font-size:17px"><thead><tr><th>Risco</th><th>Como evitar</th></tr></thead><tbody>{rl}</tbody></table></div>''', 'Monitoramento'))

# 22 PEDIDO À LIDERANÇA
P.append(pg(f'''{head('O que precisamos de você','Três decisões','para começar','ink','verm')}
  <div style="display:grid; gap:16px; margin-top:30px">
    <div class="card" style="display:grid; grid-template-columns:100px 1fr; gap:20px; border-left:10px solid var(--verm)"><p class="num verm" style="font-size:90px">1</p><div><p class="H" style="font-size:40px">Apoio político</p><p style="font-size:19px; color:var(--muted); margin-top:4px">Reunir Estado, prefeituras, Copasa e comitês para assinar o pacto do primeiro rio.</p></div></div>
    <div class="card" style="display:grid; grid-template-columns:100px 1fr; gap:20px; border-left:10px solid var(--ouro)"><p class="num ouro" style="font-size:90px">2</p><div><p class="H" style="font-size:40px">Recurso para o rio piloto</p><p style="font-size:19px; color:var(--muted); margin-top:4px">Emenda ou parceria de cerca de {mi(min(r["T"] for r in RIOS))} para provar o modelo em um rio.</p></div></div>
    <div class="card" style="display:grid; grid-template-columns:100px 1fr; gap:20px; border-left:10px solid var(--rio)"><p class="num rio" style="font-size:90px">3</p><div><p class="H" style="font-size:40px">Padrinho do programa</p><p style="font-size:19px; color:var(--muted); margin-top:4px">Acompanhar os resultados e prestar contas à população a cada três meses.</p></div></div>
  </div>
  <p class="H" style="font-size:60px; margin-top:40px; text-align:center; line-height:1.05"><span class="ink">Rios vivos são</span><span class="verm">o futuro de Minas</span></p>''', 'Próximos passos'))

# 23 FONTES
P.append(pg(f'''{head('Referências','Fontes','e notas','ink','rio', 80)}
  <div class="card" style="margin-top:28px"><ul class="dot" style="gap:12px">
    <li style="font-size:18px">IGAM: qualidade das águas em 2023; recuperação do rio das Velhas; melhora na bacia do São Francisco.</li>
    <li style="font-size:18px">Estado de Minas (2021): 54% das amostras de rios fora do limite legal em 2020.</li>
    <li style="font-size:18px">Governo de Minas / SNIS: coleta (87,6%) e tratamento (53,7%) de esgoto em 2021.</li>
    <li style="font-size:18px">Agência Minas e Planalto: novo acordo de Mariana, R$ 170 bilhões (outubro de 2024).</li>
    <li style="font-size:18px">Acordo de Brumadinho (2021); Lei estadual 23.291/2019.</li>
    <li style="font-size:18px">Leis federais 14.026/2020 (saneamento), 9.433/1997 (recursos hídricos) e Lei estadual 13.199/1999.</li>
    <li style="font-size:18px">Embrapa (fossa séptica biodigestora); OMS (2012), custo-benefício em água e saneamento.</li>
    <li style="font-size:18px">Bandeira de Minas Gerais e contorno do estado: bases públicas.</li>
  </ul></div>
  <div class="card" style="margin-top:16px"><p style="font-size:18px">Todos os custos são estimativas para planejamento, sem cotação. As quantidades por rio são propostas iniciais e devem ser ajustadas com cada comitê de bacia. O dado estadual de esgoto mais recente encontrado é de 2021.</p></div>''', 'Fontes'))

# 24 ENCERRAMENTO
N[0] += 1
P.append(f'''<section class="p" style="padding:0; background:var(--ink); background-image:none">
  <div style="position:absolute; left:0; right:0; top:0; height:500px; background:#fff; display:grid; place-items:center"><div style="width:560px; height:392px">{FLAG}</div></div>
  <div style="position:absolute; left:0; right:0; top:500px; height:10px; background:var(--verm)"></div>
  <div style="position:absolute; left:90px; right:90px; top:600px; color:#fff">
    <p class="eyebrow" style="color:#F3B9BC">Rios Vivos de Minas</p>
    <h2 class="H" style="font-size:118px; margin-top:16px"><span>Seis rios.</span><span>Dois anos.</span><span style="color:#F3B9BC">Um estado mais vivo.</span></h2>
    <p style="font-size:22px; margin-top:30px; color:#C9CDD6">{mi(GERAL)} em 24 meses · novembro de 2026</p>
  </div>
</section>''')

html = '<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Rios Vivos de Minas</title>' + CSS + '</head><body>' + ''.join(P) + '</body></html>'
open('rios-vivos-plano.html','w').write(html)
print('ok', len(P))
