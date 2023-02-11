from itertools import chain

class FlatIterator:

    def __init__(self, list_of_list):
        self.my_list = list_of_list
        self.position = -1

    def __iter__(self):
        self.item = list(chain(*self.my_list))
        return self

    def __next__(self):
        if len(self.item) - 1 == self.position:
            raise StopIteration
        else:
            self.position += 1
            return self.item[self.position]


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    print(list(FlatIterator(list_of_lists_1)))

if __name__ == '__main__':
    test_1()