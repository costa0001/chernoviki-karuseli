import sys
sys.path.insert(0, '/home/claude/work')
from szlib import *
exec(open('/home/claude/work/nastya.py').read().split("def st(")[0].split("n = 12; sl = {}")[1])  # TEX, CSS

n = 12; sl = {}


def frame(i, inner, last=False):
    """Наш стиль по краю: фактурная синяя рамка, жёлтые уголки; в центре — карточка-сцена."""
    corners = ''.join(f'<div style="position:absolute;{v}:{'84' if v=='top' else '38'}px;{h}:38px;width:70px;height:70px;border-{v}:8px solid {Y};border-{h}:8px solid {Y}"></div>' for v in ('top', 'bottom') for h in ('left', 'right'))
    return S(i, n, CSS + TEX + corners + f'''
<div style="position:absolute;left:70px;right:70px;top:120px;bottom:80px;border-radius:26px;overflow:hidden;box-shadow:0 30px 80px rgba(0,0,0,.6)">{inner}</div>
''', last=last)


def scene(bg, emoji, title, sub='', big=300, num=None):
    return f'''<div style="position:absolute;inset:0;background:{bg}"></div>
{f'<div style="position:absolute;left:40px;top:36px;background:{NV};color:{Y};font-family:S;font-weight:800;font-size:30px;letter-spacing:3px;padding:10px 22px;border-radius:10px">ПРОБЛЕМА №{num}</div>' if num else ''}
<div style="position:absolute;left:0;right:0;top:150px;text-align:center;font-size:{big}px;line-height:1;filter:drop-shadow(0 20px 30px rgba(0,0,0,.35))">{emoji}</div>
<div style="position:absolute;left:0;right:0;bottom:0;height:560px;background:linear-gradient(180deg,rgba(6,16,34,0),rgba(6,16,34,.92) 40%)"></div>
<div style="position:absolute;left:56px;right:56px;bottom:60px;text-align:center">
<div style="font-family:S;font-weight:800;font-size:70px;line-height:1.05;color:#fff;text-transform:uppercase">{title}</div>
{f'<div style="font-family:S;font-weight:600;font-size:36px;line-height:1.3;color:#DDE6F3;margin-top:22px">{sub}</div>' if sub else ''}</div>'''


SEA = 'linear-gradient(180deg,#7EC8F2 0%,#BFE6F7 45%,#2E7FB8 46%,#15507E 100%)'
SKY2 = 'linear-gradient(180deg,#F7C98B 0%,#F3A86B 40%,#5B6FA8 100%)'
HALL = 'linear-gradient(180deg,#E9DFCF 0%,#CDBEA6 60%,#8C7A62 100%)'
NIGHT = 'linear-gradient(180deg,#1B2A4A 0%,#33476E 60%,#0E1A30 100%)'
GREEN = 'linear-gradient(180deg,#9ED6B8 0%,#4FA88B 55%,#1F5F57 100%)'

sl[1] = frame(1, scene(SEA, '🛥️', 'Проблемы,<br>о которых<br><span class="mk">мечтают все</span>', 'Когда денег так много, что начинаются странности', big=260))
sl[2] = frame(2, scene(SEA, '⚓', 'Яхта<br><span class="mk">не помещается</span><br>в марину', 'Причал просто слишком маленький', num=1))
sl[3] = frame(3, scene(SKY2, '✈️', 'Личный самолёт<br><span class="mk">больше ангара</span>', 'Приходится строить свой', num=2))
sl[4] = frame(4, scene(HALL, '📶', 'Дом такой большой, что <span class="mk">Wi-Fi</span> не достаёт до всех комнат', num=3))
sl[5] = frame(5, scene(GREEN, '🏝️', 'На своём острове <span class="mk">не ловит</span> телефон', 'Приходится строить свою связь', num=4))
sl[6] = frame(6, scene(HALL, '🖼️', 'Картине нужна <span class="mk">своя охрана</span>', 'И отдельная комната с климатом', num=5))
sl[7] = frame(7, scene(SEA, '🚤', 'Вторая яхта, чтобы <span class="mk">возить игрушки</span> для первой', 'Катера, гидроциклы, вертолёт', num=6))
sl[8] = frame(8, scene(NIGHT, '🧳', 'Домов столько, что дети <span class="mk">не знают</span>, где их одежда', num=7))

