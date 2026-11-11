import os, sys, math
sys.path.insert(0, '/home/claude/chernoviki-karuseli/tools')
os.chdir('/home/claude/chernoviki-karuseli')
from gendesign import *
N = 13
R = '#FF6B6B'
GR = '#9AA6B8'


def zone(i, k, title, text, ill, top=700):
    badge = f'<div style="display:inline-block;border:3px solid {Y};color:{Y};border-radius:40px;padding:6px 26px;font-weight:800;font-size:30px;letter-spacing:3px">СЛЕПАЯ ЗОНА {k}</div>'
    return S(i, N, f'''{ill}<div class="txt" style="top:{top}px">{badge}<h1 style="margin-top:26px">{title}</h1>
<div class="p">{text}</div></div>''')


def why(i, title, text, ill, top=700):
    badge = f'<div style="display:inline-block;background:{R};color:#fff;border-radius:40px;padding:8px 26px;font-weight:800;font-size:30px;letter-spacing:3px">ПОЧЕМУ НЕ РАБОТАЕТ</div>'
    return S(i, N, f'''{ill}<div class="txt" style="top:{top}px">{badge}<h1 style="margin-top:26px">{title}</h1>
<div class="p">{text}</div></div>''')


def card(t, extra=''):
    return f'<div style="background:#F6F1E6;color:{NV};border-radius:18px;padding:22px 30px;font-weight:700;font-size:34px;line-height:1.3;box-shadow:0 14px 40px rgba(0,0,0,.35);{extra}">{t}</div>'


def quotes(items, top=150):
    q = ''.join(card(f'«{t}»', f'transform:rotate({r}deg);margin-top:26px;{s}') for t, r, s in items)
    return f'<div style="position:absolute;top:{top}px;left:100px;right:100px">{q}</div>'


def chip(t, c=None, extra=''):
    c = c or SKY
    return f'<div style="display:inline-block;background:rgba(255,255,255,.07);border:3px solid {c};border-radius:50px;padding:14px 30px;font-weight:800;font-size:36px;margin:10px;{extra}">{t}</div>'


def two(lt, lbig, ltxt, rt, rbig, rtxt, top=140, h=390, lc=None, rc=None):
    lc = lc or GR; rc = rc or Y
    return f'''<div style="position:absolute;top:{top}px;left:110px;right:110px;display:flex;gap:40px">
<div style="flex:1;border-radius:30px;background:rgba(255,255,255,.05);border:3px solid {lc};padding:34px;height:{h}px">
<div style="font-weight:800;font-size:34px;color:{lc}">{lt}</div><div style="font-weight:800;font-size:84px;margin-top:20px;line-height:1.05;color:{R if lc==GR else '#fff'}">{lbig}</div><div style="font-weight:600;font-size:32px;color:#E6ECF5;margin-top:16px">{ltxt}</div></div>
<div style="flex:1;border-radius:30px;background:rgba(245,197,66,.1);border:3px solid {rc};padding:34px;height:{h}px">
<div style="font-weight:800;font-size:34px;color:{rc}">{rt}</div><div style="font-weight:800;font-size:84px;margin-top:20px;line-height:1.05;color:{rc}">{rbig}</div><div style="font-weight:600;font-size:32px;color:#E6ECF5;margin-top:16px">{rtxt}</div></div></div>'''


def cover_full(img, pos, tag, title, sub):
    """Новая раскладка обложки: фото на весь слайд, текст поверх снизу."""
    return f'''<div class="s"><img src="file://{img}" style="position:absolute;inset:0;width:1080px;height:1350px;object-fit:cover;object-position:{pos}">
<div style="position:absolute;left:0;right:0;top:680px;bottom:0;background:linear-gradient(180deg,rgba(8,20,40,0) 0%,rgba(8,20,40,.85) 35%,#081428 65%)"></div>
<div class="top" style="color:#fff;text-shadow:0 2px 8px rgba(0,0,0,.6)"><span>@bravo.konstantin</span><span>1 / {N} &rarr;</span></div>
<div class="txt" style="bottom:90px"><div style="display:inline-block;background:{Y};color:{NV};font-weight:800;font-size:30px;letter-spacing:3px;padding:8px 22px;border-radius:10px;text-transform:uppercase">{tag}</div>
<h1 style="font-size:80px;margin-top:24px;text-shadow:0 4px 20px rgba(0,0,0,.5)">{title}</h1><div class="p" style="margin-top:22px">{sub}</div></div></div>'''


def personal(i):
    return S(i, N, f'''<div class="txt" style="top:0;bottom:80px;display:flex;flex-direction:column;justify-content:center">
<div class="tag">моя история</div>
<h1 style="font-size:70px;margin-top:20px">Я тоже долго не мог <span class="y">вырасти в доходе</span></h1>
<div class="p" style="font-size:46px">Пока не начал устранять свои слепые зоны.</div>
<div style="margin-top:50px;border-radius:30px;background:rgba(245,197,66,.1);border:3px solid {Y};padding:34px 40px">
<div style="font-weight:800;font-size:120px;line-height:1;color:{Y}">300 000</div>
<div style="font-weight:600;font-size:42px;line-height:1.3;margin-top:16px;color:#E6ECF5">подписчиков в Instagram за год <b style="font-weight:800;color:#fff">без вложений в рекламу</b></div></div></div>''')


def cta_opyt(i):
    return S(i, N, f'''<div class="txt" style="top:0;bottom:70px;display:flex;flex-direction:column;justify-content:center;text-align:center">
<div class="tag">бесплатно · 2 минуты</div>
<h1 style="font-size:66px;text-transform:none;margin-top:24px;line-height:1.15">Хотите разобраться, как применить <span class="it" style="font-size:80px">ваш опыт</span>, чтобы расти в доходе?</h1>
<div class="p" style="margin-top:40px">Это займёт всего 2 минуты.</div>
<div style="margin-top:50px;background:{Y};color:{NV};padding:36px 20px;border-radius:18px;box-shadow:0 0 60px rgba(245,197,66,.35)"><div style="font-weight:800;font-size:86px;line-height:1;white-space:nowrap">Пишите «ОПЫТ» &darr;</div><div style="font-weight:600;font-size:38px;margin-top:12px">в комментариях</div></div></div>''', last=True)
