import os, sys
sys.path.insert(0, '/home/claude/chernoviki-karuseli/tools')
os.chdir('/home/claude/chernoviki-karuseli')
from gendesign import *
N = 13
R = '#FF6B6B'
GR = '#9AA6B8'


def zone(i, k, title, text, ill, top=700):
    badge = f'<div style="display:inline-block;border:3px solid {Y};color:{Y};border-radius:40px;padding:6px 26px;font-weight:800;font-size:30px;letter-spacing:3px">СЛЕПАЯ ЗОНА {k} / 5</div>'
    return S(i, N, f'''{ill}<div class="txt" style="top:{top}px">{badge}<h1 style="margin-top:26px">{title}</h1>
<div class="p">{text}</div></div>''')


def why(i, k, title, text, ill, top=700):
    badge = f'<div style="display:inline-block;background:{R};color:#fff;border-radius:40px;padding:8px 26px;font-weight:800;font-size:30px;letter-spacing:3px">ПОЧЕМУ НЕ РАБОТАЕТ</div>'
    return S(i, N, f'''{ill}<div class="txt" style="top:{top}px">{badge}<h1 style="margin-top:26px">{title}</h1>
<div class="p">{text}</div></div>''')


def card(t, extra=''):
    return f'<div style="background:#F6F1E6;color:{NV};border-radius:18px;padding:22px 30px;font-weight:700;font-size:34px;line-height:1.3;box-shadow:0 14px 40px rgba(0,0,0,.35);{extra}">{t}</div>'


def bubble(t, me=False, extra=''):
    if me:
        return f'<div style="display:flex;justify-content:flex-end;margin-top:20px"><div style="background:{SKY};color:{NV};font-weight:700;font-size:34px;padding:18px 28px;border-radius:28px 28px 6px 28px;{extra}">{t}</div></div>'
    return f'<div style="display:flex;margin-top:20px"><div style="background:#1E2C48;font-weight:600;font-size:34px;padding:18px 28px;border-radius:28px 28px 28px 6px;{extra}">{t}</div></div>'


sl = {}
sl[1] = cover(SH + 'cover_sz.jpg', 'center 22%',
              f'<div class="tag" style="font-size:32px;margin-bottom:6px">Первая серия · 5 слепых зон</div>Почему у вас не получается<br><span class="y" style="white-space:nowrap">расти в доходе?</span>',
              'Листайте и отметьте, что из этого про вас', N)

# --- Зона 1: коллекционирование знаний
items = ''.join(f'<div style="display:flex;align-items:center;gap:20px;background:rgba(255,255,255,.06);border:2px solid #3A4E73;border-radius:20px;padding:18px 24px;margin-top:16px;opacity:{o}"><div style="font-size:44px">{e}</div><div style="font-weight:700;font-size:34px">{t}</div></div>'
                for e, t, o in [('🎓', 'Курс №7: «Доход онлайн»', 1), ('📺', 'Эфир: «10 идей заработка»', .85), ('📌', 'Сохранено: 347 постов', .7), ('📚', 'Ещё один марафон', .5)])
ill1 = f'<div style="position:absolute;top:130px;left:150px;right:150px">{items}</div>'
sl[2] = zone(2, 1, 'Вы собираете знания',
             'Ещё один курс, ещё один эфир, ещё сотня сохранённых постов. Кажется, что <span class="y">не хватает информации.</span>', ill1, top=680)

ill1w = f'''<svg width="1080" height="540" style="position:absolute;top:120px;left:0">
<line x1="140" y1="460" x2="960" y2="460" stroke="#3A4E73" stroke-width="4"/>
<path d="M140,440 C350,400 550,250 940,80" fill="none" stroke="{SKY}" stroke-width="10" stroke-linecap="round"/>
<text x="940" y="60" text-anchor="end" font-family="S" font-weight="800" font-size="40" fill="{SKY}">ЗНАНИЯ</text>
<path d="M140,420 L940,420" fill="none" stroke="{R}" stroke-width="10" stroke-linecap="round" stroke-dasharray="2 22"/>
<text x="940" y="400" text-anchor="end" font-family="S" font-weight="800" font-size="40" fill="{R}">ДОХОД</text></svg>'''
sl[3] = why(3, 1, 'Знания не платят',
            'Каждый курс даёт ощущение движения. Но <span class="y">деньги приносит только действие.</span> Сохранёнки растут, а доход стоит на месте.', ill1w, top=680)

# --- Зона 2: нет цели в цифрах
q = ''.join(card(f'«{t}»', f'transform:rotate({r}deg);margin-top:26px;{s}') for t, r, s in
            [('Хочу зарабатывать больше', -2, 'margin-right:120px'), ('Хочу свободы', 2, 'margin-left:260px'), ('Хочу стабильности', -1, 'margin-right:60px;margin-left:80px')])