sl[9] = frame(9, f'''<div style="position:absolute;inset:0;background:#0E2244"></div>
<div style="position:absolute;left:60px;right:60px;top:0;bottom:0;display:flex;flex-direction:column;justify-content:center">
<div style="font-family:S;font-weight:800;font-size:74px;line-height:1.08;color:#fff;text-transform:uppercase">А теперь честно</div>
<div style="font-family:S;font-weight:600;font-size:46px;line-height:1.35;color:#EEF2F8;margin-top:36px">У большинства из нас проблемы другие:</div>
<div style="margin-top:26px">{''.join(f'<div style="font-family:S;font-weight:700;font-size:44px;color:#fff;margin-top:18px">{e} {t}</div>' for e, t in [('💶', 'цены в евро растут, доход нет'), ('📄', 'резюме после 45 не читают'), ('🔁', 'опыт есть, а применить негде')])}</div></div>''')

sl[10] = frame(10, f'''<div style="position:absolute;inset:0;background:#0E2244"></div>
<div style="position:absolute;left:60px;right:60px;top:0;bottom:0;display:flex;flex-direction:column;justify-content:center;text-align:center">
<div style="font-size:150px">🪜</div>
<div style="font-family:S;font-weight:800;font-size:68px;line-height:1.1;color:#fff;text-transform:uppercase;margin-top:20px">Яхта начинается<br>не с яхты</div>
<div style="font-family:S;font-weight:600;font-size:44px;line-height:1.35;color:#EEF2F8;margin-top:30px">А с первого евро, который вам заплатили <span class="mk">за ваш опыт.</span></div></div>''')

sl[11] = frame(11, f'''<div style="position:absolute;inset:0;background:#0E2244"></div>
<div style="position:absolute;left:60px;right:60px;top:0;bottom:0;display:flex;flex-direction:column;justify-content:center">
<div style="font-family:S;font-weight:800;font-size:32px;letter-spacing:4px;color:{Y}">МОЯ ИСТОРИЯ</div>
<div style="font-family:S;font-weight:600;font-size:46px;line-height:1.35;color:#EEF2F8;margin-top:24px">Я начинал онлайн с нуля в 52 года, после переезда в Швейцарию.</div>
<div style="font-family:S;font-weight:600;font-size:46px;line-height:1.35;color:#EEF2F8;margin-top:24px">Сегодня у меня <span class="mk">300 000+ подписчиков</span> за год без рекламы и коллабораций.</div></div>''')

sl[12] = frame(12, f'''<div style="position:absolute;inset:0;background:#0E2244"></div>
<div style="position:absolute;left:60px;right:60px;top:0;bottom:0;display:flex;flex-direction:column;justify-content:center;text-align:center">
<div style="font-family:S;font-weight:700;font-size:50px;line-height:1.3;color:#fff">Хотите понять, как ваш опыт может принести <span class="mk">первые деньги в евро?</span></div>
<div style="font-family:S;font-weight:600;font-size:36px;color:#C9D6EA;margin-top:26px">Разберётесь за 2 минуты.</div>
<div style="margin-top:44px;background:{Y};color:{NV};padding:34px 20px;border-radius:18px;box-shadow:0 0 60px rgba(245,197,66,.35)"><div style="font-family:S;font-weight:800;font-size:72px;line-height:1;white-space:nowrap">Пишите «ОПЫТ» &darr;</div><div style="font-family:S;font-weight:600;font-size:36px;margin-top:12px">в комментариях</div></div></div>''', last=True)

render(sl, os.path.abspath('/home/claude/chernoviki-karuseli/out_bogachi')); print('ok')
