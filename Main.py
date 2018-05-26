
import random
from time import sleep
tabuleiro = []
for repeticao in range(0,5):
    tabuleiro.append(["~"] * 5)
	
    
# função para criar o tabuleiro do jogo da dificuldade FÁCIL.
def construir_tabuleiro(tabuleiro):
    for espaços in tabuleiro:
        print((" ").join(espaços))
        
#função com as instruções do jogo.
def instrucao():
    print("~Este jogo se chama Batalha Naval, em que o objetivo é descobrir as coordenadas de uma embarcação e a afundar~")
    sleep(4)
    print("~Neste jogo, as coordenadas são identificadas por números de linhas e colunas~")
    sleep(4)   
    print("~Para tentar afundar um navio, é necessário além de informar as coordenas, acertar uma conta matemática~")
    sleep(4)    
    print("{:=^40}".format("TUTORIAL"))
    sleep(4)
    print(""">Modo FÁCIL: 2 embarcações
>Modo DIFÍCIL: 4 embarcações""")
    sleep(2)
    print("Como saber o número das linhas e colunas?")
    sleep(2)
    print("""~[~]~ ~ ~
~ ~ ~ ~ ~
~ ~ ~ ~ ~
~ ~ ~ ~ ~
~ ~ ~ ~ ~
> A coordenada do local selecionado é linha 0 e coluna 1""")
    sleep(4)
    print("""~ ~ ~ ~ ~
~[~]~ ~ ~
~ ~ ~ ~ ~
~ ~ ~ ~ ~
~ ~ ~ ~ ~
>A coordenada do local selecionado é igual a quanto?""")
    tutorial_linha = int(input("Digite a linha: "))
    tutorial_coluna = int(input("Digite a coluna: "))
    while tutorial_linha != 1 or tutorial_coluna != 1:
        print("Opa, tente novamente...acho que você se esqueceu que a contagem  de linhas e colunas começa no 0 e vai até o 4.")
        tutorial_linha = int(input("Digite a linha: "))
        tutorial_coluna = int(input("Digite a coluna: "))          
    print("Parabéns!!! Você pegou o jeito, agora vamos jogar pra valer")   
#função para randomizar a linha onde estará a embarcação 1
def linha1(tabuleiro):
    linha_aleatoria1 =  random.randint(0,len(tabuleiro)-1)
    return linha_aleatoria1

#função para randomizar a coluna onde estará a embarcação 1
def coluna1(tabuleiro):
    coluna_aleatoria1 = random.randint(0,len(tabuleiro[0])-1)
    return coluna_aleatoria1

#função para randomizar a coluna onde estará a embarcação 2
def coluna2(tabuleiro):
    coluna_aleatoria2 = random.randint(0,len(tabuleiro[0])-1)
    while coluna_aleatoria2 == coluna1(tabuleiro):
        coluna_aleatoria2 = random.randint(0,len(tabuleiro[0])-1)
    return coluna_aleatoria2
#função para randomizar a linha onde estara a embarcação 2
def linha2(tabuleiro):
    linha_aleatoria2 = random.randint(0,len(tabuleiro)-1)
    while linha_aleatoria2 == linha1(tabuleiro):
        linha_aleatoria2 = random.randint(0,len(tabuleiro)-1)
    return linha_aleatoria2
#função para randomizar a linha onde estará a embarcação 3
def linha3(tabuleiro):
	linha_aleatoria3 = random.randint(0,len(tabuleiro)-1)
	while linha_aleatoria3 == linha2(tabuleiro):
		linha_aleatoria3 = random.randint(0,len(tabuleiro)-1)
	return linha_aleatoria3
#função para randomizar a coluna onde estará a embarcação 3
def coluna3(tabuleiro):
	coluna_aleatoria3 = random.randint(0,len(tabuleiro[0])-1)
	while coluna_aleatoria3 == coluna2(tabuleiro):
		coluna_aleatoria3 = random.randint(0,len(tabuleiro[0])-1)
	return coluna_aleatoria3
