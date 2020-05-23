from array import array
from vetores import vetor
from listas import lista_ligada
from listas import  lista_duplamente_ligada
from pilhas import pilha
from filas import fila

print(30 * "-","MENU",30*"-")
print("1. Vetores")
print("2. Lista Ligadas")
print("3. Lista Duplamente Ligadas")
print("4. Pilhas")
print("5. Filas")


menu = int(input("Digite a opcao desejada: "))

if menu == 1:
    vetor_teste = vetor.Vetor(0)
    vetor_teste.inserir_elemento_posicion(1,0)
    vetor_teste.inserir_elemento_posicion(2,1)
    vetor_teste.inserir_elemento_posicion(3,2)
    vetor_teste.inserir_elemento_posicion(4,2)
    vetor_teste.inserir_elemento_posicion(5,2)
    vetor_teste.inserir_elemento_final(1)

    print(vetor_teste.tamanho_vetor())
    print(vetor_teste)

    print(vetor_teste.indice(4))
    vetor_teste.remover_elemento_indice(3)
    print(vetor_teste)
    vetor_teste.remover_elemento(5)
    print(vetor_teste)

elif menu == 2:
    lista_teste = lista_ligada.ListaLigada()
    lista_teste.inserir(1)
    lista_teste.inserir(4)
    lista_teste.inserir(5)
    lista_teste.inserir_posicao(2,10)
    print(lista_teste)
    lista_teste.remover_elemento(4)
    print(lista_teste)


elif menu == 3:
    lista_teste = lista_duplamente_ligada.ListaDuplamenteLigada()
    lista_teste.inserir(1)
    lista_teste.inserir(4)
    lista_teste.inserir(5)
    lista_teste.inserir_posicao(2,10)
    print(lista_teste)
    lista_teste.remover_posicao(1)
    print(lista_teste)

elif menu == 4:
    pilha_teste = pilha.Pilha()
    pilha_teste.empilhar(5)
    #pilha_teste.empilhar(6)
    #pilha_teste.empilhar(7)
    print(pilha_teste.desempilhar())

elif menu == 5:
    fila_teste = fila.Fila()
    fila_teste.enfileira(1)
    fila_teste.enfileira(2)
    fila_teste.enfileira(3)
    fila_teste.enfileira(4)
    print(fila_teste)
    print(fila_teste.desenfileirar())
    print(fila_teste)
    print(fila_teste.desenfileirar())
    print(fila_teste)
    fila_teste.enfileira(6)
    print(fila_teste)
else:
    print('opcao invalida')


