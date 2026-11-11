import sys
sys.path.insert(0, '/home/claude/work')
from szlib import *

sl = {}
sl[1] = cover_full(SH + 'cover_sz3.jpg', 'center 90%', 'Третья серия · слепые зоны 11–15',
                   'Работаете<br>больше всех,<br><span class="y" style="white-space:nowrap">а доход тот же?</span>',
                   '5 ошибок, которые съедают ваше время')

# 11 — в одиночку
roles = ''.join(f'<div style="display:flex;align-items:center;gap:22px;margin-top:16px"><div style="width:70px;height:70px;border-radius:50%;background:{SKY};color:{NV};display:flex;align-items:center;justify-content:center;font-weight:800;font-size:28px">ВЫ</div><div style="font-weight:800;font-size:40px">{t}</div></div>' for t in ['Эксперт', 'Маркетолог', 'Продавец', 'Дизайнер', 'Судья самому себе'])
ill = f'<div style="position:absolute;top:130px;left:220px;right:100px">{roles}</div>'
sl[2] = zone(2, 11, 'Вы всё делаете в одиночку', 'Сам себе эксперт, маркетолог и судья. <span class="y">Спросить не у кого.</span>', ill, top=720)
ill = f'''<svg width="1080" height="600" style="position:absolute;top:110px;left:0">
<circle cx="540" cy="290" r="200" fill="none" stroke="{R}" stroke-width="10" stroke-dasharray="40 18"/>
<path d="M720,200 L760,250 L700,262 Z" fill="{R}"/>
<text x="540" y="270" text-anchor="middle" font-family="S" font-weight="800" font-size="46" fill="#fff">та же ошибка</text>
<text x="540" y="340" text-anchor="middle" font-family="S" font-weight="800" font-size="56" fill="{R}">× 6 месяцев</text></svg>'''
sl[3] = why(3, 'Свою ошибку изнутри не видно', 'Слепая зона так и называется: её не видит сам человек. <span class="y">Ошибки повторяются месяцами,</span> а мотивация гаснет.', ill, top=720)

# 12 — продаёт часы
hrs = ''.join(f'<div style="display:flex;align-items:center;gap:20px;margin-top:12px"><div style="width:120px;font-weight:800;font-size:32px;color:{GR}">{h}:00</div><div style="flex:1;border-radius:14px;background:{SKY if h!=13 else "#3A4E73"};color:{NV};font-weight:800;font-size:30px;padding:12px 20px">{"клиент · 1 час = 1 оплата" if h!=13 else "обед"}</div></div>' for h in range(9, 16))
ill = f'<div style="position:absolute;top:120px;left:110px;right:110px">{hrs}</div>'
sl[4] = zone(4, 12, 'Вы продаёте свои часы', 'Консультации, уроки, сессии один на один. <span class="y">Каждый евро стоит вам часа жизни.</span>', ill, top=720)
bars = ''.join(f'<rect x="{150+j*170}" y="{470-h}" width="110" height="{h}" rx="14" fill="{c}"/>' for j, (h, c) in enumerate([(150, '#2C4A7A'), (260, '#3E67A8'), (330, SKY), (330, SKY), (330, R)]))
ill = f'''<svg width="1080" height="560" style="position:absolute;top:120px;left:0">{bars}
<line x1="110" y1="130" x2="970" y2="130" stroke="{Y}" stroke-width="6" stroke-dasharray="20 12"/>
<text x="970" y="105" text-anchor="end" font-family="S" font-weight="800" font-size="38" fill="{Y}">ПОТОЛОК: 24 ЧАСА</text></svg>'''
sl[5] = why(5, 'У дня есть потолок', 'В сутках 24 часа. Больше клиентов значит больше усталости, а <span class="y">не больше свободы.</span>', ill, top=720)

