# "Nordeste: dados e onde investir". Padrão do plano do Amapá, 1080x1350.
import json
fmt = lambda v: f'{v:,.0f}'.replace(',', '.')
UF = [('BA','Bahia',14.14,-12.5,-41.7),('PE','Pernambuco',9.06,-8.4,-37.9),('CE','Ceará',8.79,-5.2,-39.5),('MA','Maranhão',6.78,-5.1,-45.3),
      ('PB','Paraíba',3.97,-7.1,-36.6),('RN','Rio Grande do Norte',3.30,-5.8,-36.6),('PI','Piauí',3.27,-7.7,-42.7),('AL','Alagoas',3.13,-9.6,-36.6),('SE','Sergipe',2.21,-10.6,-37.4)]
POP = sum(u[2] for u in UF)

CSS = '''
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Anton&family=Poppins:ital,wght@0,400;0,500;0,600;0,700;0,800;1,700&family=IBM+Plex+Mono:wght@500&display=swap">
<style>
/* Nordeste: sol (laranja), mar (azul), caatinga (verde-oliva), papel quadriculado claro. */
:root{
  --paper:#FBFAF7; --grid:rgba(40,35,25,.05); --ink:#1F1B16; --muted:#625B50; --line:rgba(40,35,25,.12);
  --sol:#E8892C; --sol-bg:#FCEBD8; --mar:#0E6FA8; --mar-bg:#DCEDF7; --caat:#6A8F3B; --caat-bg:#E8F0DC; --verm:#C0392B; --verm-bg:#F8DEDB; --card:#FFFFFF;
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
.sol{color:var(--sol)} .mar{color:var(--mar)} .caat{color:var(--caat)} .ink{color:var(--ink)} .verm{color:var(--verm)}
p{font-size:21px; line-height:1.46}
.card{background:var(--card); border-radius:18px; padding:24px 28px; box-shadow:0 1px 0 rgba(40,35,25,.06), 0 10px 30px -18px rgba(40,35,25,.35); border:1px solid rgba(40,35,25,.06)}
.dark{background:var(--ink); color:#fff; border:0}
.num{font-family:var(--fh); font-weight:400; line-height:.95; font-variant-numeric:tabular-nums}
.small{font-size:16px; color:var(--muted); line-height:1.4}
.eyebrow{font-family:var(--fm); font-size:16px; letter-spacing:.12em; text-transform:uppercase; color:var(--sol)}
.top{position:absolute; left:90px; right:90px; top:44px; display:flex; justify-content:space-between; font-size:16px; color:var(--muted)}
.top b{color:var(--ink); font-weight:800}
.stripe{position:absolute; left:0; top:0; bottom:0; width:14px; display:flex; flex-direction:column}
.stripe i{flex:1}
.foot{position:absolute; left:90px; right:90px; bottom:42px; display:flex; justify-content:space-between; font-size:15px; color:var(--muted)}
ul.dot{list-style:none; display:grid; gap:10px}
ul.dot li{position:relative; padding-left:26px; font-size:19px; line-height:1.4}
ul.dot li::before{content:""; position:absolute; left:2px; top:.45em; width:12px; height:12px; border-radius:50%; background:var(--sol)}
table{border-collapse:collapse; width:100%; font-size:17px}
th{font-family:var(--fm); font-weight:500; font-size:13px; letter-spacing:.08em; text-transform:uppercase; color:var(--muted); text-align:left; padding:9px 10px; border-bottom:2px solid var(--ink)}
td{padding:8px 10px; border-bottom:1px solid var(--line); vertical-align:top}
td.r, th.r{text-align:right; font-variant-numeric:tabular-nums; white-space:nowrap}
.pill{display:inline-block; font-weight:700; font-size:14px; padding:4px 11px; border-radius:999px}
</style>'''
STRIPE = '<div class="stripe"><i style="background:var(--sol)"></i><i style="background:var(--mar)"></i><i style="background:var(--caat)"></i></div>'
N = [0]
def pg(inner, secao, fonte=''):
    N[0] += 1
    return (f'<section class="p">{STRIPE}<div class="top"><span><b>Nordeste</b> · dados e onde investir</span><span>{secao}</span></div>'
            f'{inner}<div class="foot"><span>{fonte}</span><span>{N[0]:02d}</span></div></section>')
