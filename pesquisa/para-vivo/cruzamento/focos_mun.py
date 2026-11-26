import json, csv, sys
D = sys.argv[1]
geo = json.load(open(f'{D}/mun-pa.json'))
mun = []
for f in geo['features']:
    g = f['geometry']; nm = f['properties']['name']
    rings = [p[0] for p in g['coordinates']] if g['type']=='MultiPolygon' else [g['coordinates'][0]]
    bbs = []
    for r in rings:
        xs=[p[0] for p in r]; ys=[p[1] for p in r]; bbs.append((r,(min(xs),min(ys),max(xs),max(ys))))
    mun.append((nm,bbs))
def inside(x,y,r):
    c=False; j=len(r)-1
    for i in range(len(r)):
        xi,yi=r[i][0],r[i][1]; xj,yj=r[j][0],r[j][1]
        if (yi>y)!=(yj>y) and x<(xj-xi)*(y-yi)/(yj-yi+1e-12)+xi: c=not c
        j=i
    return c
cnt={m[0]:0 for m in mun}; frp={m[0]:0.0 for m in mun}; dates=set(); pts=[]
for row in csv.DictReader(open(f'{D}/viirs7d.csv')):
    if row['confidence']=='low': continue
    x=float(row['longitude']); y=float(row['latitude'])
    if not (-59.2<x<-45.8 and -10.1<y<2.8): continue
    for nm,bbs in mun:
        hit=False
        for r,(a,b,c,d) in bbs:
            if a<=x<=c and b<=y<=d and inside(x,y,r): hit=True; break
        if hit:
            cnt[nm]+=1; frp[nm]+=float(row['frp'] or 0); dates.add(row['acq_date']); pts.append((x,y)); break
tot=sum(cnt.values())
top=sorted(cnt.items(), key=lambda kv:-kv[1])[:20]
json.dump({'cnt':cnt,'total':tot,'dates':sorted(dates),'pts':pts}, open(f'{D}/focos_pa.json','w'), ensure_ascii=False)
print(tot, min(dates), max(dates)); print(top)
