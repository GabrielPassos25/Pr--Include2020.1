import random
palavras = ['petcomputacao','cenoura']
escolha = random.choice(palavras)

#Variáveis Utilizadas
erros = 0
letras_descobertas = ["_"] * len(escolha)
letras_utilizadas = []
vitoria = False

#Printando forca
print("\033[31m|=======================================================================|")
print("Bem vindo ao jogo da forca, a palavra a ser adivinhada está abaixo:\nSalve o pequeno Jucicleiton  ( ͡° ͜ʖ ͡°)_/\033[0;0m\n")
print("\033[36m",letras_descobertas,"\033[0;0m\n")
print("\033[31m|=======================================================================|\033[0;0m")
print("""
|||||||||||||
|                     
|                     
|     
|                    
|                     
|                       
|                                  
|                
|
""")
print("\033[31m|=======================================================================|\033[0;0m")

while erros != 6 and not vitoria:
    acertou = False
    receberEntrada = True

    # Repete até receber uma entrada aceitável
    while receberEntrada:
        chute = input("\033[31mQual a letra deseja saber se existe na frase?\033[0;0m ")
        print("\033[31m|=======================================================================|\033[0;0m")
        receberEntrada = False
        # Checa se é uma letra, pra evitar tirar ponto por espaço ou caractere especial
        if not chute.isalpha():
            print("\033[31mInsira apenas letras, por favor.\033[0;0m")
            print("\033[31m|=======================================================================|\033[0;0m")
            receberEntrada = True
        # Converte em lowercase por constância, porque B é igual a b. 
        chute = chute.lower()
        # Verifica cada letra utilizada
        for letra in letras_utilizadas:
            if chute == letra:
                receberEntrada = True
                print("\033[41mLetra já utilizada, tente novamente.\033[0;0m")
                print("\033[31m|=======================================================================|\033[0;0m")
    letras_utilizadas.append(chute)

    # Faz a busca do chute
    for i in range(len(escolha)):
        if(chute == escolha[i]):
            letras_descobertas[i] = chute
            acertou = True
    print("\033[36m",letras_descobertas,"\033[0;0m\n")

    if acertou:
        print("\033[36mExiste essa letra na palavra!\033[0;0m")
        print("\033[31m|=======================================================================|\033[0;0m")
        vitoria = True
        # Verifica se as letras da escolha e as letras descobertas batem
        for i in range(len(escolha)):
            if escolha[i] != letras_descobertas[i]:
                vitoria = False
        if vitoria:
            print("\033[32mVocê ganhou!\033[0;0m")
            print("\033[31m|=======================================================================|\033[0;0m")
    else:
        erros += 1
        print("\033[36mNão existe essa letra na palavra!\033[0;0m")
        print("\033[36mTentativas restantes: ", 6-erros, "\033[0;0m")
        if erros == 1:
            print("""
            ||||||||||||
            |         °°°
            |        °UwU°
            |         °°°
            |
            |
            |
            |
            |
            """)
            print("\033[31m|=======================================================================|\033[0;0m")
        elif erros == 2:
            print("""
            ||||||||||||
            |         °°°
            |        °V-V°
            |         °°°
            |          |
            |          |
            |          |
            |          
            |
            """)

        elif erros == 3:
            print("""
            ||||||||||||
            |         °°°
            |        °Q_Q°
            |         °°°
            |         /|
            |        / |
            |          |
            |          
            |
            """)
            print("\033[31m|=======================================================================|\033[0;0m")        
        elif erros == 4:
            print("""
            ||||||||||||
            |         °°°
            |        °O_O°
            |         °°°
            |         /|\ 
            |        / | \ 
            |          |
            |          
            |
            """)

        elif erros == 5:
            print("""
            ||||||||||||
            |         °°°
            |        °0_0°
            |         °°°
            |         /|\ 
            |        / | \ 
            |          |
            |         /
            |        
            """)
            print("\033[31m|=======================================================================|\033[0;0m")
        else:
            print("""
            ||||||||||||
            |         °°°
            |        °X_X°
            |         °°°
            |         /|\ 
            |        / | \ 
            |          |
            |         / \ 
            |
            """)
            print("\033[32mVocê perdeu!\033[0;0m")
            print("\033[31m|=======================================================================|\033[0;0m")
    