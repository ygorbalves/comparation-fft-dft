import numpy as np
import time

def dft(x):
  tempo_inicial=time.time()#em segundos
  N = len(x)
  y = np.zeros(N, dtype = np.complex128)

  novox = np.zeros(N, dtype = np.complex128)
  for i in range(N): #Passando a matriz de entrada para o formato complexo
    novox[i] = complex(x[i][0], x[i][1])

  for i in range(N): # k = i
    for j in range(N): # n = j
      y[i] += np.round(novox[j]*np.exp((-2j*np.pi*i*j)/N),5)
  tempo_final=time.time()# em segundos
  print(f"{np.round(tempo_final-tempo_inicial,8)} segundos")
  i=0
  output = input('Digite o nome do arquivo de extensão .txt de saída: ')
  with open(output, 'w') as saida: #Salvando resultado num arquivo de saída txt
    while i < len(y):
      saida.write(str(y[i])+'\n')
      i+=1  
  return y #Resultado Final obtido

