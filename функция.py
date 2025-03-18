def get_factors(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors

# Проверка
print(get_factors(1))    # [1]
print(get_factors(5))    # [1, 5]
print(get_factors(10))   # [1, 2, 5, 10]
print(get_factors(36))   # [1, 2, 3, 4, 6, 9, 12, 18, 36]
print(get_factors(101))  # [1, 101]