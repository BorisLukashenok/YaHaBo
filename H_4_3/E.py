def result_accumulator(fn):
    def wrapper(*args, **kwargs):
        wrapper.results.append(fn(*args))
        if kwargs.get('method') == 'drop':
            res, wrapper.results = wrapper.results, []
            return res
    wrapper.results = []
    return wrapper