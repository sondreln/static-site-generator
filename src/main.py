import os
import sys
import shutil

from copystatic import copy_files_recursive
from generate_page import generate_pages_recursive

dir_path_static = "./static"
dir_path_docs = "./docs"
dir_path_content = "./content"


def main() -> None:
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"

    print("Deleting docs directory...")
    if os.path.exists(dir_path_docs):
        shutil.rmtree(dir_path_docs)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_docs)
    generate_pages_recursive(basepath, dir_path_content, "./template.html", dir_path_docs)


main()
