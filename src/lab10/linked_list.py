from typing import Any, Iterator


class Node:
    """
    узел односвязного списка
    
    attributes
        value значение элемента
        next ссылка на следующий узел или None
    """
    
    def __init__(self, value: Any, next: "Node | None" = None):
        self.value = value
        self.next = next
    
    def __repr__(self) -> str:
        return f"Node({self.value})"


class SinglyLinkedList:
    """
    односвязный список с оптимизацией через tail
    
    attributes
        head голова списка (первый элемент) или None
        tail хвост списка (последний элемент) или None
        _size количество элементов в списке
    """
    
    def __init__(self):
        """инициализация пустого списка"""
        self.head: Node | None = None
        self.tail: Node | None = None
        self._size: int = 0
    
    def append(self, value: Any) -> None:
        """
        добавить элемент в конец списка
        
        args
            value значение для добавления
        
        сложность O(1) благодаря tail
        """
        new_node = Node(value)
        
        if self.head is None:
            # список пуст
            self.head = new_node
            self.tail = new_node
        else:
            # добавляем в конец
            self.tail.next = new_node
            self.tail = new_node
        
        self._size += 1
    
    def prepend(self, value: Any) -> None:
        """
        добавить элемент в начало списка
        
        args
            value значение для добавления
        
        сложность O(1)
        """
        new_node = Node(value, next=self.head)
        self.head = new_node
        
        if self.tail is None:
            # список был пуст
            self.tail = new_node
        
        self._size += 1
    
    def insert(self, idx: int, value: Any) -> None:
        """
        вставить элемент по индексу
        
        args
            idx индекс для вставки (0 <= idx <= len)
            value значение для вставки
        
        raises
            IndexError если индекс вне диапазона [0, len]
        
        сложность O(n)
        """
        if idx < 0 or idx > self._size:
            raise IndexError(
                f"индекс {idx} вне диапазона [0, {self._size}]"
            )
        
        if idx == 0:
            self.prepend(value)
            return
        
        if idx == self._size:
            self.append(value)
            return
        current = self.head
        for _ in range(idx - 1):
            current = current.next
        
        new_node = Node(value, next=current.next)
        current.next = new_node
        self._size += 1
    
    def remove(self, value: Any) -> None:
        """
        удалить первое вхождение значения
        
        args
            value значение для удаления
        
        raises
            ValueError если значение не найдено
        
        сложность O(n)
        """
        if self.head is None:
            raise ValueError(f"значение {value} не найдено в списке")
        if self.head.value == value:
            self.head = self.head.next
            self._size -= 1
            
            if self.head is None:
                self.tail = None
            
            return
        
        current = self.head
        while current.next is not None:
            if current.next.value == value:
                if current.next == self.tail:
                    self.tail = current
                
                current.next = current.next.next
                self._size -= 1
                return
            
            current = current.next
        
        raise ValueError(f"значение {value} не найдено в списке")
    
    def __iter__(self) -> Iterator[Any]:
        """
        итератор по значениям списка (от головы к хвосту)
        
        yields
            значения элементов списка
        """
        current = self.head
        while current is not None:
            yield current.value
            current = current.next
    
    def __len__(self) -> int:
        """
        вернуть количество элементов в списке
        
        returns
            количество элементов
        
        сложность O(1)
        """
        return self._size
    
    def __repr__(self) -> str:
        """строковое представление списка"""
        values = list(self)
        return f"SinglyLinkedList({values})"


