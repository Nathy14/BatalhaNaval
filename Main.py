import random
from time import sleep
tabuleiro = []
for repeticao in range(0,5):
    tabuleiro.append(["~"] * 5)
    

#função com as instruções do jogo.
def instrucao():
    print("Este jogo se chama Batalha Naval, em que o objetivo é descobrir as coordenadas de uma embarcação e a afundar,")
    sleep(4)
    print("neste jogo, as coordenadas são linhas e colunas que a identificação delas são feitas do número 0 até o 4.")
    sleep(4)
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

instrucao()
sleep(4)
construir_tabuleiro(tabuleiro)
def jogo():
    usuario_linha = int(input("Digite a linha: "))
    usuario_coluna = int(input("Digite a coluna: "))
    if (usuario_linha == linha_barco1) and (usuario_coluna == coluna_barco1):
        if tabuleiro[usuario_linha][usuario_coluna] == "X":
            print("Opa, você já escolheu essas coordenadas")
        else:
            print("Parabéns você conseguiu afundar uma  embarcação")
            tabuleiro[usuario_linha][usuario_coluna] = "X"
    elif (usuario_linha == linha_barco2) and (usuario_coluna == coluna_barco2):
        if tabuleiro[usuario_linha][usuario_coluna] == "X":
            print("Opa, você já escolheu essas coordenadas")
        else:
            print("Parabéns você conseguiu afundar uma  embarcação")
            tabuleiro[usuario_linha][usuario_coluna] = "X"
    elif (usuario_coluna<0 or usuario_coluna>4) or (usuario_linha<0 or usuario_linha>4):
        print("""Opa, essas coordenadas não são válidas.
              Lembre-se de que as coordenadas são números de 0 a 4""")
    #inserir o teste de perícia em matemática e verificar resultado.
    #inserir um fim com história.
    #calcular pontuação do usuario.
    else:
        if tabuleiro[usuario_linha][usuario_coluna] == "X":
            print("Opa, você já escolheu essas coordenadas")
        else:     
            print("Opa, você não afundou nada.")
            tabuleiro[usuario_linha][usuario_coluna] = "X"
while tabuleiro[linha_barco1][coluna_barco1] != "X" or tabuleiro[linha_barco2][coluna_barco2] != "X":
    construir_tabuleiro(tabuleiro)
    jogo()

        

