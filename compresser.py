import os
from PIL import Image

# Dossier à parcourir
img_dir = "img/preview"
# Taille max en Ko (par exemple 500 Ko)
MAX_SIZE_KO = 500
# Largeur max en pixels (optionnel)
MAX_WIDTH = 1920

for root, dirs, files in os.walk(img_dir):
    for f in files:
        if f.lower().endswith(('.jpg', '.jpeg', '.png')):
            path = os.path.join(root, f)
            size_ko = os.path.getsize(path) // 1024
            if size_ko > MAX_SIZE_KO:
                print(f"Compression de {path} ({size_ko} Ko)")
                img = Image.open(path)
                # Redimensionne si trop large
                if img.width > MAX_WIDTH:
                    ratio = MAX_WIDTH / img.width
                    new_size = (MAX_WIDTH, int(img.height * ratio))
                    img = img.resize(new_size, Image.LANCZOS)
                # Sauvegarde en JPEG compressé (qualité 85)
                img.save(path, optimize=True, quality=85)