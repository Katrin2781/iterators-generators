import types


def flat_generator(list_of_list):
    new_list = []

    def list_convert(list_source):
        for item in list_source:
            if type(item) == list:
                list_convert(item)
            else:
                new_list.append(item)

    list_convert(list_of_list)
    for item in new_list:
        yield item


def test_4():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)
    print(list(flat_generator(list_of_lists_2)))

if __name__ == '__main__':
    test_4()
