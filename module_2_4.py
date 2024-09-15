numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
NewNumbers = []
primes = []
not_primes = []
for i in range(len(numbers)):
    if numbers[i] <= 1 or numbers[i] % 1 != 0:
        continue
    NewNumbers.append(numbers[i])
numbers = NewNumbers
for i in range(len(numbers)):
    counter = 0
    for j in range(i + 1):
        if numbers[i] % numbers [j] == 0:
            counter +=1
    if counter > 1 :
        not_primes.append(numbers[i])
    else:
        primes.append(numbers[i])
print(f'Простые числа из списка: {primes}')
print(f'Не простые числа из списка: {not_primes}')
