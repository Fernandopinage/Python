#Desenvolvar um programa que pergunte a distancia de uma viagem em KM.
#Calcule o preço  da passagem, combrando R$0,50 por KM para cada viagem ate 200km e 0,45 para viagem  mas longas

viagem = float(input('informe a distancia da viagem: '))


if viagem <= 200:

    preco = (viagem * 0.50)
    print ("Sua viagem vai custa {}R$".format(preco))

else : 
    preco =  (viagem * 0.45)
    print ("Sua viagem vai custa {}R$".format(preco))