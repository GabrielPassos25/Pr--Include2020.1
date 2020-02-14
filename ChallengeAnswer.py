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

while erros != 3 and not vitoria:
    acertou = False
    receberEntrada = True

    # Verificações de entradas
    while receberEntrada:
        chute = input("\033[31mQual a letra deseja saber se existe na frase?\033[0;0m ")
        print("\033[31m|=======================================================================|\033[0;0m")
        receberEntrada = False
        # Verificando se o chute é uma letra
        if not chute.isalpha() or len(chute) >=2:
            print("\033[31mInsira apenas uma LETRA, por favor.\033[0;0m")
            print("\033[31m|=======================================================================|\033[0;0m")
            receberEntrada = True
        # Converte em minúsculo para não ocorrer conflitos 
        chute = chute.lower()
        # Impede repetições
        for letra in letras_utilizadas:
            if chute == letra:
                receberEntrada = True
                print("\033[41mLetra já utilizada, tente novamente.\033[0;0m")
                print("\033[31m|=======================================================================|\033[0;0m")
    letras_utilizadas.append(chute)

    # Verifica se a letra do chute está na palavra
    for i in range(len(escolha)):
        if(chute == escolha[i]):
            letras_descobertas[i] = chute
            acertou = True
    print("\033[36m",letras_descobertas,"\033[0;0m\n")

    if acertou:
        print("\033[36mExiste essa letra na palavra!\033[0;0m")
        print("\033[31m|=======================================================================|\033[0;0m")
        vitoria = True
        # Verifica se o usuário ganhou o jogo
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
    