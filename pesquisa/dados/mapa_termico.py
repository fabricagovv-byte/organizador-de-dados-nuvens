import json, csv, sys
D = sys.argv[1]
AL = ['AC','AP','AM','PA','RO','RR','TO','MT','MA']
geo = json.load(open(f'{D}/uf.json'))
polys = {}   # sigla -> list of rings (outer rings only, fine for point test)
allbr = {}
for f in geo['features']:
    s = f['properties']['sigla']; g = f['geometry']
    rings = [p[0] for p in g['coordinates']] if g['type']=='MultiPolygon' else [g['coordinates'][0]]
    allbr[s] = rings
    if s in AL: polys[s] = rings
def bbox(r): xs=[p[0] for p in r]; ys=[p[1] for p in r]; return min(xs),min(ys),max(xs),max(ys)
idx = {s:[(r,bbox(r)) for r in rs] for s,rs in polys.items()}
def inside(x,y,r):
    c=False; n=len(r); j=n-1
    for i in range(n):
        xi,yi=r[i][0],r[i][1]; xj,yj=r[j][0],r[j][1]
        if (yi>y)!=(yj>y) and x < (xj-xi)*(y-yi)/(yj-yi+1e-12)+xi: c=not c
        j=i
    return c
cnt={s:0 for s in AL}; pts=[]; dates=set()
for row in csv.DictReader(open(f'{D}/viirs7d.csv')):
    if row['confidence']=='low': continue
    x=float(row['longitude']); y=float(row['latitude'])
    if not (-74.5<x<-41 and -18.5<y<5.5): continue
    for s,lst in idx.items():
        hit=False
        for r,(a,b,c,d) in lst:
            if a<=x<=c and b<=y<=d and inside(x,y,r): hit=True; break
        if hit: cnt[s]+=1; pts.append((x,y)); dates.add(row['acq_date']); break
# grade 0.3°
G=0.3; grid={}
for x,y in pts:
    k=(int((x+75)//G), int((y+20)//G)); grid[k]=grid.get(k,0)+1
# projeção
X0,X1,Y0,Y1=-74.5,-41.5,-18.5,5.5
W=720; H=int(W*(Y1-Y0)/(X1-X0))
px=lambda x:(x-X0)/(X1-X0)*W; py=lambda y:(Y1-y)/(Y1-Y0)*H
def path(r, step):
    pts_=r[::step] if len(r)>step*8 else r
    return 'M'+' L'.join(f'{px(p[0]):.1f},{py(p[1]):.1f}' for p in pts_)+'Z'
out=[f'<svg viewBox="0 0 {W} {H}" style="width:100%; height:100%; display:block" role="img" aria-label="Mapa térmico de focos de calor na Amazônia Legal, últimos 7 dias">']
# vizinhos fora da Amazônia Legal, apagados
for s,rs in allbr.items():
    if s in AL: continue
    for r in rs:
        if max(p[0] for p in r) < X0 or min(p[1] for p in r) > Y1: continue
        out.append(f'<path d="{path(r,6)}" fill="#163E14" stroke="#24521F" stroke-width="0.6"/>')
for s,rs in polys.items():
    for r in rs: out.append(f'<path d="{path(r,4)}" fill="#1D5418" stroke="#E2F27A" stroke-opacity=".45" stroke-width="1"/>')
# rampa sequencial de um matiz (laranja), escuro -> claro
ramp=['#8A3B12','#B5501A','#DE6A25','#F2894A','#F8AE7E','#FCD3B6']
th=[1,3,8,20,45,90]
def cor(n):
    c=ramp[0]
    for t,col in zip(th,ramp):
        if n>=t: c=col
    return c
cw=G/(X1-X0)*W; ch=G/(Y1-Y0)*H
for (i,j),n in sorted(grid.items(), key=lambda kv: kv[1]):
    x=-75+i*G; y=-20+(j+1)*G
    out.append(f'<rect x="{px(x):.1f}" y="{py(y):.1f}" width="{cw:.1f}" height="{ch:.1f}" rx="1.5" fill="{cor(n)}"/>')
# rótulos dos estados (centroide aproximado pela bbox do maior anel)
for s,rs in polys.items():
    r=max(rs,key=len); a,b,c,d=bbox(r)
    cx,cy=(a+c)/2,(b+d)/2
    if s=='PA': cx,cy=-52.5,-4.6
    if s=='MA': cx,cy=-45.3,-5.2
    if s=='AM': cx,cy=-64.5,-4.2
    out.append(f'<text x="{px(cx):.0f}" y="{py(cy):.0f}" text-anchor="middle" fill="#F3F6EA" font-family="IBM Plex Mono" font-size="13" font-weight="500" opacity=".9">{s}</text>')
out.append('</svg>')
open(f'{D}/mapa.svg','w').write('\n'.join(out))
leg=''.join(f'<span style="display:inline-flex;align-items:center;gap:5px;margin-right:10px"><i style="width:14px;height:10px;border-radius:2px;background:{c};display:inline-block"></i>{t}+</span>' for t,c in zip(th,ramp))
json.dump({'cnt':cnt,'total':sum(cnt.values()),'dates':sorted(dates),'legend':leg,'W':W,'H':H}, open(f'{D}/stats.json','w'), ensure_ascii=False)
print(sum(cnt.values()), sorted(dates)[0], sorted(dates)[-1]); print(sorted(cnt.items(), key=lambda kv:-kv[1]))
