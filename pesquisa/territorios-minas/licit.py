import io, contextlib, html as H, re, csv
with contextlib.redirect_stdout(io.StringIO()):
    import doc as D
COMP = sorted([x for x in D.COMP if not re.search(r'eletrocardiogra|pacs|laudos de exames|radiolog|tomograf', D._n(x['objeto']))], key=lambda x: x['data'], reverse=True)
cons = {c['cnpj']: c for c in D.CONS}
N = [0]
def pg(inner):
    N[0] += 1
    return f'<section class="p"><div class="top"><img src="{D.LOGO}" alt="DigitalGov"><span>Licitações de digitalização</span></div>{inner}<div class="foot"><span>Consórcios de Minas · digitalização, gestão documental e GED · PNCP, consulta de 27/11/2026</span><span>{N[0]:02d}</span></div></section>'
def linha(x):
    c = cons.get(x['cnpj'], {})
    ti = D.id2inter.get(str(c.get('ibge') or ''), '')
    dt = f'{x["data"][8:10]}/{x["data"][5:7]}/{x["data"][:4]}'
    return (f'<div style="break-inside:avoid; border-top:.6pt solid var(--k); padding:3mm 0 3.5mm">'
            f'<div style="display:flex; justify-content:space-between; gap:4mm"><p style="font-family:var(--fh); font-size:12.5pt; font-weight:700">{H.escape(D.short(c, 60) if c else x["orgao"][:60])}</p>'
            f'<p style="font-family:var(--fm); font-size:8.5pt; white-space:nowrap">{dt} · {"EDITAL" if x["tipo"] == "edital" else "ATA"}</p></div>'
            f'<p style="font-size:8.5pt; color:var(--g5)">{H.escape((c.get("municipio") or "").title())} · {H.escape(ti)} · tel. {D.tel(c.get("tel1"))} · {H.escape(x.get("modalidade") or "")} · {H.escape(x.get("situacao") or "")}</p>'
            f'<p style="font-size:9.5pt; margin-top:1.5mm">{H.escape(x["objeto"][:340])}{"…" if len(x["objeto"]) > 340 else ""}</p>'
            f'<p style="font-family:var(--fm); font-size:7.5pt; margin-top:1.5mm">{x["url"].replace("https://","")}</p></div>')
nc = len({x['cnpj'] for x in COMP}); ne = sum(1 for x in COMP if x['tipo'] == 'edital'); na = len(COMP) - ne
P = []
N[0] += 1
P.append(f'''<section class="p" style="padding:30mm 18mm">
  <img src="{D.LOGO}" alt="DigitalGov" style="height:20mm">
  <div style="margin-top:34mm; border-top:2pt solid var(--k); padding-top:8mm">
    <p class="eb">Consórcios intermunicipais de Minas Gerais</p>
    <h1 style="font-size:48pt; margin-top:4mm">Licitações de<br>digitalização</h1>
    <p style="font-size:13pt; margin-top:6mm; max-width:150mm">Editais e atas de digitalização de documentos, gestão documental e GED publicados pelos consórcios no PNCP, do mais recente para o mais antigo.</p>
  </div>
  <div class="kpis" style="margin-top:20mm">
    <div><b>{len(COMP)}</b><span>licitações</span></div>
    <div><b>{ne}</b><span>editais</span></div>
    <div><b>{na}</b><span>atas de registro de preços</span></div>
    <div><b>{nc}</b><span>consórcios</span></div>
  </div>
  <div class="box" style="margin-top:10mm"><p><b>Atas</b> são as melhores portas de entrada: outros municípios e consórcios podem aderir a elas dentro dos limites da Lei 14.133. <b>Editais recentes</b> mostram quem está comprando agora.</p></div>
</section>''')
blocos = [linha(x) for x in COMP]
for k in range(0, len(blocos), 5):
    head = '<p class="eb">Licitações</p><h2 style="font-size:20pt; margin-top:1mm; margin-bottom:3mm">Da mais recente para a mais antiga</h2>' if k == 0 else ''
    P.append(pg(head + ''.join(blocos[k:k+5])))
html = '<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Licitações de Digitalização</title>' + D.CSS + '</head><body>' + ''.join(P) + '</body></html>'
open('licitacoes.html', 'w').write(html)
with open('Licitacoes-digitalizacao-consorcios.csv', 'w', newline='', encoding='utf-8-sig') as f:
    w = csv.writer(f, delimiter=';'); w.writerow(['Data','Tipo','Consórcio','Cidade-sede','Território','Telefone','Modalidade','Situação','Objeto','Link'])
    for x in COMP:
        c = cons.get(x['cnpj'], {})
        w.writerow([x['data'], x['tipo'], D.short(c, 80) if c else x['orgao'], (c.get('municipio') or '').title(), D.id2inter.get(str(c.get('ibge') or ''), ''), D.tel(c.get('tel1')), x.get('modalidade') or '', x.get('situacao') or '', x['objeto'], x['url']])
print('ok', len(COMP), ne, na, nc, len(P))
