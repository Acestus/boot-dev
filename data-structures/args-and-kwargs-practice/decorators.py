def configure_plugin_decorator(func):
    def wrapper(*args, **kwargs):
        kwargs_from_args = dict(args)
        return func(**kwargs_from_args)
    return wrapper