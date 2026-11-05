# PNG-слайды из render() -> JPG в папку репозитория.
# python3 tools/to_jpg.py <папка_png> <папка_репо>
import sys, glob, os
from PIL import Image
src, dst = sys.argv[1], sys.argv[2]; os.makedirs(dst, exist_ok=True)
for f in sorted(glob.glob(src + '/slide_*.png')):
    Image.open(f).convert('RGB').save(os.path.join(dst, os.path.basename(f)[:-4] + '.jpg'), quality=93)
