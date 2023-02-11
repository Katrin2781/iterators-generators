class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.new_list = []
        self.position = -1

    def __iter__(self):
        def list_convert(list_source):
            for item in list_source:
                if type(item) == list:
                    list_convert(item)
                else:
                    self.new_list.append(item)
        list_convert(self.list_of_list)
        return self

    def __next__(self):
        if len(self.new_list) - 1 == self.position:
            raise StopIteration
        else:
            self.position += 1
            return self.new_list[self.position]


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    print(list(FlatIterator(list_of_lists_2)))

if __name__ == '__main__':
    test_3()