#função para randomizar a linha onde estará a embarcação 4
def linha4(tabuleiro):
	linha_aleatoria4 = random.randint(0,len(tabuleiro)-1)
	while linha_aleatoria4 == linha3(tabuleiro):
		linha_aleatoria4 = random.randint(0,len(tabuleiro)-1)
	return linha_aleatoria4
#função para randomizar a coluna onde estará a embarcação 4
def coluna4(tabuleiro):
	coluna_aleatoria4 =  random.randint(0,len(tabuleiro[0])-1)
	while coluna_aleatoria4 == coluna3(tabuleiro):
		coluna_aleatoria4 =  random.randint(0,len(tabuleiro[0])-1)
	return coluna_aleatoria4
	
#função para realizar o teste de perícia em matemática.
def mat_titulo():
    tipo_de_conta = random.randint(0,3)
    num = random.randint(0,10)
    num2 = random.randint(0,10)
    if tipo_de_conta==0:
        print("Seu calculo para atingir o local escolhido é ",num,"+ ",num2,".")
        resultado = num+num2
    elif tipo_de_conta==1:
        while num < num2:
            num2 = random.randint(0,10)
        print("Seu calculo para atingir o local escolhido é ",num,"- ",num2,".")
        resultado = num-num2
    elif tipo_de_conta==2:
        print("Seu calculo para atingir o local escolhido é ",num,"* ",num2,".")
        resultado = num*num2
    else:
        while num2 == 0:
            num2 = random.randint(0,10)
        while num<num2:
            num = random.randint(0,10)
        while num%num2 != 0:
            num = random.randint(0,10)
        print("Seu calculo para atingir o local escolhido é ",num,"/ ",num2,".")
        resultado = num/num2
    return resultado

#função para calcular a pontuação.
def pontuação(contador_erro,contador_acerto):
    if contador_erro == 0:
        print("\nVocê afundou todos barcos sem errar nenhuma conta, você é realmente um excelente matemático! \n")
    elif contador_erro > contador_acerto:
        print("\nVocê cometeu muitos erros, poderia praticar mais alguns cálculos básicos, estudar nunca é demais! \n")
    elif contador_acerto > contador_erro:
        print("\nVocê acertou várias contas, parabéns, mas ainda tem como melhorar? Prátique mais alguns cálculos básicos e tente jogar novamente! \n")

#coordenadas da embarcação 
linha_barco1 = linha1(tabuleiro)
coluna_barco1 = coluna1(tabuleiro)
linha_barco2 = linha2(tabuleiro)
coluna_barco2 = coluna2(tabuleiro)
coluna_barco3 = coluna3(tabuleiro)
linha_barco3 = linha3(tabuleiro)
coluna_barco4 = coluna4(tabuleiro)
linha_barco4 = linha4(tabuleiro)
print("Linha {}   {}   {}      {}".format(linha_barco1,linha_barco2,linha_barco3,linha_barco4))
print("Coluna {}   {}   {}      {}".format(coluna_barco1,coluna_barco2,coluna_barco3,coluna_barco4))

