# Relatório 2026 da DigitalGov: mercado de digitalização no setor público e plano de vendas. Padrão do plano do Amapá.
import json, collections, io, contextlib
import analise
A = analise.agg()
IT26 = [i for i in analise.IT if i['_ano'] == '2026' and i['_dt'] >= '2026-09-01']
N26 = len(IT26)
brl = lambda v: 'R$ ' + f'{v:,.0f}'.replace(',', '.')
mi = lambda v: 'R$ ' + f'{v/1e6:,.1f}'.replace('.', ',') + ' mi'
fmt = lambda v: f'{v:,.0f}'.replace(',', '.')
pc = lambda a, b: f'{a/b*100:.0f}%'
C = collections.Counter
tipo = C(analise.tipo_orgao(i) for i in IT26)
esf = C(i.get('esfera_nome') or 'n/d' for i in IT26)
uf = C(i.get('uf') for i in IT26)
mod = C(i.get('modalidade_licitacao_nome') for i in IT26)
srp = sum(1 for i in IT26 if i.get('srp'))
mes = C(i['_mes'] for i in IT26)
import re
temas = {t: sum(1 for i in IT26 if re.search(rx, i['_d'])) for t, rx in analise.TEMAS}
vals = sorted(v for v in (i.get('valor_total_estimado') for i in IT26) if isinstance(v, (int, float)) and v > 0)
med = vals[len(vals)//2]; q1 = vals[len(vals)//4]; q3 = vals[3*len(vals)//4]
ate65 = sum(1 for v in vals if v <= 65492.11)
MG = sorted([i for i in IT26 if i.get('uf') == 'MG'], key=lambda i: -(i.get('valor_total_estimado') or 0))

VENDAS = [('2026','Prefeitura de Ibiá','Pregão eletrônico',1179000,'Solução integrada de serviços administrativos e LGPD'),
          ('2026','Prefeitura de Cordisburgo','Pregão (registro de preço)',99990,'Digitalização e licença de software de gestão'),
          ('2025','Prefeitura de Araçuaí','Pregão (registro de preço)',10980650,'Solução integrada de serviços administrativos'),
          ('2024','Prefeitura de Santo Antônio do Itambé','Pregão eletrônico (suspenso)',149865,'Digitalização em PDF e indexação'),
          ('2024','Câmara de Manhumirim','Dispensa',30600,'Arquivologia: organização e restauração')]
VA = collections.defaultdict(float)
for a,_,_,v,_ in VENDAS: VA[a] += v
TOTV = sum(VA.values())

CSS = '''
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Anton&family=Poppins:ital,wght@0,400;0,500;0,600;0,700;0,800;1,700&family=IBM+Plex+Mono:wght@500&display=swap">
<style>
/* Padrão do plano do Amapá com identidade de tecnologia: azul-profundo, azul DigitalGov, verde de crescimento, laranja para alertas. */
:root{
  --paper:#F8FAFC; --grid:rgba(19,32,58,.05); --ink:#13203A; --muted:#566178; --line:rgba(19,32,58,.12);
  --azul:#1546A0; --azul-bg:#E1E9F8; --verde:#12A150; --verde-bg:#DDF3E6; --lar:#E8692C; --lar-bg:#FCE7DC; --ouro:#B8902A; --ouro-bg:#F5EDD6; --card:#FFFFFF;
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
.azul{color:var(--azul)} .verde{color:var(--verde)} .lar{color:var(--lar)} .ink{color:var(--ink)} .ouro{color:var(--ouro)}
p{font-size:21px; line-height:1.46}
.card{background:var(--card); border-radius:18px; padding:24px 28px; box-shadow:0 1px 0 rgba(19,32,58,.06), 0 10px 30px -18px rgba(19,32,58,.35); border:1px solid rgba(19,32,58,.06)}
.dark{background:var(--ink); color:#fff; border:0}
.num{font-family:var(--fh); font-weight:400; line-height:.95; font-variant-numeric:tabular-nums}
.small{font-size:16px; color:var(--muted); line-height:1.4}
.eyebrow{font-family:var(--fm); font-size:16px; letter-spacing:.12em; text-transform:uppercase; color:var(--azul)}
.top{position:absolute; left:90px; right:90px; top:44px; display:flex; justify-content:space-between; font-size:16px; color:var(--muted)}
.top b{color:var(--ink); font-weight:800}
.stripe{position:absolute; left:0; top:0; bottom:0; width:14px; display:flex; flex-direction:column}
.stripe i{flex:1}
.foot{position:absolute; left:90px; right:90px; bottom:42px; display:flex; justify-content:space-between; font-size:15px; color:var(--muted)}
ul.dot{list-style:none; display:grid; gap:10px}
ul.dot li{position:relative; padding-left:26px; font-size:20px; line-height:1.4}
ul.dot li::before{content:""; position:absolute; left:2px; top:.5em; width:11px; height:11px; border-radius:3px; background:var(--verde)}
table{border-collapse:collapse; width:100%; font-size:17px}
th{font-family:var(--fm); font-weight:500; font-size:13px; letter-spacing:.08em; text-transform:uppercase; color:var(--muted); text-align:left; padding:9px 10px; border-bottom:2px solid var(--ink)}
td{padding:7px 10px; border-bottom:1px solid var(--line); vertical-align:top}
td.r, th.r{text-align:right; font-variant-numeric:tabular-nums; white-space:nowrap}
.pill{display:inline-block; font-weight:700; font-size:15px; padding:5px 12px; border-radius:999px}
</style>'''
STRIPE = '<div class="stripe"><i style="background:var(--azul)"></i><i style="background:var(--verde)"></i><i style="background:var(--ink)"></i></div>'
N = [0]
def pg(inner, secao, fonte=''):
    N[0] += 1
    return (f'<section class="p">{STRIPE}<div class="top"><span><b>DigitalGov</b> · relatório 2026</span><span>{secao}</span></div>'
            f'{inner}<div class="foot"><span>{fonte}</span><span>{N[0]:02d}</span></div></section>')
def head(eye, l1, l2, c1='ink', c2='azul', size=92):
    return f'<p class="eyebrow">{eye}</p><h2 class="H" style="font-size:{size}px; margin-top:12px"><span class="{c1}">{l1}</span><span class="{c2}">{l2}</span></h2>'
def barras(pares, cor, total=None, w=230, fs=17, sufixo=''):
    mx = max(v for _, v in pares)
    return ''.join(f'<div style="display:grid; grid-template-columns:{w}px 1fr 110px; gap:12px; align-items:center; padding:6px 0"><span style="font-size:{fs}px; font-weight:600">{n}</span><span style="height:20px; background:rgba(19,32,58,.06); border-radius:0 5px 5px 0; overflow:hidden"><span style="display:block; height:100%; width:{v/mx*100:.1f}%; background:{cor}; border-radius:0 5px 5px 0"></span></span><span style="text-align:right; font-variant-numeric:tabular-nums; font-size:{fs}px"><b>{fmt(v)}</b>{(" · "+pc(v,total)) if total else ""}{sufixo}</span></div>' for n, v in pares)
FONTE_A = f'PNCP, amostra de {N26} editais de digitalização publicados de set. a nov. de 2026'
P = []

# 1 CAPA
N[0] += 1
P.append(f'''<section class="p" style="padding:0; background:var(--ink); background-image:none">
  <svg viewBox="0 0 1080 640" style="position:absolute; left:0; top:0; width:1080px; height:640px" aria-hidden="true">
    <rect width="1080" height="640" fill="#13203A"/>
    {''.join(f'<rect x="{140+c*64}" y="{90+r*84}" width="{44 if (r+c)%3 else 44}" height="60" rx="6" fill="{"#1546A0" if (r*7+c*3)%5 else "#12A150"}" opacity="{0.25+((r+c)%4)*0.18:.2f}"/>' for r in range(6) for c in range(13))}
    <rect x="460" y="180" width="160" height="210" rx="12" fill="#F8FAFC"/><path d="M580 180 L620 220 L580 220 Z" fill="#C9D3E6"/>
    <g fill="#1546A0"><rect x="485" y="245" width="110" height="10" rx="3"/><rect x="485" y="270" width="90" height="10" rx="3"/><rect x="485" y="295" width="110" height="10" rx="3"/><rect x="485" y="320" width="70" height="10" rx="3"/></g>
    <circle cx="610" cy="380" r="34" fill="#12A150"/><path d="M594 380 l11 11 l21 -22" stroke="#fff" stroke-width="7" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
  </svg>
  <div style="position:absolute; left:90px; right:90px; top:700px; color:#fff">
    <p class="eyebrow" style="color:#7FA6F0">DigitalGov Tecnologia da Informação · relatório 2026</p>
    <h1 class="H" style="font-size:118px; margin-top:14px"><span>Digitalização</span><span style="color:#7FE0A8">no setor público</span></h1>
    <p style="font-size:24px; margin-top:18px; max-width:880px; color:#D5DCEA">Nossas vendas, o mercado em 2026, quem compra, por que compra e como vender mais em 2027.</p>
  </div>
  <p style="position:absolute; left:90px; bottom:50px; color:#8C97AE; font-size:16px; font-family:var(--fm); letter-spacing:.1em">DADOS DO PNCP · NOVEMBRO DE 2026</p>
</section>''')

# 2 RESUMO
P.append(pg(f'''{head('Resumo executivo','O ano','em uma página')}
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:14px; margin-top:28px">
    <div class="card"><p class="num azul" style="font-size:64px">{mi(TOTV)}</p><p style="font-size:17px; margin-top:6px">vencidos pela DigitalGov de 2024 a 2026 em processos públicos achados no PNCP</p></div>
    <div class="card"><p class="num verde" style="font-size:64px">≈ {round((mes["10"]+mes["11"])/2)}</p><p style="font-size:17px; margin-top:6px">editais de digitalização por mês no Brasil (média de outubro e novembro de 2026)</p></div>
    <div class="card"><p class="num ink" style="font-size:64px">{pc(esf["Municipal"],N26)}</p><p style="font-size:17px; margin-top:6px">das compras são de municípios: prefeituras, câmaras, autarquias e consórcios</p></div>
    <div class="card"><p class="num lar" style="font-size:64px">{brl(med)}</p><p style="font-size:17px; margin-top:6px">é o valor mediano: quase o teto da dispensa (R$ 65.492,11)</p></div>
  </div>
  <div class="card dark" style="margin-top:16px">
    <p class="eyebrow" style="color:#7FE0A8">Três decisões para 2027</p>
    <ul class="dot" style="margin-top:12px"><li>Criar um <b>pacote abaixo de R$ 65 mil</b> para vender por dispensa, que é metade do mercado.</li><li>Atacar as <b>câmaras municipais</b>: 1 em cada 5 compras do setor.</li><li>Usar a <b>ata de Araçuaí</b> e os consórcios de Minas para escalar sem nova licitação.</li></ul>
  </div>''', 'Resumo', 'PNCP; valores estimados dos editais'))

# 3 NOSSAS VENDAS
vt = ''.join(f'<tr><td><b>{a}</b></td><td><b>{o}</b><br><span style="font-size:14px; color:var(--muted)">{obj}</span></td><td>{m}</td><td class="r">{brl(v)}</td></tr>' for a,o,m,v,obj in VENDAS)
mxa = max(VA.values())
ab = ''.join(f'<div style="display:grid; grid-template-rows:auto 1fr auto; justify-items:center; gap:8px; height:280px"><span class="num" style="font-size:22px; white-space:nowrap">{mi(VA[a]).replace("R$ ","")}</span><span style="width:84px; align-self:end; height:{max(VA[a]/mxa*200,6):.0f}px; background:{"#1546A0" if a!="2025" else "#12A150"}; border-radius:8px 8px 0 0"></span><span class="H" style="font-size:30px">{a}</span></div>' for a in ('2024','2025','2026'))
P.append(pg(f'''{head('Nossas vendas','DigitalGov','2024 a 2026','ink','verde')}
  <div style="display:grid; grid-template-columns:420px 1fr; gap:16px; margin-top:26px; align-items:start">
    <div class="card" style="display:grid; grid-template-columns:repeat(3,1fr); gap:10px; align-items:end"><p class="eyebrow" style="grid-column:1/-1; color:var(--muted); font-size:13px">Valor vencido por ano (R$)</p>{ab}</div>
    <div class="card" style="padding:18px 22px"><p class="eyebrow" style="color:var(--muted)">Leitura</p><p style="font-size:18px; margin-top:8px">2025 foi puxado por um único contrato grande (Araçuaí). Em 2026 vencemos <b>Ibiá</b> e <b>Cordisburgo</b>. A carteira depende de poucos contratos: o objetivo de 2027 é ter muitos contratos médios e recorrentes.</p></div>
  </div>
  <div class="card" style="margin-top:14px; padding:12px 22px"><table style="font-size:16.5px"><thead><tr><th>Ano</th><th>Órgão e objeto</th><th>Modalidade</th><th class="r">Valor vencido</th></tr></thead><tbody>{vt}</tbody></table></div>
  <p class="small" style="margin-top:10px">Todos os órgãos em Minas Gerais. Santo Antônio do Itambé está suspenso. Araçuaí é ata de registro de preço: o valor é o teto, não o já pago. Só aparecem processos que citam a empresa no texto do PNCP.</p>''',
  'Vendas', 'PNCP: resultados dos itens de cada processo, CNPJ 24.361.188/0001-61'))

# 4 MERCADO AGORA
mb = barras([('Setembro', mes['09']), ('Outubro', mes['10']), ('Novembro (até dia 26)', mes['11'])], '#1546A0', w=260, fs=19)
P.append(pg(f'''{head('O mercado agora','A demanda','está aquecida','ink','verde')}
  <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:14px; margin-top:26px">
    <div class="card"><p class="num azul" style="font-size:60px">{N26}</p><p style="font-size:16px; margin-top:6px">editais de digitalização em menos de 3 meses</p></div>
    <div class="card"><p class="num azul" style="font-size:60px">{len(uf)}</p><p style="font-size:16px; margin-top:6px">estados com compras no período</p></div>
    <div class="card"><p class="num verde" style="font-size:46px; white-space:nowrap">{mi(sum(vals))}</p><p style="font-size:16px; margin-top:6px">em valores estimados somados</p></div>
  </div>
  <div class="card" style="margin-top:14px"><p class="eyebrow" style="color:var(--muted)">Editais por mês</p><div style="margin-top:10px">{mb}</div></div>
  <div class="card" style="margin-top:14px; background:var(--verde-bg); border:0"><p style="font-size:19px"><b class="verde">Fim de ano compra mais:</b> outubro e novembro concentram compras para usar o orçamento antes de dezembro. Propostas e atas precisam estar prontas em setembro.</p></div>
  <p class="small" style="margin-top:10px">Setembro aparece menor porque a amostra começa no fim de agosto e uma página da consulta falhou.</p>''', 'Mercado', FONTE_A))

# 5 QUEM COMPRA
tp = barras(tipo.most_common(), '#1546A0', N26, w=260)
P.append(pg(f'''{head('Quem compra','Prefeituras','e câmaras lideram','ink','azul')}
  <div class="card" style="margin-top:26px">{tp}</div>
  <div style="display:grid; grid-template-columns:repeat(3,1fr); gap:14px; margin-top:14px">
    <div class="card"><p class="num azul" style="font-size:50px">{pc(esf["Municipal"],N26)}</p><p style="font-size:16px">municipal</p></div>
    <div class="card"><p class="num azul" style="font-size:50px">{pc(esf["Federal"],N26)}</p><p style="font-size:16px">federal</p></div>
    <div class="card"><p class="num azul" style="font-size:50px">{pc(esf["Estadual"],N26)}</p><p style="font-size:16px">estadual</p></div>
  </div>
  <div class="card dark" style="margin-top:14px"><p style="font-size:19px"><b style="color:#7FE0A8">Oportunidade:</b> as câmaras municipais são {pc(tipo["Câmaras municipais"],N26)} das compras. Têm arquivo antigo, pouca equipe e compram por dispensa. São mais de 5.500 no Brasil.</p></div>''', 'Quem compra', FONTE_A + '; "Outros órgãos" inclui conselhos profissionais e autarquias'))

# 6 ONDE
ub = barras(uf.most_common(15), '#12A150', N26, w=80, fs=17)
P.append(pg(f'''{head('Onde','Estados que','mais compram','ink','verde')}
  <div class="card" style="margin-top:26px">{ub}</div>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:14px; margin-top:14px">
    <div class="card"><p class="H azul" style="font-size:30px">Minas é o 2º mercado</p><p style="font-size:17px; color:var(--muted); margin-top:4px">{uf["MG"]} editais no período, atrás só de São Paulo. Já temos atestados aqui.</p></div>
    <div class="card"><p class="H lar" style="font-size:30px">Nordeste em alta</p><p style="font-size:17px; color:var(--muted); margin-top:4px">Maranhão e Bahia ({uf["MA"]} e {uf["BA"]}) compram tanto quanto estados maiores. Mercado a abrir.</p></div>
  </div>''', 'Estados', FONTE_A))

# 7 COMO COMPRAM
mdb = barras([(k.replace(' - ',' '), v) for k, v in mod.most_common(4)], '#1546A0', N26, w=240)
P.append(pg(f'''{head('Como compram','Metade é','dispensa','ink','lar')}
  <div class="card" style="margin-top:26px">{mdb}</div>
  <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:14px; margin-top:14px">
    <div class="card"><p class="num lar" style="font-size:52px">{brl(med)}</p><p style="font-size:15px; margin-top:6px">valor mediano dos editais</p></div>
    <div class="card"><p class="num lar" style="font-size:52px">{pc(ate65,len(vals))}</p><p style="font-size:15px; margin-top:6px">estão até o teto da dispensa (R$ 65.492,11)</p></div>
    <div class="card"><p class="num azul" style="font-size:52px">{srp}</p><p style="font-size:15px; margin-top:6px">usam registro de preço, que permite adesão de outros órgãos</p></div>
  </div>
  <div class="card" style="margin-top:14px"><p style="font-size:18px"><b>Faixas de valor:</b> 25% dos editais até {brl(q1)}, metade até {brl(med)} e 75% até {brl(q3)}. Poucos contratos muito grandes, como o do Consórcio de Saúde do Norte de Minas, puxam a soma.</p></div>
  <div class="card dark" style="margin-top:14px"><p style="font-size:19px"><b style="color:#7FE0A8">Consequência:</b> quem tem uma oferta pronta, documentada e abaixo de R$ 65 mil fecha em semanas, sem disputa longa.</p></div>''', 'Modalidades', FONTE_A))

# 8 O QUE COMPRAM
tb = barras(sorted(temas.items(), key=lambda kv: -kv[1]), '#12A150', N26, w=330, fs=17)
P.append(pg(f'''{head('O que compram','Não é só','escanear papel','ink','verde')}
  <div class="card" style="margin-top:26px"><p class="eyebrow" style="color:var(--muted)">Assuntos citados no objeto dos editais (um edital pode citar vários)</p><div style="margin-top:8px">{tb}</div></div>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:14px; margin-top:14px">
    <div class="card"><p class="H azul" style="font-size:30px">Software recorrente</p><p style="font-size:17px; color:var(--muted); margin-top:4px">{pc(temas["Software de gestão de documentos (GED)"],N26)} pedem sistema ou licença. É receita mensal, não só serviço único.</p></div>
    <div class="card"><p class="H lar" style="font-size:30px">LGPD quase ausente</p><p style="font-size:17px; color:var(--muted); margin-top:4px">Só {temas["LGPD"]} edital cita LGPD no objeto. Quem levar LGPD junto da digitalização se diferencia.</p></div>
  </div>''', 'Objetos', FONTE_A))

# 9 CRESCEU? POR QUÊ
P.append(pg(f'''{head('Cresceu ou não?','O setor cresce,','e há motivos','ink','verde')}
  <div class="card" style="margin-top:26px"><p style="font-size:20px"><b>Resposta curta:</b> a demanda está forte em 2026, com cerca de 90 editais por mês no fim do ano, em todos os estados e esferas. A amostra não permite medir o crescimento exato contra 2025, mas as leis abaixo empurram os órgãos para o digital todo ano.</p></div>
  <div style="display:grid; gap:12px; margin-top:14px">
    <div class="card" style="border-left:8px solid var(--azul); padding:18px 24px"><p class="H" style="font-size:28px">Lei 14.133/2021</p><p style="font-size:17px; color:var(--muted)">Os atos das licitações devem ser preferencialmente digitais.</p></div>
    <div class="card" style="border-left:8px solid var(--azul); padding:18px 24px"><p class="H" style="font-size:28px">Decreto 10.278/2020 e Lei 13.874/2019</p><p style="font-size:17px; color:var(--muted)">Dão valor legal ao documento digitalizado com requisitos técnicos. Permitem descartar papel com segurança.</p></div>
    <div class="card" style="border-left:8px solid var(--verde); padding:18px 24px"><p class="H" style="font-size:28px">Prazo de abril de 2027</p><p style="font-size:17px; color:var(--muted)">Municípios de até 20 mil habitantes precisam cumprir as regras de divulgação da Lei 14.133. Corrida por organização documental.</p></div>
    <div class="card" style="border-left:8px solid var(--verde); padding:18px 24px"><p class="H" style="font-size:28px">LGPD, Lei de Acesso e tribunais de contas</p><p style="font-size:17px; color:var(--muted)">Pedidos de informação, auditorias e proteção de dados exigem achar documentos rápido.</p></div>
    <div class="card" style="border-left:8px solid var(--lar); padding:18px 24px"><p class="H" style="font-size:28px">Espaço e risco</p><p style="font-size:17px; color:var(--muted)">Arquivos lotados, mofo, enchentes e incêndios: digitalizar é também proteger a memória do órgão.</p></div>
  </div>''', 'Motivos', 'Leis 14.133/2021, 13.874/2019, 13.709/2018, 12.527/2011; Decreto 10.278/2020'))

# 10 MINAS: OPORTUNIDADES
mgr = ''.join(f'<tr><td><b>{i["orgao_nome"].title()}</b>{" <span class=\"pill\" style=\"background:var(--verde-bg); color:var(--verde); font-size:12px\">nosso</span>" if "CORDISBURGO" in i["orgao_nome"] else ""}</td><td>{i["_dt"][8:]}/{i["_dt"][5:7]}</td><td>{(i.get("modalidade_licitacao_nome") or "").replace("Pregão - Eletrônico","Pregão")}</td><td class="r">{brl(i.get("valor_total_estimado") or 0) if (i.get("valor_total_estimado") or 0) > 100 else "—"}</td></tr>' for i in MG[:18])
P.append(pg(f'''{head('Minas Gerais agora','Editais recentes','no nosso estado','ink','azul', 80)}
  <div class="card" style="margin-top:22px; padding:12px 22px"><table style="font-size:15.5px"><thead><tr><th>Órgão</th><th>Data</th><th>Modalidade</th><th class="r">Valor estimado</th></tr></thead><tbody>{mgr}</tbody></table></div>
  <div class="card dark" style="margin-top:14px"><p style="font-size:18px"><b style="color:#7FE0A8">Ação imediata:</b> conferir quais ainda estão abertos, participar dos pregões e oferecer adesão às atas que já temos. Os consórcios de saúde do Norte de Minas e do Médio São Francisco são os maiores valores.</p></div>''',
  'Minas Gerais', FONTE_A + '; ordenados por valor estimado'))

# 11 COMO VENDER MAIS
est = [('Pacote Dispensa','Oferta fechada até R$ 65 mil: digitalização de um setor + 12 meses de software. Proposta pronta em 24 horas.','#E8692C'),
       ('Programa Câmaras','Kit para câmaras municipais: arquivo legislativo, atas, leis e portal de transparência digitalizados.','#1546A0'),
       ('Carona na ata','Divulgar a ata de registro de preço de Araçuaí para que outros órgãos possam aderir, dentro dos limites da lei.','#12A150'),
       ('Consórcios','Vender para o consórcio e atender dezenas de municípios com um único processo.','#12A150'),
       ('Monitor diário do PNCP','Rotina de busca por "digitalização" todos os dias; responder a toda cotação de preço.','#1546A0'),
       ('Atestados que vendem','Cada contrato entregue gera atestado de capacidade técnica e um caso de sucesso com números.','#B8902A'),
       ('Diferencial LGPD + validade legal','Digitalização conforme o Decreto 10.278, com assinatura, metadados e política de dados.','#E8692C'),
       ('Novos estados','Entrar em São Paulo, Bahia e Maranhão com parceiro local ou representante.','#13203A')]
ec = ''.join(f'<div class="card" style="padding:18px 22px; border-top:6px solid {c}"><p class="H" style="font-size:28px">{a}</p><p style="font-size:16.5px; color:var(--muted); margin-top:4px">{b}</p></div>' for a,b,c in est)
P.append(pg(f'''{head('Como vender mais','Oito jogadas','para 2027','ink','verde')}
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px; margin-top:24px">{ec}</div>''', 'Estratégia'))

# 12 PACOTES E PREÇOS
pac = [('Dispensa Express','Câmaras e prefeituras pequenas','Até 100 mil páginas + software 12 meses','R$ 49 mil a R$ 64 mil'),
       ('Câmara Digital','Câmaras municipais','Acervo legislativo + portal + treinamento','R$ 35 mil a R$ 60 mil'),
       ('Prefeitura Integrada','Prefeituras médias','Digitalização por secretaria + GED + LGPD','R$ 300 mil a R$ 1,5 mi (pregão/ata)'),
       ('GED por assinatura','Clientes que já digitalizaram','Software, suporte e armazenamento','R$ 1,5 mil a R$ 8 mil por mês'),
       ('Consórcio','Consórcios intermunicipais','Ata para todos os municípios consorciados','Sob medida')]
pt = ''.join(f'<tr><td><b>{a}</b></td><td>{b}</td><td style="color:var(--muted)">{c}</td><td class="r">{d}</td></tr>' for a,b,c,d in pac)
P.append(pg(f'''{head('Produtos','Pacotes','e faixas de preço','ink','azul')}
  <div class="card" style="margin-top:26px; padding:12px 22px"><table style="font-size:16.5px"><thead><tr><th>Pacote</th><th>Para quem</th><th>O que inclui</th><th class="r">Faixa sugerida</th></tr></thead><tbody>{pt}</tbody></table></div>
  <div class="card" style="margin-top:14px; background:var(--azul-bg); border:0"><p style="font-size:18px"><b class="azul">Por que essas faixas:</b> metade dos editais de 2026 fica até {brl(med)}. O Dispensa Express cabe abaixo do teto de R$ 65.492,11 e pode ser contratado em semanas.</p></div>
  <p class="small" style="margin-top:10px">Faixas sugeridas para planejamento. Ajustar ao custo real por página e à margem da empresa.</p>''', 'Produtos'))

# 13 PLANO COMERCIAL 2027
tri = [('JAN–MAR','Base','Pacotes prontos, cadastro em portais de compras de MG, SP, BA e MA, monitor diário do PNCP, 3 casos de sucesso documentados.','#1546A0'),
       ('ABR–JUN','Câmaras','Campanha para 300 câmaras de Minas; meta de 10 contratos por dispensa.','#12A150'),
       ('JUL–SET','Escala','Consórcios e adesões às atas; primeiras propostas em SP e no Nordeste.','#B8902A'),
       ('OUT–DEZ','Colheita','Fim de ano concentra compras: equipe dedicada a cotações e pregões.','#E8692C')]
tt = ''.join(f'<div style="display:grid; grid-template-columns:190px 1fr; gap:18px"><div style="background:{c}; color:#fff; border-radius:14px; display:grid; place-items:center; padding:16px"><p class="H" style="font-size:34px; text-align:center">{a}</p></div><div class="card" style="padding:18px 22px"><p class="H" style="font-size:30px">{b}</p><p style="font-size:17px; color:var(--muted); margin-top:4px">{d}</p></div></div>' for a,b,d,c in tri)
P.append(pg(f'''{head('Plano comercial','Metas','para 2027','ink','verde')}
  <div style="display:grid; grid-template-columns:repeat(3,1fr); gap:14px; margin-top:24px">
    <div class="card"><p class="num verde" style="font-size:56px">40</p><p style="font-size:16px">contratos no ano</p></div>
    <div class="card"><p class="num verde" style="font-size:56px">4</p><p style="font-size:16px">estados com venda</p></div>
    <div class="card"><p class="num verde" style="font-size:56px">30%</p><p style="font-size:16px">da receita em software recorrente</p></div>
  </div>
  <div style="display:grid; gap:14px; margin-top:16px">{tt}</div>''', 'Plano 2027', 'Metas sugeridas para discussão interna'))

# 14 MÉTODO
P.append(pg(f'''{head('Método e limites','Como os dados','foram obtidos','ink','azul', 80)}
  <div class="card" style="margin-top:26px"><ul class="dot" style="gap:12px">
    <li style="font-size:18px"><b>Vendas da DigitalGov:</b> processos do PNCP que citam a empresa; para cada item, o resultado com fornecedor e valor homologado.</li>
    <li style="font-size:18px"><b>Mercado:</b> busca no PNCP por "digitalização documentos" em editais, ordenados do mais novo para o mais antigo. Foram lidos 950 editais e mantidos {N26} cujo objeto cita digitalização ou gestão eletrônica de documentos, publicados de setembro a 26 de novembro de 2026.</li>
    <li style="font-size:18px"><b>Classificação:</b> tipo de órgão pelo nome; assuntos por palavras-chave no objeto; valores pelo valor estimado do edital.</li>
  </ul></div>
  <div class="card" style="margin-top:14px; background:var(--lar-bg); border:0"><p style="font-size:18px"><b class="lar">Limites:</b> é uma amostra de cerca de três meses, não o ano todo, e uma página da consulta falhou. Não dá para afirmar o crescimento exato contra 2025. Valores estimados não são valores contratados. Contratos da empresa que não citam o nome no PNCP podem ter ficado de fora.</p></div>
  <div class="card dark" style="margin-top:14px"><p style="font-size:18px">Os programas de consulta estão no repositório e podem ser rodados de novo para completar o ano inteiro e comparar com 2025.</p></div>''', 'Método', 'Portal Nacional de Contratações Públicas (pncp.gov.br)'))

html = '<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>DigitalGov Relatório 2026</title>' + CSS + '</head><body>' + ''.join(P) + '</body></html>'
open('relatorio-digitalgov.html', 'w').write(html)
print('ok', len(P), N26, med, ate65, len(vals), dict(mes))
