import sys
sys.path.insert(0, '/home/claude/work')
from szlib import *

n = 12; sl = {}
PAPER = '#F6F1E6'


def note(lines, top=120, left=230, right=230, rot=-2, title='на завтра', strike=None, highlight=0):
    strike = strike or []
    rows = ''.join(f'<div style="display:flex;align-items:center;gap:18px;border-bottom:2px solid #D9CFBB;padding:14px 0;font-family:S;font-weight:700;font-size:36px;color:{NV};{"background:rgba(245,197,66,.55);border-radius:8px;padding-left:10px;" if highlight == j+1 else ""}{"text-decoration:line-through;opacity:.55;" if j+1 in strike else ""}"><span style="font-weight:800;color:#C0392B;width:34px">{j+1}.</span>{t}</div>' for j, t in enumerate(lines))
    return f'''<div style="position:absolute;top:{top}px;left:{left}px;right:{right}px;background:{PAPER};border-radius:10px;padding:26px 40px 30px;box-shadow:0 30px 70px rgba(0,0,0,.5);transform:rotate({rot}deg)">
<div style="font-family:S;font-weight:800;font-size:30px;letter-spacing:4px;color:#8A7A5A;text-transform:uppercase">{title}</div>{rows}</div>'''


six = ['Главное дело', 'Второе по важности', 'Третье', 'Четвёртое', 'Пятое', 'Шестое']

sl[1] = cover_polaroid(SH + 'c_list.jpg', 'center 18%', n,
    'Метод за 500&nbsp;000&nbsp;$,<br>который помещается<br><span class="y" style="white-space:nowrap">на одном листке</span>', 'И как он поможет вашему доходу', sticker='1918 год', rot=4).replace('font-size:74px', 'font-size:66px')

ill = f'''<div style="position:absolute;top:130px;left:0;right:0;text-align:center">
<div style="display:inline-block;background:{PAPER};color:{NV};border-radius:12px;padding:26px 60px;transform:rotate(-2deg);box-shadow:0 30px 70px rgba(0,0,0,.45)">
<div style="font-weight:800;font-size:34px;letter-spacing:6px;color:#8A7A5A">США</div><div style="font-weight:800;font-size:200px;line-height:1">1918</div></div></div>'''
sl[2] = txt(2, 'Сталь, заводы и один вопрос', 'Чарльз Шваб, глава одной из крупнейших сталелитейных компаний Америки, спрашивает консультанта Айви Ли: <span class="y">как успевать больше?</span>', ill, top=640, n=n)

ill = f'''<div style="position:absolute;top:130px;left:120px;right:120px">
{bubble("Дайте мне 15 минут с каждым руководителем.")}
{bubble("А сколько это стоит?", me=True)}
{bubble("Попробуйте 3 месяца. Потом заплатите, сколько посчитаете нужным.", extra="border:3px solid " + Y)}</div>'''
sl[3] = txt(3, 'Он не взял ни цента', 'Только 15 минут с каждым руководителем и <span class="y">оплата по результату.</span>', ill, top=740, n=n)

ill = f'''<div style="position:absolute;top:150px;left:120px;right:120px;background:#E9F0E6;color:{NV};border-radius:14px;padding:34px 44px;box-shadow:0 30px 70px rgba(0,0,0,.45);transform:rotate(1.5deg);border:3px dashed #8FA88A">
<div style="display:flex;justify-content:space-between;font-weight:800;font-size:28px;letter-spacing:3px;color:#5D7359"><span>ЧЕК</span><span>1918</span></div>
<div style="font-weight:600;font-size:32px;margin-top:26px">Заплатить Айви Ли</div>
<div style="font-weight:800;font-size:110px;line-height:1.1;margin-top:10px">$ 25 000</div>
<div style="font-weight:600;font-size:28px;margin-top:16px;color:#5D7359">подпись: Ч. Шваб</div></div>'''
sl[4] = txt(4, 'Через 3 месяца пришёл чек', 'На 25 000 $. По сегодняшним деньгам <span class="y">это около 500 000 $.</span> Вот за что.', ill, top=720, n=n)

sl[5] = txt(5, 'Шаг 1. Вечером 6 дел', 'Запишите шесть главных дел на завтра. <span class="y">И ни одного больше.</span>', note(six), top=740, n=n)
sl[6] = txt(6, 'Шаг 2. По важности', 'Расставьте их от самого главного <span class="y">до того, что может подождать.</span>', note(six, highlight=1, rot=1.5), top=740, n=n)
sl[7] = txt(7, 'Шаг 3. Только первое', 'Утром беритесь за первое и не трогайте второе, пока не закончите. <span class="y">Что не успели, переходит в новый список.</span>', note(six, strike=[1, 2], rot=-1.5), top=740, n=n)

ill = two('УТРОМ БЕЗ СПИСКА', '«с чего начать?»', 'силы уходят на выбор', 'УТРОМ СО СПИСКОМ', 'дело №1', 'лучшие часы на главное', top=150, lc=GR, rc=Y).replace('font-size:84px', 'font-size:52px')
sl[8] = txt(8, 'Почему это работает', 'Решение принято с вечера. Утром вы не тратите силы на выбор, и <span class="y">лучшие часы уходят на главное.</span>', ill, top=660, n=n)

ill = note(['Шаг к своему доходу', 'Работа', 'Документы', 'Магазин', 'Звонок родным', 'Спорт'], highlight=1, title='ваш список')
sl[9] = txt(9, 'А теперь про вас', 'Если вы хотите свой доход, в этом списке каждый день должно быть дело для него. <span class="y">Не «потом», а первым номером.</span>', ill, top=740, n=n)

sl[10] = big_center(10, '🤔', 'Но что именно поставить первым?', 'Здесь застревают почти все. Непонятно, <span class="y">с какого шага превратить опыт в доход.</span>', n=n)
sl[11] = personal2(11, 'Я начинал онлайн с нуля', 'В 52 года, после переезда в Швейцарию.', n=n)
sl[12] = cta2(12, 'Хотите понять, какое дело из <span class="it" style="font-size:78px">вашего опыта</span> поставить первым?', 'Разберётесь за 2 минуты.', n=n)

render(sl, os.path.abspath('/home/claude/chernoviki-karuseli/out_list')); print('ok')
