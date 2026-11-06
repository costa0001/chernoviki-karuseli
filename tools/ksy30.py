# Движок каруселей в формате «текстовых» каруселей (обложка-фото + текстовые слайды + призыв).
# python3 tools/ksy30.py <from> <to>   (индексы в списке K из dannye_20/ksy30_data.py)
import os, sys, re, json
sys.path.insert(0, os.path.dirname(__file__)); sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'dannye_20'))
from gendesign import CSS, Y, NV, SKY, cta
from PIL import Image, ImageFilter
from playwright.sync_api import sync_playwright
from ksy30_data import K

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
FB = os.path.join(ROOT, 'foto-baza', '2026-10-zheneva')
CR = '#F4EFE4'; RD = '#FF6B6B'
CSS2 = CSS + f'''
.cream{{background:{CR}!important}} .cream .bg,.cream .grid{{display:none}}
.cream .top{{color:#7A6E58}} .cream h1{{color:{NV}}} .cream .p{{color:#23324F}} .cream .tag{{color:#A07A1F}}
.row{{font-weight:600;font-size:46px;line-height:1.28;padding:22px 0;border-bottom:2px solid rgba(255,255,255,.14)}}
.cream .row{{border-color:#D9CFBB;color:{NV}}}
.pr{{background:#FFFDF7;color:#1B2436;border-radius:26px;padding:34px 40px;font-family:"DejaVu Sans Mono",monospace;font-size:34px;line-height:1.38;box-shadow:0 24px 60px rgba(0,0,0,.35)}}
.huge{{font-weight:800;font-size:112px;line-height:1;text-transform:uppercase}}
.ni{{display:flex;gap:30px;align-items:flex-start;padding:26px 0;border-bottom:2px solid rgba(255,255,255,.14)}}
.cream .ni{{border-color:#D9CFBB}}
.nn{{flex:none;width:92px;height:92px;border-radius:50%;background:{Y};color:{NV};font-weight:800;font-size:52px;display:flex;align-items:center;justify-content:center}}
.nt{{font-weight:800;font-size:50px;line-height:1.15}} .cream .nt{{color:{NV}}}
.nd{{font-weight:600;font-size:40px;line-height:1.3;color:#C9D3E3;margin-top:10px}} .cream .nd{{color:#4A5875}}
'''

def S(i, N, inner, cls='', last=False):
    return (f'<div class="s {cls}"><div class="bg"></div><div class="grid"></div>'
            f'<div class="top"><span>@bravo.konstantin</span><span>{i} / {N}{"" if last else " &rarr;"}</span></div>{inner}</div>')

def box(html):
    return f'<div class="txt" style="top:120px;bottom:70px;display:flex;flex-direction:column;justify-content:center">{html}</div>'

def tagh(s, size=82):
    t = f'<div class="tag">{s["tag"]}</div>' if s.get('tag') else ''
    return t + f'<h1 style="font-size:{size}px">{s["h"]}</h1>'

