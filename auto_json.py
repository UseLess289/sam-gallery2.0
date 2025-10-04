import os
import json

img_dir = "img/preview"
output = []

# Parcours tous les sous-dossiers (tags)
for root, dirs, files in os.walk(img_dir):
    tag = os.path.relpath(root, img_dir)
    if tag == ".":
        tag = "misc"
    for f in files:
        if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp')):
            path = os.path.join(root, f).replace("\\", "/")
            output.append({
                "filename": path,
                "tag": tag
            })

# Tri optionnel par nom de fichier
output.sort(key=lambda x: x["filename"])

with open("photos.json", "w") as json_file:
    json.dump(output, json_file, indent=4)

