from gendesign import *
N=9
R='#FF6B6B'
def card(t,extra=''):
    return f'<div style="background:#F6F1E6;color:{NV};border-radius:18px;padding:22px 28px;font-weight:700;font-size:30px;line-height:1.3;box-shadow:0 14px 40px rgba(0,0,0,.35);{extra}">{t}</div>'
sl={}
sl[1]=cover(SH+'e_cover.jpg','center 22%','Наступает эра <span class="y">анти-контента</span>','Опытные авторы уже перестроились. Готовые советы больше не собирают подписчиков',N)
sl[2]=S(2,N,f'''<div style="position:absolute;top:200px;left:110px;right:110px;display:flex;align-items:center;justify-content:center;gap:26px">
{card('Зацепить внимание')}<div style="font-size:60px;color:#9AA6B8">→</div>{card('Дать готовый ответ')}</div>
<div style="position:absolute;top:262px;left:90px;width:900px;height:10px;background:{R};transform:rotate(-6deg);border-radius:5px;box-shadow:0 0 22px rgba(255,107,107,.6)"></div>
<div style="position:absolute;top:420px;left:0;right:0;text-align:center;font-weight:800;font-size:38px;letter-spacing:6px;color:{R}">СТАРАЯ ФОРМУЛА</div>
<div class="txt" style="top:640px"><div class="tag">что изменилось</div><h1>Старая формула больше не работает</h1>
<div class="p">Люди устали не от контента. А от ощущения, что их снова <span class="y">сравнивают с чужим идеалом.</span></div></div>''')
posts=''.join(f'<div style="flex:1;border-radius:22px;background:rgba(255,255,255,.06);border:2px solid #3A4E73;padding:22px;opacity:{o}"><div style="font-weight:800;font-size:30px">Вот 3 совета</div><div style="height:12px;background:#3A4E73;border-radius:6px;margin-top:16px"></div><div style="height:12px;width:80%;background:#3A4E73;border-radius:6px;margin-top:12px"></div><div style="height:12px;width:60%;background:#3A4E73;border-radius:6px;margin-top:12px"></div></div>' for o in (1,.7,.45))
sl[3]=S(3,N,f'''<div style="position:absolute;top:140px;left:72px;right:72px">
<div style="display:flex;justify-content:flex-end"><div style="background:{SKY};color:{NV};font-weight:700;font-size:30px;padding:16px 26px;border-radius:26px 26px 6px 26px">Дай советы по теме</div></div>
<div style="display:flex;margin-top:18px"><div style="background:#1E2C48;font-weight:600;font-size:30px;padding:16px 26px;border-radius:26px 26px 26px 6px">🤖 Готово. Вот 3 совета...</div></div>
<div style="display:flex;gap:20px;margin-top:40px">{posts}</div></div>
<div class="txt" style="top:700px"><div class="tag">ИИ изменил правила</div><h1>Советы теперь даёт нейросеть</h1>
<div class="p">За секунду и каждому. Поэтому на тех, кто просто раздаёт готовые ответы, <span class="y">подписываются всё реже.</span></div></div>''')
lines=[('День 1','Я заметил, что...'),('День 2','Я начал...'),('День 3','Я попробовал...')]
diary=''.join(f'<div style="display:flex;gap:22px;align-items:baseline;border-bottom:2px solid #D9CFBB;padding:18px 0"><div style="font-family:L;font-style:italic;font-weight:700;font-size:30px;color:#B08A3E;width:120px">{d}</div><div style="font-family:L;font-style:italic;font-size:36px;color:{NV}">{t}</div></div>' for d,t in lines)
sl[4]=S(4,N,f'''<div style="position:absolute;top:130px;left:150px;right:150px;background:#F6F1E6;border-radius:18px;padding:40px 50px 30px 70px;box-shadow:0 30px 70px rgba(0,0,0,.45);transform:rotate(-2deg)">
<div style="position:absolute;left:34px;top:0;bottom:0;width:4px;background:#E7A0A0"></div>
<div style="font-weight:800;font-size:28px;letter-spacing:4px;color:#8A7A5A">ДНЕВНИК ПУТИ</div>{diary}</div>
<div class="txt" style="top:720px"><div class="tag">новый подход</div><h1>Дневник вашего пути</h1>
<div class="p">Люди идут за теми, кто проходит тот же путь, что и они. <span class="y">Доверие рождается в самом процессе.</span></div></div>''')
sl[5]=S(5,N,f'''<div style="position:absolute;top:170px;left:90px;right:90px;display:flex;justify-content:space-between;align-items:center">
<div style="position:relative;width:360px;height:300px;border-radius:40px;border:3px solid #3A4E73;display:flex;flex-direction:column;align-items:center;justify-content:center"><div style="font-size:110px">🎥</div><div style="font-weight:800;font-size:30px;color:{R}">● REC 12 ч</div>
<div style="position:absolute;top:48%;left:-5%;width:110%;height:9px;background:{R};transform:rotate(-20deg);border-radius:5px"></div></div>
<div style="width:380px;height:300px;border-radius:150px 150px 150px 30px;background:{Y};color:{NV};display:flex;align-items:center;justify-content:center;text-align:center;font-weight:800;font-size:36px;line-height:1.25;padding:30px">Мысли вслух,<br>которые<br>уже есть</div></div>
<div class="txt" style="top:640px"><div class="tag">что это НЕ значит</div><h1>Не нужно снимать весь день</h1>
<div class="p">Достаточно вслух проговорить то, о чём вы уже думаете, что замечаете, где застряли. <span class="y">Придумывать ничего не нужно.</span></div></div>''')
tiles=''.join(f'<div style="border-radius:28px;background:rgba(255,255,255,.05);border:2px solid {c};padding:30px;height:180px;display:flex;flex-direction:column;justify-content:space-between"><div style="font-size:54px">{e}</div><div style="font-weight:800;font-size:36px">{t}</div></div>' for e,t,c in [('🔭','Взгляд со стороны',SKY),('💭','Размышления',SKY),('🧭','Своя точка зрения',SKY),('⭐','Реальный опыт',Y)])
sl[6]=S(6,N,f'''<div style="position:absolute;top:140px;left:72px;right:72px;display:grid;grid-template-columns:1fr 1fr;gap:24px">{tiles}</div>
<div class="txt" style="top:700px"><div class="tag">что ценно сейчас</div><h1>От автора ждут живой опыт</h1>
<div class="p">Не готовые решения, а ваш взгляд на жизнь, ваши выводы и <span class="y">то, что вы прошли сами.</span></div></div>''')
bars=''.join(f'<div style="display:flex;flex-direction:column;align-items:center;gap:14px"><div style="width:150px;height:{h}px;border-radius:20px 20px 6px 6px;background:{c}"></div><div style="font-weight:800;font-size:34px">{a}</div></div>' for a,h,c in [('40+',180,'#2C4A7A'),('50+',270,'#3E67A8'),('60+',360,SKY),('70+',450,Y)])
sl[7]=S(7,N,f'''<div style="position:absolute;top:130px;left:0;right:0;display:flex;justify-content:center;align-items:flex-end;gap:40px;height:540px">{bars}</div>
<div class="txt" style="top:720px"><div class="tag">ваше преимущество</div><h1>Ваш опыт не заменит ИИ</h1>
<div class="p">В 40, 50, 60 лет у вас за плечами то, чего нет ни у одной нейросети: <span class="y">прожитая жизнь.</span> Именно это сейчас и ценят.</div></div>''')
steps=''.join(f'<circle cx="{120+k*190}" cy="{430-k*60}" r="34" fill="{NV}" stroke="{SKY}" stroke-width="5"/><text x="{120+k*190}" y="{441-k*60}" text-anchor="middle" font-family="S" font-weight="800" font-size="30" fill="#fff">{k+1}</text>' for k in range(5))
sl[8]=S(8,N,f'''<svg width="1080" height="600" style="position:absolute;top:110px;left:0">
<path d="M120,430 L310,370 L500,310 L690,250 L880,190" fill="none" stroke="{SKY}" stroke-width="6" stroke-dasharray="16 12"/>{steps}
<line x1="960" y1="70" x2="960" y2="200" stroke="#fff" stroke-width="6"/><path d="M960,70 L1040,95 L960,120 Z" fill="{Y}"/>
<text x="960" y="250" text-anchor="middle" font-family="S" font-weight="800" font-size="34" fill="{Y}">ЦЕЛЬ</text></svg>
<div class="txt" style="top:720px"><div class="tag">но есть условие</div><h1>У дневника должна быть цель</h1>
<div class="p">Без направления дневник превращается в рассказ ни о чём. <span class="y">Путь к вашей цели и есть лучший контент.</span></div></div>''')
sl[9]=cta(9,N,'Поставьте цель, и ваш путь к ней станет контентом, за которым пойдут люди.')
render(sl,os.path.abspath('prodE')); print('ok')
