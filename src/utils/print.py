def printc(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")

def erro(text):
    printc("\n[ERRO] " + text + "\n", "91")  # Vermelho

def sucesso(text):
    printc(text, "92")  # Verde

def aviso(text):
    printc(text, "93")  # Amarelo

def padrao(text):
    printc(text, "33")  # Amarelo padrão