def render_slide(i, N, s):
    k = s['t']; cr = s.get('bg') == 'c'; hc = NV if cr else '#fff'
    if k == 'rows':
        rows = ''.join(f'<div class="row">{r}</div>' for r in s['rows'])
        h = (tagh(s) + (f'<div class="p">{s["p"]}</div>' if s.get('p') else '') + f'<div style="margin-top:26px">{rows}</div>'
             + (f'<div class="p" style="margin-top:28px">{s["p2"]}</div>' if s.get('p2') else '')
             + (f'<div style="font-weight:800;font-size:64px;color:{RD if cr else Y};margin-top:40px;text-transform:uppercase;line-height:1.05">{s["acc"]}</div>' if s.get('acc') else ''))
    elif k == 'big':
        h = (tagh(s) + (f'<div class="p">{s["p"]}</div>' if s.get('p') else '')
             + f'<div class="huge" style="color:{NV if cr else Y};margin-top:50px">{s["huge"]}</div>'
             + (f'<div class="p" style="margin-top:40px">{s["p2"]}</div>' if s.get('p2') else ''))
    elif k == 'prompt':
        h = (tagh(s, 66) + f'<div style="font-weight:800;font-size:32px;letter-spacing:4px;margin:30px 0 16px;color:{SKY}">СКОПИРУЙТЕ И ВСТАВЬТЕ ↓</div>'
             + f'<div class="pr">{s["pr"]}</div>' + (f'<div class="p" style="font-size:40px;margin-top:28px">{s["note"]}</div>' if s.get('note') else ''))
    elif k == 'flow':
        st = s['steps']; fs = 52 if len(st) <= 4 else 44
        fl = ''.join(f'<div style="font-weight:800;font-size:{fs}px;color:{NV};text-align:center;background:{Y if j == 0 else "#fff"};border:3px solid {NV};border-radius:22px;padding:22px 20px;line-height:1.15">{x}</div>'
                     + ('' if j == len(st) - 1 else f'<div style="text-align:center;font-size:54px;line-height:1.05;color:{NV if cr else Y}">↓</div>') for j, x in enumerate(st))
        h = (tagh(s) + (f'<div class="p">{s["p"]}</div>' if s.get('p') else '') + f'<div style="margin-top:40px">{fl}</div>'
             + (f'<div class="p" style="margin-top:34px">{s["p2"]}</div>' if s.get('p2') else ''))
    elif k == 'vs':
        a, b = s['a'], s['b']
        card = lambda t, x, c: f'<div style="flex:1;border:4px solid {c};border-radius:28px;padding:34px;background:{"#fff" if cr else "rgba(255,255,255,.05)"}"><div style="font-weight:800;font-size:36px;color:{c};letter-spacing:3px">{t}</div><div style="font-weight:700;font-size:46px;line-height:1.25;margin-top:18px;color:{hc}">{x}</div></div>'
        h = tagh(s) + f'<div style="display:flex;flex-direction:column;gap:28px;margin-top:50px">{card(a[0], a[1], RD)}{card(b[0], b[1], "#2E9E5B" if cr else Y)}</div>'
    elif k == 'num':
        it = ''.join(f'<div class="ni"><div class="nn">{j + 1}</div><div><div class="nt">{t}</div><div class="nd">{d}</div></div></div>' for j, (t, d) in enumerate(s['items']))
        h = tagh(s) + f'<div style="margin-top:30px">{it}</div>'
    return S(i, N, box(h), 'cream' if cr else '')

CTA = {
 'УРОК': dict(tag='бесплатно', title='Бесплатный урок', product='«Моя система с ИИ»', line='Как работает моя система с ИИ-сотрудниками для роста дохода.', days_tiles=False),
 'ЦЕЛИ': dict(tag='бесплатно · 5 дней', title='Практикум', product='«Воплощение целей»', line='Поставьте цель и сделайте первые шаги за 5 дней.', days_tiles=True),
 'ЗАПРОС': dict(tag='бесплатно', title='Текст-запрос', product='«Упаковка опыта»', line='Поможет упаковать ваш опыт в понятный цифровой продукт.', days_tiles=False),
}

def cover(N, c, ph):
    return S(1, N, f'''<img src="file://{ph}" style="position:absolute;inset:0;width:1080px;height:1350px;object-fit:cover">
<div style="position:absolute;left:0;right:0;bottom:0;height:860px;background:linear-gradient(180deg,rgba(10,23,48,0),rgba(10,23,48,.9) 45%,#0A1730)"></div>
<div class="txt" style="bottom:90px">
<div style="font-weight:800;font-size:44px;line-height:1.2;text-transform:uppercase">{c['kick']}</div>
<div class="huge" style="margin-top:24px;font-size:{c.get('fs', 112)}px">{c['title']} <span style="color:{Y}">{c['acc']}</span></div>
<div class="p" style="margin-top:32px;font-size:44px">{c['sub']}</div></div>''')

# Положение лица на фото: (центр x, центр y, ширина лица) в долях кадра. Для обложек, где лицо уходило под текст.
FACE = {'g45_terrasa-fontan_ruki-skreshcheny_uverennyy.jpg': (.55, .40, .25), 'g71_sad-dom_ruka-u-podborodka_dumaet.jpg': (.53, .35, .22),
 'g43_fontan_portret_spokoynyy.jpg': (.54, .44, .26), 'g42_fontan_popravlyaet-ochki_ulybka.jpg': (.50, .42, .25),
 'g29_naberezhnaya-zdaniya_ruki-skreshcheny_shirokaya-ulybka.jpg': (.55, .43, .18), 'g46_terrasa-fontan_ruki-skreshcheny_vzglyad-vverh.jpg': (.55, .45, .22),
 'g37_fontan_ladoni-vmeste_krupno.jpg': (.50, .43, .20), 'g05_most-flag_vzglyad-vdal_ruki-skreshcheny.jpg': (.72, .36, .18),
 'g30_naberezhnaya-zdaniya_ruki-skreshcheny_legkaya-ulybka.jpg': (.53, .40, .20), 'g13_fontan_krupnyy-plan_ulybka.jpg': (.48, .44, .28),
 'g16_naberezhnaya_ruka-na-perilah_ulybka.jpg': (.66, .37, .13), 'g20_most-flag-sprava_shirokaya-ulybka.jpg': (.42, .37, .13),
 'g24_most-flag_ruki-szhaty_ulybka.jpg': (.63, .42, .13)}

