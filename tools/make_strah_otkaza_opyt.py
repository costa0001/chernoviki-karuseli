import sys
sys.path.insert(0, '/home/claude/work')
from szlib import *

n = 10; sl = {}
sl[1] = cover_full(SH + 'c_otkaz.jpg', 'center 85%', 'Честный разговор',
                   'Почему опытные<br>люди боятся<br><span class="y" style="white-space:nowrap">продавать?</span>',
                   'Прочитайте, если после «нет» хочется всё бросить').replace('1 / 13', '1 / 10')

ill = two('ВЫ ДУМАЕТЕ', 'прогрев', 'посты, сторис, объяснения', 'НА САМОМ ДЕЛЕ', 'риск', 'услышать «нет» от людей', top=150, lc=SKY, rc=R).replace('font-size:84px', 'font-size:70px')
sl[2] = txt(2, 'Почему мы не продаём', 'Сделать прогрев и не получить заявки <span class="y">= получить отказ.</span> А отказ это больно и страшно.', ill, top=660, n=n)

ill = f'''<div style="position:absolute;top:150px;left:110px;right:110px;border-radius:30px;background:rgba(255,255,255,.05);border:3px solid #3A4E73;padding:40px 46px">
<div style="font-weight:800;font-size:32px;letter-spacing:4px;color:{GR}">ИТОГ НЕДЕЛИ ПРОГРЕВА</div>
<div style="display:flex;justify-content:space-between;align-items:baseline;margin-top:24px"><div style="font-weight:600;font-size:40px">Публикаций</div><div style="font-weight:800;font-size:64px">14</div></div>
<div style="display:flex;justify-content:space-between;align-items:baseline;border-top:2px solid #3A4E73;padding-top:14px;margin-top:10px"><div style="font-weight:600;font-size:40px">Продаж</div><div style="font-weight:800;font-size:110px;color:{R}">0</div></div></div>'''
sl[3] = txt(3, 'Знакомая картина?', 'Неделю рассказывали о себе и продукте. <span class="y">И ни одной заявки.</span>', ill, top=720, n=n)

ill = f'''<div style="position:absolute;top:130px;left:120px;right:120px;background:#F6F1E6;color:{NV};border-radius:22px;padding:40px 46px;box-shadow:0 30px 70px rgba(0,0,0,.45);transform:rotate(-1.5deg)">
<div style="font-weight:700;font-size:40px;line-height:1.45;font-style:italic">«Ну и ладно.<br>Значит, никому не нужно.<br>Кому я нужен в моём возрасте?<br><b>Больше не буду</b> этим заниматься»</div></div>'''
sl[4] = txt(4, 'И в голове звучит вот это', 'После 40 этот голос особенно громкий. <span class="y">Он и останавливает большинство.</span>', ill, top=740, n=n)

sl[5] = big_center(5, '💊', 'Страх отказов лечится опытом отказов', 'Пока «нет» не превратится для вас <span class="y">в сухую статистику.</span>', n=n)

ill = cards_list([('🎯', 'Не попали в боль аудитории', SKY), ('🗣', 'Не теми словами её назвали', SKY), ('🧩', 'Слишком сложное описание', SKY), ('📦', 'Слабый оффер', SKY), ('🔥', 'Продавали холодным, не прогрев', Y)], top=110, size=36)
sl[6] = txt(6, 'Ноль продаж не значит, что дело в вас', 'Скорее всего, нерабочая связка. <span class="y">Её надо докрутить.</span>', ill, top=760, n=n)

ill = f'''<svg width="1080" height="560" style="position:absolute;top:120px;left:0">
{''.join(f'<rect x="{110+j*175}" y="{430-h}" width="120" height="{h}" rx="14" fill="{c}"/><text x="{170+j*175}" y="{410-h}" text-anchor="middle" font-family="S" font-weight="800" font-size="34" fill="#fff">{v}</text><text x="{170+j*175}" y="480" text-anchor="middle" font-family="S" font-weight="600" font-size="28" fill="{GR}">тест {j+1}</text>' for j, (h, c, v) in enumerate([(20, R, '0'), (40, R, '1'), (90, '#3E67A8', '3'), (180, SKY, '7'), (300, Y, '12')]))}</svg>'''
sl[7] = txt(7, 'Чтобы найти рабочую связку, нужно попробовать неподходящие', 'Тестируйте: меняйте боль, слова, оффер. <span class="y">Каждый «ноль» подсказывает, что поправить.</span>', ill, top=720, n=n)

ill = two('ОТКАЗ ЭТО НЕ', 'оценка вас', 'и не всегда оценка продукта', 'ОТКАЗ ЭТО', 'данные', 'обратная связь от рынка', top=150, lc=GR, rc=Y).replace('font-size:84px', 'font-size:66px')
sl[8] = txt(8, 'Как смотреть на «нет»', 'Сделайте выводы <span class="y">и идите продавать дальше.</span> Планирование без действий страх не лечит.', ill, top=660, n=n)

sl[9] = personal2(9, 'Я начинал онлайн с нуля', 'В 52 года, после переезда в Швейцарию.', n=n)
sl[10] = cta2(10, 'Хотите понять, как продавать <span class="it" style="font-size:78px">ваш опыт</span> без страха отказа?', 'Разберётесь за 2 минуты.', n=n)

render(sl, os.path.abspath('/home/claude/chernoviki-karuseli/out_otkaz')); print('ok')
