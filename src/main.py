
# Written by Evert Ramos

# Importa funções externas
from utils.print import sucesso, erro, aviso, padrao

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
                mega()
            case 2:
                quina()
            case _:
                erro("Opção inválida, por favor escolha uma das opoções indicadas.")
                return escolher_jogos()
    except ValueError:
        erro("Entrada inválida, por favor insira um número.")
        return escolher_jogos()
    print("---fim [Jogar]---")

# Jogo Mega
def mega():
    qtd_numeros = 6
    numeros = []
    print("Iniciando o jogo Mega...")

# Jogo Quina
def quina():
    qtd_numeros = 5
    numeros = []
    print("Iniciando o jogo Quina...")

# Menu da aplicação
while True:
    print()
    padrao("Menu:")
    padrao("1. Jogar")
    padrao("2. Opção 2")
    padrao("0. Sair")

    try:
        escolha = int(pergunta("Escolha uma opção: "))
        print("---fim [Menu]---")
        print() 
    except ValueError:
        erro("Entrada inválida, por favor insira um número.")
        continue

    if escolha == 0:
        break
    elif escolha == 1:
        escolher_jogos()
    elif escolha == 2:
        print("Você escolheu a Opção 2.")
    else:
        print("Opção inválida, tente novamente.")
    
print('Programa encerrado.')