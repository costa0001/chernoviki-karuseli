import sys
sys.path.insert(0, '/home/claude/work')
from szlib import *

n = 12; sl = {}

# Фирменная фактура: тёмно-синяя бумага с зерном, клетка «блокнота», виньетка
TEX = '''<svg style="position:absolute;inset:0;width:1080px;height:1350px" viewBox="0 0 1080 1350">
<defs><filter id="g"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="3" stitchTiles="stitch"/><feColorMatrix values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 .09 0"/></filter>
<pattern id="c" width="54" height="54" patternUnits="userSpaceOnUse"><path d="M54 0H0V54" fill="none" stroke="#6BB8FF" stroke-opacity=".07" stroke-width="2"/></pattern>
<radialGradient id="v" cx="50%" cy="45%" r="75%"><stop offset="60%" stop-color="#000" stop-opacity="0"/><stop offset="100%" stop-color="#000" stop-opacity=".45"/></radialGradient></defs>
<rect width="1080" height="1350" fill="url(#c)"/><rect width="1080" height="1350" filter="url(#g)"/><rect width="1080" height="1350" fill="url(#v)"/></svg>'''

CSS = f'''<style>.mk{{background:linear-gradient(100deg,rgba(245,197,66,.0) 0 1%,{Y} 3% 96%,rgba(245,197,66,.0) 99%);color:{NV};padding:0 14px;margin:0 -6px;border-radius:6px 14px 8px 12px;box-decoration-break:clone;-webkit-box-decoration-break:clone;display:inline;}}
.ul{{background:linear-gradient(transparent 72%,{Y} 72% 92%,transparent 92%);padding:0 4px}}
.story{{position:absolute;left:96px;right:96px;top:0;bottom:120px;display:flex;flex-direction:column;justify-content:center}}
.story p{{font-family:S;font-weight:600;font-size:52px;line-height:1.32;color:#EEF2F8;margin:0 0 36px}}
.story b{{font-weight:800;color:#fff}}
.story i{{font-style:italic;color:#C9D6EA}}
.tape{{position:absolute;width:190px;height:54px;background:rgba(245,197,66,.85);box-shadow:0 6px 16px rgba(0,0,0,.35)}}</style>'''


def st(i, html, last=False):
    return S(i, n, CSS + TEX + f'<div class="story">{html}</div>', last=last)


# Обложка: без фото, фирменная фактура + стикер-лист
sl[1] = S(1, n, CSS + TEX + f'''
<div style="position:absolute;left:80px;top:170px;right:80px;bottom:170px;background:#F3EEE3;border-radius:6px;transform:rotate(-1.6deg);box-shadow:0 40px 90px rgba(0,0,0,.55)">
<svg style="position:absolute;inset:0;width:100%;height:100%"><defs><pattern id="l" width="10" height="62" patternUnits="userSpaceOnUse"><path d="M0 61H10" stroke="#9DB6D6" stroke-opacity=".45" stroke-width="2"/></pattern></defs><rect width="100%" height="100%" fill="url(#l)"/><line x1="120" y1="0" x2="120" y2="2000" stroke="#E07A7A" stroke-opacity=".5" stroke-width="3"/></svg>
<div style="position:absolute;left:160px;right:70px;top:110px">
<div style="font-family:S;font-weight:800;font-size:30px;letter-spacing:5px;color:#8A7A5A">ИСТОРИЯ НАСТЕНЬКИ</div>
<div style="font-family:S;font-weight:800;font-size:92px;line-height:1.08;color:{NV};margin-top:34px;text-transform:uppercase">Доход растёт<br><span style="color:#C0392B">не после</span><br>нового курса</div>
<div style="font-family:S;font-weight:700;font-size:46px;line-height:1.3;color:{NV};margin-top:44px">А тогда, когда вы делаете одно и то же <span class="mk">снова и снова</span></div></div>
<div style="position:absolute;right:60px;bottom:60px;transform:rotate(-8deg);border:6px solid #C0392B;color:#C0392B;border-radius:14px;padding:6px 22px;font-family:S;font-weight:800;font-size:40px">курс №8</div></div>
<div class="tape" style="left:430px;top:140px;transform:rotate(3deg)"></div>
<div style="position:absolute;left:80px;right:80px;bottom:70px;display:flex;justify-content:space-between;font-family:S;font-weight:700;font-size:30px;color:#C9D6EA"><span></span><span style="color:{Y}">листайте →</span></div>''')

