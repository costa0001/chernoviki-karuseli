import sys
sys.path.insert(0, '/home/claude/work')
from szlib import *

out = {}

# ===== 1. Доказываете опыт =====
n = 11; sl = {}
sl[1] = cover_polaroid(SH + 'c_k1.jpg', 'center 20%', n,
    'Чем больше вы доказываете опыт, <span class="y">тем меньше платят</span>', 'Неудобная правда для тех, кому за 40', sticker='20 лет стажа!', rot=-4, side='left')
ill = f'''<div style="position:absolute;top:120px;left:130px;right:130px">
{card("🎓 Диплом с отличием", "transform:rotate(-2deg);margin-right:200px")}
{card("📜 Сертификат №14", "transform:rotate(2deg);margin-top:24px;margin-left:220px")}
{card("💼 20 лет в профессии", "transform:rotate(-1deg);margin-top:24px;margin-right:120px")}
{card("🏆 Руководил отделом", "transform:rotate(1.5deg);margin-top:24px;margin-left:120px")}</div>'''
sl[2] = txt(2, 'Знакомо?', 'Дипломы, стаж, должности. Вы выкладываете всё это, <span class="y">чтобы вам поверили.</span>', ill, top=760, n=n)
ill = two('ВЫ ПОКАЗЫВАЕТЕ', 'резюме', 'дипломы, годы, должности', 'ЧЕЛОВЕК ДУМАЕТ', '«а мне?»', 'это поможет именно мне?', top=150, lc=SKY, rc=Y)
sl[3] = txt(3, 'Клиенту не нужны регалии', 'Ему нужен его результат. Ваше резюме он пролистывает, <span class="y">свою проблему он читает.</span>', ill, top=660, n=n)
ill = f'<div style="position:absolute;top:200px;left:120px;right:120px">{bubble("Поверьте, я правда эксперт! У меня 20 лет опыта!", me=True, extra="font-size:40px")}{bubble("Хм... а почему вы так стараетесь?", extra="font-size:40px")}</div>'
sl[4] = txt(4, 'Доказательство звучит как оправдание', 'Чем громче «поверьте мне», <span class="y">тем меньше доверия.</span> Уверенным не нужно доказывать.', ill, top=700, n=n)
ill = f'''<div style="position:absolute;top:130px;left:110px;right:110px">
<div style="border-radius:24px;border:3px solid {R};background:rgba(255,107,107,.08);padding:26px 30px"><div style="font-weight:800;font-size:30px;color:{R}">✗ ТАК</div><div style="font-weight:700;font-size:38px;margin-top:10px">«У меня 20 лет опыта в бухгалтерии»</div></div>
<div style="border-radius:24px;border:3px solid {Y};background:rgba(245,197,66,.1);padding:26px 30px;margin-top:26px"><div style="font-weight:800;font-size:30px;color:{Y}">✓ ТАК</div><div style="font-weight:700;font-size:38px;margin-top:10px">«Помогу за месяц разобраться с налогами в новой стране»</div></div></div>'''
sl[5] = txt(5, 'Говорите о его жизни, а не о своей карьере', 'Тот же опыт. Но во второй фразе <span class="y">человек видит себя.</span>', ill, top=700, n=n)
steps = ''.join(f'<div style="flex:1;border-radius:26px;background:rgba(255,255,255,.05);border:3px solid {c};padding:30px 20px;text-align:center"><div style="font-weight:800;font-size:34px;color:{c}">{a}</div><div style="font-weight:600;font-size:32px;margin-top:14px;line-height:1.3">{b}</div></div>' for a, b, c in [('БЫЛО', 'что мешало человеку', GR), ('СДЕЛАЛИ', 'какой шаг вместе', SKY), ('СТАЛО', 'что изменилось', Y)])
ill = f'<div style="position:absolute;top:200px;left:90px;right:90px;display:flex;gap:24px">{steps}</div>'
sl[6] = txt(6, 'Показывайте опыт историями', 'Формула простая: <span class="y">было, сделали, стало.</span> Одна такая история сильнее десяти дипломов.', ill, top=680, n=n)
ill = cards_list([('📌', 'Шапка профиля: 1 строка', SKY), ('⭐', 'Хайлайтс «Обо мне»', SKY), ('📝', 'Лента: истории людей', Y)], top=170)
sl[7] = txt(7, 'Регалиям место в шапке', 'Одной строки хватит. А в ленте <span class="y">пусть говорят результаты людей.</span>', ill, top=680, n=n)
ill = f'<div style="position:absolute;top:150px;left:0;right:0;text-align:center"><div style="font-weight:800;font-size:200px;line-height:1;color:{Y}">45+</div><div style="font-weight:800;font-size:46px;margin-top:24px">это не стаж в резюме</div><div style="font-weight:800;font-size:46px;color:{SKY};margin-top:8px">это сотни решённых задач</div></div>'
sl[8] = txt(8, 'Ваш возраст это козырь', 'Только показывайте его <span class="y">через задачи, которые вы решали,</span> а не через годы.', ill, top=740, n=n)
sl[9] = big_center(9, '🔄', 'Перестаньте доказывать. Начните показывать.', 'Не «кто я», а <span class="y">«что изменится у вас».</span>', n=n)
sl[10] = personal2(10, 'Я начинал онлайн с нуля', 'После 28 лет в бизнесе, в 52 года, в новой стране.', n=n)
sl[11] = cta2(11, 'Хотите понять, какой результат из <span class="it" style="font-size:78px">вашего опыта</span> нужен людям?', 'Разберётесь за 2 минуты.', n=n)
out['k1'] = sl

