def markdown_to_text_decorator(func):
    def wrapper(*args, **kwargs):
        converted_args = list(map(convert_md_to_txt, args))

        def kwarg_item_to_txt(item_tuple):
            key, value = item_tuple
            return (key, convert_md_to_txt(value))

        converted_kwargs = dict(map(kwarg_item_to_txt, kwargs.items()))
        return func(*converted_args, **converted_kwargs)

    return wrapper


# don't touch below this line


def convert_md_to_txt(doc):
    lines = doc.split("\n")
    for i in range(len(lines)):
        line = lines[i]
        lines[i] = line.lstrip("# ")
    return "\n".join(lines)