ill2 = f'<div style="position:absolute;top:150px;left:100px;right:100px">{q}</div>'
sl[4] = zone(4, 2, 'У вас нет цели в цифрах',
             'Звучит как цель. Но <span class="y">это только желание.</span> В нём нет ни суммы, ни срока.', ill2, top=700)

arrows = ''.join(f'<g transform="translate(540,300) rotate({a})"><line x1="60" y1="0" x2="{l}" y2="0" stroke="{c}" stroke-width="8" stroke-linecap="round"/><path d="M{l},-16 L{l+26},0 L{l},16 Z" fill="{c}"/></g>'
                 for a, l, c in [(0, 220, SKY), (50, 160, GR), (110, 200, SKY), (165, 230, GR), (215, 170, SKY), (270, 150, GR), (320, 210, SKY)])
ill2w = f'''<svg width="1080" height="600" style="position:absolute;top:100px;left:0">{arrows}
<circle cx="540" cy="300" r="56" fill="{NV}" stroke="{R}" stroke-width="6"/><text x="540" y="322" text-anchor="middle" font-family="S" font-weight="800" font-size="64" fill="{R}">?</text></svg>'''
sl[5] = why(5, 2, 'Вам некуда идти',
            'Без суммы и срока нет плана. Вы беретесь за всё сразу, и <span class="y">ничего не доходит до денег.</span>', ill2w, top=700)

# --- Зона 3: прыжки между идеями
chips = [('Маркетплейсы', 110, 170), ('Крипта', 600, 130), ('ИИ', 760, 330), ('Коучинг', 170, 420), ('Свой курс', 520, 520)]
ch = ''.join(f'<div style="position:absolute;left:{x}px;top:{y}px;background:rgba(255,255,255,.07);border:3px solid {SKY};border-radius:50px;padding:16px 34px;font-weight:800;font-size:38px">{t}</div>' for t, x, y in chips)
ill3 = f'''<svg width="1080" height="640" style="position:absolute;top:0;left:0">
<path d="M330,230 C450,80 560,90 640,170 M760,200 C900,230 900,300 850,330 M760,390 C600,420 450,420 390,450 M330,500 C380,600 470,600 520,570" fill="none" stroke="{Y}" stroke-width="5" stroke-dasharray="14 12"/></svg>{ch}'''
sl[6] = zone(6, 3, 'Вы прыгаете между идеями',
             'Маркетплейсы, крипта, ИИ, коучинг. <span class="y">Каждый месяц новая ниша.</span>', ill3, top=720)

runs = ''.join(f'<line x1="140" y1="{y}" x2="{x}" y2="{y}" stroke="{SKY}" stroke-width="12" stroke-linecap="round" opacity="{o}"/><circle cx="{x}" cy="{y}" r="16" fill="{R}"/>' for y, x, o in [(150, 640, 1), (260, 560, .85), (370, 700, .7), (480, 610, .55)])
ill3w = f'''<svg width="1080" height="600" style="position:absolute;top:100px;left:0">{runs}
<line x1="830" y1="90" x2="830" y2="540" stroke="{Y}" stroke-width="6" stroke-dasharray="18 12"/>
<circle cx="930" cy="315" r="72" fill="{Y}"/><text x="930" y="342" text-anchor="middle" font-family="S" font-weight="800" font-size="80" fill="{NV}">€</text></svg>'''
sl[7] = why(7, 3, 'Вы уходите за шаг до денег',
            'Первые 2–3 месяца всегда идут без результата. Именно тогда вы бросаете, и <span class="y">всё начинается с нуля.</span>', ill3w, top=700)

# --- Зона 4: «начинаю с нуля»
ill4 = f'''<div style="position:absolute;top:150px;left:0;right:0;display:flex;justify-content:center;gap:60px;align-items:center">
<div style="width:380px;height:420px;border-radius:36px;background:rgba(255,255,255,.06);border:3px solid {Y};display:flex;flex-direction:column;align-items:center;justify-content:center">
<div style="font-size:120px">💼</div><div style="font-weight:800;font-size:44px;color:{Y};margin-top:10px">25 ЛЕТ</div><div style="font-weight:600;font-size:34px;color:#E6ECF5">опыта</div></div>
<div style="font-weight:800;font-size:90px;color:{GR}">→</div>
<div style="width:300px;height:420px;border-radius:36px;background:rgba(255,255,255,.03);border:3px dashed {GR};display:flex;align-items:center;justify-content:center"><div style="font-weight:800;font-size:220px;color:{GR}">0</div></div></div>'''
sl[8] = zone(8, 4, 'Вы «начинаете с нуля»',
             'Кажется, что 20–30 лет опыта на родине здесь <span class="y">ничего не стоят.</span> И вы идёте учиться новой профессии.', ill4, top=680)