# ===== 2. Идеальным не доверяют =====
n = 10; sl = {}
sl[1] = cover_full(SH + 'c_k2.jpg', 'center 85%', 'Честный разговор', 'Идеальным<br><span class="y" style="white-space:nowrap">не доверяют</span>', 'Почему ошибки продают лучше побед').replace('1 / 13', '1 / 10')
icons = ''.join(f'<div style="width:240px;height:240px;border-radius:20px;background:#1E2C48;display:flex;align-items:center;justify-content:center;font-size:90px">{e}</div>' for e in ['🏆', '✨', '💎', '🥂', '🚀', '✅'])
ill = f'<div style="position:absolute;top:110px;left:150px;right:150px;display:flex;flex-wrap:wrap;gap:20px;justify-content:center">{icons}</div>'
sl[2] = txt(2, 'Только победы. Ни одной ошибки', 'Безупречные фото, успешный успех. Кажется, <span class="y">так выглядит эксперт.</span>', ill, top=760, n=n)
ill = f'''<svg width="1080" height="600" style="position:absolute;top:110px;left:0">
<rect x="430" y="140" width="220" height="380" rx="10" fill="#2C4A7A"/><circle cx="540" cy="90" r="46" fill="{Y}"/><rect x="505" y="135" width="70" height="10" fill="{Y}"/>
{''.join(f'<circle cx="{x}" cy="500" r="26" fill="#3A4E73"/>' for x in [120, 200, 280, 800, 880, 960])}
<text x="540" y="580" text-anchor="middle" font-family="S" font-weight="800" font-size="36" fill="{GR}">далеко и непонятно</text></svg>'''
sl[3] = txt(3, 'Идеальный образ отталкивает', 'Тому, у кого не бывает неудач, не верят. И <span class="y">не узнают в нём себя.</span>', ill, top=740, n=n)
ill = cards_list([('📉', 'Не купил акции Google, Apple и биткоин по 1 $', R), ('🚲', 'Вложил 50 000 $ в чужой стартап электровелосипедов. Он обанкротился из-за войны', R)], top=170, size=36)
sl[4] = txt(4, 'Мои ошибки', 'Я мог купить и не купил. Я вложил и <span class="y">потерял всё полностью.</span>', ill, top=720, n=n)
ill = two('ОШИБКИ', '50&nbsp;000&nbsp;$', 'потеряно в чужом стартапе', 'ТЕ ЖЕ ГОДЫ', '×10 и ×14', 'лучшие проекты', top=150, lc=R, rc=Y).replace('font-size:84px', 'font-size:62px')
sl[5] = txt(5, 'Ошибки были платой за вход', 'Кто не рискует, <span class="y">не получает ни того, ни другого.</span>', ill, top=660, n=n)
ill = f'''<svg width="1080" height="560" style="position:absolute;top:130px;left:0">
<line x1="160" y1="430" x2="920" y2="430" stroke="#3A4E73" stroke-width="6"/>
<circle cx="380" cy="230" r="70" fill="{SKY}"/><rect x="320" y="310" width="120" height="120" rx="30" fill="{SKY}"/>
<circle cx="700" cy="230" r="70" fill="{Y}"/><rect x="640" y="310" width="120" height="120" rx="30" fill="{Y}"/>
<text x="380" y="500" text-anchor="middle" font-family="S" font-weight="800" font-size="36" fill="#fff">вы</text><text x="700" y="500" text-anchor="middle" font-family="S" font-weight="800" font-size="36" fill="#fff">он</text></svg>'''
sl[6] = txt(6, 'Ошибка ставит вас рядом', 'Человек видит: <span class="y">«он тоже был там, где я».</span> С этого начинается доверие.', ill, top=740, n=n)
ill = cards_list([('1️⃣', 'Что пробовали и не вышло', SKY), ('2️⃣', 'Что поняли', SKY), ('3️⃣', 'Что делаете иначе сейчас', Y)], top=170)
sl[7] = txt(7, 'Как рассказывать об ошибке', 'Три шага. Тогда это <span class="y">не жалоба, а опыт.</span>', ill, top=680, n=n)
ill = cards_list([('✗', 'Жалобы без вывода', R), ('✗', 'Чужие ошибки и сплетни', R), ('✗', 'То, что вредит клиентам', R)], top=170)
sl[8] = txt(8, 'Что показывать не стоит', 'Честность это не исповедь. <span class="y">Ошибка нужна ради урока.</span>', ill, top=680, n=n)
sl[9] = big_center(9, '🪞', 'Ваши ошибки уже стали опытом', 'Осталось <span class="y">показать его людям,</span> которые сейчас там, где были вы.', n=n)
sl[10] = cta2(10, 'Хотите понять, сколько стоит <span class="it" style="font-size:78px">ваш опыт?</span>', 'Вместе со всеми ошибками. За 2 минуты.', n=n)
out['k2'] = sl