def head(eye, l1, l2, c1='ink', c2='sol', size=92):
    return f'<p class="eyebrow">{eye}</p><h2 class="H" style="font-size:{size}px; margin-top:12px"><span class="{c1}">{l1}</span><span class="{c2}">{l2}</span></h2>'
def nota(n): return {1:('Alta','#6A8F3B'),2:('Média','#E8892C'),3:('Cautela','#C0392B')}[n]
P = []

# mapa do Nordeste (contornos reais)
geo = json.load(open('../dados/uf.json'))
X0,X1,Y0,Y1 = -48.9,-34.6,-18.4,-1.0
W=820; H=int(W*(Y1-Y0)/(X1-X0))
px=lambda x:(x-X0)/(X1-X0)*W; py=lambda y:(Y1-y)/(Y1-Y0)*H
def mapa(cores, rotulos=True, pins=''):
    out=''
    for f in geo['features']:
        s=f['properties']['sigla']
        if s not in cores: continue
        g=f['geometry']; rings=[p[0] for p in g['coordinates']] if g['type']=='MultiPolygon' else [g['coordinates'][0]]
        d=''.join('M'+' L'.join(f'{px(a):.1f},{py(b):.1f}' for a,b in r[::2])+'Z' for r in rings)
        out+=f'<path d="{d}" fill="{cores[s]}" stroke="#fff" stroke-width="2"/>'
    if rotulos:
        for s,n,pop,la,lo in UF:
            out+=f'<text x="{px(lo):.0f}" y="{py(la):.0f}" text-anchor="middle" font-family="Poppins" font-weight="800" font-size="20" fill="#1F1B16" stroke="#fff" stroke-width="4" paint-order="stroke">{s}</text>'
    return f'<svg viewBox="-10 -10 {W+20} {H+20}" style="width:100%; display:block">{out}{pins}</svg>'

# 1 CAPA
N[0] += 1
cores_capa = {u[0]: c for u,c in zip(UF, ['#E8892C','#F2A65A','#0E6FA8','#6A8F3B','#F2C14E','#3E8FC4','#A8B86A','#E07A5F','#5FA8D3'])}
P.append(f'''<section class="p" style="padding:0">
  <div style="position:absolute; left:0; right:0; top:0; height:690px; background:#FCEBD8; display:grid; place-items:center"><div style="width:520px">{mapa(cores_capa)}</div></div>
  <div style="position:absolute; left:0; right:0; top:690px; height:10px; background:var(--ink)"></div>
  <div style="position:absolute; left:90px; right:90px; top:750px">
    <p class="eyebrow">Pesquisa de dados · novembro de 2026</p>
    <h1 class="H" style="font-size:150px; margin-top:12px"><span class="ink">Nordeste</span><span class="sol" style="font-size:74px; margin-top:6px">Dados e onde investir</span></h1>
    <p style="font-size:23px; margin-top:20px; max-width:860px">Economia, energia, população, gargalos e as melhores oportunidades de investimento nos nove estados.</p>
  </div>
</section>''')

