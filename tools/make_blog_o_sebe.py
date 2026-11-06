# Карусель «Перестаньте вести блог о себе» (по мотивам формата, тексты свои). 9 слайдов.
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from gendesign import CSS, Y, NV, SKY
from PIL import Image, ImageFilter
from playwright.sync_api import sync_playwright

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
OUT = os.path.join(ROOT, sys.argv[1] if len(sys.argv) > 1 else 'blog-o-sebe-urok')
PH = os.path.join(ROOT, 'foto-baza', '2026-10-zheneva', 'g57_park_ruka-u-lica_v-kameru.jpg')
N = 9
CR = '#F4EFE4'  # светлый фон

CSS2 = CSS + f'''
.cream{{background:{CR}!important}} .cream .bg,.cream .grid{{display:none}}
.cream .top{{color:#7A6E58}} .cream h1{{color:{NV}}} .cream .p{{color:#23324F}}
.row{{font-weight:600;font-size:44px;line-height:1.28;padding:22px 0;border-bottom:2px solid rgba(255,255,255,.14)}}
.cream .row{{border-color:#D9CFBB;color:{NV}}}
.pr{{background:#FFFDF7;color:#1B2436;border-radius:26px;padding:36px 40px;font-family:"DejaVu Sans Mono",monospace;font-size:31px;line-height:1.38;box-shadow:0 24px 60px rgba(0,0,0,.35)}}
.prt{{font-weight:800;font-size:32px;letter-spacing:4px;margin:34px 0 16px}}
.huge{{font-weight:800;font-size:118px;line-height:.98;text-transform:uppercase}}
'''

def S(i, inner, cls='', last=False):
    arr = '' if last else ' &rarr;'
    return (f'<div class="s {cls}"><div class="bg"></div><div class="grid"></div>'
            f'<div class="top"><span>@bravo.konstantin</span><span>{i} / {N}{arr}</span></div>{inner}</div>')

def box(html, top=120, bottom=70, center=True):
    j = 'center' if center else 'flex-start'
    return f'<div class="txt" style="top:{top}px;bottom:{bottom}px;display:flex;flex-direction:column;justify-content:{j}">{html}</div>'

sl = {}
# 1. Обложка: фото на весь слайд
sl[1] = S(1, f'''<img src="file://{OUT}/_cover.jpg" style="position:absolute;inset:0;width:1080px;height:1350px;object-fit:cover;object-position:center 22%">
<div style="position:absolute;left:0;right:0;bottom:0;height:820px;background:linear-gradient(180deg,rgba(10,23,48,0),rgba(10,23,48,.88) 42%,#0A1730)"></div>
<div class="txt" style="bottom:90px">
<div style="font-weight:800;font-size:44px;line-height:1.2;text-transform:uppercase">Хотите, чтобы на вас<br>подписывались?</div>
<div class="huge" style="margin-top:26px;font-size:124px">Перестаньте<br>вести блог<br><span style="color:{Y}">о себе</span></div>
<div class="p" style="margin-top:34px;font-size:44px">Покажу, что публиковать вместо&nbsp;этого&nbsp;&rarr;</div></div>''')

# 2. Угадаю
rows = ['Рассказываете в сторис, что у вас нового.', 'Показываете свои работы и услуги.',
        'Делитесь мыслями и историями из жизни.', 'Рассказываете о своём пути и достижениях.']
sl[2] = S(2, box(f'''<h1 style="font-size:84px">Угадаю, как вы сейчас ведёте блог.</h1>
<div style="margin-top:30px">{''.join(f'<div class="row">{r}</div>' for r in rows)}</div>
<div class="p" style="margin-top:26px">И ждёте, что люди проникнутся доверием и начнут подписываться.</div>
<div style="font-weight:800;font-size:66px;color:{Y};margin-top:40px;text-transform:uppercase">Но есть одна деталь…</div>'''))

