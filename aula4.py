a = int(input('primeiro valor:  '))
b = int(input('segundo valor:  '))
c = int(input('terceiro valor:  '))
if a > b and a > c:

    print('o maior número é {}'.format(a))
elif b>a and b>c:
    print('o maior número é {}'.format(b))
else:
    print('o maior número é {}'.format(c))
print('final do programa')
