num= int(input())
for i in range(num):
    s=input()
    even = ''
    odd = ''

    for j in range(len(s)):
        if j%2 == 0:
            even += s[j]
        else:
            odd+= s[j]
    
    print('{} {}'.format(even,odd))

