# python_labs

## Лабораторная работа 1

### Задание 1
```python
name = input('Имя: ')
age = int(input('Возраст: '))
print(f"Привет, {name}! Через год тебе будет {age + 1}.")
```
![Картинка 1](images/lab_01/01.png)

### Задание 2
```python
a = float(input("a: ").replace(',', '.'))
b = float(input("b: ").replace(',', '.'))
summ = a+b
average = round(summ / 2, 2)
print(f'sum={summ}; avg={average}')
```
![Картинка 1](images/lab_01/02.png)

### Задание 3
```python
price = float(input())
discount = float(input())
vat = float(input())
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount
print(f'База после скидки: {base:.2f} ₽')
print(f'НДС:               {vat_amount:.2f} ₽')
print(f'Итого к оплате:    {total:.2f} ₽')
```
![Картинка 1](images/lab_01/03.png)

### Задание 4
```python
m = int(input('Минуты: '))
print(f'{int(m/60)}:{int(m%60):02d}')
```
![Картинка 1](images/lab_01/04.png)

### Задание 5
```python
fio = input('ФИО: ').strip()
cl = ' '.join(fio.split())
ini = ''.join(x[0].upper() for x in cl.split())
print(f'Инициалы: {ini}\nДлина (символов): {len(cl)}')
```
![Картинка 1](images/lab_01/05.png)

### Задание 6
```python
N = int(input())
ochn = 0
zaochn = 0
for i in range(N):
    inf = input().split()
    if inf[-1] == 'True':
        ochn += 1
    else:
        zaochn += 1
print(f'out: {ochn} {zaochn}')
```
![Картинка 1](images/lab_01/06.png) 

### Задание 7
```python
n = input('in: ')
out = ''
for i in range(len(n)):
    if n[i].isupper():
        out += (n[i])
        for j in range(i, len(n)):
            if n[j].isdigit():
                out += n[j+1]
                out += n[j+1+j+1-i::j+1-i]
                break
print(f'out: {out}')
```
![Картинка 1](images/lab_01/07.png)

## Лабораторная работа 2

### Задание 1
```python 
def min_max(nums):
    if nums == []:
        return 'ValueError'
    
    minimum = nums[0]
    maximum = nums[0]

    for i in range(len(nums)):
        if nums[i] < minimum:
            minimum = nums[i]
        if nums[i] > maximum:
            maximum = nums[i]

    return (minimum, maximum)

print('min_max')
print(min_max([3, -1, 5, 5, 0]))
print(min_max([42]))
print(min_max([-5, -2, -9]))
print(min_max([]))
print(min_max([1.5, 2, 2.0, -3.1]))

def unique_sorted(nums):
    if nums == []:
        return []
    
    unique = []
    for x in nums:
        if x not in unique:
            unique.append(x)

    n = len(unique)
    for i in range(n):
        for j in range(0, n-i-1):
            if unique[j] > unique[j+1]:
                unique[j], unique[j+1] = unique[j+1], unique[j]
    
    return unique

print('unique_sorted')
print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([]))
print(unique_sorted([-1, -1, 0, 2, 2]))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))

def flatten(mat):
    result = []
    for i in range(len(mat)):
        if type(mat[i]) != list and type(mat[i]) != tuple:
            return 'TypeError'
        
        for j in range(len(mat[i])):
            result.append(mat[i][j])
    
    return result

print('flatten')
print(flatten([[1, 2], [3, 4]]))
print(flatten([[1, 2], (3, 4, 5)]))
print(flatten([[1], [], [2, 3]]))
print(flatten([[1, 2], "ab"]))
```
![Картинка 1](images/lab_02/01.png)

### Задание 2
```python
def transpose(mat):
    if mat == []:
        return []
    
    n = len(mat[0])
    for i in range(len(mat)):
        if len(mat[i]) != n:
            return 'ValueError'
    
    new_mat = []
    for j in range(len(mat[0])):  
        new_row = []
        for i in range(len(mat)):  
            new_row.append(mat[i][j])
        new_mat.append(new_row)
    
    return new_mat

print('transpose')
print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([]))
print(transpose([[1, 2], [3]]))


def row_sums(mat):
    if mat == []:
        return []
    
    n = len(mat[0])
    for i in range(len(mat)):
        if len(mat[i]) != n:
            return 'ValueError'
    
    sums = []
    for i in range(len(mat)):
        s = 0
        for j in range(len(mat[i])):
            s = s + mat[i][j]
        sums.append(s)
    
    return sums

print('row_sums')
print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
print(row_sums([[1, 2], [3]]))


def col_sums(mat):
    if mat == []:
        return []
    
    n = len(mat[0])
    for i in range(len(mat)):
        if len(mat[i]) != n:
            return 'ValueError'
    
    sums = []
    for j in range(len(mat[0])):  
        s = 0
        for i in range(len(mat)):  
            s = s + mat[i][j]
        sums.append(s)
    
    return sums

print('col_sums')
print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]]))
```
![Картинка 1](images/lab_02/02.png)

### Задание 3
```python
def format_record(rec):
    fio = rec[0]
    group = rec[1]
    gpa = rec[2]
    
    if fio == "" or group == "":
        return 'ValueError'
    
    if not isinstance(gpa, (int, float)):
        return 'TypeError'
    
    fio_parts = fio.split()
    clean_parts = []
    for p in fio_parts:
        if p != "":
            clean_parts.append(p.strip())
    
    if len(clean_parts) == 3:
        initials = clean_parts[1][0].upper() + "." + clean_parts[2][0].upper() + "."
    elif len(clean_parts) == 2:
        initials = clean_parts[1][0].upper() + "."
    else:
        return 'ValueError'
    
    gpa_str = str(round(gpa, 2))
    if "." in gpa_str:
        parts = gpa_str.split(".")
        if len(parts[1]) == 1:
            gpa_str = gpa_str + "0"
    else:
        gpa_str = gpa_str + ".00"

    surname = clean_parts[0].capitalize()
    
    result = surname + " " + initials + ", гр. " + group + ", GPA " + gpa_str
    return result

print('format_record')
print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
print(format_record(("", "BIVT-25", 4.0)))  # пустое фио
```
![Картинка 1](images/lab_02/03.png)
