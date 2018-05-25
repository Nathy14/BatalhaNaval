import random
from time import sleep
tabuleiro = []
for repeticao in range(0,5):
    tabuleiro.append(["~"] * 5)
    

#função com as instruções do jogo.
def instrucao():
    print("Este jogo se chama Batalha Naval, em que o objetivo é descobrir as coordenadas de uma embarcação e a afundar,")
    sleep(2)
    print("neste jogo, as coordenadas são linhas e colunas que a identificação delas são feitas do número 0 até o 4.")
    sleep(2)
    print("Para tentar afundar um navio, é necessário além de informas as coordenas, acertar um teste de perícia em matemática.")
    
# função para criar o tabuleiro do jogo.
def construir_tabuleiro(tabuleiro):
    for espaços in tabuleiro:
        print((" ").join(espaços))
        
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
#coordenadas da embarcação
linha_barco1 = linha1(tabuleiro)
coluna_barco1 = coluna1(tabuleiro)
linha_barco2 = linha2(tabuleiro)
coluna_barco2 = coluna2(tabuleiro)
print("Linha {}        {}".format(linha_barco1,linha_barco2))
print("Coluna  {}       {}".format(coluna_barco1,coluna_barco2))
#inserir o teste de perícia em matemática e verificar resultado.
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
        print("Seu calculo para atingir o local escolhido é ",num,"/ ",num2,".")
        resultado = num/num2
    return resultado
def pontuação(contador_erro,contador_acerto):
    if contador_erro == 0:
        print("\nVocê afundou todos barcos sem errar nenhuma conta, você é realmente um excelente matemático! \n")
    elif contador_erro > contador_acerto:
        print("\nVocê cometeu muitos erros, poderia praticar mais alguns cálculos básicos, estudar nunca é demais! \n")
    elif contador_acerto > contador_erro:
        print("\nVocê acertou várias contas, parabéns, mas ainda tem como melhorar? Prátique mais alguns cálculos básicos e tente jogar novamente! \n")

instrucao()
sleep(4)
construir_tabuleiro(tabuleiro)
contador_erro=0
contador_acerto=0
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
        print("\n Opa, você não afundou nada.")
        tabuleiro[usuario_linha][usuario_coluna] = "X"
    #inserir um fim com história.
    #calcular pontuação do usuario. #Eu não sei onde é o loop final pra mostrar isso so no final do jogo, visto que jogo é uma definição e não algo imperativo.
while tabuleiro[linha_barco1][coluna_barco1] != "X" or tabuleiro[linha_barco2][coluna_barco2] != "X":
    construir_tabuleiro(tabuleiro)
    contador_erro=0
    contador_acerto=0
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
            print("\n Opa, você não afundou nada.")
            tabuleiro[usuario_linha][usuario_coluna] = "X"
pontuação(contador_erro,contador_acerto)
