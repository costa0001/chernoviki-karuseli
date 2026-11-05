# Подготовка фото для обложки: ресайз до 1080 по ширине + лёгкая резкость, без фильтров.
# python3 tools/prep_photo.py foto-baza/2026-10-zheneva/g58_....jpg sharp/cover.jpg
import sys, os
from PIL import Image, ImageFilter
src, dst = sys.argv[1], sys.argv[2]
os.makedirs(os.path.dirname(dst) or '.', exist_ok=True)
im = Image.open(src).convert('RGB')
im = im.resize((1080, int(im.height*1080/im.width)), Image.LANCZOS).filter(ImageFilter.UnsharpMask(1.5, 80, 2))
im.save(dst, quality=95)