# ===== 3. Об этом рассказали тысячи =====
n = 10; sl = {}
sl[1] = cover_split(SH + 'c_k3.jpg', 'center 30%', n, 'для тех, кто молчит', 'Об этом рассказали тысячи. <span class="y">Но не вы</span>', 'Почему «всё уже сказано» это неправда')
ill = quotes([('Об этом уже все всё сказали', -2, 'margin-right:160px'), ('Кому интересно ещё одно мнение?', 2, 'margin-left:140px'), ('Есть эксперты и получше меня', -1, 'margin-right:80px;margin-left:40px')])
sl[2] = txt(2, 'Знакомые мысли?', 'И вы снова откладываете <span class="y">первый пост.</span>', ill, top=740, n=n)
ill = f'<div style="position:absolute;top:150px;left:0;right:0;text-align:center"><div style="font-weight:800;font-size:220px;line-height:1;color:{R}">0</div><div style="font-weight:800;font-size:44px;margin-top:20px">постов · клиентов · евро</div></div>'
sl[3] = txt(3, 'Так вы не начинаете вообще', 'Пока вы молчите, люди учатся <span class="y">у тех, кто говорит.</span> Даже если знают меньше вас.', ill, top=720, n=n)
dots = ''.join(f'<circle cx="{170+(j%14)*53}" cy="{150+(j//14)*53}" r="18" fill="{Y if j == 61 else "#3A4E73"}"/>' for j in range(98))
ill = f'<svg width="1080" height="560" style="position:absolute;top:100px;left:0">{dots}</svg>'
sl[4] = txt(4, 'Слышат от ста. Внедряют от одного', 'Одну и ту же мысль человек слышит десятки раз. А делает, <span class="y">когда её скажет «свой» человек.</span>', ill, top=740, n=n)
sl[5] = big_center(5, '🧭', 'Люди приходят не за информацией', 'Информации и так слишком много. Они приходят <span class="y">за человеком.</span>', n=n)
ill = f'<div style="position:absolute;top:170px;left:90px;right:90px;text-align:center">{chip("ваш возраст")}{chip("ваш переезд", Y)}{chip("ваша профессия")}{chip("ваш язык")}{chip("ваши ошибки", Y)}{chip("ваша семья")}</div>'
sl[6] = txt(6, 'Ваш угол уже есть', 'То, что вы прошли, <span class="y">никто не расскажет за вас.</span>', ill, top=700, n=n)
ill = two('БЛОГЕР 25 ЛЕТ', '«Как вести бюджет»', '', 'ВЫ, 50+', '«Бюджет семьи после переезда»', '', top=150, lc=GR, rc=Y).replace('font-size:84px', 'font-size:50px')
sl[7] = txt(7, 'Та же тема. Другой человек', 'И ровесники выбирают того, <span class="y">кто прошёл их путь.</span>', ill, top=660, n=n)
ill = cards_list([('❓', 'Что вы прошли сами?', SKY), ('❓', 'Кому вы помогли бы 5 лет назад?', SKY), ('❓', 'Что вас злит в чужих советах?', Y)], top=170)
sl[8] = txt(8, 'Как найти свой угол', 'Ответьте честно на три вопроса. <span class="y">Ответы и есть ваша тема.</span>', ill, top=680, n=n)
sl[9] = personal2(9, 'Про онлайн до меня тоже рассказали тысячи', 'Но я начал в 52 года, в новой стране. И говорил с теми, кто там же.', n=n)
sl[10] = cta2(10, 'Хотите найти, что в <span class="it" style="font-size:78px">вашем опыте</span> не расскажет никто другой?', 'Разберётесь за 2 минуты.', n=n)
out['k3'] = sl