def face_crop(path, fy=400, fw=270):
    im = Image.open(path).convert('RGB'); W0, H0 = im.size
    fc = FACE.get(os.path.basename(path))
    if not fc:
        sc = max(1080 / W0, 1350 / H0); x0 = (W0 * sc - 1080) / 2; y0 = (H0 * sc - 1350) * .18
    else:
        sc = max(fw / (fc[2] * W0), 1080 / W0, 1350 / H0)
        x0 = min(max(fc[0] * W0 * sc - 540, 0), W0 * sc - 1080); y0 = min(max(fc[1] * H0 * sc - fy, 0), H0 * sc - 1350)
    im = im.resize((int(W0 * sc) + 1, int(H0 * sc) + 1), Image.LANCZOS).crop((int(x0), int(y0), int(x0) + 1080, int(y0) + 1350))
    return im.filter(ImageFilter.UnsharpMask(1.5, 80, 2))

FIT = '''()=>{const t=document.querySelector('.txt');if(!t)return 0;let g=0;
while(t.scrollHeight>t.clientHeight+2&&g<40){g++;t.style.zoom=(parseFloat(t.style.zoom||1)*0.97)}return g}'''
HFIX = '''()=>{let g=0;document.querySelectorAll('.huge,[style*="nowrap"]').forEach(e=>{let n=0;
const box=e.parentElement;while((e.scrollWidth>box.clientWidth+2||e.getBoundingClientRect().right>1040)&&n<40){n++;g++;
e.style.fontSize=(parseFloat(getComputedStyle(e).fontSize)*0.95)+'px'}});return g}'''

def build(c, out):
    os.makedirs(out, exist_ok=True)
    N = len(c['sl']) + 2
    ph = f'{out}/_cover.jpg'
    face_crop(f'{FB}/{c["photo"]}').save(ph, quality=95)
    sl = {1: cover(N, c, ph)}
    for j, s in enumerate(c['sl']):
        sl[j + 2] = render_slide(j + 2, N, s)
    p = CTA[c['word']]
    sl[N] = cta(N, N, p['line'], word=c['word'], tag=p['tag'], title=p['title'], product=p['product'], days_tiles=p['days_tiles'])
    fits = {}
    with sync_playwright() as pw:
        b = pw.chromium.launch(); pg = b.new_page(viewport={'width': 1080, 'height': 1350})
        for k in sorted(sl):
            open(f'{out}/_t.html', 'w').write(f'<html><head><meta charset="utf-8"><style>{CSS2}</style></head><body>{sl[k]}</body></html>')
            pg.goto(f'file://{out}/_t.html'); pg.wait_for_timeout(250)
            h = pg.evaluate(HFIX)
            if k < N: fits[k] = pg.evaluate(FIT)
            if h: fits[f'h{k}'] = h
            pg.screenshot(path=f'{out}/slide_{k:02d}.png')
        b.close()
    for k in sorted(sl):
        Image.open(f'{out}/slide_{k:02d}.png').convert('RGB').save(f'{out}/slide_{k:02d}.jpg', quality=93)
        os.remove(f'{out}/slide_{k:02d}.png')
    os.remove(f'{out}/_t.html'); os.remove(ph)
    return {k: v for k, v in fits.items() if v}

# ---------- подписи ----------
START = {
 'УРОК': 'Пишите «УРОК» в комментариях, и я пришлю бесплатный урок о том, как работает моя система с ИИ.',
 'ЦЕЛИ': 'Пишите «ЦЕЛИ» в комментариях, и я пришлю ссылку на бесплатный практикум «Воплощение целей». 5 дней, без сложных заданий.',
 'ЗАПРОС': 'Пишите «ЗАПРОС» в комментариях, и я пришлю бесплатный текст-запрос, который поможет упаковать ваш опыт в цифровой продукт.',
}
MID = {
 'УРОК': 'Хотите увидеть, как это работает у меня вместе с командой ИИ-сотрудников? Пишите «УРОК».',
 'ЦЕЛИ': 'Хотите поставить цель и сделать к ней первые шаги? Пишите «ЦЕЛИ».',
 'ЗАПРОС': 'Хотите превратить свой опыт в понятный продукт? Пишите «ЗАПРОС».',
}
FREE = {
 'УРОК': 'Урок бесплатный. Он подходит, даже если вы только начинаете и раньше не работали с ИИ.',
 'ЦЕЛИ': 'Практикум бесплатный и проходит онлайн. Он подходит, даже если вы давно ничего не планировали для себя и думаете, что уже поздно. Поздно бывает только тогда, когда вы так и не начали.',
 'ЗАПРОС': 'Текст-запрос бесплатный. Вы вставляете его в ИИ, отвечаете на вопросы и получаете основу своего продукта.',
}
B2 = 'Вернитесь к этой карусели через неделю и честно проверьте, что изменилось за это время.'
B3 = 'Ваши вопросы в комментариях помогают мне выбирать темы для следующих каруселей, так что пишите смело.'
FACT = ['Я начал онлайн с нуля в 52 года, и за год без рекламы и коллабораций у меня появилось более 300 000 подписчиков.',
        'Сегодня ИИ мой главный тренд: со мной работает команда ИИ-сотрудников.',
        'За 28 лет в бизнесе я 5 раз уходил в новое направление раньше других.']
