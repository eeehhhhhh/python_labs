fio = input('ФИО: ').strip()
cl = ' '.join(fio.split())
ini = ''.join(x[0].upper() for x in cl.split())
print(f'Инициалы: {ini}\nДлина (символов): {len(cl)}')
