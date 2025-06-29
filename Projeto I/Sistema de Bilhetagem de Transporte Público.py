# /*******************************************************************************
# Autor: Gustavo Leão de Jesus
# Componente Curricular: MI Algoritmos
# Concluido em: 14/03/2025
# Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
# trecho de código de outro colega ou de outro autor, tais como provindos de livros e
# apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
# de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
# do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
# ******************************************************************************************/

# A variável "recarga_total" irá armazenar todas as recargas realizadas pelo programa. 
# Variáveis que contém "_r" no nome receberão o número de recargas realizadas por cada usuário/categoria.
# Variáveis que contém "_p" no nome receberão a quantidade de passagens usadas por cada usuário/categoria. 
# Variáveis que contém "_g" no nome receberão o valor gasto com passagens por cada usuário/categoria.
# Variáveis que contém "_s" no nome contabilizarão o saldo restante a ser utilizado por cada categoria.

# Local das Variáveis 
recarga_total = 0

padrao_r = 0
estudIdoso_r = 0
social_r = 0

padrao_p = 0
estudIdoso_p = 0
social_p = 0

padrao_g = 0
estudIdoso_g = 0
social_g = 0

padrao_s = 0
estudIdoso_s = 0
social_s = 0

Passagem = 0

# Validação do valor da passagem do tipo float. 
on = 0

# Validação do valor da passagem: garante que seja um número positivo
while on == 0 or Passagem < 0:
    
    # O método try-except permite tratar possíveis erros que podem ocorrer  
    # durante a execução do programa devido a entradas inválidas do usuário.
    try: 
        print("=" * 50)
        Passagem = float(input("Digite o valor da Tarifa atual: "))
        on += 1
    except ValueError: # 
        print("Digite um valor válido!")

# Laço de repetição principal do código que funciona de acordo 
# com a entrada do usuário, as opções variam de 0 a 4 e são 
# análisadas pelas estruturas condicionais para direcionar
# o usuário nas opções do menu. 

# A variável "on" mantém o loop ativo, se o usuário digitar a opção 4, 
# "on" vai receber o valor 1, encerrando o loop. 
on = 0

