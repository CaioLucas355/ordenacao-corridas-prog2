# ordenacao-corridas-prog2
Trabalho prático de Programação 2 (BSI - Ifes Serra): ordenação recursiva O(n log n) do histórico de corridas de um aplicativo de transporte, com múltiplos critérios de classificação.

# Histórico de Corridas - Ordenação Multicritério

Trabalho prático da disciplina de **Programação 2** (Bacharelado em Sistemas de Informação - Ifes Campus Serra).

## 📋 Sobre o projeto

O programa simula a etapa de histórico de corridas de um aplicativo de transporte de
passageiros. A partir de três dicionários (usuários, veículos e corridas), o sistema:

1. Lê os dados de um arquivo binário (`entrada.bin`), gerado previamente com o módulo `pickle`;
2. Monta uma lista contendo os identificadores de cada corrida;
3. Ordena essa lista segundo cinco critérios, em uma **única ordenação recursiva O(n·log n)**;
4. Gera um relatório formatado em `saida.txt`, agrupando as corridas por categoria e data.

## 🗂️ Estrutura dos dados de entrada

| Dicionário | Chave | Valor |
|---|---|---|
| `usuarios` | CPF | (nome, estrelas, é_motorista) |
| `veiculos` | Placa | (categoria, CPF do motorista) |
| `corridas` | ID da corrida | (placa, CPF do cliente, data, hora_início, duração, valor) |

## 🔢 Critérios de ordenação (em ordem de prioridade)

1. Categoria da corrida: `Black` → `Comfort` → `Comum` → `Moto`
2. Data da corrida: mais recente → mais antiga
3. Estrelas do motorista: maior → menor
4. Nome do cliente: ordem alfabética
5. Valor da corrida: maior → menor

## ⚙️ Algoritmo

A ordenação é implementada com um algoritmo recursivo de complexidade média
**O(n·log n)** (Merge Sort / Quick Sort), executado **uma única vez** sobre a lista
de identificadores das corridas. Nenhuma estrutura auxiliar adicional é criada.

A função `sort()` nativa do Python **não é utilizada**, conforme exigido pelo enunciado.

## 📁 Arquivos
.

├── main.py          # Programa principal

├── entrada.bin      # Arquivo de entrada (não versionado)

├── saida.txt        # Arquivo de saída gerado (não versionado)

└── README.md

> ⚠️ Os arquivos `entrada.bin` e `saida.txt` não são versionados neste repositório,
> conforme orientação do enunciado.

## ▶️ Como executar

```bash
python main.py
```

O programa lê automaticamente `entrada.bin` (mesmo diretório) e gera `saida.txt`
com o relatório formatado.

## 📤 Exemplo de saída
CATEGORIA: Black

02/05/2026

Motorista: Antonio Barbosa Rodrigues ****

Cliente: Lucas Soares Lopes

Periodo: 12:10 - 12:36

Valor: R$28.00

## 👥 Integrantes

- [Caio Lucas da Silva]
- [Arthur Corrêa Sobrinho]

## 📚 Disciplina

Programação 2 - BSI - Ifes Campus Serra
Professor: [Hilario Seibel Júnior]
Data de entrega: 23/06/2026
