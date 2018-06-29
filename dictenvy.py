VERSION = (0, 2, 0)
__version__ = '.'.join(map(str, VERSION))


def merge(d1, d2):
    """Merges d2 into d1 without overwriting keys."""
    left = d1.copy()
    right = d2.copy()

    for key in right.keys():
        if key in left:
            left_is_dict = isinstance(left[key], dict)
            right_is_dict = isinstance(right[key], dict)

            if left_is_dict and right_is_dict: 
                left[key] = merge(left[key], right[key])
            elif right_is_dict:
                left[key] = merge({'': left[key]}, right[key])
            elif left_is_dict:
                left[key] = merge(left[key], {'': right[key]})
            else:
                left[key] = right[key]
        else:
            left[key] = right[key]

    return left


def _dict_from_key_path(segments, value):
    """Creates a nested dict out of array of keys."""
    ret = {}
    for segment in reversed(segments):
        if ret:
            ret = {segment: ret}
        else:
            ret[segment] = value
    return ret


def dictate(store, depth):
    """Transforms environment variables into a dictionary.

    Key in conjugation with depth is what controls the depth of the nested
    dicts. Variables that start with an underscore will be left alone.

    Sometimes you may encounter the following situation:

        TERM_PROGRAM=Apple_Terminal
        TERM=xterm-256color
    
    In which case, the return value would still be a dict, but `TERM` value
    would have an empty key.

    Examples:
        store={'A_B_C': 1}, depth=0 => {'a_b_c': 1}}
        store={'A_B_C': 1}, depth=1 => {'a': {'b_c': 1}}
        store={'A_B_C': 1}, depth=2 => {'a': {'b': {'c': 1}}}

        store={'A': 1, 'A_B': 2}, depth=1 => {'a': {'': '1', 'b': '2'}}
    """
    ret = {}
    for key, value in store.items():
        lkey = str(key).lower()
        if lkey.startswith('_'):
            ret[lkey] = value
            continue
        parts = lkey.split('_', depth)
        dict_value = _dict_from_key_path(parts, value)
        ret = merge(ret, dict_value)
    return ret
