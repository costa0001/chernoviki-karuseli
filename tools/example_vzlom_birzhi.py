from gendesign import *
N=15; R='#FF6B6B'
def ex(i,k,kind,name,year,amount,what,clients,icon):
    col=SKY if kind=='криптобиржа' else Y
    return S(i,N,f'''<div style="position:absolute;top:120px;left:72px;right:72px;display:flex;justify-content:space-between;align-items:center">
<div class="tag" style="color:#9AA6B8">пример {k} из 10</div>
<div style="font-weight:800;font-size:28px;padding:10px 22px;border-radius:30px;border:2px solid {col};color:{col}">{kind}</div></div>
<div style="position:absolute;top:210px;left:72px;right:72px;display:flex;align-items:center;gap:34px">
<div style="width:170px;height:170px;border-radius:40px;background:rgba(255,107,107,.12);border:3px solid {R};display:flex;align-items:center;justify-content:center;font-size:96px;flex:none">{icon}</div>
<div><div style="font-weight:800;font-size:76px;line-height:1">{name}</div><div style="font-family:L;font-style:italic;font-size:46px;color:#9AA6B8;margin-top:10px">{year}</div></div></div>
<div style="position:absolute;top:440px;left:72px;right:72px;font-weight:800;font-size:{110 if len(amount)<14 else 86}px;color:{Y};line-height:1">{amount}</div>
<div class="p" style="position:absolute;top:600px;left:72px;right:72px;margin:0">{what}</div>
<div style="position:absolute;left:72px;right:72px;bottom:90px;border-radius:26px;background:rgba(255,107,107,.1);border:2px solid {R};padding:30px 34px">
<div style="font-weight:800;font-size:28px;letter-spacing:3px;color:{R}">ЧТО С ДЕНЬГАМИ КЛИЕНТОВ</div>
<div style="font-weight:600;font-size:40px;line-height:1.3;margin-top:12px">{clients}</div></div>''')
sl={}
coins=''.join(f'<g transform="translate({x},{y}) rotate({r})" opacity="{o}"><circle r="{rad}" fill="#F5A623" stroke="#FFD27A" stroke-width="5"/><text y="{rad*0.36}" text-anchor="middle" font-family="S" font-weight="800" font-size="{rad*1.05}" fill="#7A4A00">₿</text></g>' for x,y,r,rad,o in [(830,150,18,46,.9),(950,300,-12,34,.75),(700,80,-25,28,.6),(980,120,30,24,.5),(610,250,10,22,.45)])
sl[1]=S(1,N,f'''<svg width="1080" height="700" style="position:absolute;top:60px;left:0">
<defs><radialGradient id="gl" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#F5C542" stop-opacity=".55"/><stop offset="1" stop-color="#F5C542" stop-opacity="0"/></radialGradient>
<linearGradient id="cg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FFD978"/><stop offset=".55" stop-color="#F5A623"/><stop offset="1" stop-color="#B86E00"/></linearGradient></defs>
<circle cx="440" cy="360" r="330" fill="url(#gl)"/>
<g transform="translate(440,360)">
<circle r="230" fill="#7A4A00"/><circle r="222" fill="url(#cg)" transform="translate(-8,-10)"/>
<circle r="180" fill="none" stroke="#FFE7A8" stroke-width="6" stroke-dasharray="4 14" transform="translate(-8,-10)"/>
<text x="-8" y="70" text-anchor="middle" font-family="S" font-weight="800" font-size="240" fill="#8A5200">₿</text>
<path d="M-60,-232 L-10,-120 L-70,-40 L20,40 L-30,120 L30,232" fill="none" stroke="#0A1730" stroke-width="22" stroke-linejoin="round"/>
<path d="M-60,-232 L-10,-120 L-70,-40 L20,40 L-30,120 L30,232" fill="none" stroke="{R}" stroke-width="6" stroke-linejoin="round"/></g>
{coins}
<g transform="translate(70,40)"><rect width="300" height="64" rx="32" fill="rgba(255,107,107,.15)" stroke="{R}" stroke-width="3"/>
<circle cx="36" cy="32" r="10" fill="{R}"/><text x="58" y="43" font-family="S" font-weight="800" font-size="30" fill="{R}">ВЗЛОМ · 29.10</text></g></svg>
<div class="txt" style="top:720px">
<div style="font-weight:800;font-size:44px;letter-spacing:3px;color:#C9D3E3">ХАКЕРЫ</div>
<div style="font-weight:800;font-size:150px;line-height:.95;color:{R};letter-spacing:2px;text-shadow:0 2px 0 #C94848,0 4px 0 #B03C3C,0 6px 0 #962F2F,0 8px 0 #7C2424,0 10px 0 #631B1B,0 22px 30px rgba(0,0,0,.6)">УКРАЛИ</div>
<div style="font-weight:800;font-size:132px;line-height:1.05;color:{Y};margin-top:8px;text-shadow:0 2px 0 #D9A72E,0 4px 0 #BF9126,0 6px 0 #A57B1E,0 8px 0 #8B6616,0 10px 0 #70510F,0 22px 30px rgba(0,0,0,.6)">6,3 МЛРД $</div>
<div class="p" style="margin-top:22px;font-size:40px">у крупнейшей криптобиржи мира. И это не первый раз</div></div>''')
tl=''.join(f'<div style="display:flex;gap:28px;align-items:flex-start;margin-top:{0 if j==0 else 26}px"><div style="width:26px;height:26px;border-radius:50%;background:{c};margin-top:12px;flex:none;box-shadow:0 0 18px {c}"></div><div><div style="font-weight:800;font-size:34px;color:{c}">{d}</div><div style="font-weight:600;font-size:38px;line-height:1.25;margin-top:4px">{t}</div></div></div>' for j,(d,t,c) in enumerate([('29 октября 2026','Хакеры заходят в систему Binance',R),('20 минут','Выводят около 6,3 млрд $',R),('В тот же день','Биржа останавливает торги и вывод денег',Y),('1 ноября','Вывод средств постепенно возобновляют',SKY)]))
sl[2]=S(2,N,f'''<div class="txt" style="top:120px"><div class="tag">что случилось</div><h1>Крупнейшая кража в истории крипты</h1></div>
<div style="position:absolute;top:470px;left:72px;right:72px;border-left:4px solid #3A4E73;padding-left:30px">{tl}</div>
<div class="p" style="position:absolute;left:72px;right:72px;bottom:80px;margin:0;font-size:38px">Путь внутрь, по данным биржи, начался с <span class="y">фейкового собеседования</span> с её сотрудником.</div>''')
E=[('криптобиржа','Bybit','февраль 2025','~1,5 млрд $','Хакеры, которых ФБР связало с Северной Кореей, увели эфир из кошелька биржи.','Биржа закрыла дыру займами и своими средствами. Клиенты пережили панику и очередь на вывод.','💻'),
('криптобиржа','Mt. Gox','2014','~850 000 BTC','Крупнейшая биржа биткоина своего времени объявила, что монеты клиентов пропали.','Биржа обанкротилась. Первые выплаты клиенты начали получать только в 2024 году, через 10 лет.','⛔'),
('криптобиржа','Bitfinex','август 2016','119 756 BTC','Хакеры вывели биткоины клиентов с кошельков биржи.','Убыток разложили на всех: балансы клиентов урезали примерно на 36%.','✂️'),
('криптобиржа','Coincheck','январь 2018','~530 млн $','Украли токены NEM, которые хранились в «горячем» кошельке, подключённом к интернету.','Вывод средств остановили. Компенсацию клиенты получили только примерно через полтора месяца.','🔥'),
('криптобиржа','Binance','май 2019','7 000 BTC','Хакеры получили ключи доступа и вывели биткоины одной операцией.','Вывод заморозили примерно на неделю. Убыток покрыли из резервного фонда биржи.','🔑'),
('криптобиржа','FTX','ноябрь 2022','заморожено всё','Одна из крупнейших бирж мира рухнула за несколько дней. В ночь банкротства с неё ещё и украли около 477 млн $.','Вывод закрыли в один день. Деньги клиентов застряли в процедуре банкротства на годы.','🧊'),
('криптобиржа','DMM Bitcoin','май 2024','4 502 BTC','Японская биржа потеряла биткоины после взлома.','Биржа не пережила взлом: в том же году объявила о закрытии и передаче счетов другой компании.','🚪'),
('криптобиржа','WazirX','июль 2024','~230 млн $','Крупнейшую биржу Индии взломали через кошелёк с несколькими подписями.','Вывод средств заморозили на многие месяцы, клиентам предложили схему с частичным возвратом.','🔒'),
('банк','ЦБ Бангладеш','февраль 2016','81 млн $','Хакеры через систему SWIFT отправили поддельные переводы со счёта банка в Нью-Йорке. Пытались вывести около 1 млрд $.','Даже деньги государства в центральном банке оказались не защищены.','🏦'),
('банк','Кипр','март 2013','до 47,5% вкладов','Это не хакеры. Банки закрыли почти на две недели, а крупные вклады принудительно «стрижнули» ради спасения системы.','Вкладчики Bank of Cyprus потеряли до 47,5% суммы свыше 100 000 €.','🏛')]
for k,e in enumerate(E,1): sl[k+2]=ex(k+2,k,*e)
sl[13]=S(13,N,f'''<svg width="1080" height="560" style="position:absolute;top:100px;left:0">
<rect x="140" y="120" width="320" height="320" rx="40" fill="none" stroke="#3A4E73" stroke-width="6"/><text x="300" y="315" text-anchor="middle" font-size="140">🏦</text>
<text x="300" y="500" text-anchor="middle" font-family="S" font-weight="800" font-size="34" fill="#9AA6B8">ЧУЖОЙ СЕЙФ</text>
<path d="M500,280 L590,280" stroke="{R}" stroke-width="8" stroke-dasharray="14 10"/><text x="545" y="250" text-anchor="middle" font-size="56" fill="{R}">✕</text>
<rect x="630" y="120" width="320" height="320" rx="40" fill="rgba(245,197,66,.1)" stroke="{Y}" stroke-width="6"/><text x="790" y="315" text-anchor="middle" font-size="140">🧠</text>
<text x="790" y="500" text-anchor="middle" font-family="S" font-weight="800" font-size="34" fill="{Y}">ВАШИ НАВЫКИ</text></svg>
<div class="txt" style="top:700px"><div class="tag">вывод</div><h1>Если деньги не у вас</h1>
<div class="p">они в любой момент могут стать <span class="y">не вашими.</span> Биржа, банк, государство: решение принимают другие, а не вы.</div></div>''')
steps=''.join(f'<div style="flex:1;border-radius:26px;border:2px solid {c};background:rgba(255,255,255,.04);padding:30px 20px;text-align:center"><div style="font-size:70px">{e}</div><div style="font-weight:800;font-size:34px;margin-top:12px">{t}</div></div>' for e,t,c in [('📚','Опыт','#3A4E73'),('🛠','Навык',SKY),('💶','Доход',Y)])
sl[14]=S(14,N,f'''<div style="position:absolute;top:150px;left:72px;right:72px;display:flex;gap:22px;align-items:center">{steps}</div>
<div class="txt" style="top:520px"><div class="tag">что делать</div><h1>Самая надёжная защита это вы сами</h1>
<div class="p">Научитесь <span class="y">самостоятельно обеспечивать</span> своё финансовое благополучие. Навык зарабатывать нельзя взломать, заморозить или отнять.</div></div>''')
sl[15]=S(15,N,f'''<div class="txt" style="top:0;bottom:70px;display:flex;flex-direction:column;justify-content:center;text-align:center">
<div class="tag">28 лет в бизнесе</div>
<h1 style="font-size:66px;text-transform:none;margin-top:20px">Я выгружаю свой<br>бизнес-опыт <span class="it" style="font-size:78px">на платформу</span></h1>
<div class="p" style="margin-top:34px">Напишите слово, и я пришлю ссылку, чтобы присоединиться. <span class="y">Забрать этот опыт можно только сейчас.</span></div>
<div style="margin-top:50px;background:{Y};color:{NV};padding:34px 20px;border-radius:18px;box-shadow:0 0 60px rgba(245,197,66,.35)"><div style="font-weight:800;font-size:90px;line-height:1;white-space:nowrap">Пишите «КЛУБ» &darr;</div><div style="font-weight:600;font-size:38px;margin-top:12px">в комментариях</div></div></div>''',last=True)
render(sl,os.path.abspath('prodH')); print('ok')
