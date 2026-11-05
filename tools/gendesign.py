import os, sys, math
from playwright.sync_api import sync_playwright
I='/usr/share/fonts/opentype/inter/'; G='/usr/share/fonts/truetype/google-fonts/'
SH=os.path.abspath('sharp')+'/'  # папка с подготовленными фото обложек
Y='#F5C542'; NV='#0E2244'; SKY='#6FB7FF'
CSS=f'''@font-face{{font-family:S;font-weight:800;src:url(file://{I}Inter-ExtraBold.otf)}}
@font-face{{font-family:S;font-weight:600;src:url(file://{I}Inter-SemiBold.otf)}}
@font-face{{font-family:L;src:url(file://{G}Lora-Variable.ttf);font-weight:400 700}}
@font-face{{font-family:L;font-style:italic;src:url(file://{G}Lora-Italic-Variable.ttf);font-weight:400 700}}
body{{margin:0}} .s{{width:1080px;height:1350px;position:relative;overflow:hidden;font-family:S;color:#fff;background:#0A1730}}
.bg{{position:absolute;inset:0;background:radial-gradient(900px 600px at 85% 8%,rgba(111,183,255,.18),transparent 60%),radial-gradient(800px 700px at 0% 100%,rgba(245,197,66,.12),transparent 60%),linear-gradient(180deg,#0E2244,#081428)}}
.grid{{position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.035) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.035) 1px,transparent 1px);background-size:60px 60px}}
.top{{position:absolute;top:44px;left:72px;right:72px;display:flex;justify-content:space-between;font-size:26px;color:#9AA6B8;font-weight:600;z-index:3}}
.tag{{font-weight:800;font-size:30px;letter-spacing:4px;color:{Y};text-transform:uppercase}}
h1{{font-weight:800;font-size:72px;line-height:1.06;margin:14px 0 0;text-transform:uppercase}}
.p{{font-weight:600;font-size:44px;line-height:1.32;margin-top:30px;color:#E6ECF5}}
.y{{background:{Y};color:{NV};padding:0 10px;border-radius:6px;-webkit-box-decoration-break:clone;box-decoration-break:clone}}
.it{{font-family:L;font-style:italic;color:{Y}}}
.txt{{position:absolute;left:72px;right:72px;z-index:2}}'''
def S(i,N,inner,last=False): return f'<div class="s"><div class="bg"></div><div class="grid"></div><div class="top"><span>@bravo.konstantin</span><span>{i} / {N}{"" if last else " &rarr;"}</span></div>{inner}</div>'
def render(sl,OUT):
    os.makedirs(OUT,exist_ok=True)
    with sync_playwright() as p:
        b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1350})
        for k in sorted(sl):
            open(f'{OUT}/_t.html','w').write(f'<html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{sl[k]}</body></html>')
            pg.goto(f'file://{OUT}/_t.html'); pg.wait_for_timeout(300); pg.screenshot(path=f'{OUT}/slide_{k:02d}.png')
        b.close()
    from PIL import Image
    ims=[Image.open(f'{OUT}/slide_{k:02d}.png').resize((300,375)) for k in sorted(sl)]
    n=len(ims); cols=5; rows=(n+cols-1)//cols
    sh=Image.new('RGB',(310*cols,385*rows),'#777')
    for j,im in enumerate(ims): sh.paste(im,((j%cols)*310,(j//cols)*385))
    sh.save(f'{OUT}/sheet.png')
def cover(img,pos,title,sub,N):
    return S(1,N,f'''<img src="file://{img}" style="position:absolute;top:0;left:0;width:1080px;height:760px;object-fit:cover;object-position:{pos}">
<div style="position:absolute;top:520px;left:0;right:0;height:260px;background:linear-gradient(180deg,rgba(10,23,48,0),#0A1730)"></div>
<div class="txt" style="top:700px;bottom:90px;display:flex;flex-direction:column;justify-content:center"><h1 style="font-size:76px">{title}</h1><div class="p">{sub}</div></div>''')
def cta(i,N,line,word='ЦЕЛИ',tag='бесплатно · 5 дней',title='Практикум',product='«Воплощение целей»',days_tiles=True):
    days=''.join(f'<div style="flex:1;border:2px solid rgba(245,197,66,.6);border-radius:18px;padding:18px 0;text-align:center;background:rgba(255,255,255,.04)"><div style="font-size:24px;color:#9AA6B8;font-weight:600">день</div><div style="font-weight:800;font-size:58px;color:{Y if d==1 else "#fff"}">{d}</div></div>' for d in range(1,6))
    return S(i,N,f'''<div class="txt" style="top:0;bottom:70px;display:flex;flex-direction:column;justify-content:center;text-align:center">
<div class="tag">{tag}</div>
<h1 style="font-size:68px;text-transform:none;margin-top:20px">{title}<br><span class="it" style="font-size:84px">{product}</span></h1>
{('<div style="display:flex;gap:14px;margin-top:44px">'+days+'</div>') if days_tiles else ""}
<div class="p" style="margin-top:34px">{line}</div>
<div style="margin-top:40px;background:{Y};color:{NV};padding:34px 20px;border-radius:18px;box-shadow:0 0 60px rgba(245,197,66,.35)"><div style="font-weight:800;font-size:86px;line-height:1;white-space:nowrap">Пишите «{word}» &darr;</div><div style="font-weight:600;font-size:38px;margin-top:12px">в комментариях</div></div></div>''',last=True)
