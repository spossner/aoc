from aoc.linked_list import LinkedList, SinglyListNode, ListNode

def check_list(node, l):
    for expected in l:
        assert node.val == expected
        node = node.next_node
    assert node is None

def test_singly():
    l = [-4, -1, 0, 3, 10]
    node = SinglyListNode.from_list(l)
    check_list(node, l)

def test_reverse_singly():
    l = [-4, -1, 0, 3, 10]
    node = SinglyListNode.from_list(reversed(l))
    new_head = node.reverse()
    check_list(new_head, l)

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

def test_iterator():
    l = [-4, -1, 0, 3, 10]
    node = ListNode.from_list(l)
    for i, v in enumerate(node):
        assert v == l[i]

def test_singly_iterator():
    l = [-4, -1, 0, 3, 10]
    node = SinglyListNode.from_list(l)
    for i, v in enumerate(node):
        assert v == l[i]
