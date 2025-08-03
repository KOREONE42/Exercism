import re

def process_inline(text):
    """
    Process inline markdown formatting for bold and italic text.
    
    Bold text is wrapped with double underscores (__text__) and is converted to <strong>.
    Italic text is wrapped with single underscores (_text_) and is converted to <em>.
    
    The substitutions are applied to all occurrences in the text.
    """
    # Replace bold text: __text__ -> <strong>text</strong>
    text = re.sub(r'__(.*?)__', r'<strong>\1</strong>', text)
    # Replace italic text: _text_ -> <em>text</em>
    text = re.sub(r'_(.*?)_', r'<em>\1</em>', text)
    return text

def parse(markdown):
    """
    Convert a Markdown-formatted string into HTML.
    
    Supports:
      - Headers: lines starting with 1 to 6 '#' characters followed by a space.
      - Unordered lists: lines starting with "* " (consecutive list items are grouped into a <ul> block).
      - Paragraphs: any other lines.
      
    Inline formatting for bold (__text__) and italic (_text_) is applied to all text content,
    even within headers, list items, and paragraphs.
    """
    lines = markdown.split('\n')
    output = []
    in_list = False

    for line in lines:
        # Check for header syntax. It must start with 1-6 '#' followed by a space.
        header_match = re.match(r'^(#{1,6})\s+(.*)$', line)
        if header_match:
            # Close any open list if starting a header block.
            if in_list:
                output.append('</ul>')
                in_list = False

            header_level = len(header_match.group(1))
            # Process inline formatting within header content.
            header_content = process_inline(header_match.group(2))
            output.append(f'<h{header_level}>{header_content}</h{header_level}>')
            continue  # Move on to the next line

        # Check if the line is an unordered list item (starts with "* ").
        list_match = re.match(r'^\*\s+(.*)$', line)
        if list_match:
            # If not already inside a list, start a new <ul> block.
            if not in_list:
                output.append('<ul>')
                in_list = True
            # Process inline formatting in the list item.
            list_item_content = process_inline(list_match.group(1))
            output.append(f'<li>{list_item_content}</li>')
            continue  # Move on to the next line

        # For all other lines, treat them as paragraphs.
        # If a list was open, close it before starting a new block.
        if in_list:
            output.append('</ul>')
            in_list = False

        # Process inline formatting for the paragraph text.
        paragraph_content = process_inline(line)
        output.append(f'<p>{paragraph_content}</p>')

    # If markdown ends while still inside a list, close it.
    if in_list:
        output.append('</ul>')

    # Join all parts into one string and return.
    return ''.join(output)
