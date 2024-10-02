import time

# Dicionário que armazena as informções do usuário (nome, email, senha, e características dos personagens)
users = {}

# Função para criar um novo usuário
def criar_novo_usuario(email, senha):
    if email in users:
        print("Erro: O email já está cadastrado.")
    else:
        # adicionando o email pra associar
        users[email] = {
            'senha': senha,
            'nome': nome_usuario,
            'personagem': {
                'inteligencia': 0,
                'forca': 0,
                'habilidade': 0
            }
        }

# Função de login
def login(email, senha):
    # Verifica se o email está registrado e a senha corresponde
    if email in users and users[email] == senha:
        print("Login realizado com sucesso!")
    else:
        print("E-mail ou senha incorretos! Tente novamente.")


# Função para o usuário escolher a cor
def escolhacor(parte):
    print(f"Escolha a cor para {parte}:")
    print("1. Vermelho\n2. Azul\n3. Amarelo\n4. Ciano")
    cor = input("Digite o número da cor: ")
    
    if cor == '1':
        return "\033[31m"  # Vermelho
    elif cor == '2':
        return "\033[34m"  # Azul
    elif cor == '3':
        return "\033[33m"  # Amarelo
    elif cor == '4':
        return "\033[36m"  # Ciano
    else:
        print("Opção inválida, cor padrão será usada.")
        return "\033[0m"  # Padrão (sem cor)
    
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

# # cores para o personagem
# CYAN = "\033[36m"
# RED = "\033[31m"
# BLUE = "\033[34m"
# YELLOW = "\033[33m"
# RESET = "\033[0m" 

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
            "       ############              ",  # "#" é cabelo
            "     ################            ",  # "&" é "+" é tronco
            "   ####################          ",  # $ é pé
            "   ####  ####  ########          ",  
            "   ####              ####        ",  
            "   ####              ####        ",  
            " ######  ***     ***   ##        ",  
            " ####                ####        ",  
            " ####                ####        ",
            " ########        ########        ",  
            "           &&  &&                ",
            "     &&&&++++++++++&&&&          ",
            "   &&++++++++++++++&&++          ",
            "   &&&&++++++++++++++&&          ",
            "   &&&&++++++++++++++&&          ",
            "       ++++&&&&++++++            ",
            "       $$$$$$$$$$$$$$            ",
            "         $$$$$$$$$$        "
        ]

        print(character)
        # Cores escolhidas pelo usuário
        corcabelo = escolhacor("cabelo")
        cortronco = escolhacor("tronco")
        corpe = escolhacor("pés")
        RESET = "\033[0m"  # Reseta a cor para o padrão

        # Iterando sobre as linhas do personagem
        for row in character:
            # Se a linha contém parte do cabelo, imprime em vermelho
            if "####" in row:  # Condição simplificada para detectar o cabelo
                print(f"{corcabelo}{row}{RESET}")
            elif "++" in row:
                print(f"{cortronco}{row}{RESET}")
            elif "&&&&&&&&&&" in row:
                print(f"{corpe}{row}{RESET}")
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
    print("\nSeu personagem possui as seguintes habilidades:")
    print(f"Inteligência: {personagem['inteligencia']}")
    print(f"Força: {personagem['forca']}")
    print(f"Habilidade: {personagem['habilidade']}")