# 2 RESUMO
P.append(pg(f'''{head('Resumo','O Nordeste','em uma página')}
  <div style="display:grid; grid-template-columns:repeat(3,1fr); gap:14px; margin-top:26px">
    <div class="card"><p class="num sol" style="font-size:58px">54,6 mi</p><p style="font-size:16px; margin-top:6px">habitantes, 27% do Brasil (Censo 2022)</p></div>
    <div class="card"><p class="num sol" style="font-size:58px">≈ 14%</p><p style="font-size:16px; margin-top:6px">do PIB brasileiro</p></div>
    <div class="card"><p class="num sol" style="font-size:58px">2,9%</p><p style="font-size:16px; margin-top:6px">de crescimento em 2023 (IBGE)</p></div>
    <div class="card"><p class="num mar" style="font-size:58px">≈ 95%</p><p style="font-size:16px; margin-top:6px">da energia eólica do país sai da região</p></div>
    <div class="card"><p class="num mar" style="font-size:58px">≈ 60%</p><p style="font-size:16px; margin-top:6px">da capacidade solar centralizada</p></div>
    <div class="card"><p class="num caat" style="font-size:58px">1.794</p><p style="font-size:16px; margin-top:6px">municípios, o maior número entre as regiões</p></div>
  </div>
  <div class="card dark" style="margin-top:16px">
    <p class="eyebrow" style="color:#F6C08A">Onde investir, em ordem de atratividade</p>
    <ul class="dot" style="margin-top:12px"><li>Armazenamento de energia e transmissão, para aproveitar a energia que hoje é cortada</li><li>Data centers e tecnologia em Fortaleza e Recife</li><li>Água, saneamento e dessalinização no semiárido</li><li>Fruticultura irrigada, turismo e serviços para o setor público</li></ul>
  </div>''', 'Resumo', 'IBGE; ABEEólica; Governo da Bahia (SDE)'))

# 3 ESTADOS
mx = UF[0][2]
rows = ''.join(f'<div style="display:grid; grid-template-columns:230px 1fr 110px; gap:12px; align-items:center; padding:7px 0; border-bottom:1px solid var(--line)"><span style="font-size:18px; font-weight:700">{n}</span><span style="height:22px; background:rgba(40,35,25,.06); border-radius:0 5px 5px 0; overflow:hidden"><span style="display:block; height:100%; width:{p/mx*100:.1f}%; background:var(--sol); border-radius:0 5px 5px 0"></span></span><span style="text-align:right; font-weight:700">{str(p).replace(".",",")} mi</span></div>' for s,n,p,la,lo in UF)
P.append(pg(f'''{head('Os nove estados','População','por estado','ink','sol')}
  <div class="card" style="margin-top:26px; padding:16px 24px"><p class="eyebrow" style="color:var(--muted)">Habitantes · Censo 2022</p>{rows}</div>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:14px; margin-top:14px">
    <div class="card"><p class="H mar" style="font-size:30px">Três estados grandes</p><p style="font-size:17px; color:var(--muted); margin-top:4px">Bahia, Pernambuco e Ceará somam 59% da população e concentram indústria, portos e serviços.</p></div>
    <div class="card"><p class="H caat" style="font-size:30px">Capitais fortes</p><p style="font-size:17px; color:var(--muted); margin-top:4px">Salvador, Fortaleza e Recife estão entre as maiores metrópoles do país.</p></div>
  </div>''', 'Estados', 'IBGE, Censo Demográfico 2022, valores arredondados'))

# 4 ECONOMIA
P.append(pg(f'''{head('Economia','Cresce, mas','ainda é desigual','ink','sol')}
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:14px; margin-top:26px">
    <div class="card"><p class="num sol" style="font-size:66px">2,9%</p><p style="font-size:17px; margin-top:6px">crescimento do PIB do Nordeste em 2023. Foi a única região que manteve estável a fatia do PIB nacional.</p></div>
    <div class="card"><p class="num verm" style="font-size:66px">Menor</p><p style="font-size:17px; margin-top:6px">renda por pessoa do país: o desafio e, ao mesmo tempo, o espaço para crescer.</p></div>
  </div>
  <div class="card" style="margin-top:14px">
    <p class="eyebrow" style="color:var(--muted)">Motores da economia</p>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px 28px; margin-top:12px">
      <p style="font-size:18px"><b>Serviços e comércio</b> · a maior parte do PIB</p>
      <p style="font-size:18px"><b>Energia renovável</b> · eólica e solar em expansão</p>
      <p style="font-size:18px"><b>Agro</b> · soja no MATOPIBA, frutas no São Francisco</p>
      <p style="font-size:18px"><b>Indústria</b> · Camaçari, Suape, Pecém</p>
      <p style="font-size:18px"><b>Turismo</b> · litoral de 3.300 km</p>
      <p style="font-size:18px"><b>Tecnologia</b> · Porto Digital (Recife) e Fortaleza</p>
    </div>
  </div>
  <div class="card dark" style="margin-top:14px"><p style="font-size:19px"><b style="color:#F6C08A">Leitura:</b> a região tem mercado consumidor grande (54,6 milhões de pessoas) e renda ainda baixa. Produtos e serviços que reduzem custo para famílias, empresas e prefeituras têm demanda garantida.</p></div>''',
  'Economia', 'IBGE, Contas Regionais 2023 (divulgadas em nov/2025); FGV IBRE'))

