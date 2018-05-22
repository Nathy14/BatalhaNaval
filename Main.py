import random
tabuleiro = []
for repeticao in range(0,5):
    tabuleiro.append(["~"] * 5)
    
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

#validar linha
def validar_linha(usuario_linha):
    while usuario_linha<0 or usuario_linha>4:
        usuario_linha = int(input("Opa, digite a linha, sendo um número de 0 à 4: "))
        
#validar coluna
def validar_coluna(usuario_coluna):
    while usuario_coluna<0 or usuario_coluna>4:
        usuario_coluna = int(input("Opa, digite a coluna, sendo um número de 0 à 4: "))

construir_tabuleiro(tabuleiro)
usuario_linha = int(input("Digite a linha: "))
validar_linha(usuario_linha)
usuario_coluna = int(input("Digite a coluna: "))
validar_coluna(usuario_coluna)
if (usuario_linha == linha_barco1) and (usuario_coluna == coluna_barco1):
    print("Parabéns você conseguiu afundar uma  embarcação")
elif (usuario_linha == linha_barco2) and (usuario_coluna == coluna_barco2):
    print("Parabéns você conseguiu afundar uma embarcação")
    #inserir o teste de perícia em matemática e verificar resultado.
    #inserir um fim com história.
    #calcular pontuação do usuario.
else:
    print("Opa, você não afundou nada.")
    tabuleiro[usuario_linha][usuario_coluna] = "X"
while ( usuario_linha != linha_barco1 and usuario_coluna != coluna_barco1) or (usuario_linha != linha_barco2 and usuario_coluna != coluna_barco2):
    construir_tabuleiro(tabuleiro)
    usuario_linha = int(input("Digite a linha: "))
    validar_linha(usuario_linha)
    usuario_coluna = int(input("Digite a coluna: "))
    validar_coluna(usuario_coluna)
    if (usuario_linha == linha_barco1) and (usuario_coluna == coluna_barco1):
        print("Parabéns você conseguiu afundar uma  embarcação")
    elif (usuario_linha == linha_barco2) and (usuario_coluna == coluna_barco2):
        print("Parabéns você conseguiu afundar uma embarcação")
    #inserir o teste de perícia em matemática e verificar resultado.
    #inserir um fim com história.
    #calcular pontuação do usuario.
    else:
        print("Opa, você não afundou nada.")
        tabuleiro[usuario_linha][usuario_coluna] = "X"
        

