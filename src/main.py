from textnode import *
from copy_static import *
from text_handler import *
from generate_page import *

def main():
    src = '/home/lera_proxy/workspace/github.com/codenodrama/static_site_generator/static'
    dest = '/home/lera_proxy/workspace/github.com/codenodrama/static_site_generator/public'
    copy_static(src, dest)

    content_path = '/home/lera_proxy/workspace/github.com/codenodrama/static_site_generator/content'
    template_path = '/home/lera_proxy/workspace/github.com/codenodrama/static_site_generator'
    generate_pages_recursive(content_path, template_path, dest)

main()