#base do jogo dificuldade FÁCIL
def jogo_facil():
    construir_tabuleiro(tabuleiro)
    contador_erro=0
    contador_acerto=0
    usuario_linha = int(input("Digite a linha: "))
    usuario_coluna = int(input("Digite a coluna: "))
    #verifica se o usuário acertou as coordenadas da embarcação 1.
    if (usuario_linha == linha_barco1) and (usuario_coluna == coluna_barco1):
        if tabuleiro[usuario_linha][usuario_coluna] == "X":
            print("Opa, você já escolheu essas coordenadas")
        else:
            tentativa_jogo = mat_titulo()
            tentativa_jogador = int(input("Qual é o resultado da conta? "))
            while tentativa_jogo != tentativa_jogador:
                tentativa_jogador = int(input("Parece que você errou o calculo, vamos tentar novamente? Qual é o resultado da conta?"))
                contador_erro = contador_erro+1
            contador_acerto = contador_acerto+1
            print("""
      _.-^^---....,,--
 _--                  --_
<                        >)
|                         |
 \._                   _./
    ```--. . , ; .--'''
          | |   |
       .-=||  | |=-.
       `-=#$%&%$#=-'
          | ;  :|
 _____.,-#%&$@%#&#~,._____ """)
            print("KAAAABUUUM!!!")
            sleep(2)
            print("\nParabéns você conseguiu afundar uma  embarcação")
            tabuleiro[usuario_linha][usuario_coluna] = "X"
	#verifica se o usuário acrtou as coordenadas da embarcação 2.
    elif (usuario_linha == linha_barco2) and (usuario_coluna == coluna_barco2):
        if tabuleiro[usuario_linha][usuario_coluna] == "X":
            print("Opa, você já escolheu essas coordenadas")
        else:
            tentativa_jogo = mat_titulo()
            tentativa_jogador = int(input("Qual é o resultado da conta? "))
            while tentativa_jogo != tentativa_jogador:
                tentativa_jogador = int(input("Parece que você errou o calculo, vamos tentar novamente? Qual é o resultado da conta?"))
                contador_erro+=1
            contador_acerto = contador_acerto+1
            print("""
     _.-^^---....,,--
 _--                  --_
<                        >)
|                         |
 \._                   _./
    ```--. . , ; .--'''
          | |   |
       .-=||  | |=-.
       `-=#$%&%$#=-'
          | ;  :|
 _____.,-#%&$@%#&#~,._____ """)
            print("KAAAABUUUM!!!")
            sleep(2)
            print("\nParabéns você conseguiu afundar uma  embarcação")
            tabuleiro[usuario_linha][usuario_coluna] = "X"
	# verifica se o usuário entrou com valores de coordenadas inválidas.
    elif (usuario_coluna<0 or usuario_coluna>4) or (usuario_linha<0 or usuario_linha>4):
        print("""Opa, essas coordenadas não são válidas.
Lembre-se de que as coordenadas são números de 0 a 4""")
	#verifica se o usuário errou as coordenadas.
    else:
        if tabuleiro[usuario_linha][usuario_coluna] == "X":
            print("Opa, você já escolheu essas coordenadas")
        else:
            tentativa_jogo = mat_titulo()
            tentativa_jogador = int(input("Qual é o resultado da conta? "))
            while tentativa_jogo != tentativa_jogador:
                tentativa_jogador = int(input("Parece que você errou o calculo, vamos tentar novamente? Qual é o resultado da conta?"))
                contador_erro = contador_erro+1
            contador_acerto = contador_acerto+1
            print("Opa, você não afundou nada.")
            tabuleiro[usuario_linha][usuario_coluna] = "X"
	#laço de repetição ativada até que o usuário acerte as coordenadas das duas embarcações.
    while tabuleiro[linha_barco1][coluna_barco1] != "X" or tabuleiro[linha_barco2][coluna_barco2] != "X":
        construir_tabuleiro(tabuleiro)
        usuario_linha = int(input("Digite a linha: "))
        usuario_coluna = int(input("Digite a coluna: "))
        if (usuario_linha == linha_barco1) and (usuario_coluna == coluna_barco1):
            if tabuleiro[usuario_linha][usuario_coluna] == "X":
                print("Opa, você já escolheu essas coordenadas")
            else:
                tentativa_jogo = mat_titulo()
                tentativa_jogador = int(input("Qual é o resultado da conta? "))
                while tentativa_jogo != tentativa_jogador:
                    tentativa_jogador = int(input("Parece que você errou o calculo, vamos tentar novamente? Qual é o resultado da conta?"))
                    contador_erro = contador_erro+1
                contador_acerto = contador_acerto+1
                print("""
     _.-^^---....,,--
 _--                  --_
<                        >)
|                         |
 \._                   _./
    ```--. . , ; .--'''
          | |   |
       .-=||  | |=-.
       `-=#$%&%$#=-'
          | ;  :|
 _____.,-#%&$@%#&#~,._____ """)
            print("KAAAABUUUM!!!")
            sleep(2)
            print("Parabéns você conseguiu afundar uma  embarcação")
            tabuleiro[usuario_linha][usuario_coluna] = "X"
        elif (usuario_linha == linha_barco2) and (usuario_coluna == coluna_barco2):
            if tabuleiro[usuario_linha][usuario_coluna] == "X":
                print("Opa, você já escolheu essas coordenadas")
            else:
                tentativa_jogo = mat_titulo()
                tentativa_jogador = int(input("Qual é o resultado da conta? "))
                while tentativa_jogo != tentativa_jogador:
                    tentativa_jogador = int(input("Parece que você errou o calculo, vamos tentar novamente? Qual é o resultado da conta?"))
                    contador_erro+=1
                contador_acerto = contador_acerto+1
                print("""
     _.-^^---....,,--
 _--                  --_
<                        >)
|                         |
 \._                   _./
    ```--. . , ; .--'''
          | |   |
       .-=||  | |=-.
       `-=#$%&%$#=-'
          | ;  :|
 _____.,-#%&$@%#&#~,._____ """)
            print("KAAAABUUUM!!!")
            sleep(2)
            print("\nParabéns você conseguiu afundar uma  embarcação")
            tabuleiro[usuario_linha][usuario_coluna] = "X"
        elif (usuario_coluna<0 or usuario_coluna>4) or (usuario_linha<0 or usuario_linha>4):
            print("""Opa, essas coordenadas não são válidas.
Lembre-se de que as coordenadas são números de 0 a 4""")
        else:
            if tabuleiro[usuario_linha][usuario_coluna] == "X":
                print("Opa, você já escolheu essas coordenadas")
            else:
                tentativa_jogo = mat_titulo()
                tentativa_jogador = int(input("Qual é o resultado da conta? "))
                while tentativa_jogo != tentativa_jogador:
                    tentativa_jogador = int(input("Parece que você errou o calculo, vamos tentar novamente? Qual é o resultado da conta?"))
                    contador_erro = contador_erro+1
                contador_acerto = contador_acerto+1
                print("Opa, você não afundou nada.")
                tabuleiro[usuario_linha][usuario_coluna] = "X"
    #mostra a pontuação do usuário.
    pontuação(contador_erro,contador_acerto)