# ===== 4. Блог это 6 профессий =====
n = 10; sl = {}
sl[1] = cover_polaroid(SH + 'c_k4.jpg', 'center 18%', n,
    'Блог это 6 профессий. <span class="y">И вы удивляетесь усталости?</span>', 'Что можно не делать самому', sticker='маркетолог? монтажёр?')
roles = ''.join(f'<div style="width:270px;height:200px;border-radius:24px;background:rgba(255,255,255,.05);border:2px solid #3A4E73;display:flex;flex-direction:column;align-items:center;justify-content:center"><div style="font-size:70px">{e}</div><div style="font-weight:800;font-size:32px;margin-top:8px">{t}</div></div>' for e, t in [('📊', 'Маркетолог'), ('✍️', 'Копирайтер'), ('🎨', 'Дизайнер'), ('🎬', 'Монтажёр'), ('🎤', 'Оратор'), ('📈', 'Аналитик')])
ill = f'<div style="position:absolute;top:120px;left:100px;right:100px;display:flex;flex-wrap:wrap;gap:22px;justify-content:center">{roles}</div>'
sl[2] = txt(2, 'Вы ведёте блог сами', 'Значит, вы одновременно <span class="y">шесть специалистов.</span> Каждый день.', ill, top=760, n=n)
ill = two('КАЖДОЙ РОЛИ', 'годы', 'люди учатся профессионально', 'ВЫ ЖДЁТЕ', '2 месяца', 'и уже результат', top=150, lc=SKY, rc=R)
sl[3] = txt(3, 'И ждёте результата за 2 месяца', 'А потом ругаете себя: <span class="y">«у меня не получается».</span>', ill, top=660, n=n)
ill = f'''<div style="position:absolute;top:200px;left:0;right:0;display:flex;justify-content:center;align-items:center;gap:20px">
<div style="width:560px;height:250px;border-radius:40px;border:8px solid #fff;padding:16px;box-sizing:border-box;display:flex"><div style="width:10%;background:{R};border-radius:22px"></div></div>
<div style="width:34px;height:110px;border-radius:0 14px 14px 0;background:#fff"></div></div>'''
sl[4] = txt(4, 'Вы не ленивы. Вы перегружены', 'Шесть ролей на одном человеке. <span class="y">Выгорание здесь закономерно.</span>', ill, top=700, n=n)
ill = cards_list([('✍️', 'Тексты и подписи', SKY), ('💡', 'Идеи и сценарии', SKY), ('🎨', 'Обложки', SKY), ('📈', 'Разбор цифр', SKY)], top=120)
sl[5] = txt(5, 'Что можно отдать ИИ', 'Черновики, идеи, рутина. <span class="y">ИИ делает это за минуты.</span>', ill, top=740, n=n)
ill = cards_list([('🙂', 'Ваше лицо и голос', Y), ('🧠', 'Ваш опыт и истории', Y), ('🤝', 'Общение с людьми', Y)], top=170)
sl[6] = txt(6, 'Что оставить себе', 'То, за что вам доверяют. <span class="y">Этого ИИ не заменит.</span>', ill, top=680, n=n)
ill = two('РАНЬШЕ', '10 часов', 'в день на контент', 'СЕЙЧАС', '≈ 1 час', 'с командой ИИ-сотрудников', top=160)
sl[7] = txt(7, 'Мои цифры', 'Я раньше тратил на контент 10 часов в день. <span class="y">Сейчас около часа.</span>', ill, top=660, n=n)
ill = cards_list([('1', 'Неделя 1: тексты через ИИ', SKY), ('2', 'Неделя 2: идеи и сценарии', SKY), ('3', 'Неделя 3: обложки', SKY), ('4', 'Неделя 4: разбор цифр', Y)], top=120)
sl[8] = txt(8, 'Начните с одной роли', 'Не всё сразу. <span class="y">Одна роль в неделю,</span> и через месяц вы дышите свободнее.', ill, top=740, n=n)
sl[9] = big_center(9, '⏳', 'Освободите время для главного', 'Для людей и для <span class="y">своего опыта.</span> Остальное делегируйте.', n=n)
sl[10] = cta2(10, 'Хотите понять, как превратить <span class="it" style="font-size:78px">ваш опыт</span> в доход без шести профессий?', 'Разберётесь за 2 минуты.', n=n)
out['k4'] = sl

