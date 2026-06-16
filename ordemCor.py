import pickle
#Entrada de Dados

def chamado():
    return input("Digite o Nome do Arquivo:\t")

#Processamento de Dados

def main():
    
    arq = chamado();
    with open(arq , "rb") as f:
        usuarios = pickle.load(f)
        veiculos = pickle.load(f)
        corrida = pickle.load(f)



#Saída de Dados