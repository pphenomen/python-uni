# Функция 1. Найти количество чисел, взаимно простых с заданным.
def gcd(num1, num2):
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1

def count_coprimes(n):
    count = 0
    for i in range(1, n):
        if gcd(i, n) == 1:  # проверка что нод = 1
            count += 1
    return count

# ввод числа от пользователя
n = int(input("Введите число: "))
print(f"Количество взаимно простых чисел с {n}: {count_coprimes(n)}")

# Функция 2. Найти сумму цифр числа, делящихся на 3.
def sum_of_digits_div_by_3(n):
    sum = 0 
    while n > 0:
        digit = n % 10   
        if digit % 3 == 0: 
            sum += digit
        n //= 10 
    return sum

# ввод числа от пользователя
n = int(input("Введите число: "))
result = sum_of_digits_div_by_3(n)
print(f"Сумма цифр числа {n}, которые делятся на 3: {result}")

# Функция 3. Найти делитель числа, являющийся взаимно простым с цифрами данного числа
# нод
def gcd(num1, num2):
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1

# извлечение цифр числа
def extract_digits(n):
    digits = []
    while n > 0:
        digits.append(n % 10)  
        n //= 10 
    return digits

# поиск делителей числа 
def find_coprime_divisor(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    
    # поиск цифр
    digits = extract_digits(n)
    
    coprime_divisors = []
    for divisor in divisors:
        is_coprime = True
        for digit in digits:
            if digit != 0 and gcd(divisor, digit) != 1:
                is_coprime = False
                break
        if is_coprime:
            coprime_divisors.append(divisor)
    
    return coprime_divisors

# ввод числа от пользователя
n = int(input("Введите число: "))
coprime_divisors = find_coprime_divisor(n)

if coprime_divisors:
    print(f"Делители числа {n}, взаимно простые с его цифрами: {coprime_divisors}")
else:
    print(f"Нет делителей числа {n}, взаимно простых с его цифрами.")
