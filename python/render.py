import os
import json
import sys
from liquid import Environment, FileSystemLoader

def render_dosage(dosage_json, template_path="./templates/", template="dosage.liquid"):
    env = Environment(loader=FileSystemLoader(template_path))
    template = env.get_template(template)
    return template.render({"dosage": dosage_json})

def main():
    if len(sys.argv) != 2:
        print("Verwendung: python render_dosage.py <dosage.json>")
        sys.exit(1)

    with open(sys.argv[1], encoding="utf-8") as f:
        dosage = json.load(f)

    base_dir = os.path.dirname(os.path.abspath(__file__))
    template_path = os.path.join(base_dir, "..", "templates")
    result = render_dosage(dosage, template_path=template_path)
    print(result.strip())

if __name__ == "__main__":
    main()
