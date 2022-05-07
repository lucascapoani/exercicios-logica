
'''
Faça um algoritmo que leia uma frase e mostre: 
- A quantidade de caracters digitadas na frase

- A quantidade de vogais digitadas.
'''



'''
teste = "Frase qualquer"

print(len(teste))

for i in range(len(teste)):
    print(teste[i])


for caracter in teste:
    print (caracter)

'''

frase = input("Digite algo: ").lower()
cont = 0


for caracter in frase:
    if caracter == "a":
        cont += 1
    if caracter == "e":
        cont += 1
    if caracter == "i":
        cont += 1
    if caracter == "o":
        cont += 1
    if caracter == "u":
        cont += 1

print(f"Quantidade de caracteres= {len(frase)} - Qt. vogais= {cont}")
        
        











