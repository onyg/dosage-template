#!/bin/bash


EXAMPLES_DIR="./examples"

if [ ! -d "$EXAMPLES_DIR" ]; then
    echo "Verzeichnis '$EXAMPLES_DIR' nicht gefunden!"
    exit 1
fi

for file in "$EXAMPLES_DIR"/*.json; do
    echo "➤ Verarbeite Datei: $file"

    # dosage-to-text.py ausführen
    python ./hl7/dosage-to-text.py "$file"

    # # render.py ausführen
    # python ./python/render.py "$file"

    echo "----------------------------------------------------------------"
    echo " "
done