# ===== 5. Клиент покупает себя через 3 месяца =====
n = 10; sl = {}
sl[1] = cover_full(SH + 'c_k5.jpg', 'center 80%', 'Про продажи без давления', 'Клиент покупает<br>не курс, а себя<br><span class="y" style="white-space:nowrap">через 3 месяца</span>', 'Как это использовать').replace('1 / 13', '1 / 10')
ill = cards_list([('📚', '8 модулей', GR), ('🎥', '24 видеоурока', GR), ('🎁', '3 бонуса', GR), ('💬', 'Чат поддержки', GR)], top=120)
sl[2] = txt(2, 'Вы рассказываете программу', 'Модули, уроки, бонусы. <span class="y">А человек зевает.</span>', ill, top=740, n=n)
sl[3] = big_center(3, '😐', 'В программе он себя не видит', 'Он видит работу, которую надо сделать. <span class="y">А не жизнь, которую получит.</span>', n=n)
ill = f'''<svg width="1080" height="580" style="position:absolute;top:110px;left:0">
<ellipse cx="560" cy="230" rx="330" ry="170" fill="#1E2C48" stroke="{Y}" stroke-width="6"/>
<circle cx="300" cy="440" r="30" fill="#1E2C48" stroke="{Y}" stroke-width="5"/><circle cx="250" cy="510" r="18" fill="#1E2C48" stroke="{Y}" stroke-width="4"/>
<text x="560" y="210" text-anchor="middle" font-family="S" font-weight="800" font-size="44" fill="#fff">«Я уже получаю</text><text x="560" y="270" text-anchor="middle" font-family="S" font-weight="800" font-size="44" fill="{Y}">свои 500 € в месяц»</text></svg>'''
sl[4] = txt(4, 'Желание купить рождается здесь', 'В момент, когда человек <span class="y">представил свой результат.</span>', ill, top=740, n=n)
ill = two('БЫЛО', 'страх', '«проедаю подушку, опыт не нужен»', 'СТАЛО', 'опора', '«свой доход из того, что я умею»', top=150, lc=GR, rc=Y).replace('font-size:84px', 'font-size:70px')
sl[5] = txt(5, 'Нарисуйте «было» и «стало»', 'Словами человека, а не своими. <span class="y">Так, чтобы он узнал себя.</span>', ill, top=660, n=n)
ill = cards_list([('💶', 'Что изменится в деньгах?', SKY), ('❤️', 'Что изменится в чувствах?', SKY), ('☀️', 'Как пройдёт обычный день?', Y)], top=170)
sl[6] = txt(6, 'Три вопроса для картинки', 'Ответьте за клиента. <span class="y">Это и есть ваш главный текст.</span>', ill, top=680, n=n)
ill = f'''<div style="position:absolute;top:130px;left:110px;right:110px">
<div style="border-radius:24px;border:3px solid {R};background:rgba(255,107,107,.08);padding:26px 30px"><div style="font-weight:800;font-size:30px;color:{R}">✗ ПРОЦЕСС</div><div style="font-weight:700;font-size:38px;margin-top:10px">«Курс из 8 модулей по созданию онлайн-продукта»</div></div>
<div style="border-radius:24px;border:3px solid {Y};background:rgba(245,197,66,.1);padding:26px 30px;margin-top:26px"><div style="font-weight:800;font-size:30px;color:{Y}">✓ РЕЗУЛЬТАТ</div><div style="font-weight:700;font-size:38px;margin-top:10px">«Через 3 месяца вы знаете, кому и за сколько продавать свой опыт»</div></div></div>'''
sl[7] = txt(7, 'Одна фраза, два мира', 'Первая про вашу работу. <span class="y">Вторая про его жизнь.</span>', ill, top=700, n=n)
sl[8] = big_center(8, '⚠️', 'Но не обещайте чудо', 'Картинка должна быть честной. <span class="y">Доверие дороже одной продажи.</span>', n=n)
sl[9] = personal2(9, 'Я начинал онлайн с нуля', 'В 52 года, после переезда в Швейцарию.', n=n)
sl[10] = cta2(10, 'Хотите увидеть, какой результат может дать <span class="it" style="font-size:78px">ваш опыт?</span>', 'Разберётесь за 2 минуты.', n=n)
out['k5'] = sl

for k, s in out.items():
    render(s, os.path.abspath(f'/home/claude/chernoviki-karuseli/out_{k}'))
print('ok')
