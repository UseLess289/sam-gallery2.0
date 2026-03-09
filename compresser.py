import os
from PIL import Image

img_dir = "img/preview"
MAX_SIZE_KO = 500
MAX_WIDTH = 1920

for root, dirs, files in os.walk(img_dir):
    for f in files:
        if f.lower().endswith(('.jpg', '.jpeg', '.png')):
            path = os.path.join(root, f)
            size_ko = os.path.getsize(path) // 1024
            if size_ko > MAX_SIZE_KO:
                print(f"Compression de {path} ({size_ko} Ko)")
                img = Image.open(path)
                if img.width > MAX_WIDTH:
                    ratio = MAX_WIDTH / img.width
                    new_size = (MAX_WIDTH, int(img.height * ratio))
                    img = img.resize(new_size, Image.LANCZOS)
                img.save(path, optimize=True, quality=85)