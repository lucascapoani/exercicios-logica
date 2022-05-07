''' 
1                 1
12               21
123             321
1234           4321
12345         54321
123456       654321
1234567     7654321
12345678   87654321
123456789 987654321
'''



linha = ""
final = ""
tam = 17

for i in range (1,10):
    linha = linha + str(i)
    final = str(i) + final
    
    print (linha + "."*tam + final)
    tam -= 2
