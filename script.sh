# Renommer toutes les extensions en minuscules (récursif)
find . -name '*.*' | while read f; do
  ext="${f##*.}"
  lower_ext=$(echo "$ext" | tr '[:upper:]' '[:lower:]')
  if [ "$ext" != "$lower_ext" ]; then
    mv "$f" "${f%.*}.$lower_ext"
  fi
done
