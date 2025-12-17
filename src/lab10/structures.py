from collections import deque
from typing import Any


class Stack:
    """
    структура данных cтек (LIFO) на базе list
    вершина стека — последний элемент списка
    """
    
    def __init__(self):
        """инициализация пустого стека"""
        self._data: list[Any] = []
    
    def push(self, item: Any) -> None:
        """
        добавить элемент на вершину стека
        
        args:
            item элемент для добавления
        
        сложность O(1) амортизированная
        """
        self._data.append(item)
    
    def pop(self) -> Any:
        """
        снять верхний элемент стека и вернуть его
        
        returns:
            верхний элемент стека
        
        raises:
            IndexError, если стек пуст
        
        сложность O(1)
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._data.pop()
    
    def peek(self) -> Any | None:
        """
        вернуть верхний элемент без удаления
        
        returns
            верхний элемент или None, если стек пуст
        
        сложность O(1)
        """
        if self.is_empty():
            return None
        return self._data[-1]
    
    def is_empty(self) -> bool:
        """
        проверить, пуст ли стек
        
        returns
            true если стек пуст, иначе false
        
        сложность O(1)
        """
        return len(self._data) == 0
    
    def __len__(self) -> int:
        """
        вернуть количество элементов в стеке
        
        returns
            количество элементов
        
        сложность O(1)
        """
        return len(self._data)
    


class Queue:
    """
    структура данных «очередь» (FIFO) на базе collections.deque
    голова очереди — левый край структуры (dequeue берёт слева)
    """
    
    def __init__(self):
        """инициализация пустой очереди"""
        self._data: deque[Any] = deque()
    
    def enqueue(self, item: Any) -> None:
        """
        добавить элемент в конец очереди
        
        args:
            item: элемент для добавления
        
        сложность: O(1)
        """
        self._data.append(item)
    
    def dequeue(self) -> Any:
        """
        взять элемент из начала очереди и вернуть его
        
        returns
            первый элемент очереди
        
        raises
            IndexError если очередь пуста
        
        сложность O(1)
        """
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._data.popleft()
    
    def peek(self) -> Any | None:
        """
        вернуть первый элемент без удаления
        
        returns
            первый элемент или None, если очередь пуста
        
        сложность O(1)
        """
        if self.is_empty():
            return None
        return self._data[0]
    
    def is_empty(self) -> bool:
        """
        проверить, пуста ли очередь
        
        returns:
            true если очередь пуста, иначе false
        
        сложность O(1)
        """
        return len(self._data) == 0
    
    def __len__(self) -> int:
        """
        вернуть количество элементов в очереди
        
        returns
            количество элементов
        
        сложность O(1)
        """
        return len(self._data)
   


