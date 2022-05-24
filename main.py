def main(url):
    """
    Pseudocode of write-tight v0.1.
    """
    raw_html = read_url(url)
    clean_html = remove_tag_content(raw_html)
    clean_html = add_inline_css(clean_html)
    
    pattern_matches = get_matches(clean_html)
    output_html = apply_matches(pattern_matches)

    return show_in_browser(output_html)