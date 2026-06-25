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


"""
(Ah, queria deixar algo de zero relação com o código: to pensando fortemente
em substituir parte dos meus comentários com HASHTAG por essa formatação aqui, ta.
É muito legal o fato de que eu posso minimizar o comentário dessa forma. Anyway, voltando para a luta:)
"""

"""
Encontrei uma maneira melhor de escrever isso durante uma aulinha do Hilário Legal. 

for elem in corridas:
    ids_corridas.append(elem)

    
"""

#criação da lista de ids:
ids_corridas = [elem for elem in corridas]


#-----------------------------------------------------------------


#PRÉ-CÁLCULO DAS CHAVES (SUBSTITUI OS IDs POR TUPLAS (chave, id))
for i in range(len(ids_corridas)):
    identidadeC = ids_corridas[i]
    placa, cpf_cliente, data, _, _, valor = corridas[identidadeC]
    dia, mes, ano = data
    cat = veiculos[placa][0]
    
    #prioridade da categoria
    if cat == 'Black':
        prio = 1
    elif cat == 'Comfort':
        prio = 2
    elif cat == 'Comum':
        prio = 3
    else:  # 'Moto'
        prio = 4
    
    cpf_motorista = veiculos[placa][1]
    _, estrelas, _ = usuarios[cpf_motorista]
    nome_cliente, _, _ = usuarios[cpf_cliente]
    chave = (prio, -ano, -mes, -dia, -estrelas, nome_cliente, -valor)
    ids_corridas[i] = (chave, identidadeC)

#Critérios (em ordem de prioridade):
            #1. Categoria (Black > Comfort > Comum > Moto)
            #2. Data (mais recente primeiro)
            #3. Estrelas do motorista (maior primeiro)
            #4. Nome do cliente (ordem alfabética)
            #5. Valor da corrida (maior primeiro)

"""


        Função antiga dessa joça:


        def comparar(id1, id2):
        
        #Retorna True se id1 deve vir antes de id2 na ordenação.
        #Critérios (em ordem de prioridade):
        #1. Categoria (Black > Comfort > Comum > Moto)
        #2. Data (mais recente primeiro)
        #3. Estrelas do motorista (maior primeiro)
        #4. Nome do cliente (ordem alfabética)
        #5. Valor da corrida (maior primeiro)
    

        #desempacotamento do dicionario corridas
        placa1, cpf_cliente1, data1, horario1, duracao1, valor1 = corridas[id1]
        placa2, cpf_cliente2, data2, horario2, duracao2, valor2 = corridas[id2]


        #desempacotamento de data
        dia1, mes1, ano1 = data1
        dia2, mes2, ano2 = data2

        #1.Categoria
        cat1 = veiculos[placa1][0]
        cat2 = veiculos[placa2][0]
        prio1 = categoria_prioridade[cat1]
        prio2 = categoria_prioridade[cat2]

        if prio1 != prio2:
            return prio1 < prio2


        #2.Data (mais recente primeiro)

        #comparar ano, mês, dia de forma decrescente
        if ano1 != ano2:
            return ano1 > ano2
        if mes1 != mes2:
            return mes1 > mes2
        if dia1 != dia2:
            return dia1 > dia2

        #3.Estrelas do motorista (maior primeiro)
        cpf_motorista1 = veiculos[placa1][1]
        cpf_motorista2 = veiculos[placa2][1]

        #desempacota os dados do motorista (nome, estrelas, status)
        _, estrelas1, _ = usuarios[cpf_motorista1]
        _, estrelas2, _ = usuarios[cpf_motorista2]

        if estrelas1 != estrelas2:
            return estrelas1 > estrelas2

        #4.Nome do cliente (ordem alfabética)
        nome_cliente1, _, _ = usuarios[cpf_cliente1]
        nome_cliente2, _, _ = usuarios[cpf_cliente2]

        if nome_cliente1 != nome_cliente2:
            return nome_cliente1 < nome_cliente2

        #5.Valor da corrida (maior primeiro)
        return valor1 > valor2


        """


#-----------------------------------------------------------------

def insertion_sort(l, inicio, fim):
    for i in range(inicio + 1, fim):
        chave = l[i]
        j = i - 1
        while j >= inicio and chave[0] < l[j][0]:
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = chave

#-----------------------------------------------------------------

def merge(l, lEsq, lDir):
    i = 0  #ponteiro para lEsq
    j = 0  #ponteiro para lDir
    k = 0  #ponteiro para l (resultado)

    while i < len(lEsq) and j < len(lDir):
        if lEsq[i][0] < lDir[j][0]:
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

#extrai os IDs de volta
for i in range(len(ids_corridas)):
    ids_corridas[i] = ids_corridas[i][1]

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
            print(f' {dia}/{mes}/{ano}\n', file=exitFile)
            data_atual = data
            
        print(f'  Motorista: {nome_m} {stars * "*"}', file=exitFile)
        print(f'  Cliente: {nome_c}', file=exitFile)
        print(f'  Periodo: {hora}:{minuto} - {hora_final}:{minuto_final}', file=exitFile)
        print(f'  Valor: R${valor:.2f}\n', file=exitFile)
        
    
t2 = time()
print(f'Arquivo gerado: {nome_saida}')
print("tempo total: ", t2 - t1)