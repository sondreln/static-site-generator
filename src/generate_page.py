import os
from markdown_blocks import markdown_to_html_node, extract_title

def generate_page(basepath, from_path, template_path, dest_path) -> None:
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, encoding="utf-8") as f:
        markdown = f.read()

    with open(template_path, encoding="utf-8") as f:
        template = f.read()

    html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    page = template.replace("{{ Title }}", title).replace("{{ Content }}", html).replace('href="/', f'href="{basepath}').replace('src="/', f'src="{basepath}')

    dest_dir = os.path.dirname(dest_path)
    if dest_dir:
        os.makedirs(dest_dir, exist_ok=True)
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(page)

def generate_pages_recursive(basepath, dir_path_content, template_path, dest_dir_path) -> None:
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            if from_path.endswith(".md"):
                generate_page(basepath, from_path, template_path, dest_path[:-3] + ".html")
        else:
            generate_pages_recursive(basepath, from_path, template_path, dest_path)