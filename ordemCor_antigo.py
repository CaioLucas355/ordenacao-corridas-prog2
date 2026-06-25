#ARTHUR CORRÊA SOBRINHO 20252BSI0046
#CAIO LUCAS DA SILVA NASCIMENTO 20252BSI007

#--------------------------------------------------------------------------

import pickle
from time import time


def chamado():
    return input("Digite o Nome do Arquivo:\t")


arq = chamado()
#leitura do arquivo binário:
with open(arq, 'rb') as arquivo:
    usuarios = pickle.load(arquivo)
    veiculos = pickle.load(arquivo)
    corridas = pickle.load(arquivo)


#criação da lista de ids (somente as chaves do dicionário corridas):
ids_corridas = [elem for elem in corridas]


#mapeamento de prioridade das categorias:
categoria_prioridade = {'Black': 1,'Comfort': 2,'Comum': 3,'Moto': 4}


#-----------------------------------------------------------------
def comparar(id1, id2):
    """
    Retorna True se id1 deve vir antes de id2 na ordenação.
    Critérios (em ordem de prioridade):
      1. Categoria (Black > Comfort > Comum > Moto)
      2. Data (mais recente primeiro)
      3. Estrelas do motorista (maior primeiro)
      4. Nome do cliente (ordem alfabética)
      5. Valor da corrida (maior primeiro)
    """
    placa1, cpf_cliente1, data1, horario1, duracao1, valor1 = corridas[id1]
    placa2, cpf_cliente2, data2, horario2, duracao2, valor2 = corridas[id2]
    dia1, mes1, ano1 = data1
    dia2, mes2, ano2 = data2

    cat1 = veiculos[placa1][0]
    cat2 = veiculos[placa2][0]
    prio1 = categoria_prioridade[cat1]
    prio2 = categoria_prioridade[cat2]
    if prio1 != prio2:
        return prio1 < prio2

    if ano1 != ano2:
        return ano1 > ano2
    if mes1 != mes2:
        return mes1 > mes2
    if dia1 != dia2:
        return dia1 > dia2

    cpf_motorista1 = veiculos[placa1][1]
    cpf_motorista2 = veiculos[placa2][1]
    _, estrelas1, _ = usuarios[cpf_motorista1]
    _, estrelas2, _ = usuarios[cpf_motorista2]
    if estrelas1 != estrelas2:
        return estrelas1 > estrelas2

    nome_cliente1, _, _ = usuarios[cpf_cliente1]
    nome_cliente2, _, _ = usuarios[cpf_cliente2]
    if nome_cliente1 != nome_cliente2:
        return nome_cliente1 < nome_cliente2

    return valor1 > valor2


#-----------------------------------------------------------------

def insertion_sort(l, inicio, fim):

    for i in range(inicio + 1, fim):
        chave = l[i]
        j = i - 1
        while j >= inicio and comparar(chave, l[j]):
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = chave

#-----------------------------------------------------------------

def merge(l, lEsq, lDir):

    i = 0  #ponteiro para lEsq
    j = 0  #ponteiro para lDir
    k = 0  #ponteiro para l (resultado)

    while i < len(lEsq) and j < len(lDir):
        if comparar(lEsq[i], lDir[j]):
            l[k] = lEsq[i]
            i += 1
        else:
            l[k] = lDir[j]
            j += 1
        k += 1


    #copia o restante de lEsq
    while i < len(lEsq):
        l[k] = lEsq[i]
        i += 1
        k += 1


    #copia o restante de lDir 
    while j < len(lDir):
        l[k] = lDir[j]
        j += 1
        k += 1


def merge_sortCA(l):

    if len(l) <= 30:
        insertion_sort(l, 0, len(l))
        return
    
    meio = len(l) // 2
    lEsq = l[:meio] #cópia da primeira metade
    lDir = l[meio:] #cópia da segunda metade
    
    merge_sortCA(lEsq)
    merge_sortCA(lDir)
    merge(l, lEsq, lDir)

#-----------------------------------------------------------------------------------

#EXECUÇÃO
t1 = time()
merge_sortCA(ids_corridas)
#Saída de Dados
nome_saida = "saida" + arq[7::]
with open(nome_saida, 'w', encoding='utf-8') as exitFile:
    categoria_atual = None
    data_atual = None
    
    for ids in ids_corridas:
        placa, cpf_passageiro, data, horario, duracao, valor = corridas[ids]
        dia, mes, ano = data
        hora, minuto = horario
        hora_final = (hora * 60 + minuto + duracao) // 60
        minuto_final = (hora * 60 + minuto + duracao) % 60
        cat, cpf_m = veiculos[placa]
        nome_m, stars, _ = usuarios[cpf_m]
        nome_c, _, _ = usuarios[cpf_passageiro]
        
        if cat != categoria_atual:
            if categoria_atual is not None:
                print(file=exitFile)
            print(f'CATEGORIA: {cat}\n', file=exitFile)
            categoria_atual = cat
            data_atual = None
            
        if data != data_atual:
            print(f'\n {dia:02d}/{mes:02d}/{ano}', file=exitFile)
            data_atual = data
            
        print(f'  Motorista: {nome_m} {stars * "*"}', file=exitFile)
        print(f'  Cliente: {nome_c}', file=exitFile)
        print(f'  Periodo: {hora:02d}:{minuto:02d} - {hora_final:02d}:{minuto_final:02d}', file=exitFile)
        print(f'  Valor: R${valor:.2f}\n', file=exitFile)
t2 = time()
print(f'Arquivo gerado: {nome_saida}')
print("tempo total: ", t2 - t1)