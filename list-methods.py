numbers = [1,10,25,88,17,73]
letters = ['a','c','g','k','a','y']

val = min(numbers)
print(val)
val = max(numbers)
print(val)
val = min(letters)
print(val)

val = numbers[3:6]
print(val)
val = numbers[:3]
print(val)
val = numbers[4:]
print(val)

numbers[4]=40
print(numbers)

numbers.append(49)
print(numbers)

numbers.insert(3,78) # -1 yaparsak en sondakiden bir öncesini ekler
print(numbers)

#numbers.pop() #(silmek için) en sondakini siler
numbers.pop(0) #verilen indexteki rakamı siler
print(numbers)

numbers.remove(78)
print(numbers)

numbers.sort() #sayısal olarak sıralanır
print(numbers)
letters.sort() #alfabetik olarak sıralar
print(letters)

print(len(numbers))

print(numbers.count(10))
print(letters.count('y'))

numbers.clear()
print(numbers)
