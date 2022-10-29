import numpy as np
def file_input():
    arquivo = input('Digite o endereço do arquivo de entrada: ')
    fileID = open(arquivo);
    x = np.loadtxt(fileID,delimiter=' ');
    fileID.close()