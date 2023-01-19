numbers = [1, 2, 3, 4, 5]
print({i for i in numbers if i ** 0.5 % 1 == 0})
numbers = [number for number in range(16, 100, 4)]
print({i for i in numbers if  not i ** 0.5 % 1})