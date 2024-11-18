import re
from textnode import *
from htmlnode import *

def check_delimiter(delimiter):
    match delimiter:
        case '**':
            return TextType.BOLD
        case '*':
            return TextType.ITALIC
        case '`':
            return TextType.CODE
        case _:
            raise Exception("Invalid Markdown syntax.")
        

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if not node.text_type == 'text':
            new_nodes.append(node)
        else:
            blank_list = node.text.split(delimiter)
            for item in blank_list:
                item_list = []
                if(len(item) > 0 and not item == ' '):
                    if f"{delimiter}{delimiter}{item}{delimiter}{delimiter}" in node.text and not item[0] == " ":
                        item_list.append(TextNode(item, check_delimiter(f"{delimiter}{delimiter}")))
                    elif f"{delimiter}{item}{delimiter}" in node.text and not item[0] == " ":
                        item_list.append(TextNode(item, check_delimiter(f"{delimiter}")))
                    else:
                        item_list.append(TextNode(item, TextType.TEXT))
                    new_nodes.extend(item_list)
    return new_nodes

def extract_markdown_images(text):
    matches = re.findall(r"!+\[(.*?)\]+\((.*?)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]+\((.*?)\)", text)
    return matches

def extract_markdown_links_list(matches):
    result_arr = []
    for links in matches:
        value = links[0]
        link = links[1]
        result_arr.append([value, link])
    return result_arr

def extract_markdown_images_list(matches):
    result_arr = []
    for img in matches:
        value = img[0]
        link = img[1]
        result_arr.append([value, link])
    return result_arr

def split_one_node_link(original_text):
    result_arr = []
    link_arr = extract_markdown_links_list(extract_markdown_links(original_text))
    for link in link_arr:
        new_node = original_text.split(f"[{link[0]}]({link[1]})", 1)
        if(not new_node[0] == ''):
            result_arr.append(TextNode(new_node[0], TextType.TEXT))
        result_arr.append(TextNode(link[0], TextType.LINK, link[1]))
        original_text = "".join(new_node[1:])
        
    if(original_text):
        result_arr.append(TextNode(original_text, TextType.TEXT))

    return result_arr
    
def split_one_node_images(original_text):
    result_arr = []
    img_arr = extract_markdown_images_list(extract_markdown_images(original_text))
    for img in img_arr:
        new_node = original_text.split(f"![{img[0]}]({img[1]})", 1)
        if(not new_node[0] == ''):
            result_arr.append(TextNode(new_node[0], TextType.TEXT))
        result_arr.append(TextNode(img[0], TextType.IMAGE, img[1]))
        original_text = "".join(new_node[1:])
        
    if(original_text):
        result_arr.append(TextNode(original_text, TextType.TEXT))

    return result_arr

def split_nodes_links(old_nodes):
    result_nodes = []
    for node in old_nodes:
        if not node.text_type == 'text':
            result_nodes.append(node)
        elif(not node.text == ''):
            blank_nodes = split_one_node_link(node.text)
            result_nodes.extend(blank_nodes)
    return result_nodes

def split_nodes_images(old_nodes):
    result_nodes = []
    for node in old_nodes:
        if not node.text_type == 'text':
            result_nodes.append(node)
        elif not node.text == '':
            blank_nodes = split_one_node_images(node.text)
            result_nodes.extend(blank_nodes)
    return result_nodes
    
def text_to_textnodes(text):
    text_obj = TextNode(text, TextType.TEXT)
    result_node = split_nodes_images([text_obj])
    result_node = split_nodes_links(result_node)
    result_node = split_nodes_delimiter(result_node, '*', TextType.TEXT)
    result_node = split_nodes_delimiter(result_node, '`', TextType.TEXT)

    return result_node

def markdown_to_blocks(markdown):
    blank_list = markdown.splitlines()
    blank_str = ""
    block_list = []
    for block_item in blank_list:
        if(not block_item.strip()):
            block_list.append(blank_str)
            blank_str = ""
        else:
            res_str = block_item.strip()
            if(blank_str):
                blank_str += '\n'
            blank_str += res_str

    if(blank_str):
        block_list.append(blank_str)

    return block_list

