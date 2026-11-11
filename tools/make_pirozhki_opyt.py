import sys
sys.path.insert(0, '/home/claude/work')
from szlib import *

FB = '/home/claude/chernoviki-karuseli/foto-baza/2026-10-zheneva/'


def polaroid(img, pos, x, y, w, h, rot, cap=''):
    c = f'<div style="font-family:S;font-weight:700;font-size:30px;color:{NV};text-align:center;margin-top:14px">{cap}</div>' if cap else ''
    return f'''<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;background:#F6F1E6;padding:18px 18px {26 if cap else 18}px;border-radius:6px;transform:rotate({rot}deg);box-shadow:0 30px 70px rgba(0,0,0,.55)">
<img src="file://{img}" style="width:{w-36}px;height:{h}px;object-fit:cover;object-position:{pos};display:block">{c}</div>'''


def txt(i, title, text, ill='', top=700, tag=None):
    t = f'<div class="tag">{tag}</div>' if tag else ''
    return S(i, N, f'''{ill}<div class="txt" style="top:{top}px">{t}<h1 style="margin-top:{20 if tag else 0}px">{title}</h1><div class="p">{text}</div></div>''')


def bubble(t, me=False, extra=''):
    if me:
        return f'<div style="display:flex;justify-content:flex-end;margin-top:20px"><div style="background:{SKY};color:{NV};font-weight:700;font-size:34px;padding:18px 28px;border-radius:28px 28px 6px 28px;max-width:640px;{extra}">{t}</div></div>'
    return f'<div style="display:flex;margin-top:20px"><div style="background:#1E2C48;font-weight:600;font-size:34px;padding:18px 28px;border-radius:28px 28px 28px 6px;max-width:680px;{extra}">{t}</div></div>'


sl = {}
# 1 — обложка: полароид + текст
sl[1] = f'''<div class="s">
<div class="top"><span>@bravo.konstantin</span><span>1 / {N} &rarr;</span></div>
{polaroid(SH + 'cover_pr.jpg', 'center 20%', 380, 110, 600, 640, 4)}
<div style="position:absolute;left:90px;top:170px;transform:rotate(-6deg);background:{Y};color:{NV};font-weight:800;font-size:34px;padding:12px 26px;border-radius:12px;box-shadow:0 14px 40px rgba(0,0,0,.4)">«Куда платить?!»</div>
<div class="txt" style="bottom:90px"><h1 style="font-size:76px">Можно ли сделать продукт, который <span class="y" style="white-space:nowrap">раскупают сами?</span></h1>
<div class="p" style="margin-top:22px">Без дожима, скидок и уговоров</div></div></div>'''

ill = f'''<div style="position:absolute;top:120px;left:120px;right:120px">
<div style="font-weight:800;font-size:30px;letter-spacing:4px;color:{GR}">ДИРЕКТ · 2 МИНУТЫ ПОСЛЕ СТОРИС</div>
{bubble("Куда платить? 🙏")}{bubble("Вы будто прочитали мои мысли!")}{bubble("Мне это нужно. Есть ссылка?")}</div>'''
sl[2] = txt(2, 'Представьте такую картину', 'Вы выложили сторис с анонсом, и в директ сразу летит: <span class="y">«Куда платить?»</span>', ill, top=720)

ill = f'''<div style="position:absolute;top:170px;left:90px;right:90px;text-align:center">{chip("дожим", R, "text-decoration:line-through")}{chip("скидка −70%", R, "text-decoration:line-through")}{chip("«последний шанс»", R, "text-decoration:line-through")}{chip("золотые горы", R, "text-decoration:line-through")}{chip("уговоры в личке", R, "text-decoration:line-through")}</div>'''
sl[3] = txt(3, 'Никого не надо уговаривать', 'Ни скидок, ни обещаний золотых гор. Люди <span class="y">сами просят ссылку.</span> Звучит заманчиво?', ill, top=700)

sl[4] = S(4, N, f'''<div class="txt" style="top:0;bottom:80px;display:flex;flex-direction:column;justify-content:center">
<div style="font-size:150px">🤫</div>
<h1 style="font-size:72px;margin-top:20px">Думаете, сейчас будет секретный инструмент?</h1>
<div class="p" style="font-size:48px;margin-top:30px">Нет. Всё гораздо <span class="y">проще и скучнее.</span></div></div>''')

ill = f'''<div style="position:absolute;top:130px;left:170px;right:170px;background:#F6F1E6;color:{NV};border-radius:22px;padding:34px 40px;box-shadow:0 30px 70px rgba(0,0,0,.45);transform:rotate(-1.5deg)">
<div style="font-weight:800;font-size:44px">Ирина, 47 · Германия</div>
<div style="font-weight:600;font-size:32px;line-height:1.5;margin-top:16px">Боится: «уже поздно начинать»<br>Хочет: свой доход в евро<br>Говорит: «я всё умею, но кому это нужно?»</div></div>
<svg width="260" height="260" style="position:absolute;top:420px;left:700px"><circle cx="110" cy="110" r="80" fill="none" stroke="{Y}" stroke-width="16"/><line x1="168" y1="168" x2="240" y2="240" stroke="{Y}" stroke-width="22" stroke-linecap="round"/></svg>'''
sl[5] = txt(5, 'Секрет: знать свою аудиторию', 'До мелочей. Что болит, чего боятся и <span class="y">какими словами</span> они об этом говорят.', ill, top=740)

