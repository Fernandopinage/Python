# Cria um programa que faça um game do jokempô

from random import randint 


print("=="* 14)
print("1 - Tesoura")
print("2 - Papel")
print("3 - Pedra")
print("=="* 14)

opicao = int(input("Informe qual sua escolha: "))
rdm = randint(1,3)

if opicao == 1:
    opicao = str("tesoura") 
    print("Minha escolhar foi {}".format(opicao))
    if rdm == 1:
       rdm = str("tesoura") 
       print ("Você é o computador escolheram {}".format(rdm))
    elif rdm == 2:
       rdm = str("Papel") 
       print("Você escolheu {} é computador{} voce ganhou  ".format(opicao,rdm))
    else:
        rdm = str("Pedra") 
        print("Você perdeu, sua escolha foi {} é do computador escolheu {}".format(opicao,rdm))        


elif opicao == 2:
    opicao = str("Papel")
    print ("Minha escolhar foi {}".format(opicao))

    if rdm == 1:
       rdm = str("tesoura") 
       print("Você perdeu, sua escolha foi {} é do computador escolheu {}".format(opicao,rdm)) 
    elif rdm == 2:
        rdm = str("Papel")
        print ("Você é o computador escolheram {} então EMPATE".format(rdm))
    else:
        rdm = str("Pedra") 
        print("Você escolheu {} é computador{} voce ganhou  ".format(opicao,rdm))
    
elif opicao == 3:
    opicao = str("Pedra")
    print ("Minha escolhar foi {}".format(opicao))

    if rdm == 1:
        rdm = str("tesoura")
        print("Você escolheu {} é computador{} voce ganhou  ".format(opicao,rdm))
    elif rdm == 2:
        rdm = str("Papel")
        print("Você perdeu, sua escolha foi {} é do computador escolheu {}".format(opicao,rdm)) 
    else:
        rdm = str("Pedra")
        print ("Você é o computador escolheram {} então EMPATE".format(rdm))
else:
    print("Opção invalida ")               



