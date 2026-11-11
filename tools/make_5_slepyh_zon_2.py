import os, sys
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


def bubble(t, me=False, extra=''):
    if me:
        return f'<div style="display:flex;justify-content:flex-end;margin-top:20px"><div style="background:{SKY};color:{NV};font-weight:700;font-size:34px;padding:18px 28px;border-radius:28px 28px 6px 28px;{extra}">{t}</div></div>'
    return f'<div style="display:flex;margin-top:20px"><div style="background:#1E2C48;font-weight:600;font-size:34px;padding:18px 28px;border-radius:28px 28px 28px 6px;{extra}">{t}</div></div>'


def stat(e, v, t, c='#fff'):
    return f'<div style="flex:1;border-radius:26px;background:rgba(255,255,255,.06);border:2px solid #3A4E73;padding:26px 10px;text-align:center"><div style="font-size:52px">{e}</div><div style="font-weight:800;font-size:58px;color:{c};margin-top:6px">{v}</div><div style="font-weight:600;font-size:30px;color:{GR}">{t}</div></div>'


sl = {}
sl[1] = cover(SH + 'cover_sz2b.jpg', 'center 18%',
              f'<div class="tag" style="font-size:32px;margin-bottom:6px">Вторая серия · слепые зоны 6–10</div>Курс готов,<br>блог ведёте,<br><span class="y" style="white-space:nowrap">а денег нет?</span>',
              '5 ошибок, которых вы не видите', N)

# --- Зона 6: продукт без покупателей
rows = ''.join(f'<div style="display:flex;align-items:center;gap:24px;border-bottom:2px solid #D9CFBB;padding:20px 0"><div style="width:54px;height:54px;border-radius:12px;background:{c};color:#fff;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:38px">{m}</div><div style="font-weight:700;font-size:40px;color:{NV}">{t}</div></div>'
               for t, m, c in [('Курс записан', '✓', '#3BA776'), ('Сайт готов', '✓', '#3BA776'), ('Логотип и визитки', '✓', '#3BA776'), ('Покупатели', '✗', R)])
ill6 = f'<div style="position:absolute;top:130px;left:170px;right:170px;background:#F6F1E6;border-radius:22px;padding:24px 44px;box-shadow:0 30px 70px rgba(0,0,0,.45);transform:rotate(-1.5deg)">{rows}</div>'
sl[2] = zone(2, 6, 'Вы делаете продукт без покупателей',
             'Месяцами пишете курс, делаете сайт и логотип. <span class="y">И только потом ищете, кому продать.</span>', ill6, top=700)

ill6w = f'''<div style="position:absolute;top:150px;left:140px;right:140px;border-radius:34px;background:rgba(255,255,255,.05);border:3px solid #3A4E73;padding:40px 50px">
<div style="font-weight:800;font-size:34px;letter-spacing:4px;color:{GR}">СТАРТ ПРОДАЖ · ДЕНЬ 7</div>
<div style="display:flex;justify-content:space-between;align-items:baseline;margin-top:30px"><div style="font-weight:600;font-size:40px">Заказы</div><div style="font-weight:800;font-size:110px;color:{R}">0</div></div>
<div style="display:flex;justify-content:space-between;align-items:baseline;border-top:2px solid #3A4E73;padding-top:16px"><div style="font-weight:600;font-size:40px">Потрачено</div><div style="font-weight:800;font-size:56px;color:#fff">6 месяцев</div></div></div>'''
sl[3] = why(3, 'На запуске тишина',
            'Спрос никто не проверил. Время и силы потрачены, а <span class="y">купить некому.</span>', ill6w, top=720)

# --- Зона 7: перфекционизм
files = ''.join(f'<div style="display:flex;align-items:center;gap:20px;margin-top:14px;opacity:{o}"><div style="font-size:40px">📄</div><div style="font-weight:700;font-size:34px">{t}</div></div>' for t, o in
                [('курс_финал.docx', .45), ('курс_финал_2.docx', .6), ('курс_точно_финал.docx', .8), ('курс_финал_НОВЫЙ.docx', 1)])
ill7 = f'''<div style="position:absolute;top:130px;left:150px;right:150px">{files}
<div style="margin-top:40px;height:44px;border-radius:22px;background:rgba(255,255,255,.08);overflow:hidden"><div style="width:97%;height:100%;background:{SKY}"></div></div>
<div style="font-weight:800;font-size:34px;color:{SKY};margin-top:14px">97% · ещё чуть-чуть доделаю...</div></div>'''
sl[4] = zone(4, 7, 'Вы ждёте, когда будет идеально',
             '«Ещё не готово». «Доделаю и тогда запущу». <span class="y">И так уже полгода.</span>', ill7, top=720)

