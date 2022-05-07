"""
Exercício extra 1.
Crie um algoritmo para escrever o que segue:
1
12
123
1234
12345
123456
1234567
"""


"""

linha = ""
for i in range (1,8):
    linha = linha + str(i)
    print (linha)

"""


# --------------------- Outra maneira de fazer --------------------------- #


linha = 0
for i in range (1,8):
    linha = linha * 10 + i
    print(linha)