# 5 ENERGIA
P.append(pg(f'''{head('Energia','A bateria','limpa do Brasil','ink','mar')}
  <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:14px; margin-top:26px">
    <div class="card"><p class="num mar" style="font-size:58px">≈ 95%</p><p style="font-size:16px; margin-top:6px">da geração eólica do país (março de 2025)</p></div>
    <div class="card"><p class="num mar" style="font-size:58px">≈ 60%</p><p style="font-size:16px; margin-top:6px">da solar centralizada, com destaque para Bahia, Piauí e Pernambuco</p></div>
    <div class="card"><p class="num mar" style="font-size:58px">102%</p><p style="font-size:16px; margin-top:6px">da demanda do Nordeste atendida só pelo vento em dia recorde</p></div>
  </div>
  <div class="card" style="margin-top:14px; border-left:8px solid var(--verm)"><p class="H verm" style="font-size:32px">O problema: energia jogada fora</p><p style="font-size:18px; margin-top:6px">Mais de 95% dos cortes de geração do país acontecem no Nordeste: há energia sobrando e faltam linhas de transmissão e armazenamento. Empresas de renováveis chegaram a suspender quase R$ 40 bilhões em investimentos na região.</p></div>
  <div class="card" style="margin-top:14px; background:var(--mar-bg); border:0"><p style="font-size:19px"><b class="mar">A oportunidade está no gargalo:</b> baterias, transmissão, consumo local da energia (indústria, data centers, hidrogênio) e serviços de manutenção dos parques.</p></div>''',
  'Energia', 'Governo da Bahia (SDE, informes de energia eólica); ABEEólica; O Povo; Folha'))

# 6 HIDROGÊNIO
P.append(pg(f'''{head('Hidrogênio verde','Promessa grande,','prazo longo','ink','caat')}
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:14px; margin-top:26px">
    <div class="card"><p class="eyebrow">Pecém · Ceará</p><p class="num caat" style="font-size:58px; margin-top:8px">R$ 71,7 bi</p><p style="font-size:16px; margin-top:6px">em seis projetos anunciados, com cerca de 25 mil empregos na obra (ABIHV)</p></div>
    <div class="card"><p class="eyebrow">Suape · Pernambuco</p><p class="num caat" style="font-size:58px; margin-top:8px">R$ 15,7 bi</p><p style="font-size:16px; margin-top:6px">projeto listado pelo Ministério de Minas e Energia, com operação prevista a partir de 2030</p></div>
  </div>
  <div class="card" style="margin-top:14px; border-left:8px solid var(--sol)"><p class="H sol" style="font-size:30px">Realidade em 2026</p><p style="font-size:18px; margin-top:6px">Os acordos do Pecém ainda são pré-contratos. Reportagens de 2026 mostram que boa parte das promessas segue no papel, e a decisão final de grandes investidores é esperada para 2027 em diante.</p></div>
  <div class="card dark" style="margin-top:14px"><p style="font-size:19px"><b style="color:#F6C08A">Como entrar sem esperar:</b> serviços para a cadeia que já existe nos portos: engenharia, licenciamento, formação de mão de obra, fornecedores locais e monitoramento ambiental.</p></div>''',
  'Hidrogênio', 'Diário do Nordeste (2025-2026); MME, lista de projetos 2025'))

