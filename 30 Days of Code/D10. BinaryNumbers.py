#take input and strips any spaces on either side, then converts it from a string to an interger
num=int(input().strip())

#bin converts num into binary and  returns '0b1101'. the [2:] allows us to omit the '0b' at the beginning of the string. which leaves us with '1101'.split('0'). This string method takes '1101' and splits it into a list. We end up with ['11','1'].
binary_num=bin(num)[2:].split('0')

#returns biggest value which will contain highest occourance of 1
print(len(max(binary_num)))