ill7w = f'''<div style="position:absolute;top:140px;left:110px;right:110px;display:flex;gap:40px">
<div style="flex:1;border-radius:30px;background:rgba(255,255,255,.05);border:3px solid {GR};padding:34px;height:390px">
<div style="font-weight:800;font-size:34px;color:{GR}">ИДЕАЛЬНО</div><div style="font-weight:600;font-size:34px;color:#E6ECF5;margin-top:14px">но так и не вышло</div><div style="font-weight:800;font-size:110px;margin-top:40px;color:{R}">0 €</div></div>
<div style="flex:1;border-radius:30px;background:rgba(245,197,66,.1);border:3px solid {Y};padding:34px;height:390px">
<div style="font-weight:800;font-size:34px;color:{Y}">ДОСТАТОЧНО</div><div style="font-weight:600;font-size:34px;color:#E6ECF5;margin-top:14px">но уже работает</div><div style="font-weight:800;font-size:64px;margin-top:40px;color:{Y};line-height:1.1">первые клиенты</div></div></div>'''
sl[5] = why(5, 'Идеал не платит',
            'За «доделываю» прячется страх оценки и отказа. А <span class="y">деньги приходят только после запуска.</span>', ill7w, top=660)

# --- Зона 8: стыд продавать
q = ''.join(card(f'«{t}»', f'transform:rotate({r}deg);margin-top:26px;{s}') for t, r, s in
            [('Продавать неудобно', -2, 'margin-right:220px'), ('Большие деньги нечестные', 2, 'margin-left:120px'), ('Неловко называть цену', -1, 'margin-right:120px;margin-left:60px')])
ill8 = f'<div style="position:absolute;top:150px;left:100px;right:100px">{q}</div>'
sl[6] = zone(6, 8, 'Вам стыдно продавать',
             'Вы помогаете людям, но <span class="y">стесняетесь назвать цену.</span> Ждёте, что спросят сами.', ill8, top=700)

ill8w = f'<div style="position:absolute;top:170px;left:90px;right:90px;display:flex;gap:24px">{stat("❤️", "340", "лайков")}{stat("💬", "25", "спасибо")}{stat("💶", "0", "продаж", R)}</div>'
sl[7] = why(7, 'Люди не знают, что у вас купить',
            'Полезный контент есть, а предложения нет. Цена занижена, и <span class="y">даже продажи не дают дохода.</span>', ill8w, top=680)

# --- Зона 9: блог без воронки
ill9 = f'''<div style="position:absolute;top:120px;left:300px;width:480px;height:540px;border-radius:56px;border:6px solid #3A4E73;background:#0B1A36;padding:36px 34px;box-sizing:border-box">
<div style="height:200px;border-radius:24px;background:linear-gradient(135deg,#2C4A7A,#1E2C48)"></div>
<div style="display:flex;justify-content:space-between;margin-top:30px;font-weight:800;font-size:36px"><span>👁 12 400</span><span>❤️ 640</span></div>
<div style="margin-top:34px;border-radius:20px;border:3px dashed {R};padding:20px;text-align:center;font-weight:800;font-size:40px;color:{R}">Заявки: 0</div></div>'''
sl[8] = zone(8, 9, 'У вашего блога нет воронки',
             'Просмотры есть, лайки есть. <span class="y">А заявок нет.</span>', ill9, top=740)

def node(t, c):
    return f'<div style="border-radius:24px;border:3px solid {c};padding:24px 22px;font-weight:800;font-size:36px;text-align:center;background:rgba(255,255,255,.05)">{t}</div>'
ill9w = f'''<div style="position:absolute;top:220px;left:60px;right:60px;display:flex;align-items:center;justify-content:space-between">
{node("Подписчик", SKY)}<div style="flex:1;height:6px;background:{SKY};margin:0 10px"></div>
<div style="width:150px;height:150px;border-radius:50%;border:4px dashed {R};display:flex;align-items:center;justify-content:center;font-weight:800;font-size:80px;color:{R}">?</div>
<div style="flex:1;height:6px;background:repeating-linear-gradient(90deg,{GR} 0 14px,transparent 14px 26px);margin:0 10px"></div>{node("Оплата", Y)}</div>'''
sl[9] = why(9, 'Человек посмотрел и ушёл',
            'Нет пути от подписчика к оплате: ни призыва, ни бесплатного шага, ни переписки. <span class="y">Внимание уходит к другим.</span>', ill9w, top=640)