# 13 — остаточный принцип
rows = [('Работа', '9 ч', SKY), ('Дорога', '1,5 ч', '#3E67A8'), ('Семья и быт', '4 ч', '#3E67A8'), ('Документы, магазины', '1 ч', '#2C4A7A'), ('Своё дело', '0 мин', R)]
r = ''.join(f'<div style="display:flex;justify-content:space-between;align-items:center;border-radius:18px;background:rgba(255,255,255,.05);border:2px solid {c};padding:16px 26px;margin-top:14px"><div style="font-weight:800;font-size:38px">{a}</div><div style="font-weight:800;font-size:40px;color:{c}">{b}</div></div>' for a, b, c in rows)
ill = f'<div style="position:absolute;top:120px;left:130px;right:130px">{r}</div>'
sl[6] = zone(6, 13, 'Своё дело у вас «по остатку»', 'Работа, семья, быт, бюрократия. А своё дело <span class="y">«когда останется время».</span>', ill, top=720)
days = ''.join(f'<div style="flex:1;border-radius:18px;background:rgba(255,255,255,.05);border:2px solid #3A4E73;height:330px;padding:14px 0;text-align:center"><div style="font-weight:800;font-size:30px;color:{GR}">{d}</div>' + ''.join(f'<div style="margin:10px 10px 0;height:44px;border-radius:10px;background:#2C4A7A"></div>' for _ in range(3)) + f'<div style="margin:10px 10px 0;height:56px;border-radius:10px;border:3px dashed {R};color:{R};font-weight:800;font-size:34px;line-height:52px">?</div></div>' for d in ['пн', 'вт', 'ср', 'чт', 'пт'])
ill = f'<div style="position:absolute;top:170px;left:90px;right:90px;display:flex;gap:16px">{days}</div>'
sl[7] = why(7, 'Время не остаётся никогда', 'Вечером на усталости ничего не строится. <span class="y">Чего нет в календаре, того не происходит.</span>', ill, top=700)

# 14 — ИИ стороной
ill = f'''<div style="position:absolute;top:150px;left:90px;right:90px;text-align:center">{chip("ChatGPT?")}{chip("Claude?")}{chip("Боты?", GR)}{chip("Агенты?")}{chip("Промпты?", GR)}{chip("Автоматизация?")}{chip("Это для молодых?", R)}</div>'''
sl[8] = zone(8, 14, 'Вы обходите ИИ стороной', '«Я не технарь», «это не для моего возраста». <span class="y">А другие уже работают быстрее.</span>', ill, top=720)
ill = two('РАНЬШЕ', '10 часов', 'в день на контент', 'СЕЙЧАС', '≈ 1 час', 'с командой ИИ-сотрудников', top=160)
sl[9] = why(9, 'Вы тратите часы там, где хватит минут', 'Тексты, идеи, ответы клиентам ИИ делает быстро. Я раньше тратил на контент 10 часов в день, <span class="y">сейчас около часа.</span>', ill, top=640)

# 15 — не тот рынок
ill = two('МЕСТНЫЙ РЫНОК', 'язык', 'дипломы, связи, конкуренция с местными', 'РУБЛИ', 'курс', 'платежи, блокировки, нестабильность', top=150, rc=R)
sl[10] = zone(10, 15, 'Вы ищете клиентов не там', 'Пробиваетесь на местный рынок без языка или держитесь за рубли. <span class="y">И упираетесь в потолок.</span>', ill, top=660)
cs = [('Германия', 120, 120), ('Польша', 640, 90), ('Испания', 80, 330), ('Израиль', 700, 300), ('США', 230, 500), ('Канада', 620, 510), ('Чехия', 410, 40)]
c = ''.join(f'<div style="position:absolute;left:{x}px;top:{y}px">{chip(t)}</div>' for t, x, y in cs)
ill = f'''<div style="position:absolute;top:110px;left:0;right:0;height:640px">{c}
<div style="position:absolute;left:430px;top:250px;width:220px;height:220px;border-radius:50%;background:{Y};color:{NV};display:flex;align-items:center;justify-content:center;font-weight:800;font-size:130px;box-shadow:0 0 70px rgba(245,197,66,.4)">€</div></div>'''
sl[11] = why(11, 'Ваш рынок это весь мир', 'Русскоязычные живут в десятках стран и платят в евро. <span class="y">Онлайн переезжает вместе с вами.</span>', ill, top=780)

sl[12] = personal(12)
sl[13] = cta_opyt(13)
render(sl, os.path.abspath('out_sz3')); print('ok')
