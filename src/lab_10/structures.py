class Stack:
    def __init__(self):
        self._data = []  # вершина стека - последний элемент списка
    
    def push(self, item):
        # Добавить элемент на вершину стека
        self._data.append(item)
    
    def pop(self):
        # Снять верхний элемент стека и вернуть его
        if self.is_empty():
            raise IndexError("Попытка извлечения из пустого стека")
        return self._data.pop()
    
    def peek(self):
        # Вернуть верхний элемент без удаления
        if self.is_empty():
            return None
        return self._data[-1]
    
    def is_empty(self):
        # Проверить, пуст ли стек
        return len(self._data) == 0
    
    def __len__(self):
        # Количество элементов в стеке
        return len(self._data)
    
    def __repr__(self):
        return f"Stack({self._data})"


class Queue:
    def __init__(self):
        from collections import deque
        self._data = deque()  # голова очереди - левый край
    
    def enqueue(self, item):
        # Добавить элемент в конец очереди
        self._data.append(item)
    
    def dequeue(self):
        # Взять элемент из начала очереди и вернуть его
        if self.is_empty():
            raise IndexError("Попытка извлечения из пустой очереди")
        return self._data.popleft()
    
    def peek(self):
        # Вернуть первый элемент без удаления
        if self.is_empty():
            return None
        return self._data[0]
    
    def is_empty(self):
        # Проверить, пуста ли очередь
        return len(self._data) == 0
    
    def __len__(self):
        # Количество элементов в очереди
        return len(self._data)
    
    def __repr__(self):
        return f"Queue({list(self._data)})"
    
    print("=== Тестирование Stack ===")
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(f"Стек: {stack}")
print(f"Вершина: {stack.peek()}")
print(f"Размер: {len(stack)}")

popped = stack.pop()
print(f"Извлечено: {popped}")
print(f"Теперь стек: {stack}")
print(f"Пуст ли? {stack.is_empty()}")

print("\n=== Тестирование Queue ===")
queue = Queue()
queue.enqueue("a")
queue.enqueue("b")
queue.enqueue("c")
print(f"Очередь: {queue}")
print(f"Первый элемент: {queue.peek()}")
print(f"Размер: {len(queue)}")

dequeued = queue.dequeue()
print(f"Извлечено: {dequeued}")
print(f"Теперь очередь: {queue}")
print(f"Пуста ли? {queue.is_empty()}")