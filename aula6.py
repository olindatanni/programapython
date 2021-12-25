a = int(input('Entre com o número para ver se ele é primo: '))
div = 0
for x in range (1, a+1):
    resto = a % x
    print (x, resto)
    if resto == 0:
        div += 1
if div == 2:
    print ('quantidade de divisores {}'.format(div))
    print('número {} é primo'.format(a))
else:
    print('quantidade de divisores {}'.format(div))
    print ('número {} não é primo'.format(a))
