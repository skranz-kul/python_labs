def test_stack():
    """тесты для класса Stack"""
    from src.lab10.structures import Stack
    
    print("тесты stack")
    
    # тест 1: создание пустого стека
    stack = Stack()
    assert stack.is_empty() == True
    assert len(stack) == 0
    print("  создание пустого стека - ok")
    
    # тест 2: push элементов
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert len(stack) == 3
    assert stack.is_empty() == False
    print("  push элементов - ok")
    
    # тест 3: peek не удаляет элемент
    top = stack.peek()
    assert top == 3
    assert len(stack) == 3  # размер не изменился
    print("  peek возвращает верхний элемент без удаления - ok")
    
    # тест 4: pop возвращает элементы в обратном порядке (LIFO)
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.is_empty() == True
    print("  pop возвращает элементы в порядке LIFO - ok")
    
    # тест 5: pop из пустого стека вызывает исключение
    try:
        stack.pop()
        assert False, "должно было выброситься исключение"
    except IndexError as e:
        assert "empty stack" in str(e)
        print("  pop из пустого стека вызывает IndexError - ok")
    
    # тест 6: peek из пустого стека возвращает None
    assert stack.peek() is None
    print("  peek из пустого стека возвращает None - ok")
    
    # тест 7: работа с разными типами данных
    stack.push("строка")
    stack.push([1, 2, 3])
    stack.push({"ключ": "значение"})
    assert stack.pop() == {"ключ": "значение"}
    assert stack.pop() == [1, 2, 3]
    assert stack.pop() == "строка"
    print("  работа с разными типами данных - ok")
    
    print("все тесты stack пройдены\n")


def test_queue():
    """тесты для класса Queue"""
    from src.lab10.structures import Queue
    
    print("тесты queue")
    
    # тест 1: создание пустой очереди
    queue = Queue()
    assert queue.is_empty() == True
    assert len(queue) == 0
    print("  создание пустой очереди - ok")
    
    # тест 2: enqueue элементов
    queue.enqueue("первый")
    queue.enqueue("второй")
    queue.enqueue("третий")
    assert len(queue) == 3
    assert queue.is_empty() == False
    print("  enqueue элементов - ok")
    
    # тест 3: peek не удаляет элемент
    front = queue.peek()
    assert front == "первый"
    assert len(queue) == 3
    print("  peek возвращает первый элемент без удаления - ok")
    
    # тест 4: dequeue возвращает элементы в порядке добавления (FIFO)
    assert queue.dequeue() == "первый"
    assert queue.dequeue() == "второй"
    assert queue.dequeue() == "третий"
    assert queue.is_empty() == True
    print("  dequeue возвращает элементы в порядке FIFO - ok")
    
    # тест 5: dequeue из пустой очереди вызывает исключение
    try:
        queue.dequeue()
        assert False, "должно было выброситься исключение"
    except IndexError as e:
        assert "empty queue" in str(e)
        print("  dequeue из пустой очереди вызывает IndexError - ok")
    
    # тест 6: peek из пустой очереди возвращает None
    assert queue.peek() is None
    print("  peek из пустой очереди возвращает None - ok")
    
    # тест 7: чередование enqueue и dequeue
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.dequeue() == 1
    queue.enqueue(3)
    assert queue.dequeue() == 2
    assert queue.dequeue() == 3
    print("  чередование enqueue и dequeue - ok")
    
    print("все тесты queue пройдены\n")


def test_linked_list():
    """тесты для класса SinglyLinkedList"""
    from src.lab10.linked_list import SinglyLinkedList, Node
    
    print("тесты SinglyLinkedList")
    
    # тест 1: создание пустого списка
    lst = SinglyLinkedList()
    assert len(lst) == 0
    assert lst.head is None
    assert lst.tail is None
    print("  создание пустого списка - ok")
    
    # тест 2: append элементов
    lst.append(1)
    lst.append(2)
    lst.append(3)
    assert len(lst) == 3
    assert lst.head.value == 1
    assert lst.tail.value == 3
    print("  append элементов - ok")
    
    # тест 3: итерация по списку
    values = list(lst)
    assert values == [1, 2, 3]
    print("  итерация по списку - ok")
    
    # тест 4: prepend элементов
    lst.prepend(0)
    assert len(lst) == 4
    assert lst.head.value == 0
    assert list(lst) == [0, 1, 2, 3]
    print("  prepend элементов - ok")
    
    # тест 5: insert в середину
    lst.insert(2, 1.5)
    assert list(lst) == [0, 1, 1.5, 2, 3]
    assert len(lst) == 5
    print("  insert в середину списка - ok")
    
    # тест 6: insert в начало (idx=0)
    lst2 = SinglyLinkedList()
    lst2.insert(0, "a")
    assert list(lst2) == ["a"]
    assert lst2.head.value == "a"
    assert lst2.tail.value == "a"
    print("  insert в начало (idx=0) - ok")
    
    # тест 7: insert в конец (idx=len)
    lst2.insert(1, "b")
    assert list(lst2) == ["a", "b"]
    assert lst2.tail.value == "b"
    print("  insert в конец (idx=len) - ok")
    
    # тест 8: insert с некорректным индексом
    try:
        lst.insert(-1, "x")
        assert False, "должно было выброситься исключение"
    except IndexError:
        print("  insert с отрицательным индексом вызывает IndexError - ok")
    
    try:
        lst.insert(100, "x")
        assert False, "должно было выброситься исключение"
    except IndexError:
        print("  insert с индексом > len вызывает IndexError - ok")
    
    # тест 9: remove из середины
    lst.remove(1.5)
    assert list(lst) == [0, 1, 2, 3]
    assert len(lst) == 4
    print("  remove из середины списка - ok")
    
    # тест 10: remove головы
    lst.remove(0)
    assert list(lst) == [1, 2, 3]
    assert lst.head.value == 1
    print("  remove головы списка - ok")
    
    # тест 11: remove хвоста
    lst.remove(3)
    assert list(lst) == [1, 2]
    assert lst.tail.value == 2
    print("  remove хвоста списка - ok")
    
    # тест 12: remove несуществующего значения
    try:
        lst.remove(999)
        assert False, "должно было выброситься исключение"
    except ValueError as e:
        assert "не найдено" in str(e)
        print("  remove несуществующего значения вызывает ValueError - ok")
    
    # тест 13: remove из пустого списка
    empty_lst = SinglyLinkedList()
    try:
        empty_lst.remove(1)
        assert False, "должно было выброситься исключение"
    except ValueError:
        print("  remove из пустого списка вызывает ValueError - ok")
    
    # тест 14: удаление всех элементов
    lst.remove(1)
    lst.remove(2)
    assert len(lst) == 0
    assert lst.head is None
    assert lst.tail is None
    print("  после удаления всех элементов head и tail равны None - ok")
    
    # тест 15: __repr__
    lst3 = SinglyLinkedList()
    lst3.append(1)
    lst3.append(2)
    assert repr(lst3) == "SinglyLinkedList([1, 2])"
    print("  __repr__ возвращает корректную строку - ok")
    
    # тест 16: Node repr
    node = Node(42)
    assert repr(node) == "Node(42)"
    print("  Node __repr__ работает корректно - ok")
    
    print("все тесты SinglyLinkedList пройдены\n")


def run_all_tests():
    """запуск всех тестов"""
    print("\nзапуск тестов лр10\n")
    
    test_stack()
    test_queue()
    test_linked_list()
    
    print("все тесты успешно пройдены")


if __name__ == "__main__":
    run_all_tests()
