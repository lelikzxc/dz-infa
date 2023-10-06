a = list(map(str, input().split()))

def bm(a, b):
    if a==b:
        return 0
    elif a.startswith(b):
        return bm(a[len(b):],b)
    elif b.startswith(a):
        return bm(a, b[len(a):])
    else:
        return -1 if a<b else 1
def max_nums(s):
    num=s
    num.sort(key=lambda x:x, reverse=True, cmp=bm)
    return "".join(num)

print(max_nums(a))

# Функция, которая сравнивает два числа по их строковому представлению
def compare(a, b):
  # Если числа равны, то возвращаем 0
  if a == b:
    return 0
  # Если первое число начинается со второго, то сравниваем оставшиеся части
  elif a.startswith(b):
    return compare(a[len(b):], b)
  # Если второе число начинается с первого, то сравниваем оставшиеся части
  elif b.startswith(a):
    return compare(a, b[len(a):])
  # Иначе сравниваем числа лексикографически
  else:
    return -1 if a < b else 1

# Функция, которая получает на вход строку целых неотрицательных чисел и составляет из них наибольшее возможное число
def max_number(s):
  # Разбиваем строку на список чисел
  numbers = s.split()
  # Сортируем список по убыванию с помощью функции compare
  numbers.sort(key=lambda x: x, reverse=True, cmp=compare)
  # Соединяем отсортированные числа в одну строку и возвращаем ее
  return "".join(numbers)

# Пример ввода и вывода
s = "3 30 34 5 9"
print(max_number(s)) # Вывод: 9534330