ASK = ['Что из этого вы попробуете первым? Напишите в комментариях.', 'Какой пункт для вас самый трудный? Напишите номер в комментариях.',
       'Как вы делаете это сейчас? Поделитесь в комментариях.']

def clean(x):
    x = re.sub(r'<[^>]+>', '', x).replace('&rarr;', '').replace('&nbsp;', ' ')
    x = re.sub(r'«(УРОК|ЦЕЛИ|ЗАПРОС)»', '', x)
    return re.sub(r'\s+', ' ', x).strip()

def endp(x):
    x = clean(x)
    return x if not x or x[-1] in '.?!…»' else x + '.'

def jn(d):
    d = endp(d)
    if re.match(r'(и|а|но|или|что|в|на|по|за|от|до|к|с|о|для|сколько|какая|какой|как|кто|где|когда|если|чтобы|«)\b', d) or d.startswith('«'):
        return ': ' + d if not re.match(r'(и|а|но)\s', d) else ' ' + d
    return ': ' + d[0].lower() + d[1:]

PAD5 = 'Не откладывайте на потом: выберите один пункт из карусели и сделайте его сегодня. Маленький шаг сегодня полезнее большого плана на когда-нибудь.'
PAD4 = 'Если карусель была полезной, отправьте её тому, кому она сейчас пригодится.'

def caption(c):
    w = c['word']; i = c['i']
    hook = endp(c['kick']) + ' ' + endp(c['title'] + ' ' + c['acc'])
    body = []
    for s in c['sl']:
        k = s['t']; h = endp(s['h'])
        if k == 'rows':
            rs = [clean(r).rstrip(';.') for r in s['rows']]
            pre = (' ' + endp(s['p'])) if s.get('p') else ''
            if any(r[:1].islower() for r in rs):
                body.append(clean(s['h']).rstrip('.?:') + pre.rstrip('.:') + ': ' + ', '.join(rs) + '.' + (' ' + endp(s['acc']) if s.get('acc') else ''))
            else:
                body.append(h + pre + ' ' + ' '.join(endp(r) for r in rs) + (' ' + endp(s['acc']) if s.get('acc') else ''))
        elif k == 'big': body.append(h + ' ' + endp(s.get('p', '')) + ' ' + endp(s['huge']))
        elif k == 'num': body.append(h + '\n' + '\n'.join(f'{j + 1}. {clean(t)}{jn(d)}' for j, (t, d) in enumerate(s['items'])))
        elif k == 'flow': body.append(h + ' ' + ' → '.join(clean(x) for x in s['steps']) + '.')
        elif k == 'vs': body.append(h + f' {clean(s["a"][0]).capitalize()}{jn(s["a"][1])} {clean(s["b"][0]).capitalize()}{jn(s["b"][1])}')
        elif k == 'prompt': body.append(f'{h} Промпт со слайда {c["sl"].index(s) + 2}, скопируйте:\n{clean(s["pr"])}')
    body = [re.sub(r' +', ' ', b).strip() for b in body if clean(b)]
    while True:
        parts = [START[w], hook] + body + [MID[w], (FACT[0], FACT[2])[i % 2] if w == 'УРОК' else FACT[i % 3], ASK[i % 3]]
        txt = '\n\n'.join(parts)
        if len(txt) < 1800 or len(body) <= 2: break
        body.pop(-2)
    for blk in (FREE[w], B2, B3, PAD4, PAD5):
        if len(txt) >= 1330: break
        parts.append(blk); txt = '\n\n'.join(parts)
    txt += f'\n\nСохраните карусель и пишите «{w}» в комментариях.'
    return txt

if __name__ == '__main__':
    a, b = int(sys.argv[1]), int(sys.argv[2])
    for c in K[a:b]:
        out = os.path.join(ROOT, c['folder'])
        c['caption'] = caption(c); f = build(c, out)
        open(f'{out}/podpis.txt', 'w').write(c['caption'])
        print(c['n'], c['folder'], f, flush=True)