# 7 MAPA DE OPORTUNIDADES
OPS = [('Pecém','CE',-3.55,-38.81,'#6A8F3B','Hidrogênio e porto'),('Fortaleza','CE',-3.73,-38.53,'#0E6FA8','Cabos submarinos e data centers'),
       ('Recife','PE',-8.05,-34.9,'#0E6FA8','Porto Digital'),('Suape','PE',-8.39,-34.97,'#6A8F3B','Porto e indústria'),
       ('Petrolina','PE',-9.39,-40.50,'#6A8F3B','Frutas irrigadas'),('Salvador','BA',-12.97,-38.50,'#E8892C','Serviços e turismo'),
       ('Camaçari','BA',-12.70,-38.32,'#E8892C','Polo industrial'),('Caetité','BA',-14.07,-42.47,'#0E6FA8','Eólica e solar'),
       ('São Luís','MA',-2.53,-44.30,'#6A8F3B','Porto do Itaqui'),('Balsas','MA',-7.53,-46.03,'#E8892C','Grãos (MATOPIBA)'),
       ('Mossoró','RN',-5.19,-37.34,'#0E6FA8','Vento, sal e petróleo'),('S. J. do Piauí','PI',-8.36,-42.25,'#0E6FA8','Solar')]
pins=''
for i,(n,u,la,lo,c,d) in enumerate(OPS):
    pins+=f'<circle cx="{px(lo):.1f}" cy="{py(la):.1f}" r="15" fill="{c}" stroke="#fff" stroke-width="3"/><text x="{px(lo):.1f}" y="{py(la)+5:.1f}" text-anchor="middle" font-family="Poppins" font-size="13" font-weight="800" fill="#fff">{i+1}</text>'
cinza={u[0]:'#EDE7DD' for u in UF}
lg=''.join(f'<div style="display:grid; grid-template-columns:28px 1fr; gap:8px; align-items:center"><span style="width:28px; height:28px; border-radius:50%; background:{c}; color:#fff; font-weight:800; font-size:13px; display:grid; place-items:center">{i+1}</span><span style="font-size:13.5px; line-height:1.25"><b>{n}</b><br>{d}</span></div>' for i,(n,u,la,lo,c,d) in enumerate(OPS))
P.append(pg(f'''{head('Onde está o dinheiro','Mapa das','oportunidades','ink','sol', 84)}
  <div class="card" style="margin-top:20px; padding:10px"><div style="width:540px; margin:0 auto">{mapa(cinza, pins=pins)}</div></div>
  <div class="card" style="margin-top:12px; display:grid; grid-template-columns:1fr 1fr 1fr; gap:8px 18px; padding:16px 20px">{lg}</div>''', 'Mapa', 'Localização aproximada'))

# 8-9 SETORES PARA INVESTIR
SET = [('Armazenamento e transmissão de energia',1,'Energia sobrando e cortes de geração: baterias e linhas valem ouro.','Grande porte; parcerias com geradoras'),
       ('Data centers e nuvem',1,'Fortaleza é um dos maiores pontos de chegada de cabos submarinos do mundo, com energia renovável perto.','Grande porte; serviços de TI no entorno'),
       ('Tecnologia e software',1,'Porto Digital em Recife e polos em Fortaleza e Salvador: talento mais barato que no Sudeste.','Startups, fábricas de software, GovTech'),
       ('Água e saneamento',1,'Semiárido, meta legal de 2033 e cidades com baixa cobertura de esgoto.','Dessalinização, reúso, perdas de água'),
       ('Energia solar distribuída',2,'Sol forte o ano todo; comércio e agro reduzem a conta de luz.','Instalação, manutenção, assinatura'),
       ('Fruticultura irrigada',2,'Vale do São Francisco exporta manga e uva; irrigação e logística de frio.','Agro, packing houses, tecnologia de irrigação'),
       ('Turismo',2,'Litoral, cultura e voos internacionais em Fortaleza, Recife, Salvador e Natal.','Hospedagem, experiências, turismo de base local'),
       ('Grãos e logística (MATOPIBA)',2,'Fronteira de soja e milho no sul do Maranhão, Piauí e oeste da Bahia.','Armazéns, transporte, insumos'),
       ('Serviços para prefeituras',1,'1.794 municípios precisando digitalizar, cumprir a Lei 14.133 e organizar documentos.','Digitalização, GED, LGPD, compras'),
       ('Hidrogênio verde',3,'Bilhões anunciados, mas sem decisão final dos investidores.','Fornecedores e serviços, não aposta direta')]
