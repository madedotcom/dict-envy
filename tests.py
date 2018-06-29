import dictenvy


def test_transforms_into_dict():
    store = {'A': 1}
    assert dictenvy.dictate(store, depth=1) == {'a': 1}


def test_transforms_into_dict_one_level():
    store = {'A_B': 1}
    assert dictenvy.dictate(store, depth=1) == {'a': {'b': 1}}


def test_transforms_into_dict_one_level_with_one_underscore():
    store = {'A_B_HELLO': 1}
    assert dictenvy.dictate(store, depth=1) == {'a': {'b_hello': 1}}


def test_transforms_into_dict_one_level_with_empty_key():
    store = {'A': 1, 'A_B': 2}
    assert dictenvy.dictate(store, depth=1) == {'a': {'': 1, 'b': 2}}


def test_transforms_into_dict_two_levels():
    store = {'A_B_C': 1}
    assert dictenvy.dictate(store, depth=2) == {'a': {'b': {'c': 1}}}


def test_transforms_into_dict_two_levels_two_items_with_one_underscore():
    store = {'A_B_C_HELLO': 1, 'A_B_C_WORLD': 2}
    assert dictenvy.dictate(store, depth=2) == {'a': {'b': {'c_hello': 1, 'c_world': 2}}}


def test_transforms_into_dict_three_levels_with_two_items():
    store = {'A_B_C_HELLO': 1, 'A_B_C_WORLD': 2}
    assert dictenvy.dictate(store, depth=3) == {'a': {'b': {'c': {'hello': 1, 'world': 2}}}}


def test_variables_starting_with_underscores_are_left_intact():
    store = {'_A_B': 1}
    assert dictenvy.dictate(store, depth=1) == {'_a_b': 1}


def test_merge_simple():
    d1 = {'a': 2}
    d2 = {'a': 1}
    assert dictenvy.merge(d1, d2) == {'a': 1}


def test_merge_does_not_overwrite_existing_keys():
    d1 = {'a': {'b': 1}}
    d2 = {'a': {'c': 2}}
    assert dictenvy.merge(d1, d2) == {'a': {'b': 1, 'c': 2}}


def test_merge_creates_empty_key_for_simple_values():
    d1 = {'a': 1}
    d2 = {'a': {'b': 2}}
    assert dictenvy.merge(d1, d2) == {'a': {'': 1, 'b': 2}}
