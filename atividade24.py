# Crie um programa que receba uma quantidade indefinida de números do usuário. 
# O programa deve calcular a média desses números e parar quando o usuário digitar -1.]
soma = 0
contar = 0
while True:
    n1 = float(input('Digite um numero:'))
    if n1 == -1:
         break
    
    soma = soma + n1
    contar = contar + 1

    media= soma/contar
print(media)
    
        

   




    

