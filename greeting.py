def greet(first_name, last_name=None):
    if last_name is not None:
        return f"Hello, {first_name} {last_name}"
