# Transformada Rápida de Fourier (FFT) e Transformada Discreta de Fourier (DFT)
## Comparação entre o tempo de execução - Python
- A DFT consiste na conversão de um sinal no domínio do tempo  para o domínio da frequência. A implementação da DFT é dada pela seguinte expressão:
![image](https://user-images.githubusercontent.com/77367268/198637281-96124425-b399-4e17-8c28-f0863575f768.png)
- É uma ferramenta matemática de grande aplicabilidade na solução dos problemas de processamento digital de imagens, pois o sinal no domínio da frequência tem seu processamento facilitado. Somado a isso, tem-se aplicabilidade em análise de falhas, controle de qualidade e monitoramento de condições de máquinas ou sistemas.
- A FFT é um algoritmo otimizado para a implementação da DFT, portanto, visando comparar as duas implementações e validar a eficácia da FFT, as duas transformadas foram implementadas em Python, comparando o custo computacional (tempo de execução do código) de ambas.
- A partir de um arquivo de Entrada no formato 'txt' com a primeira coluna sendo a componente real e a segunda coluna a componente imaginária, deve-se obter o arquivo de saída após os cálculos realizados. Como exemplo de Entrada e Saída a seguir:
![compare](https://user-images.githubusercontent.com/77367268/198651509-f22dc8ad-9598-42f2-bc8d-ef1a22a24129.png)
- Visando validar o custo computacional, foi utilizado um arquivo de entrada com 2048 números (linhas).  

## Tempo de execução da DFT:
- A implementação em Python da DFT é chamada pela função dft(x), em que x é o arquivo de entrada. O tempo de execução do programa foi de: 
## *72.928784 segundos*

## Tempo de execução da FFT:
- A implementação em Python da FFT é chamada pela função fft(x), em que x é o arquivo de entrada. O tempo de execução do programa foi de: 
## *0.103755 segundos*

## Comparação
- Ou seja, validando a eficácia da FFT frente a DFT, a FFT obteve um *tempo de execução 702x menor*.

**O estatístico estadunidense John Tukey estava certo !! hehe**

# fft_dft_package

Description. 
The package fft_dft is used to:
	- Transforms
		- DFT
		- FFT
	- Utils
		- Time comparator
		- Reverse bits
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install package_name

```bash
pip install fft_dft
```

## Author
Ygor

## License
[MIT](https://choosealicense.com/licenses/mit/)






