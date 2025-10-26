data = [1,2,3,4,5]

x = lambda y: y + 4

double = list(map(lambda x: x*2, data))

print(double)

odd_numbers = list(filter(lambda x: x % 2 != 0, data))
print(odd_numbers)