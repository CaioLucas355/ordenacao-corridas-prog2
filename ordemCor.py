import pickle
#Entrada de Dados

def chamado():
    return input("Digite o Nome do Arquivo:\t")

#Processamento de Dados

def main():
    
    lcorrida = []
    arq = chamado();
    with open(arq , "rb") as f:
        usuarios = pickle.load(f)
        veiculos = pickle.load(f)
        corridas = pickle.load(f)

    for n in corridas:
        lcorrida.append(n)
        
        
        


#Estrutura dos dicionários:
# usuarios = {’468.791.579-55’: (’Lucas Soares Lopes’, 1, False),
#               cpf : (nome, estrelas, ehMotorista)
#veiculos = {’BJG-7G74’: (’Black’, ’821.833.773-30’),
#               placa : (categoria , cpf_motorista)
#corridas =  { 6: (’IXU-6J15’, ’468.791.579-55’, (2, 5, 2026), (0, 57), 11, 13),
#               if : (placa, cpf_passageiro, data(dia,mes,aano), horario(hora, minuto), duracao, valor)

#usemos essas terminologia pra facilitar o nosso trabalho para compreendermos facilmente o códgio

#Saída de Dados



#Estrutura de como deve ser a saída

    for c in lcorrida:
        
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