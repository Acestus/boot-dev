def create_markdown_image(alt_text):
    enclosed_alt = f"![{alt_text}]"
    def with_url(url):
        escape_url = url.replace("(", "%28").replace(")", "%29")
        enclosed_url = f"({escape_url}"
        markdown_image_line = enclosed_alt + enclosed_url
        def with_title(title=None):
            if title:
                escaped_title = title.replace('"', '\\"')
                full_markdown_image_line = f'{markdown_image_line} "{escaped_title}")'
            else:
                full_markdown_image_line = f"{markdown_image_line})"
            return full_markdown_image_line
        return with_title
    return with_url