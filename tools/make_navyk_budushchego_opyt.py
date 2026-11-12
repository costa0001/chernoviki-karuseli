import sys
sys.path.insert(0, '/home/claude/work')
from szlib import *

n = 11; sl = {}
sl[1] = cover_full(SH + 'c_vang.jpg', 'center 85%', 'Совет Александра Ванга, миллиардера из ИИ',
                   'Он назвал<br>навык будущего.<br><span class="y" style="white-space:nowrap">Он нужен и вам</span>',
                   'Даже если вам 45 и вы не программист').replace('1 / 13', '1 / 11')

ill = f'''<div style="position:absolute;top:140px;left:150px;right:150px;border-radius:30px;background:rgba(255,255,255,.05);border:3px solid {Y};padding:40px 44px;text-align:center">
<div style="font-weight:800;font-size:34px;letter-spacing:4px;color:{GR}">АЛЕКСАНДР ВАНГ</div>
<div style="font-weight:800;font-size:150px;line-height:1.05;color:{Y};margin-top:10px">24 года</div>
<div style="font-weight:700;font-size:38px;margin-top:10px">первый миллиард, заработанный самому</div></div>'''
sl[2] = txt(2, 'Кто это сказал', 'Основатель Scale AI. Стал <span class="y">самым молодым миллиардером,</span> который заработал состояние сам.', ill, top=700, n=n)

ill = f'''<div style="position:absolute;top:150px;left:120px;right:120px;background:#F6F1E6;color:{NV};border-radius:22px;padding:44px 48px;box-shadow:0 30px 70px rgba(0,0,0,.45);transform:rotate(-1.5deg)">
<div style="font-weight:800;font-size:120px;line-height:.6;color:{Y}">“</div>
<div style="font-weight:800;font-size:50px;line-height:1.2">Если вам 13, тратьте всё время на вайб-кодинг</div>
<div style="font-weight:600;font-size:30px;color:#8A7A5A;margin-top:24px">подкаст TBPN, 2025</div></div>'''
sl[3] = txt(3, 'Его совет подросткам', 'Он сравнил этот момент с появлением первых компьютеров: <span class="y">кто рос рядом с ними, получил огромную фору.</span>', ill, top=720, n=n)

ill = f'''<div style="position:absolute;top:130px;left:120px;right:120px">
{bubble("Сделай мне простой калькулятор стоимости моих услуг", me=True)}
{bubble("Готово. Вот страница: вводите часы, получаете цену в евро. Открыть?", extra="border:3px solid " + Y)}</div>'''
sl[4] = txt(4, 'Что такое вайб-кодинг', 'Вы не пишете программу руками. Вы <span class="y">объясняете ИИ обычными словами,</span> что нужно, и он делает сам.', ill, top=700, n=n)

ill = cards_list([('🎯', 'Поставить задачу', SKY), ('🔍', 'Проверить результат', SKY), ('✅', 'Довести до рабочего вида', Y)], top=170)
sl[5] = txt(5, 'Дело не в коде', 'Ценится не знание языка программирования, а умение <span class="y">ставить задачу и доводить до результата.</span>', ill, top=680, n=n)

ill = two('В 13 ЛЕТ', 'время', 'свободные вечера', 'В 45+', 'опыт', 'вы знаете, что нужно людям', top=150, lc=SKY, rc=Y)
sl[6] = txt(6, 'Это работает в любом возрасте', 'У подростков больше времени. Но у вас есть то, <span class="y">чего нет у них.</span>', ill, top=660, n=n)

ill = f'''<div style="position:absolute;top:210px;left:0;right:0;display:flex;justify-content:center;align-items:center;gap:26px">
<div style="width:250px;height:250px;border-radius:50%;background:rgba(245,197,66,.15);border:5px solid {Y};display:flex;align-items:center;justify-content:center;font-weight:800;font-size:46px">опыт</div>
<div style="font-weight:800;font-size:90px">+</div>
<div style="width:250px;height:250px;border-radius:50%;background:rgba(107,184,255,.15);border:5px solid {SKY};display:flex;align-items:center;justify-content:center;font-weight:800;font-size:46px">ИИ</div>
<div style="font-weight:800;font-size:90px">=</div>
<div style="font-weight:800;font-size:56px;color:{Y}">доход</div></div>'''
sl[7] = txt(7, 'Лучше всех задачу ставит тот, кто её знает', 'После 20 лет в профессии вы точно знаете, что нужно клиенту. <span class="y">ИИ сделает остальное.</span>', ill, top=720, n=n)

ill = cards_list([('1', 'Откройте ChatGPT или Claude в браузере', SKY), ('2', 'Опишите задачу из своей работы обычными словами', SKY), ('3', 'Попросите объяснять каждый шаг', Y)], top=150, size=34)
sl[8] = txt(8, 'Три шага на этот вечер', 'Ничего устанавливать не нужно. <span class="y">Начните с одной задачи.</span>', ill, top=720, n=n)

ill = f'''<div style="position:absolute;top:130px;left:110px;right:110px;border-radius:26px;background:#1E2C48;border:3px solid {Y};padding:34px 40px">
<div style="display:inline-block;background:{Y};color:{NV};font-weight:800;font-size:28px;padding:6px 18px;border-radius:8px">ПРИМЕР ЗАПРОСА</div>
<div style="font-weight:600;font-size:36px;line-height:1.4;margin-top:22px">«Я 20 лет работаю бухгалтером и живу в Германии. Помоги описать мою услугу для русскоязычных так, чтобы было понятно, какой результат они получат. Объясняй каждый шаг»</div></div>'''
sl[9] = txt(9, 'Ваш первый запрос', 'Подставьте свою профессию и страну. <span class="y">Через 10 минут у вас будет черновик.</span>', ill, top=760, n=n)

sl[10] = personal2(10, 'Мне помогает команда ИИ-сотрудников', 'Раньше я тратил на контент 10 часов в день. Сейчас около часа.', n=n)
sl[11] = cta2(11, 'Хотите понять, что из <span class="it" style="font-size:78px">вашего опыта</span> можно превратить в доход с ИИ?', 'Разберётесь за 2 минуты.', n=n)

render(sl, os.path.abspath('/home/claude/chernoviki-karuseli/out_vang')); print('ok')
