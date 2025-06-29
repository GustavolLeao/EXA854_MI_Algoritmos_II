# /*******************************************************************************
# Autor: Gustavo Leão de Jesus
# Componente Curricular: MI Algoritmos I
# Concluido em: 28/04/2025
# Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
# trecho de código de outro colega ou de outro autor, tais como provindos de livros e
# apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
# de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
# do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
# Este software foi criado em Python versão 3.13.1 e desenvolvido no sistema operacional 
# Windows 10 de 64 bits.
# ******************************************************************************************/

import time
import os

# Limpar o terminal de acordo o sistema operacional. 
def limpar():
    if os.name == "nt": 
        os.system("cls") # Windows
    else:
        os.system("clear") # Linux/Mac

# Verificar a entrada do usuário e quantidade de Células máximas.
def verificacao():

    print()
    matriz()
    print()

    while True:
        try:
            num = int(input("Determine a quantidade de células vivas: "))
            if 0 < num <= 100:   
                return num

            else:
                print("\nInforme números de 1 a 100\n")
        except ValueError:
            print("\nDigite um valor válido!\n")

# Adiciona as posições temporariamente em uma lista.
def posicao():
    while True:

        try:
            print()
            print("=" * 42)
            print("\nPara remover, informe a posição da célula.")
            print("Determine as posições de 0 a 9.")
            x = int(input("\n[Linha]: "))
            y = int(input("[Coluna]: "))
            print()

            if 0 <= x <= 9 and 0 <= y <= 9:
                eixos.append(x) # Posição 0 
                eixos.append(y) # Posição 1
                print("=" * 42)
                return eixos
            else:
                print("\nDigite uma posição existente!")
        except ValueError:
            print("\nDigite um valor válido!")

# Adiciona ou remove as células vivas nas posições fornecidas.
def celulas(): 
    global vivas # Contabiliza o total de células vivas.
    global num # Monitora a quantidade de edições na Matriz.
    for l in range(len(Matriz)): 
        for c in range(len(Matriz)):
            if l == eixos [0] and c == eixos [1]:
                if Matriz [l] [c] != "O":
                    Matriz [l] [c] = "O"
                    vivas += 1
                else:
                    # Se o usuário repetir a posição de uma célula viva
                    # ela se converte-se em morta.
                    Matriz [l] [c] = "X"
                    vivas -= 1
                    # Garante que as conversões não interfiram na quantidade de células.
                    num += 2 

    eixos.clear() # Limpa a lista com dois elementos, para que outras posições sejam armazenadas.
    print()
    matriz()
    return vivas 

# Exibição da Matriz.
def matriz():
    for l in range(len(Matriz)):

        if l == 0:
            print("     ", end="") 
            for i in coluna: 
                print(f"{i}", end="  ")

            print("\n" ,"   ", end="")
            print()

        print(l, end="    ") 
        for c in range(len(Matriz)):
            print(f"{Matriz [l] [c]}", end="  ")
        print()

def titulo(palavra):
    tamanho = len(palavra)
    meio = ((42 - tamanho) // 2) - 1
    print("=" * 42)
    print(" " * meio, palavra)
    print("=" * 42)
    print()

# Local das Listas e Variáveis.
Matriz = []
eixos = []
coluna = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
on = 0
vivas = 0

for i in range(10):
    linha = []
    for i in range(10):
        linha.append("X")
    Matriz.append(linha)

titulo("O jogo da Vida")

print("         Simbolos das Células:\n")
print("     [O] VIVAS         [X] MORTAS")

# Recebe a quantidade de células para usar no laço de repetição.
num = verificacao()

# Laço que se repete até o usuário inserir todas as células vivas desejadas. 
while on == 0 and vivas != 100:

    while num != 0 and vivas != 100:
        num -= 1
        eixos = posicao()
        limpar()
        vivas = celulas()

    if vivas != 100:    
        print()
        print("=" * 42)
        print()
        print("[S] para Sim")
        print("[N] para Não\n")

        continua = input("Adicionar mais células? ")
        s_vazio = continua.strip()
        caps = s_vazio.upper()
        while caps != "S" and caps != "N":
            print("Entrada incorreta!")
            continua = input("Adicionar mais células? ")
            s_vazio = continua.strip()
            caps = s_vazio.upper()

        print()
        print("=" * 42)
        if caps == "S":
            limpar()
            num = verificacao()
            
        elif caps == "N":
            start = input("Precione ENTER: ")
            print("=" * 42)

            on += 1

while vivas != 0:
    
    # Percorre todos os elementos da Matriz indetificando células vivas ou mortas.
    for l in range(len(Matriz)):
        for c in range(len(Matriz)):

            vizinho = 0

            # Verificações superior.
            if l -1 >= 0:
                # Em cima da célula.
                if Matriz [l - 1] [c] == "O":
                    vizinho += 1

                # Verificação superior da borda esquerda.   
                if c - 1 >= 0:   
                    # Diagonal esquerda.
                    if Matriz [l - 1] [c - 1] == "O":
                        vizinho += 1

                # Verificação superior da borda direita.
                if c + 1 <= 9:
                    # Diagonal direita.
                    if Matriz [l - 1] [c + 1] == "O":
                        vizinho += 1

            # Verificação da lateral esquerda.
            if c -1 >= 0:
                # Lado esquerdo.
                if Matriz [l] [c - 1] == "O":
                    vizinho += 1

            # Verificação da lateral direita.
            if c + 1 <= 9:
                # Lado direito.
                if Matriz [l] [c + 1] == "O":
                    vizinho += 1

            # Verificação inferior.
            if l + 1 <= 9:
                # Embaixo da célula
                if Matriz [l + 1] [c] == "O":
                    vizinho += 1
                # diagonal esquerda.
                if c -1 >= 0:
                    if Matriz [l + 1] [c - 1] == "O":
                        vizinho += 1

                # Diagonal direita 
                if c + 1 <= 9:
                    if Matriz [l + 1] [c + 1] == "O":
                        vizinho += 1

            if Matriz [l] [c] == "O":

                if vizinho < 2:
                    titulo("Solidão")

                    Matriz [l] [c] = "X"
                    vivas -= 1

                if vizinho == 2 or vizinho == 3:
                    titulo("Sobrevivência")

                if vizinho > 3:
                    titulo("Superpopulação")

                    Matriz [l] [c] = "X"
                    vivas -= 1

                matriz()
                time.sleep(0.5)
                limpar()

            if vizinho == 3 and Matriz [l] [c] == "X":
                titulo("Reprodução")

                Matriz [l] [c] = "O"
                vivas += 1

                matriz()
                time.sleep(0.5)
                limpar()

titulo("Fim")    

matriz()

fim = input("\nPrecione ENTER para sair: ")
    