# faça um sistema de conceitos ultizando valor do terminal, obtendo média de 4 ou 2 semestre
#apresentando conceito final, use functions, if/else, laço de repetição

def printa_isso(string: str):
    print(string)
    pass



if __name__=='__main__':

    valor_terminal = input('digite um valor: ')
    print('Hello "teste" world')
    print("Hello world")


    tem_dinheiro = True
    dinheiro = 10.5
    idade = 20

    nome = 'joao'
    print(nome)

    frutas = ['banana','maça','pera','uva']
    #frutas = ['banana','maça',2 , tem_dinheiro]
    
    if tem_dinheiro:
        print(dinheiro)

elif tem_dinheiro == False:
    print('voce eh pobre')
else:
    print('bug')

printa_isso(nome)

for fruta in frutas :
    printa_isso(fruta)

valor_nulo = None

printa_isso(valor_terminal)

lista_telefonica = {'joao': ['00000','ra rua dos bobos'], 'ana': '1111111'}
print(lista_telefonica['joao'])

for value in lista_telefonica['joao']:
    print(value)