ill = f'''<div style="position:absolute;top:150px;left:120px;right:120px">
{card("«Наверное, им нужен курс подлиннее»", "transform:rotate(-2deg);margin-right:120px")}
{card("«Я думаю, они хотят подешевле»", "transform:rotate(2deg);margin-top:26px;margin-left:160px")}
{card("«Мне кажется, это всем нужно»", "transform:rotate(-1deg);margin-top:26px;margin-right:60px")}</div>'''
sl[6] = txt(6, 'На догадках такой продукт не сделать', 'Если вы не знаете реальные боли людей и <span class="y">как они формулируют их у себя в голове.</span>', ill, top=760)

ill = two('В ОПРОСЕ', '87%', '«да, купил бы»', 'ОПЛАТИЛИ', '2 человека', 'когда дошло до денег', top=150, lc=SKY, rc=R)
sl[7] = txt(7, 'И опросы тут не спасут', 'Люди из вежливости говорят то, что вы хотите услышать. А когда доходит до оплаты, <span class="y">исчезают.</span>', ill, top=660)

ill = f'''<div style="position:absolute;top:110px;left:110px;right:110px;border-radius:30px;background:rgba(255,255,255,.04);border:2px solid #3A4E73;padding:26px 30px">
<div style="font-weight:800;font-size:32px;color:{GR}">💬 Чат «Наши в Мюнхене»</div>
{bubble("Уже год ищу работу по специальности, везде отказ 😔")}{bubble("Кто знает, как зарабатывать онлайн на русском?")}{bubble("Опыт 20 лет, а здесь я никто")}</div>'''
sl[8] = txt(8, 'Ищите там, где говорят без фильтра', 'Комментарии у коллег, чаты эмигрантов, форумы. Смотрите, <span class="y">какими словами люди жалуются,</span> когда им ничего не продают.', ill, top=720)

ill = f'''<div style="position:absolute;top:130px;left:120px;right:120px">
{bubble("Вот 30 фраз из чатов. Какие боли повторяются чаще всего?", me=True)}
{bubble("Три главные: страх «поздно», нет дохода в евро, опыт «не нужен» в новой стране. Вот как их назвать в посте...", extra="border:3px solid " + Y)}</div>'''
sl[9] = txt(9, 'Устройте мозговой штурм с ИИ', 'Отдайте ему собранные фразы. Он увидит закономерности, <span class="y">которые вы давно не замечаете.</span>', ill, top=700)

ill = two('ЛАЙКИ', '👏 120', 'всем понравилось', 'ОПЛАТЫ', '0 €', 'значит, идею в сторону', top=150, lc=SKY, rc=R)
sl[10] = txt(10, 'Проверяйте идею деньгами', 'Не пишите курс полгода в стол. Сначала продайте консультацию или маленький продукт. <span class="y">Хлопают, но не платят? Меняйте идею.</span>', ill, top=640)

ill = f'''<svg width="1080" height="600" style="position:absolute;top:110px;left:0">
<circle cx="400" cy="290" r="220" fill="rgba(107,184,255,.18)" stroke="{SKY}" stroke-width="6"/>
<circle cx="680" cy="290" r="220" fill="rgba(245,197,66,.18)" stroke="{Y}" stroke-width="6"/>
<text x="300" y="300" text-anchor="middle" font-family="S" font-weight="800" font-size="42" fill="#fff">ваш опыт</text>
<text x="790" y="300" text-anchor="middle" font-family="S" font-weight="800" font-size="42" fill="#fff">их боль</text>
<text x="540" y="282" text-anchor="middle" font-family="S" font-weight="800" font-size="40" fill="{Y}">ваш</text>
<text x="540" y="330" text-anchor="middle" font-family="S" font-weight="800" font-size="40" fill="{Y}">продукт</text></svg>'''
sl[11] = txt(11, 'Ваше главное преимущество', 'Вы сами из этой аудитории. Переезжали, начинали заново, искали доход. <span class="y">Вы знаете их боль изнутри.</span>', ill, top=720)

sl[12] = personal2(12, 'Я начинал так же', 'С нуля, в 52 года, в новой стране.')

sl[13] = S(13, N, f'''<div class="txt" style="top:0;bottom:70px;display:flex;flex-direction:column;justify-content:center;text-align:center">
<div class="tag">бесплатно · 2 минуты</div>
<h1 style="font-size:64px;text-transform:none;margin-top:24px;line-height:1.15">Хотите узнать, какой продукт можно сделать из <span class="it" style="font-size:78px">вашего опыта?</span></h1>
<div class="p" style="margin-top:40px">Разберётесь всего за 2 минуты.</div>
<div style="margin-top:50px;background:{Y};color:{NV};padding:36px 20px;border-radius:18px;box-shadow:0 0 60px rgba(245,197,66,.35)"><div style="font-weight:800;font-size:86px;line-height:1;white-space:nowrap">Пишите «ОПЫТ» &darr;</div><div style="font-weight:600;font-size:38px;margin-top:12px">в комментариях</div></div></div>''', last=True)

render(sl, os.path.abspath('out_pr')); print('ok')
