from xml.etree.ElementInclude import include
import numpy as np
import time

def reverseBits(num,bitSize):   #Reversão de Bits (número a ser revertido,quantidade de bits)
     binary = bin(num)
     reverse = binary[-1:1:-1]  
     reverse = reverse + (bitSize - len(reverse))*'0'
     #print(reverse) #número revertido em Bits
     #print(int(reverse,2))   #número revertido em Decimal
     return int(reverse,2)

def fft(x):
  N = len(x)
  tempo_inicial = time.time()
  novox = np.zeros(N, dtype = np.complex128)

  for i in range(N): #Passando a matriz de entrada para o formato complexo
    novox[i] = complex(x[i][0], x[i][1])
  N = len(novox)
  aux = N
  zeros = 0; #contador
  if(N&(N-1)): #Verificação se o tamanho do vetor é potência de 2
    print('Este número não é uma potência de 2.')
    while aux&(aux-1):
      aux += 1
      zeros += 1
    fill = (0, zeros)
    novox = np.pad(novox, fill, 'constant') #Zero Padding
    N = len(novox)

    
  else: print('Este número é uma potência de 2.')
  print("N2=",N)
  NU = int(np.log2(N)) #Número de Estágios
  y = np.zeros(N, dtype = np.complex128)

  for i in range(N): #Reordenação da matriz de entrada
    ordem = reverseBits(i,int(NU))
    y[i]= novox[ordem]
    #print("ordem =",ordem)

  A = np.zeros(2, dtype = np.complex128)

  # Borboleta
  for L in range(int(NU)):
    L+=1
    #print(L,"° estágio")
    k=0 #índice do vetor de saída
    LE = pow(2,L)
    LE1 = LE/2
    I=LE
    J = 0
    while J < int(LE1):
      I = J
      J +=1
      while I < N:
        n = J-1
        IP = I+LE1
        A[0] = y[I]
        A[1] = y[int(IP)]
        y[I] = y[I]+np.exp((-2j*np.pi*n)/LE)*y[int(IP)]
        y[int(IP)] = A[0]-np.exp((-2j*np.pi*n)/LE)*A[1]
        I+=LE
        
  tempo_final= time.time()
  print(f"{np.round(tempo_final-tempo_inicial,8)} segundos")
  i=0
  output = input('Digite o nome do arquivo de extensão .txt de saída: ')
  with open(output, 'w') as saida: #Salvando resultado num arquivo de saída txt
    while i < len(y):
      saida.write(str(y[i])+'\n')
      i+=1  

  return y