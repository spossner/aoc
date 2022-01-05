from aoc.linked_list import LinkedList, SinglyListNode


def test_singly():
    l = [-4, -1, 0, 3, 10]
    node = SinglyListNode.from_list(l)
    for expected in l:
        assert node.val == expected
        node = node.next_node
    assert node is None


def test_simple():
    l = LinkedList()
    l.addAtIndex(-1,0)
    l.get(0)
    l.deleteAtIndex(-1)
    assert str(l) == "[0]"
    assert l.validate() is True


def test_example():
    l = LinkedList()
    assert l.get(0) == -1
    assert l.get(1) == -1
    assert l.get(2) == -1
    l.addAtHead(1)
    assert l.get(0) == 1
    assert l.get(1) == -1
    assert l.get(2) == -1
    l.addAtTail(3)
    assert l.get(0) == 1
    assert l.get(1) == 3
    assert l.get(2) == -1
    l.addAtIndex(1, 2)
    assert l.validate() is True
    assert l.get(0) == 1
    assert l.get(1) == 2
    assert l.get(2) == 3
    l.addAtTail(4)
    assert l.get(2) == 3
    l.deleteAtIndex(1)
    assert l.get(1) == 3
    assert l.validate() is True


if __name__ == "__main__":
    test_example()