while on == 0:
    
    print("=" * 50)
    print("- " * 10,"[MENU]"," -" * 11)
    print("=" * 50,"\n")
    print("[0] Relatório")
    print("[1] Recarga")
    print("[2] Comprar")
    print("[3] Saldo")
    print("[4] Encerrar Sessão\n")
    print("=" * 50)
    opcoes = input("Digite qual a opção desejada: ")
    print("=" * 50)

    # Opção do administrador (Relatório). 
    if opcoes == "0":
        print("- " * 9,"[RELATÓRIO] ","- " * 9)
        print("=" * 50)
        print(f"Quantidade de recargas totais: ____ {recarga_total}\n")

        print(f"Número de recargas realizadas por categoria:\n")
        print(f"Usuário padrão: ___________________ {padrao_r}")
        print(f"Estudante/Idoso: __________________ {estudIdoso_r}")
        print(f"Social: ___________________________ {social_r}")       

        print(f"\nQuantidade de passagens usadas por categoria:\n")
        print(f"Usuário padrão: ___________________ {padrao_p}")
        print(f"Estudante/Idoso: __________________ {estudIdoso_p}")
        print(f"Social: ___________________________ {social_p}")   

        print(f"\nValor total gasto com passagens por categoria:\n")
        print(f"Usuário padrão: ___________________ R$ {padrao_g:.2f}")
        print(f"Estudante/Idoso: __________________ R$ {estudIdoso_g:.2f}")
        print(f"Social: ___________________________ R$ {social_g:.2f}")  

        print(f"\nSaldo restante a ser utilizado por categoria:\n")
        print(f"Usuário padrão: ___________________ R$ {padrao_s:.2f}")
        print(f"Estudante/Idoso: __________________ R$ {estudIdoso_s:.2f}")
        print(f"Social: ___________________________ R$ {social_s:.2f}")  
    
    # Opção de recarga
    elif opcoes == "1":
        
        print("- " * 9,"[RECARGA]"," -" * 10 )
        print("=" * 50)
        lig = 0
        recarga = 0

        while lig == 0 or recarga <= 0:
            try:
                recarga = float(input("Valor da recarga: "))
                lig += 1
                print("=" * 50, "\n")
            except ValueError:
                print("Digite um valor válido: ")
        
        print("[1] Usuário padrão")
        print("[2] Estudante/Idoso")
        print("[3] Social\n")

        print("=" * 50)
        categoria = input("Digite qual categoria será recarregada: ")

        while categoria != "1" and categoria != "2" and categoria != "3":
            categoria = input("Digite qual categoria será recarregada: ")

        print("Recarga concluída!")
        
        # As linhas a seguir processam a entrada do usuário para identificar 
        # a categoria que receberá o valor da recarga e atualizar o relatório.
        if categoria == "1":
            recarga_total += 1
            padrao_r += 1
            padrao_s += float(recarga)

        elif categoria == "2":
            recarga_total += 1
            estudIdoso_r += 1
            estudIdoso_s += float(recarga)

        elif categoria == "3":
            recarga_total += 1
            social_r += 1
            social_s += float(recarga)

    # Opção de compra de passagens
    elif opcoes == "2":
        
        print("- " * 7, "[COMPRAR PASSAGEM]"," -" * 8)
        print("=" * 50)
        print(f"Valor da tarifa: R$ {Passagem:.2f}\n")

        print("[1] Usuário padrão")
        print("[2] Estudante/Idoso")
        print("[3] Social\n") 
        print("=" * 50)

        categoria = input("Digite qual categoria vai comprar a passagem: ")

        while categoria != "1" and categoria != "2" and categoria != "3":
            categoria = input("Digite um valor válido: ")
        
        print("=" * 50)
        print("\n[1] Sim")
        print("[2] Não\n")
        print("=" * 50)

        # O valor da passagem só será descontado do saldo se o usuário confirmar o pagamento, 
        # se a entrada for igual a 1, o programa realizará todas as operações normalmente, 
        # entretanto, se a entrada for igual a 2, o usuário retornará ao menu sem comprar a passagem.
        confirmar = input("Confirmar pagamento: ")

        while confirmar != "1" and confirmar != "2":
            confirmar = input("Digite um valor válido: ")

        # Para realizar as operações, primeiro é avaliado o saldo atual da categoria  
        # em comparação com o valor da passagem, considerando os descontos.  
        # Somente se o saldo for igual ou maior, é possível embarcar no transporte.
        chave = 0
        while chave == 0 and confirmar == "1":

            chave += 1
            # Usuário padrão
            if categoria == "1":
                
                if padrao_s >= Passagem:
                    padrao_s -= Passagem
                    padrao_p += 1
                    padrao_g += float(Passagem)

                    print(f"Seu saldo restante é R$ {padrao_s:.2f}")

                else:
                    print("Saldo insuficiente! recarregue antes de comprar.")

            # Estudante/Idoso
            elif categoria == "2":
                valor = Passagem * 50/100
                if estudIdoso_s >= valor:
                    estudIdoso_s -= valor
                    estudIdoso_p += 1
                    estudIdoso_g += valor

                    print(f"Seu saldo restante é R$ {estudIdoso_s:.2f}")

                else:
                    print("Saldo insuficiente! recarregue antes de comprar.")

            # Social    
            elif categoria == "3":
                valor = Passagem * 20/100
                if social_s >= valor:
                    social_s -= valor
                    social_p += 1
                    social_g += valor

                    print(f"Seu saldo restante é R${social_s:.2f}")

                else:
                    print("Saldo insuficiente! recarregue antes de comprar")

    # Opção de ver o saldo
    elif opcoes == "3":
        
        print("- " * 10, "[SALDO]"," -" * 10)
        print("=" * 50)

        print("\n[1] Usuário padrão")
        print("[2] Estudante/Idoso")
        print("[3] Social\n") 
        print("=" * 50)

        categoria = input("Ver saldo de qual categoria? ")

        while categoria != "1" and categoria != "2" and categoria != "3":
            categoria = input("Digite um valor válido: ")

        if categoria == "1":

            print(f"Seu saldo é: R$ {padrao_s:.2f}")

        elif categoria == "2":

            print(f"Seu saldo é: R$ {estudIdoso_s:.2f}")

        elif categoria == "3":

            print(f"Seu saldo é: R$ {social_s:.2f}")

    # Opção de encerrar a sessão atribuindo 1 no valor da variável "on".
    elif opcoes == "4":
        on += 1

    # Validação do Menu
    else:
        print(f"'{opcoes}' Não é uma opção válida!")
