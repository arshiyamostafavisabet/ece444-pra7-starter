def add(a, b):
    return a + b


def check_none(
    x,
):  # violation E711 (Comparison to None should be 'if cond is None:' or 'if cond is not None:')
    if x is None:
        return True
    return False


def record(value, history=None):
    if history is None:
        history = []
    history.append(value)
    return history
