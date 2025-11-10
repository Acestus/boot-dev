def args_logger(*args, **kwargs):
    # Print positional arguments with numbered list format
    for i, arg in enumerate(args):
        print(f"{i + 1}. {arg}")

    # Print keyword arguments with asterisk format, sorted alphabetically
    for key, value in sorted(kwargs.items()):
        print(f"* {key}: {value}")
