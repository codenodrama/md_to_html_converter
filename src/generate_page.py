import os

from text_handler import *
from html import *

def generate_page(from_path, template_path, dest_path):
    open_from_path = open(os.path.join(from_path, 'index.md'), 'r')
    from_path_content = open_from_path.read()
    open_from_path.close()

    open_template_path = open(os.path.join(template_path, 'template.html'), 'r')
    template_path_content = open_template_path.read()
    open_template_path.close()

    content = markdown_to_html_node(from_path_content).to_html()
    title = extract_title(from_path_content)


    dest_path_content = template_path_content.replace('{{ Title }}', title).replace('{{ Content }}', content)
    with open(os.path.join(dest_path, 'index.html'), 'w') as f:
        f.write(dest_path_content)
        
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    content_dir_list = os.listdir(dir_path_content)
    for list_item in content_dir_list:
        if(os.path.isdir(os.path.join(dir_path_content, list_item))):
            new_dest_dir = os.path.join(dest_dir_path, list_item)
            os.makedirs(new_dest_dir)
            new_content_dir = os.path.join(dir_path_content, list_item)
            generate_pages_recursive(new_content_dir, template_path, new_dest_dir)
        elif(list_item[-3:] == ".md"):
            generate_page(dir_path_content, template_path, dest_dir_path)

    


