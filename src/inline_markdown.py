from textnode import Textnode
def split_nodes_delimiter(nodes, delimiter, text_type):
    text_type_text = "text",
    text_type_bold = "bold",
    text_type_italic = "italic",
    text_type_code = "code",
    text_type_link = "link",
    text_type_image = "image"
    italics = "*"
    bold = "**"
    code = "`"
    node_list = []

    for node in nodes:
        tmp_text = node.text
        split_text = tmp_text.split(delimiter)
        
        for text in tmp_text:
            tmp_tag = ""
            tmp_block = ""
            
            match_delim_count = 0

            for letter in text:
            
                
                    tmp_tag = letter
                    match_delim_count += 1
            
                    tmp_block += letter
        if match_delim_count == 1:

        