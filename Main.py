import random
from time import sleep
tabuleiro_facil = []
for repeticao in range(0,5):
    tabuleiro_facil.append(["~"] * 5)

tabuleiro_dificil = []
for repeticao in range(0,10):
	tabuleiro_dificil.append(["~"] * 10)
	
#função para criar o tabuleiro do jogo da dificuldade DIFÍCIL.
def construir_tabuleiro_dificil(tabuleiro_dificil):
	for espaços in tabuleiro_dificil:
		print((" ").join(espaços))
	
    
# função para criar o tabuleiro do jogo da dificuldade FÁCIL.
def construir_tabuleiro_facil(tabuleiro_facil):
    for espaços in tabuleiro_facil:
        print((" ").join(espaços))
        
#função com as instruções do jogo.
def instrucao():
    print("Este jogo se chama Batalha Naval, em que o objetivo é descobrir as coordenadas de uma embarcação e a afundar,")
    sleep(2)
    print("neste jogo, as coordenadas são linhas e colunas que a identificação delas são feitas do número 0 até o 4.")
    sleep(2)
    print("Ou seja, são dois pontos que indicam uma determinada localização no tabuleiro.")
    sleep(2)
    print("Para tentar afundar um navio, é necessário além de informar as coordenas, acertar uma conta matemática.")

        
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
linha_barco1 = linha1(tabuleiro_facil)
coluna_barco1 = coluna1(tabuleiro_facil)
linha_barco2 = linha2(tabuleiro_facil)
coluna_barco2 = coluna2(tabuleiro_facil)
print("Linha {}        {}".format(linha_barco1,linha_barco2))
print("Coluna  {}       {}".format(coluna_barco1,coluna_barco2))


def jogo_facil():
    construir_tabuleiro_facil(tabuleiro_facil)
    contador_erro=0
    contador_acerto=0
    usuario_linha = int(input("Digite a linha: "))
    usuario_coluna = int(input("Digite a coluna: "))
    if (usuario_linha == linha_barco1) and (usuario_coluna == coluna_barco1):
        if tabuleiro_facil[usuario_linha][usuario_coluna] == "X":
            print("Opa, você já escolheu essas coordenadas")
        else:
            tentativa_jogo = mat_titulo()
            tentativa_jogador = int(input("Qual é o resultado da conta? "))
            while tentativa_jogo != tentativa_jogador:
                tentativa_jogador = int(input("Parece que você errou o calculo, vamos tentar novamente? Qual é o resultado da conta?"))
                contador_erro = contador_erro+1
            contador_acerto = contador_acerto+1
            print("Parabéns você conseguiu afundar uma  embarcação")
            tabuleiro_facil[usuario_linha][usuario_coluna] = "X"
    elif (usuario_linha == linha_barco2) and (usuario_coluna == coluna_barco2):
        if tabuleiro_facil[usuario_linha][usuario_coluna] == "X":
            print("Opa, você já escolheu essas coordenadas")
        else:
            tentativa_jogo = mat_titulo()
            tentativa_jogador = int(input("Qual é o resultado da conta? "))
            while tentativa_jogo != tentativa_jogador:
                tentativa_jogador = int(input("Parece que você errou o calculo, vamos tentar novamente? Qual é o resultado da conta?"))
                contador_erro+=1
            contador_acerto = contador_acerto+1
            print("\nParabéns você conseguiu afundar uma  embarcação")
            tabuleiro_facil[usuario_linha][usuario_coluna] = "X"
    elif (usuario_coluna<0 or usuario_coluna>4) or (usuario_linha<0 or usuario_linha>4):
        print("""Opa, essas coordenadas não são válidas.
              Lembre-se de que as coordenadas são números de 0 a 4""")
    else:
        if tabuleiro_facil[usuario_linha][usuario_coluna] == "X":
            print("Opa, você já escolheu essas coordenadas")
        else:
            tentativa_jogo = mat_titulo()
            tentativa_jogador = int(input("Qual é o resultado da conta? "))
            while tentativa_jogo != tentativa_jogador:
                tentativa_jogador = int(input("Parece que você errou o calculo, vamos tentar novamente? Qual é o resultado da conta?"))
                contador_erro = contador_erro+1
            contador_acerto = contador_acerto+1
            print("\n Opa, você não afundou nada.")
            tabuleiro_facil[usuario_linha][usuario_coluna] = "X"
    while tabuleiro_facil[linha_barco1][coluna_barco1] != "X" or tabuleiro_facil[linha_barco2][coluna_barco2] != "X":
        construir_tabuleiro_facil(tabuleiro_facil)
        contador_erro=0
        contador_acerto=0
        usuario_linha = int(input("Digite a linha: "))
        usuario_coluna = int(input("Digite a coluna: "))
        if (usuario_linha == linha_barco1) and (usuario_coluna == coluna_barco1):
            if tabuleiro_facil[usuario_linha][usuario_coluna] == "X":
                print("Opa, você já escolheu essas coordenadas")
            else:
                tentativa_jogo = mat_titulo()
                tentativa_jogador = int(input("Qual é o resultado da conta? "))
                while tentativa_jogo != tentativa_jogador:
                    tentativa_jogador = int(input("Parece que você errou o calculo, vamos tentar novamente? Qual é o resultado da conta?"))
                    contador_erro = contador_erro+1
                contador_acerto = contador_acerto+1
                print("Parabéns você conseguiu afundar uma  embarcação")
                tabuleiro_facil[usuario_linha][usuario_coluna] = "X"
        elif (usuario_linha == linha_barco2) and (usuario_coluna == coluna_barco2):
            if tabuleiro_facil[usuario_linha][usuario_coluna] == "X":
                print("Opa, você já escolheu essas coordenadas")
            else:
                tentativa_jogo = mat_titulo()
                tentativa_jogador = int(input("Qual é o resultado da conta? "))
                while tentativa_jogo != tentativa_jogador:
                    tentativa_jogador = int(input("Parece que você errou o calculo, vamos tentar novamente? Qual é o resultado da conta?"))
                    contador_erro+=1
                contador_acerto = contador_acerto+1
                print("\nParabéns você conseguiu afundar uma  embarcação")
                tabuleiro_facil[usuario_linha][usuario_coluna] = "X"
        elif (usuario_coluna<0 or usuario_coluna>4) or (usuario_linha<0 or usuario_linha>4):
            print("""Opa, essas coordenadas não são válidas.
Lembre-se de que as coordenadas são números de 0 a 4""")
        else:
            if tabuleiro_facil[usuario_linha][usuario_coluna] == "X":
                print("Opa, você já escolheu essas coordenadas")
            else:
                tentativa_jogo = mat_titulo()
                tentativa_jogador = int(input("Qual é o resultado da conta? "))
                while tentativa_jogo != tentativa_jogador:
                    tentativa_jogador = int(input("Parece que você errou o calculo, vamos tentar novamente? Qual é o resultado da conta?"))
                    contador_erro = contador_erro+1
                contador_acerto = contador_acerto+1
                print("\n Opa, você não afundou nada.")
                tabuleiro_facil[usuario_linha][usuario_coluna] = "X"
    pontuação(contador_erro,contador_acerto)
    
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
