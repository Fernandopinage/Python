# crie um pragrama que tenha uma tupla totalmente preenchida com uma contagem em extenso, de zero  até vinte.
# seu programa devera ler um numero entre 0 a 20 e mostralo por extenso

cont = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez',
'onze','doze','treze','quatoze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte',)

while True:
    num = int(input('Digite um numero entre 0 a 20 : '))
    if num <= 20 :
        break
    else:
        print('Tente novamente.',end=" ")
print('Voce digitou um numero {}'.format(cont[num]))