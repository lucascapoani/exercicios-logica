''' 
Exercício extra 2.
Crie um algoritmo para msotrar na tela o que segue:
Digite a quantidade de linhas para montar a figura: 9
        #
       ##
      ###
     ####
    #####
   ######
  #######
 ########
#########
'''

"""
e = 9
for i in range (10):
    print(" "*e + "#"*i)
    e = e - 1
"""


### --------------- Outra maneira de resolver --------------------#

for i in range (10):
    print (" "*(10 - i) + "#"*i)
