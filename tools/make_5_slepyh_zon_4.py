import sys
sys.path.insert(0, '/home/claude/work')
from szlib import *

sl = {}
sl[1] = cover_full(SH + 'cover_sz4.jpg', 'center 90%', 'Финальная серия · слепые зоны 16–20',
                   'Пробовали<br>много раз<br><span class="y" style="white-space:nowrap">и уже не верите?</span>',
                   'Последние 5 ошибок. Самые коварные')

# 16 — копирует 25-летних
ill = f'''<div style="position:absolute;top:120px;left:330px;width:420px;height:560px;border-radius:56px;border:6px solid #3A4E73;background:#0B1A36;padding:34px;box-sizing:border-box;text-align:center">
<div style="font-size:150px;margin-top:40px">💃</div><div style="font-weight:800;font-size:44px;margin-top:20px">ТРЕНД #47</div>
<div style="font-weight:600;font-size:32px;color:{GR};margin-top:14px">«танцуем под звук»</div>
<div style="margin-top:40px;font-weight:800;font-size:40px;color:{R}">это точно про меня?</div></div>'''
sl[2] = zone(2, 16, 'Вы копируете 25-летних', 'Тренды, танцы, громкие «прогревы». <span class="y">Формат не про вас,</span> и люди это чувствуют.', ill, top=740)
ill = two('ХАЙП', '✗', 'громко, быстро, без доверия', 'ДОВЕРИЕ', '✓', 'опыт, честные истории, спокойная подача', top=150)
sl[3] = why(3, 'Ровесники покупают доверие', 'Людям 35–55 нужен человек, который сам прошёл путь. <span class="y">Не хайп, а уверенность.</span>', ill, top=660)

# 17 — бросает рано
ill = f'''<svg width="1080" height="600" style="position:absolute;top:100px;left:0">
<line x1="100" y1="480" x2="980" y2="480" stroke="#3A4E73" stroke-width="4"/>
<path d="M100,470 L560,455 C700,440 800,300 960,90" fill="none" stroke="{SKY}" stroke-width="10" stroke-linecap="round"/>
<line x1="440" y1="120" x2="440" y2="480" stroke="{R}" stroke-width="6" stroke-dasharray="16 10"/>
<text x="440" y="100" text-anchor="middle" font-family="S" font-weight="800" font-size="36" fill="{R}">вы ушли здесь</text>
<text x="960" y="70" text-anchor="end" font-family="S" font-weight="800" font-size="36" fill="{SKY}">результат</text>
<text x="100" y="530" font-family="S" font-weight="600" font-size="30" fill="{GR}">неделя 1</text><text x="440" y="530" text-anchor="middle" font-family="S" font-weight="600" font-size="30" fill="{GR}">неделя 6</text><text x="960" y="530" text-anchor="end" font-family="S" font-weight="600" font-size="30" fill="{GR}">неделя 12</text></svg>'''
sl[4] = zone(4, 17, 'Вы бросаете в первые 2 месяца', '4–8 недель без результата, и вот уже <span class="y">«это не для меня».</span>', ill, top=720)
roots = ''.join(f'<path d="M540,330 Q{540+dx},{380+dy//2} {540+dx*1.6:.0f},{330+dy}" fill="none" stroke="#B08A3E" stroke-width="{w}" stroke-linecap="round"/>' for dx, dy, w in [(-160, 220, 8), (-70, 260, 7), (0, 280, 9), (80, 250, 7), (170, 210, 8), (-230, 150, 5), (240, 140, 5)])
ill = f'''<svg width="1080" height="640" style="position:absolute;top:90px;left:0">
<rect x="80" y="330" width="920" height="300" rx="20" fill="rgba(176,138,62,.12)"/>
<line x1="80" y1="330" x2="1000" y2="330" stroke="#B08A3E" stroke-width="4"/>{roots}
<path d="M540,330 L540,270" stroke="#3BA776" stroke-width="10" stroke-linecap="round"/><path d="M540,285 Q500,255 480,270 Q505,295 540,285" fill="#3BA776"/>
<text x="110" y="300" font-family="S" font-weight="800" font-size="34" fill="#fff">видно: почти ничего</text>
<text x="110" y="610" font-family="S" font-weight="800" font-size="34" fill="{Y}">не видно: корни, навык, доверие</text></svg>'''
sl[5] = why(5, 'Вы уходите, пока растут корни', 'Деньги приходят после накопления действий и доверия. <span class="y">Вы уходите за шаг до первого результата.</span>', ill, top=760)

