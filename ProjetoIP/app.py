import time

# Dicionário que armazena os usuários e suas informações (nome, email, senha, e características dos personagens)
users = {}

# Função para criar um novo usuário
def criar_novo_usuario(email, senha):
    if email in users:
        print("Erro: O email já está cadastrado.")
    else:
        users[email] = senha
        print(f"Olá, {nome_usuario}! Você foi cadastrado com sucesso!")

# Função de login
def login(email, senha):
    # Verifica se o email está registrado e a senha corresponde
    if email in users and users[email] == senha:
        print("Login realizado com sucesso!")
    else:
        print("Erro: Email ou senha incorretos.")

# Exemplo de uso
while True:
    print("\n1. Criar novo usuário \n2. Fazer login \n3. Cancelar")
    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        # Input de email e senha para criar novo usuário
        nome_usuario = input("Digite o nome do seu personagem: ")
        novo_email = input("Digite o novo email: ")
        nova_senha = input("Digite a nova senha: ")
        criar_novo_usuario(novo_email, nova_senha)
        break

    elif escolha == '2':
        # Input de email e senha para login
        email_login = input("Digite seu email: ")
        senha_login = input("Digite sua senha: ")
        login(email_login, senha_login)
        break

    elif escolha == '3':
        print("Encerrando o programa", end="") 
        for i in range(3):
            time.sleep(0.5)  
            print(".", end="")
        print("\nPrograma encerrado.")
        quit()  

    else:
        print("Opção inválida! Tente novamente.")

# cores para o personagem
CYAN = "\033[36m"
RED = "\033[31m"
BLUE = "\033[34m"
YELLOW = "\033[33m"
RESET = "\033[0m" 

#loop para opções do jogador já logado/cadastrado no sistema
while True:
    print(f"Olá,{nome_usuario}! Está pronto para novas aventuras?")
    print("O que quer fazer?")
    print("\n1. Editar personagem \n2. Iniciar o jogo\n")
    escolha = input("Digite o número da opção: ")

    if escolha == '1':
        inteligencia = 0
        forca = 0
        habilidade = 0
        print(f'Habilidades técnicas: \n\tInteligência: {inteligencia} | Força: {forca} | Habilidade: {habilidade}')
        
        character = [
            "       ############              ",  # cabelo
            "     ################            ",  # cabelo
            "   ####################          ",  # cabelo
            "   ####  ####  ########          ",  # cabelo
            "   ####              ####        ",  # cabelo
            "   ####              ####        ",  # cabelo
            " ######  ***     ***   ##        ",  #
            " ####                ####        ",
            " ####                ####        ",
            " ########        ########        ",  # cabelo
            "           &&  &&                ",
            "     &&&&++++++++++&&&&          ",
            "   &&++++++++++++++&&++          ",
            "   &&&&++++++++++++++&&          ",
            "   &&&&++++++++++++++&&          ",
            "       ++++&&&&++++++            ",
            "       &&&&&&&&&&&&&&            ",
            "         &&&&&&&&&&        "
        ]

        print(character)
        

        # Iterando sobre as linhas do personagem
        for row in character:
            # Se a linha contém parte do cabelo, imprime em vermelho
            if "####" in row:  # Condição simplificada para detectar o cabelo
                print(f"{RED}{row}{RESET}")
            elif "++" in row:
                print(f"{BLUE}{row}{RESET}")
            elif "&&&&&&&&&&" in row:
                print(f"{YELLOW}{row}{RESET}")
            else:
                print(row)
                
    elif escolha == '2':
        print("Iniciando o jogo", end="") 
        for i in range(3):
            time.sleep(0.5)  
            print(".", end="")
        print("\nEm breve.")
        quit()
    else:
        print("Opção inválida! Tente novamente.")



def editarPersonagem():
    print

def exibirRelatorio():
    print('')