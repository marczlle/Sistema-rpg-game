# from PIL import Image

# def image_to_ascii(image_path, width=24):
#     img = Image.open(image_path)
#     img = img.resize((width, int(width * img.height / img.width)))
#     img = img.convert('L')  # Converte para tons de cinza

#     pixels = img.getdata()
#     ascii_chars = "#*+=-:. "
#     ascii_str = ''.join([ascii_chars[pixel // 32] for pixel in pixels])

#     # Imprime em linhas
#     for i in range(0, len(ascii_str), width):
#         print(ascii_str[i:i + width])

# # Caminho para sua imagem
# image_to_ascii(r'C:\Users\marce\Downloads\png-transparent-undertale-sprite-pixel-art-sprite-text-rectangle-undertale.png')

# RED = "\033[31m"
# RESET = "\033[0m"  # Reseta a cor para o padrão

# # Imprimindo uma palavra em vermelho
# print(f"{RED}Essa palavra está em vermelho!{RESET}")
                                 
                  
CYAN = "\033[36m"
RED = "\033[31m"
BLUE = "\033[34m"
YELLOW = "\033[33m"
RESET = "\033[0m"  # Reseta a cor para o padrão

# Imprimindo uma palavra em vermelho
print(f"{RED}Essa palavra está em vermelho!{RESET}")

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