#base do jogo dificuldade DIFÍCIL.
def jogo_dificil():
    construir_tabuleiro(tabuleiro)
    contador_erro=0
    contador_acerto=0
    usuario_linha = int(input("Digite a linha: "))
    usuario_coluna = int(input("Digite a coluna: "))
    #verifica se o usuário acertou as coordenadas da embarcação 1.
    if (usuario_linha == linha_barco1) and (usuario_coluna == coluna_barco1):
        if tabuleiro[usuario_linha][usuario_coluna] == "X":
            print("Opa, você já escolheu essas coordenadas")
        else:
            tentativa_jogo = mat_titulo()
            tentativa_jogador = int(input("Qual é o resultado da conta? "))
            while tentativa_jogo != tentativa_jogador:
                tentativa_jogador = int(input("Parece que você errou o calculo, vamos tentar novamente? Qual é o resultado da conta?"))
                contador_erro = contador_erro+1
            contador_acerto = contador_acerto+1
            print("""
      _.-^^---....,,--
 _--                  --_
<                        >)
|                         |
 \._                   _./
    ```--. . , ; .--'''
          | |   |
       .-=||  | |=-.
       `-=#$%&%$#=-'
          | ;  :|
 _____.,-#%&$@%#&#~,._____ """)
            print("KAAAABUUUM!!!")
            sleep(2)
            print("\nParabéns você conseguiu afundar uma  embarcação")
            tabuleiro[usuario_linha][usuario_coluna] = "X"
	#verifica se o usuário acrtou as coordenadas da embarcação 2.
    elif (usuario_linha == linha_barco2) and (usuario_coluna == coluna_barco2):
        if tabuleiro[usuario_linha][usuario_coluna] == "X":
            print("Opa, você já escolheu essas coordenadas")
        else:
            tentativa_jogo = mat_titulo()
            tentativa_jogador = int(input("Qual é o resultado da conta? "))
            while tentativa_jogo != tentativa_jogador:
                tentativa_jogador = int(input("Parece que você errou o calculo, vamos tentar novamente? Qual é o resultado da conta?"))
                contador_erro+=1
            contador_acerto = contador_acerto+1
            print("""
     _.-^^---....,,--
 _--                  --_
<                        >)
|                         |
 \._                   _./
    ```--. . , ; .--'''
          | |   |
       .-=||  | |=-.
       `-=#$%&%$#=-'
          | ;  :|
 _____.,-#%&$@%#&#~,._____ """)
            print("KAAAABUUUM!!!")
            sleep(2)
            print("\nParabéns você conseguiu afundar uma  embarcação")
            tabuleiro[usuario_linha][usuario_coluna] = "X"
	#verifica se o usuário acertou as coordenadas da embarcação 3.
    elif (usuario_linha == linha_barco3) and (usuario_coluna == coluna_barco3):
        if tabuleiro[usuario_linha][usuario_coluna] == "X":
            print("Opa, você já escolheu essas coordenadas")
        else:
            tentativa_jogo = mat_titulo()
            tentativa_jogador = int(input("Qual é o resultado da conta? "))
            while tentativa_jogo != tentativa_jogador:
                tentativa_jogador = int(input("Parece que você errou o calculo, vamos tentar novamente? Qual é o resultado da conta?"))
                contador_erro+=1
            contador_acerto = contador_acerto+1
            print("""
     _.-^^---....,,--
 _--                  --_
<                        >)
|                         |
 \._                   _./
    ```--. . , ; .--'''
          | |   |
       .-=||  | |=-.
       `-=#$%&%$#=-'
          | ;  :|
 _____.,-#%&$@%#&#~,._____ """)
            print("KAAAABUUUM!!!")
            sleep(2)
            print("\nParabéns você conseguiu afundar uma  embarcação")
            tabuleiro[usuario_linha][usuario_coluna] = "X"
	#verifica se o usuário acertou as coordenadas da embarcação 4.
    elif (usuario_linha == linha_barco4) and (usuario_coluna == coluna_barco4):
        if tabuleiro[usuario_linha][usuario_coluna] == "X":
            print("Opa, você já escolheu essas coordenadas")
        else:
            tentativa_jogo = mat_titulo()
            tentativa_jogador = int(input("Qual é o resultado da conta? "))
            while tentativa_jogo != tentativa_jogador:
                tentativa_jogador = int(input("Parece que você errou o calculo, vamos tentar novamente? Qual é o resultado da conta?"))
                contador_erro+=1
            contador_acerto = contador_acerto+1
            print("""
     _.-^^---....,,--
 _--                  --_
<                        >)
|                         |
 \._                   _./
    ```--. . , ; .--'''
          | |   |
       .-=||  | |=-.
       `-=#$%&%$#=-'
          | ;  :|
 _____.,-#%&$@%#&#~,._____ """)
            print("KAAAABUUUM!!!")
            sleep(2)
            print("\nParabéns você conseguiu afundar uma  embarcação")
            tabuleiro[usuario_linha][usuario_coluna] = "X"
	# verifica se o usuário entrou com valores de coordenadas inválidas.
    elif (usuario_coluna<0 or usuario_coluna>4) or (usuario_linha<0 or usuario_linha>4):
        print("""Opa, essas coordenadas não são válidas.
Lembre-se de que as coordenadas são números de 0 a 4""")
	#verifica se o usuário errou as coordenadas.
    else:
        if tabuleiro[usuario_linha][usuario_coluna] == "X":
            print("Opa, você já escolheu essas coordenadas")
        else:
            tentativa_jogo = mat_titulo()
            tentativa_jogador = int(input("Qual é o resultado da conta? "))
            while tentativa_jogo != tentativa_jogador:
                tentativa_jogador = int(input("Parece que você errou o calculo, vamos tentar novamente? Qual é o resultado da conta?"))
                contador_erro = contador_erro+1
            contador_acerto = contador_acerto+1
            print("Opa, você não afundou nada.")
            tabuleiro[usuario_linha][usuario_coluna] = "X"
	#laço de repetição ativada até que o usuário acerte as coordenadas das duas embarcações.
    while tabuleiro[linha_barco1][coluna_barco1] != "X" or tabuleiro[linha_barco2][coluna_barco2] != "X" or tabuleiro[linha_barco3][coluna_barco3] != "X" or tabuleiro[linha_barco4][coluna_barco4] != "X":
        construir_tabuleiro(tabuleiro)
        usuario_linha = int(input("Digite a linha: "))
        usuario_coluna = int(input("Digite a coluna: "))
        #verifica se o usuário acertou as coordenadas da embarcação 1.
        if (usuario_linha == linha_barco1) and (usuario_coluna == coluna_barco1):
            if tabuleiro[usuario_linha][usuario_coluna] == "X":
                print("Opa, você já escolheu essas coordenadas")
            else:
                tentativa_jogo = mat_titulo()
                tentativa_jogador = int(input("Qual é o resultado da conta? "))
                while tentativa_jogo != tentativa_jogador:
                    tentativa_jogador = int(input("Parece que você errou o calculo, vamos tentar novamente? Qual é o resultado da conta?"))
                    contador_erro = contador_erro+1
                contador_acerto = contador_acerto+1
                print("""
      _.-^^---....,,--
 _--                  --_
<                        >)
|                         |
 \._                   _./
    ```--. . , ; .--'''
          | |   |
       .-=||  | |=-.
       `-=#$%&%$#=-'
          | ;  :|
 _____.,-#%&$@%#&#~,._____ """)
                print("KAAAABUUUM!!!")
                sleep(2)
                print("\nParabéns você conseguiu afundar uma  embarcação")
                tabuleiro[usuario_linha][usuario_coluna] = "X"
            #verifica se o usuário acrtou as coordenadas da embarcação 2.
        elif (usuario_linha == linha_barco2) and (usuario_coluna == coluna_barco2):
            if tabuleiro[usuario_linha][usuario_coluna] == "X":
                print("Opa, você já escolheu essas coordenadas")
            else:
                tentativa_jogo = mat_titulo()
                tentativa_jogador = int(input("Qual é o resultado da conta? "))
                while tentativa_jogo != tentativa_jogador:
                    tentativa_jogador = int(input("Parece que você errou o calculo, vamos tentar novamente? Qual é o resultado da conta?"))
                    contador_erro+=1
                contador_acerto = contador_acerto+1
                print("""
     _.-^^---....,,--
 _--                  --_
<                        >)
|                         |
 \._                   _./
    ```--. . , ; .--'''
          | |   |
       .-=||  | |=-.
       `-=#$%&%$#=-'
          | ;  :|
 _____.,-#%&$@%#&#~,._____ """)
                print("KAAAABUUUM!!!")
                sleep(2)
                print("\nParabéns você conseguiu afundar uma  embarcação")
                tabuleiro[usuario_linha][usuario_coluna] = "X"
            #verifica se o usuário acertou as coordenadas da embarcação 3.
        elif (usuario_linha == linha_barco3) and (usuario_coluna == coluna_barco3):
            if tabuleiro[usuario_linha][usuario_coluna] == "X":
                print("Opa, você já escolheu essas coordenadas")
            else:
                tentativa_jogo = mat_titulo()
                tentativa_jogador = int(input("Qual é o resultado da conta? "))
                while tentativa_jogo != tentativa_jogador:
                    tentativa_jogador = int(input("Parece que você errou o calculo, vamos tentar novamente? Qual é o resultado da conta?"))
                    contador_erro+=1
                contador_acerto = contador_acerto+1
                print("""
     _.-^^---....,,--
 _--                  --_
<                        >)
|                         |
 \._                   _./
    ```--. . , ; .--'''
          | |   |
       .-=||  | |=-.
       `-=#$%&%$#=-'
          | ;  :|
 _____.,-#%&$@%#&#~,._____ """)
                print("KAAAABUUUM!!!")
                sleep(2)
                print("\nParabéns você conseguiu afundar uma  embarcação")
                tabuleiro[usuario_linha][usuario_coluna] = "X"
            #verifica se o usuário acertou as coordenadas da embarcação 4.
        elif (usuario_linha == linha_barco4) and (usuario_coluna == coluna_barco4):
            if tabuleiro[usuario_linha][usuario_coluna] == "X":
                print("Opa, você já escolheu essas coordenadas")
            else:
                tentativa_jogo = mat_titulo()
                tentativa_jogador = int(input("Qual é o resultado da conta? "))
                while tentativa_jogo != tentativa_jogador:
                    tentativa_jogador = int(input("Parece que você errou o calculo, vamos tentar novamente? Qual é o resultado da conta?"))
                    contador_erro+=1
                contador_acerto = contador_acerto+1
                print("""
     _.-^^---....,,--
 _--                  --_
<                        >)
|                         |
 \._                   _./
    ```--. . , ; .--'''
          | |   |
       .-=||  | |=-.
       `-=#$%&%$#=-'
          | ;  :|
 _____.,-#%&$@%#&#~,._____ """)
                print("KAAAABUUUM!!!")
                sleep(2)
                print("\nParabéns você conseguiu afundar uma  embarcação")
                tabuleiro[usuario_linha][usuario_coluna] = "X"
            # verifica se o usuário entrou com valores de coordenadas inválidas.
        elif (usuario_coluna<0 or usuario_coluna>4) or (usuario_linha<0 or usuario_linha>4):
            print("""Opa, essas coordenadas não são válidas.
Lembre-se de que as coordenadas são números de 0 a 4""")
            #verifica se o usuário errou as coordenadas.
        else:
            if tabuleiro[usuario_linha][usuario_coluna] == "X":
                print("Opa, você já escolheu essas coordenadas")
            else:
                tentativa_jogo = mat_titulo()
                tentativa_jogador = int(input("Qual é o resultado da conta? "))
                while tentativa_jogo != tentativa_jogador:
                    tentativa_jogador = int(input("Parece que você errou o calculo, vamos tentar novamente? Qual é o resultado da conta?"))
                    contador_erro = contador_erro+1
                contador_acerto = contador_acerto+1
                print("Opa, você não afundou nada.")
                tabuleiro[usuario_linha][usuario_coluna] = "X"
        #mostra a pontuação do usuário.
    pontuação(contador_erro,contador_acerto)
#começo do jogo.   
instrucao()
sleep(4)
print("""Selecione a dificuldade:
[ 1 ] FÁCIL
[ 2 ] DIFÍCIL""")
dificuldade = int(input(">  "))
while dificuldade != 1 and dificuldade != 2:
    print("""Opa, você digitou um número inválido.
Lembre-se:
[ 1 ] FÁCIL
[ 2 ] DIFICIL""")
    dificuldade = int(input(">  "))
if dificuldade == 1:
    jogo_facil()
else:
    jogo_dificil()
print("Saindo...")

    
