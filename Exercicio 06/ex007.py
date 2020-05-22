# Crie um programa que leia vários números inteiros pelo teclado. O programa so vai parar quando o usúario digitar 999 que e a condição de parada.
# No final mostre quantos numeros foram digitados e soma entre esses numerosdatetime A combination of a date and a time. Attributes: ()
total = 0
numero = 0
cont = 0
while numero != 999 :

    numero = int(input('Digite um numero: '))
    total = total + numero
    cont = cont + 1
print('Total de numero digitados é {} é a soma dos numeros é {}'.format(cont -1,total-999))