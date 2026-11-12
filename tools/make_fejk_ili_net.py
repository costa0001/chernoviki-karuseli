import sys
sys.path.insert(0, '/home/claude/work')
from szlib import *

n = 7; sl = {}
ORIG = '/mnt/user-data/uploads/d6065f40-image.jpg'


def tw(name, handle, init, col, lines, extra=''):
    body = ''.join(f'<div style="margin-top:14px">{l}</div>' for l in lines)
    return f'''<div style="background:#F2EEF8;color:#14161A;border-radius:28px;padding:30px 36px;box-shadow:0 24px 60px rgba(0,0,0,.45);{extra}">
<div style="display:flex;align-items:center;gap:20px"><div style="width:84px;height:84px;border-radius:50%;background:{col};color:#fff;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:34px">{init}</div>
<div><div style="font-weight:800;font-size:36px">{name} <span style="color:#1D9BF0">●</span></div><div style="font-weight:500;font-size:28px;color:#5B6270">{handle}</div></div>
<div style="margin-left:auto;font-weight:800;font-size:34px">𝕏</div></div>
<div style="font-weight:600;font-size:34px;line-height:1.3">{body}</div></div>'''


def stamp(t, top, left, rot=-10):
    return f'<div style="position:absolute;top:{top}px;left:{left}px;transform:rotate({rot}deg);border:8px solid {Y};color:{Y};border-radius:18px;padding:8px 30px;font-weight:800;font-size:64px;background:rgba(8,20,40,.75);box-shadow:0 0 50px rgba(245,197,66,.35)">{t}</div>'


sl[1] = S(1, n, f'''<div style="position:absolute;top:110px;left:70px;right:70px;text-align:center">
<div style="display:inline-block;background:{Y};color:{NV};font-weight:800;font-size:64px;padding:10px 36px;border-radius:16px">ФЕЙК ИЛИ НЕТ?</div></div>
<div style="position:absolute;top:240px;left:70px;right:70px">
{tw("Билл Гейтс", "@BillGates", "БГ", "#3E67A8", ["Илон Маск не создавал Tesla. Он её купил.", "Он не создавал X. Он купил Twitter.", "Он не изобретал ракеты, двигатели и телеметрию SpaceX. Он взял технологии NASA и переманил их инженеров.", "<b>А Я СОЗДАЛ MICROSOFT!</b>"])}
{tw("Илон Маск", "@elonmusk", "ИМ", "#14161A", ["Не заставляй меня покупать Microsoft, чтобы уволить тебя 😂", "Некоторые, похоже, забыли, сколько у меня денег.", "Был бы забавный вторник."], "margin-top:30px;margin-left:60px")}</div>''')

sl[2] = S(2, n, f'''<div style="position:absolute;top:110px;left:0;right:0;text-align:center"><div class="tag" style="font-size:34px">оригинал, который разлетелся по сети</div></div>
<img src="file://{ORIG}" style="position:absolute;top:190px;left:120px;width:840px;height:906px;object-fit:contain;border-radius:20px;box-shadow:0 30px 70px rgba(0,0,0,.5)">
<div class="txt" style="bottom:80px;text-align:center"><h1 style="font-size:64px">А вы бы поверили?</h1></div>''')

ill = f'''<div style="position:absolute;top:170px;left:0;right:0;display:flex;justify-content:center;gap:40px">
<div style="width:380px;height:300px;border-radius:30px;border:4px solid {R};background:rgba(255,107,107,.1);display:flex;flex-direction:column;align-items:center;justify-content:center"><div style="font-size:110px">🤥</div><div style="font-weight:800;font-size:54px;color:{R}">ФЕЙК</div></div>
<div style="width:380px;height:300px;border-radius:30px;border:4px solid {SKY};background:rgba(107,184,255,.1);display:flex;flex-direction:column;align-items:center;justify-content:center"><div style="font-size:110px">✅</div><div style="font-weight:800;font-size:54px;color:{SKY}">ПРАВДА</div></div></div>'''
sl[3] = txt(3, 'Как вы думаете?', 'Напишите в комментариях своё мнение, <span class="y">а потом листайте:</span> ответ на следующем слайде →', ill, top=640, n=n)

ill = cards_list([('🏢', 'Гейтс ушёл из совета директоров Microsoft ещё в 2020 году. Уволить его там неоткуда', Y), ('💰', 'Microsoft стоит около 3 трлн $. Купить её Маск не смог бы даже теоретически', Y)], top=150, size=34)
sl[4] = txt(4, 'Ответ: это фейк', 'Такой переписки не было. <span class="y">Но в одном фейк прав.</span>', ill + stamp('ФЕЙК', 520, 640, -12), top=720, n=n)

ill = two('2004 ГОД', '6,5 млн $', 'Маск вкладывает в Tesla и становится председателем', 'НО', 'не основатель', 'компанию основали инженеры до него', top=150, lc=SKY, rc=Y).replace('font-size:84px', 'font-size:58px')
sl[5] = txt(5, 'Маск правда не создавал Tesla', 'Он пришёл в уже основанную компанию как инвестор. <span class="y">И вырастил её в гиганта.</span>', ill, top=680, n=n)

sl[6] = big_center(6, '🌱', 'Не обязательно начинать с нуля', 'Маск разбогател не на том, что изобрёл, а на том, что <span class="y">взял уже существующее и вырастил.</span> Ваши навыки и опыт тоже уже есть.', n=n)

sl[7] = S(7, n, f'''<div class="txt" style="top:0;bottom:70px;display:flex;flex-direction:column;justify-content:center;text-align:center">
<div class="tag">бесплатный тест</div>
<h1 style="font-size:60px;text-transform:none;margin-top:24px;line-height:1.15">Узнайте, какие шаги сделать <span class="it" style="font-size:74px">уже сейчас,</span> чтобы выйти на новый уровень дохода на ваших навыках и опыте</h1>
<div style="margin-top:56px;background:{Y};color:{NV};padding:36px 20px;border-radius:18px;box-shadow:0 0 60px rgba(245,197,66,.35)"><div style="font-weight:800;font-size:86px;line-height:1;white-space:nowrap">Пишите «ХОЧУ» &darr;</div><div style="font-weight:600;font-size:38px;margin-top:12px">в комментариях</div></div></div>''', last=True)

render(sl, os.path.abspath('/home/claude/chernoviki-karuseli/out_fake')); print('ok')
