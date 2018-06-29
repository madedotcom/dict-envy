import pytest
import dictenvy


class TestDictate:

    @staticmethod
    def test_transforms_into_dict():
        store = {'A': 1}
        result = dictenvy.dictate(store, depth=1)
        assert result == {'a': 1}

    @staticmethod
    def test_transforms_into_dict_one_level():
        store = {'A_B': 1}
        result = dictenvy.dictate(store, depth=1)
        assert result == {'a': {'b': 1}}

    @staticmethod
    def test_transforms_into_dict_one_level_with_one_underscore():
        store = {'A_B_HELLO': 1}
        result = dictenvy.dictate(store, depth=1)
        assert result == {'a': {'b_hello': 1}}

    @staticmethod
    def test_transforms_into_dict_one_level_with_empty_key():
        store = {'A': 1, 'A_B': 2}
        result = dictenvy.dictate(store, depth=1)
        assert result == {'a': {'': 1, 'b': 2}}

    @staticmethod
    def test_transforms_into_dict_two_levels():
        store = {'A_B_C': 1}
        result = dictenvy.dictate(store, depth=2)
        assert result == {'a': {'b': {'c': 1}}}

    @staticmethod
    def test_transforms_into_dict_two_levels_two_items_with_one_underscore():
        store = {'A_B_C_HELLO': 1, 'A_B_C_WORLD': 2}
        result = dictenvy.dictate(store, depth=2)
        assert result == {'a': {'b': {'c_hello': 1, 'c_world': 2}}}

    @staticmethod
    def test_transforms_into_dict_three_levels_with_two_items():
        store = {'A_B_C_HELLO': 1, 'A_B_C_WORLD': 2}
        result = dictenvy.dictate(store, depth=3)
        assert result == {'a': {'b': {'c': {'hello': 1, 'world': 2}}}}

    @staticmethod
    def test_variables_starting_with_underscores_are_left_intact():
        store = {'_A_B': 1}
        result = dictenvy.dictate(store, depth=1)
        assert result == {'_a_b': 1}


class TestMerge:

    @staticmethod
    def test_merge_single_same_key():
        d1 = {'a': 2}
        d2 = {'a': 1}
        assert dictenvy.merge(d1, d2) == {'a': 1}

    @staticmethod
    def test_merge_same_top_level_key_with_different_children():
        d1 = {'a': {'b': 1}}
        d2 = {'a': {'c': 2}}
        assert dictenvy.merge(d1, d2) == {'a': {'b': 1, 'c': 2}}

    @staticmethod
    @pytest.mark.parametrize('types', [1, [1], '1'])
    def test_merge_same_top_level_key_with_different_types(types):
        d1 = {'a': types}
        d2 = {'a': {'b': 2}}
        assert dictenvy.merge(d1, d2) == {'a': {'': types, 'b': 2}}
