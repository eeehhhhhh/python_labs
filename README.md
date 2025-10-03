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

