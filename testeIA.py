#ARTHUR CORRÊA SOBRINHO 20252BSI0046
#CAIO LUCAS DA SILVA NASCIMENTO 20252BSI007

#--------------------------------------------------------------------------

import pickle
from time import time
from functools import lru_cache


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





#-----------------------------------------------------------------
@lru_cache(maxsize=None)
def chave(id_corrida):
    """
    Pré-computa e armazena em cache a tupla de ordenação de cada ID.
    Calculada apenas uma vez por ID — reutilizada em todas as comparações.
    """
    placa, cpf_cliente, data, horario, duracao, valor = corridas[id_corrida]
    dia, mes, ano = data

    cat        = veiculos[placa][0]
    cpf_mot    = veiculos[placa][1]
    _, estrelas, _ = usuarios[cpf_mot]
    nome_c, _, _   = usuarios[cpf_cliente]

    if cat == 'Black':
        prio = 1
    elif cat == 'Comfort':
        prio = 2
    elif cat == 'Comum':
        prio = 3
    else:
        prio = 4

    return (
        prio,                       # menor = mais prioritário
        -ano, -mes, -dia,           # negativo → mais recente primeiro
        -estrelas,                  # negativo → maior primeiro
        nome_c,                     # alfabético
        -valor                      # negativo → maior primeiro
    )


def comparar(id1, id2):
    """
    Retorna True se id1 deve vir antes de id2 na ordenação.
    Agora usa apenas comparação de tuplas — O(1) após o cache aquecido.
    """
    return chave(id1) < chave(id2)


#-----------------------------------------------------------------

def insertion_sort(l, inicio, fim):

    for i in range(inicio + 1, fim):
        chave_i = l[i]
        j = i - 1
        while j >= inicio and comparar(chave_i, l[j]):
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = chave_i

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

    if len(l) <= 32:            # limiar ligeiramente maior → menos chamadas recursivas
        insertion_sort(l, 0, len(l))
        return

    meio = len(l) // 2
    lEsq = l[:meio]             #cópia da primeira metade
    lDir = l[meio:]             #cópia da segunda metade

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
    data_atual      = None

    for ids in ids_corridas:
        placa, cpf_passageiro, data, horario, duracao, valor = corridas[ids]
        dia, mes, ano   = data
        hora, minuto    = horario
        total_min       = hora * 60 + minuto + duracao
        hora_final, minuto_final = divmod(total_min, 60)   # substitui // e %
        cat, cpf_m      = veiculos[placa]
        nome_m, stars, _ = usuarios[cpf_m]
        nome_c, _, _    = usuarios[cpf_passageiro]

        if cat != categoria_atual:
            if categoria_atual is not None:
                exitFile.write('\n')
            exitFile.write(f'CATEGORIA: {cat}\n\n')
            categoria_atual = cat
            data_atual      = None

        if data != data_atual:
            exitFile.write(f' {dia}/{mes}/{ano}\n\n')
            data_atual = data

        # Uma única chamada write por corrida — menos syscalls de I/O
        exitFile.write(
            f'  Motorista: {nome_m} {"*" * stars}\n'
            f'  Cliente: {nome_c}\n'
            f'  Periodo: {hora}:{minuto} - {hora_final}:{minuto_final}\n'
            f'  Valor: R${valor:.2f}\n\n'
        )

t2 = time()
print(f'Arquivo gerado: {nome_saida}')
print("tempo total: ", t2 - t1)