ill4w = f'''<div style="position:absolute;top:140px;left:110px;right:110px;display:flex;gap:40px">
<div style="flex:1;border-radius:30px;background:rgba(255,255,255,.05);border:3px solid {GR};padding:36px;height:380px">
<div style="font-weight:800;font-size:38px;color:{GR}">ИХ ПОЛЕ</div><div style="font-weight:800;font-size:96px;margin-top:20px">25 лет</div><div style="font-weight:600;font-size:34px;color:#E6ECF5;margin-top:16px">скорость, тренды, танцы в рилс</div></div>
<div style="flex:1;border-radius:30px;background:rgba(245,197,66,.1);border:3px solid {Y};padding:36px;height:380px">
<div style="font-weight:800;font-size:38px;color:{Y}">ВАШЕ ПОЛЕ</div><div style="font-weight:800;font-size:96px;margin-top:20px;color:{Y}">45+</div><div style="font-weight:600;font-size:34px;color:#E6ECF5;margin-top:16px">опыт, доверие, прожитая жизнь</div></div></div>'''
sl[9] = why(9, 4, 'Вы играете на чужом поле',
            'Соревнуетесь с 25-летними и выбрасываете главный актив. А ведь <span class="y">ваш опыт это преимущество, а не помеха.</span>', ill4w, top=640)

# --- Зона 5: процесс вместо результата
ill5 = f'''<div style="position:absolute;top:140px;left:120px;right:120px">
<div style="font-weight:800;font-size:30px;letter-spacing:4px;color:{GR};margin-bottom:6px">КАК ВЫ О СЕБЕ ГОВОРИТЕ</div>
{bubble("«Провожу консультации»")}{bubble("«Делаю сессии»")}{bubble("«Обучаю и сопровождаю»")}</div>'''
sl[10] = zone(10, 5, 'Вы продаёте процесс',
              'Вы рассказываете, что делаете вы. А человек хочет знать, <span class="y">что получит он.</span>', ill5, top=680)

ill5w = f'''<div style="position:absolute;top:190px;left:120px;right:120px">
{bubble("Сколько стоит?", me=True)}{bubble("150 € за консультацию")}{bubble("Я подумаю...", me=True)}
<div style="text-align:right;font-weight:600;font-size:28px;color:{GR};margin-top:14px">прочитано · ответа нет</div></div>'''
sl[11] = why(11, 5, 'Клиент покупает результат',
             'Непонятно, что он получит. Поэтому любая цена кажется дорогой, и <span class="y">человек уходит «подумать».</span>', ill5w, top=680)

# --- Личный слайд
sl[12] = S(12, N, f'''<div class="txt" style="top:0;bottom:80px;display:flex;flex-direction:column;justify-content:center">
<div class="tag">моя история</div>
<h1 style="font-size:70px;margin-top:20px">Я тоже долго не мог <span class="y">вырасти в доходе</span></h1>
<div class="p" style="font-size:46px">Пока не начал устранять свои слепые зоны.</div>
<div style="margin-top:50px;border-radius:30px;background:rgba(245,197,66,.1);border:3px solid {Y};padding:34px 40px">
<div style="font-weight:800;font-size:120px;line-height:1;color:{Y}">300 000</div>
<div style="font-weight:600;font-size:42px;line-height:1.3;margin-top:16px;color:#E6ECF5">подписчиков в Instagram за год <b style="font-weight:800;color:#fff">без вложений в рекламу</b></div></div></div>''')

# --- CTA
sl[13] = S(13, N, f'''<div class="txt" style="top:0;bottom:70px;display:flex;flex-direction:column;justify-content:center;text-align:center">
<div class="tag">бесплатно · 2 минуты</div>
<h1 style="font-size:66px;text-transform:none;margin-top:24px;line-height:1.15">Хотите разобраться, как применить <span class="it" style="font-size:80px">ваш опыт</span>, чтобы расти в доходе?</h1>
<div class="p" style="margin-top:40px">Это займёт всего 2 минуты.</div>
<div style="margin-top:50px;background:{Y};color:{NV};padding:36px 20px;border-radius:18px;box-shadow:0 0 60px rgba(245,197,66,.35)"><div style="font-weight:800;font-size:86px;line-height:1;white-space:nowrap">Пишите «ОПЫТ» &darr;</div><div style="font-weight:600;font-size:38px;margin-top:12px">в комментариях</div></div></div>''', last=True)

render(sl, os.path.abspath('out_sz')); print('ok')
