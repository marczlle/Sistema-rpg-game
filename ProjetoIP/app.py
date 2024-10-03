import time

# dicionário que armazena os usuários e suas informações (email, senha, e características dos personagens)

users = {}

# cores para o personagem   
cores = {
    '1': "\033[36m",  # ciano
    '2': "\033[31m",  # vermelho
    '3': "\033[34m",  # azul
    '4': "\033[33m",  # amarelo
    'reset': "\033[0m"
}

# função para criar um novo usuário no dicionário de usuários
def criar_novo_usuario(email, senha):
    if email in users:
        print("O email já está cadastrado!")
    else:
        users[email] = {
                'senha': senha,
                'personagem': {
                        'forca': 0,
                        'inteligencia': 0,
                        'habilidade': 0,
                'aparencia': {
                    'cabelo': cores['reset'],  # deixei reset como padrao pra iniciar
                    'tronco': cores['reset'],  
                    'pes': cores['reset']  
                }
         } 
        }

        print(f"Você foi cadastrado com sucesso!\n")
        time.sleep(0.5)

# função que valida o login
def login(email, senha):
    # faz a comparacao
    if email in users and users[email]["senha"] == senha:
        print("Login realizado com sucesso!\n")
    else:
        print("E-mail ou senha incorretos. Tente novamente.")
        quit()

# funcao pra editar as skills
def editar_habilidades(usuario):
    personagem = users[usuario]['personagem']
    habilidades = {
        '1': 'inteligencia',
        '2': 'forca',
        '3': 'habilidade'
    }
    print("\nEscolha a habilidade para editar:")
    for key, valor in habilidades.items():
        print(f"{key}. {valor.capitalize()}")
    escolha = input("Digite o número da habilidade: ")
    
    if escolha in habilidades:
        valor_novo = int(input(f"Defina o valor da {habilidades[escolha].capitalize()} (0-10): "))
        personagem[habilidades[escolha]] = valor_novo
        print(f'Habilidades atualizadas: Inteligência: {personagem["inteligencia"]}, Força: {personagem["forca"]}, Habilidade: {personagem["habilidade"]}')
    else:
        print("Opção inválida!")

# funcao pra editar a aparencia
def editar_aparencia(usuario):
    # trazendo os valores do dicionario
    personagem = users[usuario]['personagem']['aparencia']
    # novo dicionario para as partes do corpo que podem ser personalizadas
    partes = {
        '1': 'cabelo',
        '2': 'tronco',
        '3': 'pes'
    }
    print("\nEscolha a parte do corpo para alterar a cor:")
    for key, parte in partes.items(): # .items() retorna todos os pares chave-valor desse dicionário
        print(f"{key}. {parte.capitalize()}") # transforma a primeira letra da string parte em maiúscula. 
    escolha_parte = input("Digite o número da parte: ")
    
    if escolha_parte in partes:
        print("\nEscolha a cor que você quer:")
        print("1. Ciano\n2. Vermelho\n3. Azul\n4. Amarelo")
        escolha_cor = input("Digite o número da cor: ")
        
        if escolha_cor in cores:
            personagem[partes[escolha_parte]] = cores[escolha_cor]
            print(f"Aparência atualizada: {partes[escolha_parte].capitalize()} agora está com a cor {cores[escolha_cor]}{cores['reset']}")
        else:
            print("Opção de cor inválida!")
    else:
        print("Opção inválida! Tente novamente.")

    
def exibir_personagem(usuario):
    personagem = users[usuario]['personagem']
    aparencia = personagem['aparencia']
    
    print(f'\nHabilidades técnicas:\n\tInteligência: {personagem["inteligencia"]}, Força: {personagem["forca"]}, Habilidade: {personagem["habilidade"]}\n')
    
        
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

    for row in character:
        if "#" in row:  # cabelo
            print(f"{aparencia['cabelo']}{row}{cores['reset']}")
        elif "+" in row or "&" in row:  # tronco
            print(f"{aparencia['tronco']}{row}{cores['reset']}")
        elif "$" in row:  # pés
            print(f"{aparencia['pes']}{row}{cores['reset']}")
        else:
            print(row)


# acabaram as funções

# entrando no loop inicial do programa (cadastro e login)
while True:
    print("O que você quer fazer? ")
    print("\n1. Criar novo usuário \n2. Fazer login \n3. Cancelar")
    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        nome_usuario = input("Digite o nome do seu personagem: ")
        novo_email = input("Digite o novo email: ")
        nova_senha = input("Digite a nova senha: ")
        criar_novo_usuario(novo_email, nova_senha)
        time.sleep(0.3) # esperar um pouco pra nao ficar tão confuso

    elif escolha == '2':
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

# fora do loop pra nao repetir sempre
print(f"Olá, {nome_usuario}! Está pronto para novas aventuras?")
# loop para opções do jogador já logado/cadastrado no sistema
while True:
    print("\nO que quer fazer?")
    print("1. Editar personagem \n2. Iniciar o jogo\n3. Sair do sistema.")
    escolha = input("Digite o número da opção: ")

    if escolha == '1':
        if escolha == '1':
            print("\n1. Exibir meu personagem. \n2. Editar habilidades \n3. Editar aparência")
            escolha_personagem = input("O que você quer fazer? ")
            if escolha_personagem == "1": 
                exibir_personagem(email_login)
            elif escolha_personagem == "2":
                editar_habilidades(email_login)
            elif escolha_personagem == "3":
                editar_aparencia(email_login)
            else:
                print("Opção inválida!")  
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



