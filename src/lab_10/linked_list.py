class Node:
    def __init__(self, value):
        self.value = value
        self.next = None  # ссылка на следующий узел
    
    def __repr__(self):
        return f"Node({self.value})"


class SinglyLinkedList:
    def __init__(self):
        self.head = None  # первый элемент
        self.tail = None  # последний элемент
        self._size = 0    # количество элементов
    
    def append(self, value):
        # Добавить элемент в конец списка за O(1)
        new_node = Node(value)
        
        if self.head is None:  # список пуст
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self._size += 1
    
    def prepend(self, value):
        # Добавить элемент в начало списка за O(1)
        new_node = Node(value)
        
        if self.head is None:  # список пуст
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        
        self._size += 1
    
    def insert(self, idx, value):
        # Вставить элемент по индексу idx
        if idx < 0 or idx > self._size:
            raise IndexError(f"Индекс {idx} вне диапазона [0, {self._size}]")
        
        if idx == 0:
            self.prepend(value)
        elif idx == self._size:
            self.append(value)
        else:
            # Вставка в середину
            new_node = Node(value)
            current = self.head
            
            # Переходим к элементу перед позицией вставки
            for _ in range(idx - 1):
                current = current.next
            
            new_node.next = current.next
            current.next = new_node
            self._size += 1
    
    def remove_by_value(self, value):
        # Удалить первое вхождение значения value
        if self.head is None:
            return  # ничего не делаем, список пуст
        
        # Если удаляем голову
        if self.head.value == value:
            self.head = self.head.next
            if self.head is None:  # если список стал пустым
                self.tail = None
            self._size -= 1
            return
        
        # Ищем элемент для удаления
        current = self.head
        while current.next is not None and current.next.value != value:
            current = current.next
        
        # Если нашли элемент для удаления
        if current.next is not None:
            current.next = current.next.next
            if current.next is None:  # если удалили последний элемент
                self.tail = current
            self._size -= 1
    
    def remove_by_index(self, idx):
        # Удалить элемент по индексу idx
        if idx < 0 or idx >= self._size:
            raise IndexError(f"Индекс {idx} вне диапазона [0, {self._size})")
        
        if idx == 0:  # удаление головы
            self.head = self.head.next
            if self.head is None:  # если список стал пустым
                self.tail = None
        else:
            current = self.head
            # Переходим к элементу перед удаляемым
            for _ in range(idx - 1):
                current = current.next
            
            # Удаляем элемент
            current.next = current.next.next
            if current.next is None:  # если удалили последний элемент
                self.tail = current
        
        self._size -= 1
    
    def __iter__(self):
        # Итератор по значениям списка
        current = self.head
        while current is not None:
            yield current.value
            current = current.next
    
    def __len__(self):
        # Количество элементов в списке
        return self._size
    
    def __repr__(self):
        # Строковое представление списка
        values = list(self)
        return f"SinglyLinkedList({values})"

print("=== Тестирование SinglyLinkedList ===")
ll = SinglyLinkedList()

print("1. Добавление в конец (append):")
ll.append(10)
ll.append(20)
ll.append(30)
print(f"   Список: {ll}")
print(f"   Размер: {len(ll)}")

print("\n2. Добавление в начало (prepend):")
ll.prepend(5)
ll.prepend(1)
print(f"   Список: {ll}")

print("\n3. Вставка по индексу (insert):")
ll.insert(2, 15)  # между 10 и 20
ll.insert(0, 0)   # в начало
ll.insert(len(ll), 40)  # в конец
print(f"   Список: {ll}")

print("\n4. Удаление по значению (remove_by_value):")
ll.remove_by_value(15)
print(f"   После удаления 15: {ll}")

print("\n5. Удаление по индексу (remove_by_index):")
ll.remove_by_index(0)  # удаляем первый
ll.remove_by_index(2)  # удаляем третий
print(f"   После удалений: {ll}")

print("\n6. Итерация по списку:")
print("   Элементы:", end=" ")
for item in ll:
    print(item, end=" ")
print()

print("\n7. Попытка вставки с неверным индексом:")
try:
    ll.insert(100, 999)
except IndexError as e:
    print(f"   Ошибка: {e}")