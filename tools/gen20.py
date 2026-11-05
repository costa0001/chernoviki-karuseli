# Генератор "сильных" каруселей (10 слайдов) из данных. Стиль: gendesign.py.
# Каждый слайд: dict(k=тип, tag, t=заголовок, p=текст, d=данные визуала, z=тизер-петля)
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from gendesign import *
from PIL import Image, ImageFilter
R = '#FF6B6B'
FB = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'foto-baza', '2026-10-zheneva'))

CSS2 = CSS + '''
.z{position:absolute;left:72px;right:72px;bottom:46px;font-weight:800;font-size:32px;color:#F5C542;text-align:right;z-index:4}
.emo{font-family:"Noto Color Emoji"}'''

def T(tag, t, p):
    return f'<div class="tx" style="padding:0 72px"><div class="tag">{tag}</div><h1>{t}</h1><div class="p">{p}</div></div>'

W = 'width:100%;padding:0 72px;box-sizing:border-box'
def vis(k, d):
    if k == 'emo':
        cards = ''.join(f'<div style="flex:1;border-radius:34px;background:rgba(255,255,255,.06);border:3px solid {SKY if i<len(d)-1 else Y};padding:44px 8px;text-align:center"><div class="emo" style="font-size:{130 if len(d)<4 else 100}px;line-height:1.1">{e}</div><div style="font-weight:800;font-size:{38 if len(d)<4 else 32}px;margin-top:20px">{l}</div></div>' for i, (e, l) in enumerate(d))
        return f'<div style="{W};display:flex;gap:24px">{cards}</div>'
    if k == 'num':
        n, e = d
        return f'''<div style="display:flex;justify-content:center;align-items:center;gap:50px">
<div style="font-weight:800;font-size:360px;line-height:1;color:{Y};text-shadow:0 0 60px rgba(245,197,66,.35)">{n}</div>
<div style="width:320px;height:320px;border-radius:50%;background:rgba(111,183,255,.12);border:4px solid {SKY};display:flex;align-items:center;justify-content:center"><div class="emo" style="font-size:170px">{e}</div></div></div>'''
    if k == 'vs':
        a, b = d
        col = lambda items, c, h, x: f'<div style="flex:1;border-radius:28px;border:4px solid {c};background:rgba(255,255,255,.05);padding:30px 28px"><div style="font-weight:800;font-size:38px;color:{c};letter-spacing:3px">{h}</div>' + ''.join(f'<div style="font-weight:700;font-size:38px;line-height:1.2;margin-top:24px"><span style="color:{c}">{x}</span> {i}</div>' for i in items) + '</div>'
        return f'<div style="{W};display:flex;gap:24px">{col(a,R,"НЕТ","✕")}{col(b,Y,"ДА","✓")}</div>'
    if k == 'quote':
        q = ''.join(f'<div style="position:relative;background:#1E2C48;border:3px solid {R};border-radius:40px 40px 40px 10px;padding:30px 110px 30px 40px;font-family:L;font-style:italic;font-weight:600;font-size:{56 if len(d)<3 else 50}px;line-height:1.15;margin:16px 0">«{s}»<div style="position:absolute;right:26px;top:50%;transform:translateY(-50%);width:66px;height:66px;border-radius:50%;background:{R};color:#fff;font-family:S;font-style:normal;font-weight:800;font-size:40px;display:flex;align-items:center;justify-content:center">✕</div></div>' for s in d)
        return f'<div style="{W}"><div style="font-weight:800;font-size:32px;letter-spacing:5px;color:{R};margin-bottom:6px">НЕ ГОВОРИТЕ ТАК</div>{q}</div>'
    if k == 'big':
        a, b = d
        fs = 260 if len(a) <= 4 else (190 if len(a) <= 7 else 150)
        return f'<div style="text-align:center;width:100%"><div style="font-weight:800;font-size:{fs}px;line-height:1;color:{Y};text-shadow:0 0 70px rgba(245,197,66,.4)">{a}</div><div style="font-weight:800;font-size:42px;letter-spacing:6px;color:#AEB9CC;margin-top:34px">{b}</div></div>'
    if k == 'check':
        it = ''.join(f'<div style="display:flex;gap:22px;align-items:center;border-bottom:2px solid #D9CFBB;padding:15px 0"><div style="flex:none;width:46px;height:46px;border:4px solid {NV};border-radius:10px"></div><div style="font-weight:700;font-size:36px;color:{NV};line-height:1.2">{s}</div></div>' for s in d)
        return f'<div style="width:calc(100% - 200px);box-sizing:border-box;background:#F6F1E6;border-radius:22px;padding:28px 46px;box-shadow:0 30px 70px rgba(0,0,0,.45);transform:rotate(-1.5deg)"><div style="font-weight:800;font-size:30px;letter-spacing:4px;color:#8A7A5A;margin-bottom:4px">ЧЕК-ЛИСТ</div>{it}</div>'
    if k == 'scene':
        e, s = d
        return f'''<div style="text-align:center;{W}"><div class="emo" style="font-size:170px;letter-spacing:16px;line-height:1.1">{e}</div>
<div style="display:inline-block;margin-top:40px;background:{SKY};color:{NV};font-family:L;font-style:italic;font-weight:700;font-size:50px;line-height:1.2;padding:28px 44px;border-radius:44px 44px 44px 10px">«{s}»</div></div>'''
    return ''

