import random
tabuleiro = []
for repeticao in range(0,5):
    tabuleiro.append(["~"] * 5)
# função para criar o tabuleiro do jogo.
def construir_tabuleiro(tabuleiro):
    for espaços in tabuleiro:
        print((" ").join(espaços))
#função para randomizar a linha onde estará a embarcação
def linha(tabuleiro):
    linha_aleatoria =  random.randint(0,len(tabuleiro)-1)
    return linha_aleatoria
#função para randomizar a coluna onde estará a embarcação
def coluna(tabuleiro):
    coluna_aleatoria = random.randint(0,len(tabuleiro[0])-1)
    return coluna_aleatoria
#coordenadas da embarcação
linha_barco = linha(tabuleiro)
coluna_barco = coluna(tabuleiro)
#validar linha
def validar_linha():
    while usuario_linha<0 or usuario_linha>5:
        usuario_linha = int(input("Opa, digite a linha, sendo um número de 0 à 10: "))
#validar coluna
def validar_coluna():
    while usuario_coluna<0 or usuario_coluna>5:
        usuario_coluna = int(input("Opa, digite a coluna, sendo um número de 0 à 10: "))
construir_tabuleiro(tabuleiro)
#colocar um laço de repetição em que, enquanto o usuário não acertar, o jogo continua.
usuario_linha = int(input("Digite a linha: "))
validar_linha()
usuario_coluna = int(input("Digite a coluna: "))
validar_coluna()
    if (usuario_linha == linha_barco) and (usuario_coluna == coluna_barco):
        print("Parabéns você conseguiu afundar a embarcação")
    #inserir o teste de perícia em matemática e verificar resultado.
    #inserir um fim com história.
    #calcular pontuação do usuario.
else:
    print("Opa, você não afundou nada.")
    tabuleiro[usuario_linha][usuario_coluna] = "X"
        

