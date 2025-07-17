
# Written by Evert Ramos

# Importa funções externas
from utils.print import sucesso, erro, aviso, padrao, pergunta

# Escolher os jogos
def escolher_jogos():
    jogos = ['Mega', 'Quina']
    padrao('Escolha um jogo:')
    for i, jogo in enumerate(jogos, start=1):
        padrao(f'{i}. {jogo}')
    padrao('0. Voltar ao menu')
    try:
        escolha_jogo = int(pergunta('Digite o número do jogo escolhido: '))
        print()
        match escolha_jogo:
            case 0:
                return  # Voltar ao menu principal
            case 1:
                mega()
            case 2:
                quina()
            case _:
                erro('Opção inválida, por favor escolha uma das opoções indicadas.')
                return escolher_jogos()
    except ValueError:
        erro('Entrada inválida, por favor insira um número.')
        return escolher_jogos()
    print('<fim [Jogar]')

# Jogo Mega
def mega():
    # Definir variáveis do jogo
    qtd_numeros = 6
    limite_numeros = 60
    numeros = []

    # Escolha dos números
    padrao(f'Escolha {qtd_numeros} números entre 1 e {limite_numeros}:')
    for i in range(qtd_numeros):
        while True:
            try:
                print()
                padrao(f'Números escolhidos: {numeros}')
                numero = int(pergunta(f'Digite o {i + 1}° número: '))
                if numero in numeros:
                    aviso(f'Número {numero} já foi escolhido, escolha outro.')
                elif numero < 1 or numero > limite_numeros:
                    aviso(f'Número {numero} fora do intervalo. Escolha um número entre 1 e {limite_numeros}.')
                else:
                    numeros.append(numero)
                    break
            except ValueError:
                erro('Número inválido, tente novamente.')

    # Confirmação dos números
    aviso(f'Os números escolhidos foram: {numeros}')
    confirmacao = pergunta('Confirma? (s/n): ')
    if confirmacao.lower().strip() != 's':
        return mega() # Reinicia o jogo
    print()
    sucesso('Seu jogo foi confirmado!')
    print('<fim [Mega]')


# Jogo Quina
def quina():
    qtd_numeros = 5
    numeros = []
    print('Iniciando o jogo Quina...')

# Menu da aplicação
while True:
    print()
    padrao('Menu:')
    padrao('1. Jogar')
    padrao('2. Opção 2')
    padrao('0. Sair')
    print()
    padrao('00. Para sair em qualquer tela!')
    print()

    try:
        escolha = int(pergunta('Escolha uma opção: '))
        print('<fim [Menu]')
        print() 
    except ValueError:
        erro('Entrada inválida, por favor insira um número.')
        continue

    if escolha == 0:
        break
    elif escolha == 1:
        escolher_jogos()
    elif escolha == 2:
        print('Você escolheu a Opção 2.')
    else:
        print('Opção inválida, tente novamente.')
    
print('Programa encerrado.')