#!usr/bin/env python3
'''
#Before if/else added nothing displayed
a = 10
b = 10
if a > b:
    print('a is greater than b')
#added elif
elif a < b:
    print('b is greater than a')
#added else
else:
    print('a is not greater than b')
    print('a is not less than b')
    print('Therefore, a is equal to b')
'''

#TempFile for While Loops
'''
count = 0
while count != 5:
    print(count)
    count = count + 1
print('loop has ended')
'''
#sample2
password = ''
while password != 'P@ssw0rd':
    password = input("Type in your password: ")
print('Congratulations you guessed the correct password!')
