def clear_screen(func):
    def wrapper(*args, **kwargs):
        import subprocess as sp

        sp.call("clear", shell=True)
        return func(*args, **kwargs)

    return wrapper