def block_to_block_type(block):
    if block[0] == '#':
        return "heading"
    elif block[:3] == '```' and block[-3:] == '```':
        return "code"
    elif block[0] == '>' or block[:2] == '> ':
        blank_blocks = block.splitlines()
        blank_blocks = blank_blocks[1:]
        for blank_block in blank_blocks:
            if not blank_block[0] == '>' and not block[:2] == '> ':
                return 'paragraph'
        return 'quote'
    elif block[:2] == '* ' or block[:2] == '- ':
        return 'unordered_list'
    elif not re.match(r'\d+\. ', block) == None:
        return 'ordered_list'
    else:
        return 'paragraph'

def extract_formatting_text(text):
    if('**' in text):
        split_text = text.split('**')
        if not len(split_text) % 2 == 0:
            for split_text_item in split_text:
                text = text.replace(f"**{split_text_item}**", f"<b>{split_text_item}</b>")
    if('*' in text):
        split_text = text.split('*')
        if not len(split_text) % 2 == 0:
            for split_text_item in split_text:
                text = text.replace(f"*{split_text_item}*", f"<i>{split_text_item}</i>")
    if('`' in text):
        split_text = text.split('`')
        if not len(split_text) % 2 == 0:
            for split_text_item in split_text:
                text = text.replace(f"`{split_text_item}`", f"<code>{split_text_item}</code>")

    return text

def text_to_children(text):

    children = []
    html_node = HTMLNode("")

    text.strip()
    if(text[0] == '#'):
        return None
    elif(text[:3] == '```'):
        html_node = HTMLNode("code", text[3:-3].strip(), None)
        children.append(html_node)
    else:
        text_blocks = text.splitlines()
        for text_node in text_blocks:
            if(text_node[:2] == '* ' or text_node[:2] == '- '):
                res_value = extract_formatting_text(text_node[2:].strip())
                html_node = HTMLNode("li", res_value, None)
            elif(not re.match(r'\d+\. ', text_node) == None):
                res_value = extract_formatting_text(re.sub(r'\d+\. ', '', text_node).strip())
                html_node = HTMLNode("li", res_value, None)
            children.append(html_node)

    return children

def extract_link_text(text):
    link_text = text
    markdown_links = extract_markdown_links(text)
    for link in markdown_links:
        link_href = link[1]
        link_title = link[0]
        link_text = link_text.replace(f"[{link_title}]({link_href})", f'<a href="{link_href}">{link_title}</a>')
    return link_text

def extract_img_text(text):
    img_text = text
    markdown_imgs = extract_markdown_images(text)
    for img in markdown_imgs:
        print(img)
        img_href = img[1]
        img_title = img[0]
        img_text = img_text.replace(f"![{img_title}]({img_href})", f'<img src="{img_href}" alt="{img_title}" />')
    return img_text


def markdown_to_html_node(markdown):
    markdown_blocks = markdown_to_blocks(markdown)
    parent_node = HTMLNode("div", None, [], None)
    block_node = HTMLNode("div")
    for block in markdown_blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case 'heading':
                counter = 0
                for symbol in block:
                    if(not symbol == '#'):
                        break
                    counter += 1

                block_node = HTMLNode(f"h{counter}", block.strip('#').strip(), None)
            case 'code':
                block_node = HTMLNode("pre", None, text_to_children(block))
            case 'unordered_list':
                block_node = HTMLNode("ul", None, text_to_children(block))
            case 'ordered_list':
                block_node = HTMLNode("ol", None, text_to_children(block))
            case 'quote':
                block_node = HTMLNode("blockquote", block.strip('>').strip(), None)
            case _:
                block_node = HTMLNode("p", block, None)
        
        if(block_node.value):
            block_node.value = extract_formatting_text(block_node.value)
            block_node.value = extract_img_text(block_node.value)
            block_node.value = extract_link_text(block_node.value)
        parent_node.children.append(block_node)

    return parent_node

def extract_title(markdown):
    markdown_blocks = markdown_to_blocks(markdown)
    for block in markdown_blocks:
        if(block[:2] == "# "):
            return block.strip("#").strip()
    return Exception("No header in md")

