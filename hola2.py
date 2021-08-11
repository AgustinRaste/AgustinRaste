print('Programa para agregar al repo nuevo')


def tablaDe(n):
    for i in range(10):
        print(n, 'x', i, '= ', i * n)

def test():
    n = int(input('Ingrese el numero del cual desea saber la tabla: '))
    tablaDe(n)
    print('FIN DEL PROGRAMA')

if __name__ == '__main__':
    test()