# 3. Люди не собирались читать
sl[3] = S(3, box(f'''<h1 style="font-size:84px">Люди не собирались читать ваш блог.</h1>
<div class="p">Они просто открыли Instagram. Листают ленту, смотрят Reels.</div>
<div class="p" style="margin-top:20px">И вдруг видят публикацию, которая говорит то, о чём они сами сейчас думают.</div>
<div class="huge" style="color:{NV};margin-top:46px">Это же<br>про меня!</div>
<div class="p" style="margin-top:36px">Здесь человек останавливается. Не потому, что вы рассказали о себе, а потому, что <span class="y">вы рассказали о нём.</span></div>'''), 'cream')

# 4. Ищите темы в жизни аудитории
items = ['что его сегодня расстроило', 'о чём он переживает', 'чему он завидует', 'что никак не получается', 'о чём он думает перед сном']
sl[4] = S(4, box(f'''<h1 style="font-size:80px">Ищите темы не в своей жизни, а в жизни аудитории.</h1>
<div class="p">Не просто «какие у людей боли». А что конкретно происходит с человеком:</div>
<div style="margin-top:18px">{''.join(f'<div class="row" style="display:flex;gap:22px"><span style="color:{Y}">●</span><span>{r}</span></div>' for r in items)}</div>
<div class="p" style="margin-top:34px">А искать такие ситуации мне помогает ИИ. <span class="y">Промпт на следующем слайде.</span></div>'''))

P1 = ('Ты исследователь аудитории и контент-стратег. Моя ниша: [ниша]. Я помогаю людям [результат]. '
      'Найди 20 конкретных жизненных ситуаций, в которых моим людям пригодятся мои знания. '
      'Для каждой опиши, что произошло, какую эмоцию человек испытывает и что он думает про себя, но редко говорит вслух. '
      'Без общих фраз и маркетинговых штампов. Мне нужны узнаваемые ситуации, из которых получатся темы для Instagram. '
      'Отметь, какие предположения стоит проверить на реальной аудитории.')
sl[5] = S(5, box(f'''<div class="tag">шаг 1 · найти темы</div>
<h1 style="font-size:70px">Промпт для ChatGPT</h1>
<div class="prt" style="color:{SKY}">СКОПИРУЙТЕ И ВСТАВЬТЕ ↓</div>
<div class="pr" style="font-size:37px">{P1}</div>
<div class="p" style="font-size:38px;margin-top:30px">Вместо скобок впишите свою нишу и результат, который вы даёте людям.</div>'''))

P2 = ('Возьми 10 самых сильных ситуаций из прошлого ответа. Для каждой придумай 3 заголовка для карусели в Instagram: '
      '1) через внутренний монолог человека; 2) через неожиданное противоречие; 3) через ошибку, которая мешает получить результат. '
      'Пиши живым разговорным языком, как будто один друг говорит другому. Заголовок должен быть понятен человеку, который видит мой контент впервые. '
      'Без очевидных советов и пустого кликбейта. Выбери 10 лучших и объясни, чем каждый остановит читателя.')
sl[6] = S(6, box(f'''<div class="tag">шаг 2 · остановить взгляд</div>
<h1 style="font-size:66px">Начните не с себя, а с мысли, которую человек узнает как свою</h1>
<div class="prt" style="color:{SKY}">ВТОРОЙ ПРОМПТ ↓</div>
<div class="pr" style="font-size:34px">{P2}</div>'''))

# 7. Схема
st = ['Проблема человека', 'Ваш взгляд эксперта', 'Ваш опыт и живые примеры', 'Конкретное решение']
flow = ''.join((f'<div style="font-weight:800;font-size:{60 if k==0 else 50}px;color:{NV};text-align:center;background:{"#fff" if k else Y};border:3px solid {NV};border-radius:22px;padding:26px 20px">{s}</div>'
                + ('' if k == len(st)-1 else f'<div style="text-align:center;font-size:64px;line-height:1.1;color:{NV}">↓</div>')) for k, s in enumerate(st))
