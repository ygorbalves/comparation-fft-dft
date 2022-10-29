def reverseBits(num,bitSize):   #Reversão de Bits (número a ser revertido,quantidade de bits)
     binary = bin(num)
     reverse = binary[-1:1:-1]  
     reverse = reverse + (bitSize - len(reverse))*'0'
     #print(reverse) #número revertido em Bits
     #print(int(reverse,2))   #número revertido em Decimal
     return int(reverse,2)