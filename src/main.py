
# Written by Evert Ramos

# Função de impressão para exibir mensagens coloridas
def printc(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")
def erro(text):
    printc("\n[ERRO] " + text + "\n", "91")  # Vermelho
def sucesso(text):
    printc(text, "92")  # Verde
def aviso(text):
    printc(text, "93")  # Amarelo
def padrao(text):
    printc(text, "33") 

# Função de input colorido
def inputc(text, color_code):
    return input(f"\033[{color_code}m{text}\033[0m")
def pergunta(text):
    return inputc(text, "94")  # Azul


# Escolher os jogos
def escolher_jogos():
    jogos = ["Mega", "Quina"]
    padrao("Escolha um jogo:")
    for i, jogo in enumerate(jogos, start=1):
        padrao(f"{i}. {jogo}")
    padrao("0. Voltar ao menu")
    try:
        escolha_jogo = int(pergunta("Digite o número do jogo escolhido: "))
        print()
        match escolha_jogo:
            case 0:
                return  # Voltar ao menu principal
            case 1:
                sucesso("Você escolheu o jogo Mega.")
            case 2:
                sucesso("Você escolheu o jogo Quina.")
            case _:
                erro("Opção inválida, por favor escolha uma das opoções indicadas.")
                return escolher_jogos()
    except ValueError:
        erro("Entrada inválida, por favor insira um número.")
        return escolher_jogos()

# Menu da aplicação
while True:
    print()
    padrao("Menu:")
    padrao("1. Jogar")
    padrao("2. Opção 2")
    padrao("3. Sair")

    try:
        escolha = int(pergunta("Escolha uma opção: "))
        print() 
    except ValueError:
        erro("Entrada inválida, por favor insira um número.")
        continue

    if escolha == 1:
        escolher_jogos()
    elif escolha == 2:
        print("Você escolheu a Opção 2.")
    elif escolha == 3:
        break
    else:
        print("Opção inválida, tente novamente.")

print('Programa encerrado.')