sl[7] = S(7, box(f'''<h1 style="font-size:84px">Теперь самое интересное.</h1>
<div class="p">Вам не нужно исчезать из своего блога. Просто поменяйте порядок:</div>
<div style="margin-top:40px">{flow}</div>'''), 'cream')

# 8. Видите разницу
sl[8] = S(8, box(f'''<div class="tag">видите разницу?</div>
<h1 style="font-size:88px">Вы всё так же говорите о себе.</h1>
<div class="p" style="margin-top:40px">Но теперь ваша история интересна, потому что <span class="y">помогает человеку разобраться в его собственной ситуации.</span></div>
<div style="display:flex;gap:24px;margin-top:60px">
<div style="flex:1;border:4px solid #FF6B6B;border-radius:28px;padding:30px"><div style="font-weight:800;font-size:34px;color:#FF6B6B;letter-spacing:3px">БЫЛО</div><div style="font-weight:700;font-size:42px;line-height:1.25;margin-top:16px">«Вот что у меня нового»</div></div>
<div style="flex:1;border:4px solid {Y};border-radius:28px;padding:30px"><div style="font-weight:800;font-size:34px;color:{Y};letter-spacing:3px">СТАЛО</div><div style="font-weight:700;font-size:42px;line-height:1.25;margin-top:16px">«Вот что поможет вам»</div></div></div>'''))

# 9. Призыв УРОК
sl[9] = S(9, box(f'''<h1 style="font-size:74px">Вам не нужно каждый день придумывать, что рассказать о себе.</h1>
<div class="p">У вашей аудитории уже есть сотни вопросов и ситуаций. Темы, заголовки, карусели и Reels мне помогает собирать ИИ: со мной работает команда ИИ-сотрудников.</div>
<div style="margin-top:50px;background:{Y};color:{NV};padding:34px 20px;border-radius:18px;text-align:center;box-shadow:0 0 60px rgba(245,197,66,.35)">
<div style="font-weight:800;font-size:92px;line-height:1;white-space:nowrap">Пишите «УРОК» &darr;</div>
<div style="font-weight:600;font-size:38px;margin-top:14px">и я пришлю бесплатный урок о моей системе с ИИ</div></div>
<div style="font-weight:600;font-size:32px;color:#9AA6B8;margin-top:36px;text-align:center">Сохраните карусель, чтобы не потерять два промпта</div>''', bottom=60), last=True)

FIT = '''()=>{const t=document.querySelector('.txt');if(!t)return 0;let g=0;
while(t.scrollHeight>t.clientHeight+2&&g<30){g++;t.style.zoom=(parseFloat(t.style.zoom||1)*0.97)}return g}'''

os.makedirs(OUT, exist_ok=True)
im = Image.open(PH).convert('RGB')
im = im.resize((1080, int(im.height * 1080 / im.width)), Image.LANCZOS).filter(ImageFilter.UnsharpMask(1.5, 80, 2))
im.save(f'{OUT}/_cover.jpg', quality=95)
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1080, 'height': 1350})
    for k in sorted(sl):
        open(f'{OUT}/_t.html', 'w').write(f'<html><head><meta charset="utf-8"><style>{CSS2}</style></head><body>{sl[k]}</body></html>')
        pg.goto(f'file://{OUT}/_t.html'); pg.wait_for_timeout(300)
        print(k, 'fit', pg.evaluate(FIT))
        pg.screenshot(path=f'{OUT}/slide_{k:02d}.png')
    b.close()
for k in sorted(sl):
    Image.open(f'{OUT}/slide_{k:02d}.png').convert('RGB').save(f'{OUT}/slide_{k:02d}.jpg', quality=93)
    os.remove(f'{OUT}/slide_{k:02d}.png')
os.remove(f'{OUT}/_t.html'); os.remove(f'{OUT}/_cover.jpg')
