import os
import shutil

from sys import argv
from copystatic import copy_files_recursive
from gencontent import generate_pages_recursive


dir_path_static = "./static"
dir_path_docs = "./docs"
dir_path_content = "./content"
template_path = "./template.html"


def main():
    basepath = "/"
    if len(argv) > 0:
        basepath = argv[1]

    print("Deleting public directory...")
    if os.path.exists(dir_path_docs):
        shutil.rmtree(dir_path_docs)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_docs)

    print("Generating content...")
    generate_pages_recursive(dir_path_content, template_path, dir_path_docs, basepath)


main()
