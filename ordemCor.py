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

#criação da lista de ids (somente as chaves do dicionário corridas):
ids_corridas = [elem for elem in corridas]


#mapeamento de prioridade das categorias:
categoria_prioridade = {'Black': 1,'Comfort': 2,'Comum': 3,'Moto': 4}


#-----------------------------------------------------------------------------------


def chave_ordenacao(identidadeC):

    placa, cpf_cliente, data, _, _, valor = corridas[identidadeC]
    dia, mes, ano = data
    cat = veiculos[placa][0]
    prio = categoria_prioridade[cat]
    cpf_motorista = veiculos[placa][1]
    _, estrelas, _ = usuarios[cpf_motorista]
    nome_cliente, _, _ = usuarios[cpf_cliente]

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

    #Critérios (em ordem de prioridade):
          #1. Categoria (Black > Comfort > Comum > Moto)
          #2. Data (mais recente primeiro)
          #3. Estrelas do motorista (maior primeiro)
          #4. Nome do cliente (ordem alfabética)
          #5. Valor da corrida (maior primeiro)

    return (prio, -ano, -mes, -dia, -estrelas, nome_cliente, -valor)


#PRÉ-CÁLCULO DAS CHAVES DENTRO DO PRÓPRIO DICIONÁRIO "corridas".
for identidadeC in ids_corridas:
    corridas[identidadeC] = chave_ordenacao(identidadeC)

"""
"Viver é muito perigoso..."
"""


#-----------------------------------------------------------------

def insertion_sort(l, inicio, fim):

    for i in range(inicio + 1, fim):
        chave = l[i]
        j = i - 1
        #AGORA AS CHAVES ESTÃO NO DICIONÁRIO corridas
        while j >= inicio and corridas[chave] < corridas[l[j]]:
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = chave

#-----------------------------------------------------------------

def merge(l, lEsq, lDir):

    i = 0  #ponteiro para lEsq
    j = 0  #ponteiro para lDir
    k = 0  #ponteiro para l (resultado)

    while i < len(lEsq) and j < len(lDir):
        #AGORA AS CHAVES ESTÃO NO DICIONÁRIO corridas
        if corridas[lEsq[i]] < corridas[lDir[j]]: #compara as chaves
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
merge_sortCA(itens)
t2 = time()

print(ids_corridas, t2 - t1)

'''
#Estrutura dos dicionários:
# usuarios = {’468.791.579-55’: (’Lucas Soares Lopes’, 1, False),
#               cpf : (nome, estrelas, ehMotorista)
#veiculos = {’BJG-7G74’: (’Black’, ’821.833.773-30’),
#               placa : (categoria , cpf_motorista)
#corridas =  { 6: (’IXU-6J15’, ’468.791.579-55’, (2, 5, 2026), (0, 57), 11, 13),
#               if : (placa, cpf_passageiro, data(dia,mes,aano), horario(hora, minuto), duracao, valor)
#usemos essas terminologia pra facilitar o nosso trabalho para compreendermos facilmente o códgio
'''
#Saída de Dados



#Estrutura de como deve ser a saída
        
'''
CATEGORIA: Black
\t02/05/2026
\t\tMotorista: Antonio Barbosa Rodrigues ****
\t\tCliente: Lucas Soares Lopes
\t\tPeriodo: 12:10 - 12:36
\t\tValor: R$28.00

\t\tMotorista: Fernanda Santos Santana ****
\t\tCliente: Lucas Soares Lopes
\t\tPeriodo: 00:57 - 01:08
\t\tValor: R$13.00   


'''