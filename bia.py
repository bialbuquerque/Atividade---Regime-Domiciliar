preco = int(input('Digite o preço do produto:'))

nota100 = preco // 100
resto100 = preco % 100

nota50 = resto100 // 50
resto50 = resto100 % 50

nota20 = resto50 // 20
resto20 = resto50 % 20

nota10 = resto20 // 10
resto10 = resto20 % 10

nota5 = resto10 // 5
resto5 = resto10 % 5

nota2 = resto5 // 2
resto2 = resto5 % 2

nota1 = resto2 // 1
resto1 = resto2 % 1


print ("nota de 100:", nota100)
print ("nota de 50:", nota50)
print ("nota de 20:", nota20)
print ("nota de 10:", nota10)
print ("nota de 5:", nota5)
print ("nota de 2:", nota2)
print ("nota de 1:", nota1)