def slide(i, N, s):
    v = vis(s.get('k'), s.get('d'))
    inner = (f'<div style="position:absolute;top:105px;bottom:{110 if s.get("z") else 70}px;left:0;right:0;display:flex;flex-direction:column;z-index:2">'
             f'<div class="vz" style="flex:1 1 auto;min-height:0;display:flex;align-items:center;justify-content:center;padding:10px 0 34px">{v}</div>'
             f'{T(s["tag"], s["t"], s["p"])}</div>' + (f'<div class="z">{s["z"]}</div>' if s.get('z') else ''))
    return S(i, N, inner)

FIT = '''()=>{const v=document.querySelector('.vz');const t=document.querySelector('.tx');if(!v||!t)return 0;let g=0;
const h1=t.querySelector('h1'),p=t.querySelector('.p');
while(v.scrollHeight>v.clientHeight+2&&g<25){g++;
 const c=v.firstElementChild;c.style.zoom=(parseFloat(c.style.zoom||1)*0.95);
 if(g>6){h1.style.fontSize=(parseFloat(getComputedStyle(h1).fontSize)*0.96)+'px';p.style.fontSize=(parseFloat(getComputedStyle(p).fontSize)*0.96)+'px';}}
return g}'''

def build(c, out):
    """c: dict(slug, photo, pos, ct, cs, sl=[8 слайдов], cta)"""
    os.makedirs(out, exist_ok=True)
    N = 10
    ph = f'{out}/_cover.jpg'
    im = Image.open(f'{FB}/{c["photo"]}').convert('RGB')
    im = im.resize((1080, int(im.height * 1080 / im.width)), Image.LANCZOS).filter(ImageFilter.UnsharpMask(1.5, 80, 2))
    im.save(ph, quality=95)
    sl = {1: cover(ph, c.get('pos', 'center 25%'), c['ct'], c['cs'], N)}
    for j, s in enumerate(c['sl']):
        sl[j + 2] = slide(j + 2, N, s)
    sl[N] = cta(N, N, c['cta'])
    fits = {}
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1080, 'height': 1350})
        for k in sorted(sl):
            open(f'{out}/_t.html', 'w').write(f'<html><head><meta charset="utf-8"><style>{CSS2}</style></head><body>{sl[k]}</body></html>')
            pg.goto(f'file://{out}/_t.html'); pg.wait_for_timeout(250)
            if 1 < k < N: fits[k] = pg.evaluate(FIT)
            pg.screenshot(path=f'{out}/slide_{k:02d}.png')
        b.close()
    for k in sorted(sl):
        Image.open(f'{out}/slide_{k:02d}.png').convert('RGB').save(f'{out}/slide_{k:02d}.jpg', quality=93)
        os.remove(f'{out}/slide_{k:02d}.png')
    os.remove(f'{out}/_t.html'); os.remove(ph)
    ims = [Image.open(f'{out}/slide_{k:02d}.jpg').resize((270, 338)) for k in sorted(sl)]
    sh = Image.new('RGB', (280 * 5, 348 * 2), '#777')
    for j, imm in enumerate(ims): sh.paste(imm, ((j % 5) * 280, (j // 5) * 348))
    return sh, fits
