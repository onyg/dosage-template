import os
import json
import pytest
from liquid import Environment, FileSystemLoader

def render_dosage(dosage_json, template_path):
    env = Environment(loader=FileSystemLoader(os.path.dirname(template_path)))
    template = env.get_template(os.path.basename(template_path))
    return template.render({"dosage": dosage_json}).strip()

@pytest.fixture
def template_path():
    return os.path.abspath("templates/dosage.liquid")

@pytest.mark.parametrize("example_file, expected_text", [
    ("examples/Dosage-1000.json", "täglich — je 1 Stück — morgens"),
    ("examples/Dosage-1010-Unsorted.json", "täglich — je 1 Stück — morgens und abends"),
    ("examples/Dosage-1010.json", "täglich — je 1 Stück — morgens und abends"),
    ("examples/Dosage-1111.json", "täglich — je 1 Stück — morgens, mittags, abends und nachts"),
    ("examples/Dosage-1t.json", "Donnerstag — je 1 Stück"),
    ("examples/Dosage-2t.json", "Montag — je 2 Stück"),
    ("examples/Dosage-UnitMg-1000.json", "täglich — je 400 mg — morgens"),
    ("examples/Dosage-comb-dayofweek-1.json", "Montag und Freitag — je 1 Stück — morgens und abends"),
    ("examples/Dosage-interval-2d-bound.json", "alle 2 Tage — je 2 Stück — für 6 Woche(n)"),
    ("examples/Dosage-interval-2wk.json", "alle 2 Wochen — je 1 Stück"),
    ("examples/Dosage-interval-3d.json", "alle 3 Tage — je 1 Stück"),
    ("examples/Dosage-interval-4times-d.json", "viermal täglich — je 1 Stück"),
    ("examples/Dosage-interval-8d.json", "alle 8 Tage — je 1 Stück"),
    ("examples/Dosage-tod-1t-8am.json", "täglich — je 1 Stück — um 08:00 Uhr"),
    ("examples/Dosage-tod-2-12am.json", "täglich — je 2 Stück — um 12:00 Uhr"),
    ("examples/Dosage-tod-unsorted.json", "täglich — je 1 Stück — um 08:00 Uhr, 08:35 Uhr, 15:00 Uhr"),
    ("examples/Dosage-weekday-2t-bound.json", "Montag — je 2 Stück — für 10 Woche(n)"),
    ("examples/Dosage-weekday-2t.json", "Dienstag und Donnerstag — je 2 Stück"),
    ("examples/Dosage-weekday-3t.json", "Dienstag, Donnerstag und Samstag — je 2 Stück"),
    ("examples/Dosage-weekday-unsorted.json", "Montag, Dienstag, Donnerstag und Freitag — je 2 Stück"),
])
def test_render_dosage(example_file, expected_text, template_path):
    with open(example_file, encoding="utf-8") as f:
        data = json.load(f)
    result = render_dosage(data, template_path)
    assert expected_text == result