def tab(itens):
    return ''.join(f'<tr><td style="width:310px"><b style="font-size:18px">{a}</b></td><td style="font-size:16px">{b}<br><span style="color:var(--muted); font-size:14px">{d}</span></td><td><span class="pill" style="background:{nota(n)[1]}; color:#fff">{nota(n)[0]}</span></td></tr>' for a,n,b,d in itens)
P.append(pg(f'''{head('Onde investir','Dez setores','· parte 1','ink','sol', 84)}
  <div class="card" style="margin-top:22px; padding:12px 22px"><table><thead><tr><th>Setor</th><th>Por que e como entrar</th><th>Atratividade</th></tr></thead><tbody>{tab(SET[:5])}</tbody></table></div>''', 'Setores', 'Atratividade: avaliação qualitativa desta pesquisa'))
P.append(pg(f'''{head('Onde investir','Dez setores','· parte 2','ink','sol', 84)}
  <div class="card" style="margin-top:22px; padding:12px 22px"><table><thead><tr><th>Setor</th><th>Por que e como entrar</th><th>Atratividade</th></tr></thead><tbody>{tab(SET[5:])}</tbody></table></div>
  <div class="card dark" style="margin-top:14px"><p style="font-size:19px"><b style="color:#F6C08A">Ligação com a DigitalGov:</b> o Maranhão e a Bahia publicaram tantos editais de digitalização quanto estados muito maiores entre setembro e novembro de 2026. O Nordeste é o próximo mercado natural da empresa.</p></div>''', 'Setores', 'Atratividade: avaliação qualitativa; editais: amostra do PNCP'))

# 10 INCENTIVOS
inc = [('SUDENE','Redução de até 75% do imposto de renda para empreendimentos em setores prioritários na área da autarquia.'),
       ('Banco do Nordeste (FNE)','Crédito com juros menores para empresas da região, do pequeno ao grande porte.'),
       ('Zonas de processamento de exportação','Pecém (CE) tem uma zona de processamento de exportação em funcionamento, com benefícios fiscais para exportar.'),
       ('Incentivos estaduais','Programas de ICMS dos estados para atrair indústria e serviços.'),
       ('Porto Digital','Benefícios municipais de ISS para empresas de tecnologia no Recife.')]
it=''.join(f'<tr><td style="width:300px"><b>{a}</b></td><td>{b}</td></tr>' for a,b in inc)
P.append(pg(f'''{head('Dinheiro mais barato','Incentivos','para investir','ink','caat')}
  <div class="card" style="margin-top:26px; padding:14px 24px"><table style="font-size:18px"><tbody>{it}</tbody></table></div>
  <div class="card" style="margin-top:14px; background:var(--caat-bg); border:0"><p style="font-size:19px"><b class="caat">Dica:</b> projetos que combinam crédito do FNE com o incentivo da SUDENE reduzem bastante o custo do capital. Confira as regras e os setores prioritários de cada programa antes de decidir.</p></div>''',
  'Incentivos', 'SUDENE; Banco do Nordeste; governos estaduais'))

# 11 RISCOS
rs = [('Cortes de energia','Excesso de geração sem transmissão derruba a receita de parques.','#C0392B'),
      ('Água','Secas no semiárido afetam agro, indústria e cidades.','#E8892C'),
      ('Renda baixa','Consumo sensível a preço e a programas sociais.','#E8892C'),
      ('Infraestrutura','Ferrovias e estradas ainda incompletas, como a Transnordestina.','#E8892C'),
      ('Promessas sem prazo','Megaprojetos anunciados que não saem do papel.','#C0392B')]
