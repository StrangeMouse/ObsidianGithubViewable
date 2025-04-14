import os
import json
import svgwrite
from cairosvg import svg2png
from tempfile import NamedTemporaryFile

TARGET_DIR = "path/to/your/folder"

def extract_excalidraw_json(md_file):
    with open(md_file, "r", encoding="utf-8") as f:
        content = f.read()

    start_tag = "```excalidraw"
    end_tag = "```"
    start = content.find(start_tag)
    end = content.find(end_tag, start + len(start_tag))

    if start == -1 or end == -1:
        print(f"[!] No Excalidraw content found in {md_file}")
        return None

    json_str = content[start + len(start_tag):end].strip()

    try:
        return json.loads(json_str)
    except json.JSONDecodeError:
        print(f"[!] Failed to parse JSON in {md_file}")
        return None

def draw_excalidraw_svg(data, output_svg_path):
    elements = data.get("elements", [])
    dwg = svgwrite.Drawing(output_svg_path, profile='tiny')

    for el in elements:
        if el.get("isDeleted"):
            continue
        x = el.get("x", 0)
        y = el.get("y", 0)
        width = el.get("width", 100)
        height = el.get("height", 100)
        stroke = el.get("strokeColor", "#000000")
        fill = el.get("backgroundColor", "none")

        if el["type"] == "rectangle":
            dwg.add(dwg.rect(insert=(x, y), size=(width, height), fill=fill, stroke=stroke))
        elif el["type"] == "ellipse":
            dwg.add(dwg.ellipse(center=(x + width/2, y + height/2), r=(width/2, height/2), fill=fill, stroke=stroke))
        elif el["type"] == "line" and "points" in el:
            abs_points = [(x + px, y + py) for px, py in el["points"]]
            dwg.add(dwg.polyline(points=abs_points, fill="none", stroke=stroke))
        elif el["type"] == "text":
            font_size = el.get("fontSize", 16)
            text = el.get("text", "")
            dwg.add(dwg.text(text, insert=(x, y + font_size), fill=stroke, font_size=font_size))

    dwg.save()

def convert_svg_to_png(svg_path, png_path):
    svg2png(url=svg_path, write_to=png_path)
    print(f"[✓] Saved PNG to {png_path}")

def process_file(md_path):
    data = extract_excalidraw_json(md_path)
    if not data:
        return

    # Output paths
    base = os.path.splitext(md_path)[0]
    svg_path = base + ".svg"
    png_path = base + ".png"

    # Create SVG
    draw_excalidraw_svg(data, svg_path)
    # Convert to PNG
    convert_svg_to_png(svg_path, png_path)
    # Optionally remove the SVG
    os.remove(svg_path)

def process_folder(folder_path):
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".excalidraw.md"):
                process_file(os.path.join(root, file))

if __name__ == "__main__":
    process_folder(TARGET_DIR)
