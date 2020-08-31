# age = 24
# greeting = 'Hello'

# print(greeting + ' ' + str(age))
# print(int('20'))

# parrot = "Norwegian Blue"
# print(parrot)
# print(parrot[0])
# print(parrot[3])
# print(parrot[-1])
# print(parrot[0:6])
# print(parrot[:6])
# print(parrot[6:])
# print(parrot[-4:-2])
# print(parrot[0:6:2])

# print('Hello' * 5)

# today = "friday"

# print('day' in today)
# print('fri' in today)
# print('thur' in today)
# print('parrot' in "fjord")

age = 24
print('my age is {0} years old'.format(age))
print('my age is {} years old'.format(age))
print('my age is %d years old' %age)
print('my age is %d %s %d %s' %(age, 'years', 6, 'months'))

print(""" 
  January: {2}
  February: {0}
  March: {2}
  May: {2}
  June: {1}
  July: {2}
  August: {2}
  September: {1}
  October: {2}
  November: {1}
  December: {2}
 """.format(28,30,31))

for i in range(1, 12):
  print("No. %2d squared is %4d and cubed is %4d " %(i, i**2 , i**3 ))

print()

for i in range(1, 12):
  print("No. {:2} squared is {:4} and cubed is {:4}".format(i, i**2, i**3))
