# Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade, se ele ainda vai se alista 
# no serviço militar,  se e a hora de se alistar ou se ja passou tempo do alistamento. seu programa deve mostra quanto falta para o prazo

ano  = int(input("Digite seu ano de nascimento: "))

num = 2020-ano

if num <= 17 :
    print ("Você nao tem idade para se alistar, sua idade é {} ".format(num))
    print ("falta {} anos para se alistar ".format(num - 18))
elif num >= 18:    
    print ("Você tem que se alistar, sua idade é {} ".format(num))
    print ("voce deveria se alista a {} anos atras  ".format(num - 18))