rr=''.join(f'<div class="card" style="padding:18px 24px; border-left:8px solid {c}"><p class="H" style="font-size:30px">{a}</p><p style="font-size:17px; color:var(--muted); margin-top:4px">{b}</p></div>' for a,b,c in rs)
P.append(pg(f'''{head('Antes de investir','Riscos','para considerar','ink','verm')}
  <div style="display:grid; gap:12px; margin-top:26px">{rr}</div>''', 'Riscos'))

# 12 PLANO PRÁTICO
pp = [('Pequeno investimento','Até R$ 100 mil','Energia solar para comércio, serviços para prefeituras, turismo de experiência, revenda de tecnologia.','#6A8F3B'),
      ('Médio investimento','R$ 100 mil a R$ 5 mi','Software e GovTech com equipe no Recife ou em Fortaleza, packing de frutas, pequenas usinas solares, reúso de água.','#0E6FA8'),
      ('Grande investimento','Acima de R$ 5 mi','Baterias e transmissão, data centers, logística no MATOPIBA, hotelaria.','#E8892C')]
ppt=''.join(f'<div style="display:grid; grid-template-columns:230px 1fr; gap:18px"><div style="background:{c}; color:#fff; border-radius:14px; padding:18px; display:grid; align-content:center"><p class="H" style="font-size:28px">{a}</p><p style="font-size:15px; margin-top:4px">{b}</p></div><div class="card" style="padding:20px 24px"><p style="font-size:18px">{d}</p></div></div>' for a,b,d,c in pp)
P.append(pg(f'''{head('Na prática','Por onde','começar','ink','sol')}
  <div style="display:grid; gap:16px; margin-top:26px">{ppt}</div>
  <div class="card dark" style="margin-top:18px"><p style="font-size:19px"><b style="color:#F6C08A">Primeiro passo:</b> escolher um estado-base (Ceará, Pernambuco ou Bahia), visitar o Porto Digital, o Pecém e o Banco do Nordeste e validar o projeto com dois ou três clientes locais.</p></div>''', 'Começar', 'Faixas de investimento indicativas'))

# 13 FONTES
P.append(pg(f'''{head('Referências','Fontes','e notas','ink','mar', 80)}
  <div class="card" style="margin-top:26px"><ul class="dot" style="gap:12px">
    <li style="font-size:17.5px">IBGE: Censo 2022; Sistema de Contas Regionais 2023 (divulgado em nov/2025), via Movimento Econômico e FGV IBRE.</li>
    <li style="font-size:17.5px">Governo da Bahia (SDE): informes executivos de energia eólica 2025; ABEEólica: boletim anual 2026 e dados de cortes de geração (O Povo, abr/2026).</li>
    <li style="font-size:17.5px">Folha/Bahia Notícias: empresas de renováveis suspendem quase R$ 40 bilhões em investimentos no Nordeste.</li>
    <li style="font-size:17.5px">Diário do Nordeste e Ministério de Minas e Energia: projetos de hidrogênio verde no Pecém e em Suape.</li>
    <li style="font-size:17.5px">PNCP: amostra de editais de digitalização (set. a nov. de 2026), do relatório DigitalGov.</li>
    <li style="font-size:17.5px">Contornos dos estados: base pública de limites estaduais.</li>
  </ul></div>
  <div class="card" style="margin-top:14px"><p style="font-size:17.5px">Os percentuais de energia variam conforme o recorte (geração ou capacidade, mês ou ano). A atratividade dos setores é uma avaliação desta pesquisa, não recomendação de investimento.</p></div>''', 'Fontes'))

html = '<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Nordeste Dados e Investimentos</title>' + CSS + '</head><body>' + ''.join(P) + '</body></html>'
open('nordeste.html','w').write(html)
print('ok', len(P), round(POP,2))
