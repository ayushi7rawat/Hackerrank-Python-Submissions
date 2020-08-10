n= int(input())

phonebook=dict()
for i in range(n):
    entry=input().strip().split(' ')
    phonebook[entry[0]]=entry[1]

name=input()
while name:
    try:
        if name in phonebook:
            print('{}={}'.format(name,phonebook[name]))
        else:
            print('Not found')
        name = input()
    except:
        break