# --- Зона 10: ждёт большую аудиторию
ill10 = f'''<div style="position:absolute;top:170px;left:120px;right:120px">
<div style="font-weight:800;font-size:34px;letter-spacing:4px;color:{GR}">«НАЧНУ ПРОДАВАТЬ, КОГДА...»</div>
<div style="display:flex;justify-content:space-between;align-items:baseline;margin-top:30px"><div style="font-weight:800;font-size:96px">1 240</div><div style="font-weight:800;font-size:56px;color:{GR}">/ 10 000</div></div>
<div style="margin-top:20px;height:50px;border-radius:25px;background:rgba(255,255,255,.08);overflow:hidden"><div style="width:12%;height:100%;background:{SKY}"></div></div>
<div style="font-weight:600;font-size:36px;color:#E6ECF5;margin-top:24px">подписчиков · прошло 2 года</div></div>'''
sl[10] = zone(10, 10, 'Вы ждёте большую аудиторию',
              '«Сначала наберу 10 000 подписчиков, потом начну продавать». <span class="y">И годы уходят без денег.</span>', ill10, top=680)

import random
random.seed(7)
dots = ''
for r_, n_ in [(90, 8), (170, 14), (250, 20)]:
    import math
    for j in range(n_):
        a = 2 * math.pi * j / n_ + r_
        x = 540 + r_ * math.cos(a); y = 290 + r_ * math.sin(a)
        c = Y if random.random() < (.6 if r_ == 90 else .25 if r_ == 170 else .08) else '#3A4E73'
        dots += f'<circle cx="{x:.0f}" cy="{y:.0f}" r="22" fill="{c}"/>'
ill10w = f'''<svg width="1080" height="600" style="position:absolute;top:110px;left:0">{dots}
<circle cx="540" cy="290" r="44" fill="{NV}" stroke="{Y}" stroke-width="5"/><text x="540" y="304" text-anchor="middle" font-family="S" font-weight="800" font-size="38" fill="{Y}">ВЫ</text></svg>'''
sl[11] = why(11, 'Первые клиенты уже рядом',
             'Первые деньги приносят 100–500 тёплых людей, которые вам доверяют. <span class="y">Не тысячи незнакомцев.</span>', ill10w, top=700)

sl[12] = S(12, N, f'''<div class="txt" style="top:0;bottom:80px;display:flex;flex-direction:column;justify-content:center">
<div class="tag">моя история</div>
<h1 style="font-size:70px;margin-top:20px">Я тоже долго не мог <span class="y">вырасти в доходе</span></h1>
<div class="p" style="font-size:46px">Пока не начал устранять свои слепые зоны.</div>
<div style="margin-top:50px;border-radius:30px;background:rgba(245,197,66,.1);border:3px solid {Y};padding:34px 40px">
<div style="font-weight:800;font-size:120px;line-height:1;color:{Y}">300 000</div>
<div style="font-weight:600;font-size:42px;line-height:1.3;margin-top:16px;color:#E6ECF5">подписчиков в Instagram за год <b style="font-weight:800;color:#fff">без вложений в рекламу</b></div></div></div>''')

sl[13] = S(13, N, f'''<div class="txt" style="top:0;bottom:70px;display:flex;flex-direction:column;justify-content:center;text-align:center">
<div class="tag">бесплатно · 2 минуты</div>
<h1 style="font-size:66px;text-transform:none;margin-top:24px;line-height:1.15">Хотите разобраться, как применить <span class="it" style="font-size:80px">ваш опыт</span>, чтобы расти в доходе?</h1>
<div class="p" style="margin-top:40px">Это займёт всего 2 минуты.</div>
<div style="margin-top:50px;background:{Y};color:{NV};padding:36px 20px;border-radius:18px;box-shadow:0 0 60px rgba(245,197,66,.35)"><div style="font-weight:800;font-size:86px;line-height:1;white-space:nowrap">Пишите «ОПЫТ» &darr;</div><div style="font-weight:600;font-size:38px;margin-top:12px">в комментариях</div></div></div>''', last=True)

render(sl, os.path.abspath('out_sz2')); print('ok')
