const { chromium } = require('playwright');
(async () => {
  const [src, out, png] = process.argv.slice(2);
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 794, height: 1123 } });
  await p.goto('file://' + src, { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  const r = await p.evaluate(() => {
    const o = [];
    document.querySelectorAll('.p').forEach((s, i) => {
      const sb = s.getBoundingClientRect();
      s.querySelectorAll('table, .box, .kpis').forEach(e => {
        const bb = e.getBoundingClientRect();
        if (bb.bottom > sb.bottom - 40) o.push((i + 1) + ' ' + e.tagName + '.' + e.className + ' ' + Math.round(bb.bottom - sb.top));
      });
    });
    return o;
  });
  console.log(r.join('\n') || 'layout ok');
  await p.pdf({ path: out, format: 'A4', printBackground: true });
  if (png) {
    const els = await p.$$('.p');
    for (let i = 0; i < els.length; i++) await els[i].screenshot({ path: png + '/pag-' + String(i + 1).padStart(2, '0') + '.png' });
  }
  await b.close();
})();
