import time

# Dicionário que armazena os usuários e suas informações (email, senha, e características dos personagens)

users = {}

# cores para o personagem

CYAN = "\033[36m"
RED = "\033[31m"
BLUE = "\033[34m"
YELLOW = "\033[33m"
RESET = "\033[0m" 


# Função para criar um novo usuário
def criar_novo_usuario(email, senha):
    if email in users:
        print("Erro: O email já está cadastrado.")
    else:
        users[email] = {
                'senha': senha,
                'personagem': {
                        'forca': 0,
                        'inteligencia': 0,
                        'habilidade': 0
         } 
        }

        print(f"Você foi cadastrado com sucesso!")
        time.sleep(0.5)

# Função de login
def login(email, senha):
    # Verifica se o email está registrado e a senha corresponde
    if email in users and users[email] == senha:
        print("Login realizado com sucesso!\n")
    else:
        print("E-mail ou senha incorretos. Tente novamente.")
        quit()


def editar_personagem(usuario):
    personagem = users[usuario]['personagem']
    print("\nEscolha a habilidade para editar:")
    print("1. Inteligência\n2. Força\n3. Habilidade")
    escolha = input("Digite o número da habilidade: ")
    if escolha == '1':
        personagem['inteligencia'] = int(input("Defina o valor da Inteligência (0-10): "))
    elif escolha == '2':
            personagem['forca'] = int(input("Defina o valor da Força (0-10): "))
    elif escolha == '3':
            personagem['habilidade'] = int(input("Defina o valor da Habilidade (0-10): "))
    else:
            print("Opção inválida!")
    
    print(f'Habilidades atualizadas: Inteligência: {personagem["inteligencia"]}, Força: {personagem["forca"]}, Habilidade: {personagem["habilidade"]}')
    
def exibir_personagem(usuario):
    personagem = users[usuario]['personagem']
    print(f'\nHabilidades técnicas:\n\n\tInteligência: {personagem['inteligencia']} | Força: {personagem['forca']} | Habilidade: {personagem['habilidade']}\n')
    
        
    character = [
            "       ############              ",  # cabelo
            "     ################            ",  # cabelo
            "   ####################          ",  # cabelo
            "   ####  ####  ########          ",  # cabelo
            "   ####              ####        ",  # cabelo
            "   ####              ####        ",  # cabelo
            " ######  ***     ***   ##        ",  # cabelo
            " ####                ####        ",  # cabelo
            " ####                ####        ",  # cabelo
            " ########        ########        ",  # cabelo
            "           &&  &&                ",  # tronco
            "     &&&&++++++++++&&&&          ",  # tronco
            "   &&++++++++++++++&&++          ",  # tronco
            "   &&&&++++++++++++++&&          ",  # tronco
            "   &&&&++++++++++++++&&          ",  # tronco
            "       ++++&&&&++++++            ",  # tronco
            "       $$$$$$$$$$$$$$            ",  # pés
            "         $$$$$$$$$$        "         # pés
        ]
    
    # cabelo são "#"
    # tronco é "&" e "+"
    # pés são "$"

        # iterando sobre as linhas do personagem
    for row in character:
        if "#" in row:  # Condição simplificada para detectar o cabelo
            print(f"{CYAN}{row}{RESET}")
        elif "+" in row:
            print(f"{BLUE}{row}{RESET}")
        elif "$" in row:
            print(f"{YELLOW}{row}{RESET}")
        else:
            print(row)

# acabaram as funções

# entrando no loop inicial do programa (cadastro e login)
while True:
    print("O que você quer fazer? ")
    print("\n1. Criar novo usuário \n2. Fazer login \n3. Cancelar")
    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        # Input de email e senha para criar novo usuário
        nome_usuario = input("Digite o nome do seu personagem: ")
        novo_email = input("Digite o novo email: ")
        nova_senha = input("Digite a nova senha: ")
        criar_novo_usuario(novo_email, nova_senha)
        time.sleep(0.3)

    elif escolha == '2':
        # Input de email e senha para login
        email_login = input("Digite seu email: ")
        senha_login = input("Digite sua senha: ")
        login(email_login, senha_login)


    elif escolha == '3':
        print("Encerrando o programa", end="") 
        for i in range(3):
            time.sleep(0.5)  
            print(".", end="")
        print("\nPrograma encerrado.")
        quit()  

    else:
        print("Opção inválida! Tente novamente.")


print(f"Olá, {nome_usuario}! Está pronto para novas aventuras?")
# loop para opções do jogador já logado/cadastrado no sistema
while True:
    print("\nO que quer fazer?")
    print("1. Editar personagem \n2. Iniciar o jogo\n3. Sair do sistema.")
    escolha = input("Digite o número da opção: ")

    if escolha == '1':
        print("\n1. Exibir meu personagem. \n2. Editar meu personagem")
        escolha_personagem = input("O que você quer fazer? ")
        if escolha_personagem == "1": 
            exibir_personagem(email_login)
        if escolha_personagem == "2":
            editar_personagem(email_login)
                
    elif escolha == '2':
        print("Iniciando o jogo", end="") 
        for i in range(3):
            time.sleep(0.5)  
            print(".", end="")
        print("\nEm breve. Esta parte está em desenvolvimento!")
        quit()
    elif escolha == '3':
        print('Encerrando o sistema', end="")
        for i in range(3):
            time.sleep(0.5)
            print(".", end="" )
        quit()
    else:
        print("Opção inválida! Tente novamente.")



