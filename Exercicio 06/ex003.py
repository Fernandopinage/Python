# Crie um programa que leia dois valores e mostre o menu com o valor da tela seu programa devera realizar a opção solicitada em cada caso:
# [ 1 ] Somar
# [ 2 ] Multiplicar
# [ 3 ] Maior
# [ 4 ] Novos numeros
# [ 5 ] Sair"
numero = 0

while numero < 5:
        print("="*20)
        print("[ 1 ] Somar")
        print("[ 2 ] Multiplicar")
        print("[ 3 ] Maior")
        print("[ 4 ] Novos numeros")
        print("[ 5 ] Sair")
        print("="*20)
        numero = int(input('Digite um numero: '))
        if numero == 1:
            n1 = int(input('digite o primeiro numero: '))
            n2 = int(input('digite o segundo numero: '))
            soma = n1 + n2 
            print('Soma de {} + {} = {}'.format(soma,n1,n2))
        elif numero == 2:
            n1 = int(input('digite o primeiro numero: '))
            n2 = int(input('digite o segundo numero: '))
            mult = n1 * n2 
            print('A multiplicação de {} * {} = {}'.format(n1,n2,mult))
        elif numero == 3:
            n1 = int(input('digite o primeiro numero: '))
            n2 = int(input('digite o segundo numero: ')) 
            if n1 > n2:
                print('Numero {} é Maior que Numero {}'.format(n1,n2))
            else:
                print('Numero {} é Maior que Numero {}'.format(n2,n1))
        elif numero == 4:
            print("Opção 4")
        elif numero == 5:
            print("Saindo...")
            numero = numero + 5    
        else:
            print("Informe um valor valido das opçoes no menu")    