sl[2] = st(2, f'<p><b>Каждый раз одно и то же.</b></p><p>Настенька, 47 лет, живёт в Германии. Покупает очередной курс про доход онлайн. С той самой <span class="mk">секретной схемой.</span></p><p>Внутри приятное предвкушение: <i>«Ну вот! Сейчас точно получится!»</i></p>')
sl[3] = st(3, f'<p>Потом Настенька открывает ноутбук.</p><p>Начинает делать всё <span class="ul">сама</span>.</p><p>И магия <span class="mk">испаряется.</span></p>')
sl[4] = st(4, f'<p>Наступает самый <span class="mk">неприятный</span> период.</p><p>Всё в сто раз сложнее, чем на уроках. Текст не пишется. Камера пугает.</p><p>Первый пост: охваты стоят. Быстрого результата <span class="mk">нет.</span></p>')
sl[5] = st(5, f'<p>Что делают в этот момент большинство людей?</p><p><span class="mk">Сдаются.</span></p><p>Вот и Настенька тоже.</p>')
sl[6] = st(6, f'<p>Вместо того чтобы стиснуть зубы, пережить этот период и докрутить инструмент <span class="ul">до результата</span>, Настенька идёт покупать <span class="mk">новый курс.</span></p><p><i>Ну в этот раз же точно получится, да?</i></p>')
sl[7] = st(7, f'<p>Потому что на самом деле Настенька ищет <span class="mk">не инструмент.</span></p><p>Она хочет снова испытать это сладкое предвкушение:</p><p><i>«Вот эта схема точно сработает сразу!»</i></p>')
sl[8] = st(8, f'<p>Любой инструмент работает только у тех, кто способен <span class="mk">выдержать</span> этап, когда всё получается откровенно плохо.</p><p>Когда рука не набита. Когда результаты не радуют.</p>')
sl[9] = st(9, f'<p>Секретных секретов нет.</p><p>Выберите <span class="mk">один</span> надёжный инструмент.</p><p>И просто <span class="ul">продолжайте</span> практиковаться, пока не пойдёт результат.</p>')
sl[10] = st(10, f'<p>А у вас, в 35–55, есть то, чего нет у молодых: <span class="mk">ваш опыт.</span></p><p>Его не нужно покупать на курсе. Его нужно один раз правильно упаковать и <span class="ul">применять снова и снова.</span></p>')
sl[11] = st(11, f'<p style="font-size:34px;letter-spacing:4px;color:{Y};font-weight:800">МОЯ ИСТОРИЯ</p><p>Я начинал онлайн с нуля в 52 года, после переезда в Швейцарию.</p><p>Сегодня у меня <span class="mk">300 000+ подписчиков</span> за год без рекламы и коллабораций.</p>')
sl[12] = st(12, f'<p style="text-align:center">Хотите понять, какой <span class="mk">один инструмент</span> из вашего опыта начать применять уже сейчас?</p><p style="text-align:center;font-size:40px;color:#C9D6EA">Разберётесь за 2 минуты.</p>'
            f'<div style="margin-top:20px;background:{Y};color:{NV};padding:36px 20px;border-radius:18px;text-align:center;box-shadow:0 0 60px rgba(245,197,66,.35)"><div style="font-family:S;font-weight:800;font-size:86px;line-height:1">Пишите «ОПЫТ» &darr;</div><div style="font-family:S;font-weight:600;font-size:38px;margin-top:12px">в комментариях</div></div>', last=True)

render(sl, os.path.abspath('/home/claude/chernoviki-karuseli/out_nastya')); print('ok')