# 18 — окружение
ill = quotes([('В нашем-то возрасте?', -2, 'margin-right:200px'), ('Это всё инфоцыгане', 2, 'margin-left:180px'), ('Лучше держись за работу', -1, 'margin-right:80px;margin-left:60px')])
sl[6] = zone(6, 18, 'Окружение тянет вас назад', 'Родные и знакомые сомневаются вслух. <span class="y">Каждый день по капле.</span>', ill, top=700)
ill = f'''<div style="position:absolute;top:180px;left:0;right:0;display:flex;justify-content:center;align-items:center;gap:20px">
<div style="width:560px;height:250px;border-radius:40px;border:8px solid #fff;padding:16px;box-sizing:border-box;display:flex"><div style="width:15%;background:{R};border-radius:22px"></div></div>
<div style="width:34px;height:110px;border-radius:0 14px 14px 0;background:#fff"></div>
<div style="font-weight:800;font-size:110px;color:{R};margin-left:30px">15%</div></div>'''
sl[7] = why(7, 'Силы уходят на споры', 'Вместо того чтобы делать, вы оправдываетесь. <span class="y">Энергия кончается раньше, чем появляется результат.</span>', ill, top=660)

# 19 — обжёгся
rec = ''.join(f'<div style="display:flex;justify-content:space-between;border-bottom:2px dashed #D9CFBB;padding:16px 0;font-weight:700;font-size:36px;color:{NV}"><span>{a}</span><span style="color:#C0392B;font-weight:800">{b}</span></div>' for a, b in [('Курс «Доход онлайн»', '✗'), ('Марафон «Миллион»', '✗'), ('Крипто-проект', '✗'), ('«Пассивный доход»', '✗')])
ill = f'''<div style="position:absolute;top:130px;left:200px;right:200px;background:#F6F1E6;border-radius:18px;padding:26px 44px;box-shadow:0 30px 70px rgba(0,0,0,.45);transform:rotate(1.5deg)">
<div style="font-weight:800;font-size:30px;letter-spacing:4px;color:#8A7A5A">МОЙ ОПЫТ ОНЛАЙН</div>{rec}</div>
<div style="position:absolute;top:540px;left:300px;transform:rotate(-8deg);border:8px solid {R};color:{R};border-radius:18px;padding:10px 30px;font-weight:800;font-size:64px;background:rgba(8,20,40,.35)">НЕ СРАБОТАЛО</div>'''
sl[8] = zone(8, 19, 'Вы обожглись и закрылись', 'Курсы без результата, пирамиды, обман. <span class="y">Теперь вы не верите никому.</span>', ill, top=720)
ill = f'''<svg width="1080" height="600" style="position:absolute;top:110px;left:0" fill="none" stroke="#3A4E73" stroke-width="10" stroke-linecap="round">
<path d="M140,80 H940 V520 H140 Z M140,180 H760 M320,180 V420 M320,420 H620 M620,280 V520 M480,280 H860 M860,280 V420 M140,320 H220"/>
<path d="M180,130 H700 V230 H260 V370 H560 V470 H700" stroke="{R}" stroke-width="8" stroke-dasharray="14 12"/>
<circle cx="700" cy="470" r="22" fill="{R}" stroke="none"/>
<text x="940" y="575" text-anchor="end" font-family="S" font-weight="800" font-size="34" fill="{GR}" stroke="none">годы проб и ошибок</text></svg>'''
sl[9] = why(9, 'Вы годами ищете путь в одиночку', 'Или не вкладываетесь вовсе и учитесь методом проб, или снова выбираете <span class="y">самое громкое и дешёвое.</span>', ill, top=720)

# 20 — поздно
ill = f'''<div style="position:absolute;top:150px;left:0;right:0;text-align:center">
<div style="font-weight:800;font-size:280px;line-height:1;color:#fff">45+</div>
<div style="display:inline-block;margin-top:20px;transform:rotate(-4deg);background:{R};color:#fff;font-weight:800;font-size:64px;padding:10px 36px;border-radius:14px">«уже поздно?»</div></div>'''
sl[10] = zone(10, 20, 'Вы думаете, что уже поздно', 'Возраст кажется приговором. <span class="y">«Вот если бы лет 10 назад…»</span>', ill, top=720)
nodes = [('«поздно»', 540, 120, R), ('вполсилы', 830, 420, SKY), ('слабый результат', 250, 420, GR)]
n = ''.join(f'<div style="position:absolute;left:{x-170}px;top:{y-50}px;width:340px;text-align:center;border-radius:50px;border:4px solid {c};background:#0E2244;padding:20px 0;font-weight:800;font-size:38px">{t}</div>' for t, x, y, c in nodes)
ill = f'''<svg width="1080" height="600" style="position:absolute;top:110px;left:0"><circle cx="540" cy="320" r="230" fill="none" stroke="{Y}" stroke-width="6" stroke-dasharray="18 14"/></svg>
<div style="position:absolute;top:110px;left:0;right:0;height:600px">{n}</div>'''
sl[11] = why(11, 'Вы играете вполсилы', 'Решения откладываются, всё «на пробу». <span class="y">И слабый результат подтверждает «поздно».</span>', ill, top=760)

sl[12] = personal(12)
sl[13] = cta_opyt(13)
render(sl, os.path.abspath('out_sz4')); print('ok')
