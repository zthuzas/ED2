class No:
    def __init__(self, valor: int):
        self.valor = valor
        self.proximo: No = None

class ListaEncadeada:
    def __init__(self):
        self.inicio: No = None
        self.fim: No = None

    def inserir(self, valor):
        novo_no = No(valor)

        if not self.fim:
            self.inicio = novo_no
            self.fim = novo_no
        else:
            self.fim.proximo = novo_no
            self.fim = novo_no
    
    def exibir(self):
        atual = self.inicio

        while atual:
            print(atual.valor, end=' ')
            atual = atual.proximo
        print()

def ordenar_lista(lista: ListaEncadeada):
    if lista.inicio is None or lista.inicio.proximo is None:
        return lista
    
    esquerda, direita = dividir(lista)
    esquerda_ordenada = ordenar_lista(esquerda)
    direita_ordenada = ordenar_lista(direita)

    return juntar(esquerda_ordenada, direita_ordenada)

def dividir(lista: ListaEncadeada):
    lenta = lista.inicio
    rapida = lista.inicio
    anterior = None

    while rapida and rapida.proximo:
        anterior = lenta
        lenta = lenta.proximo
        rapida = rapida.proximo.proximo

    lista_esquerda = ListaEncadeada()
    lista_direita = ListaEncadeada()

    lista_esquerda.inicio = lista.inicio
    lista_direita.inicio = lenta

    if anterior:
        anterior.proximo = None

    lista_esquerda.fim = encontrar_fim(lista_esquerda.inicio)
    lista_direita.fim = encontrar_fim(lista_direita.inicio)

    return lista_esquerda, lista_direita

def encontrar_fim(no_inicial):
    atual = no_inicial
    if not atual:
        return None

    while atual.proximo:
        atual = atual.proximo

    return atual

def juntar(lista1: ListaEncadeada, lista2: ListaEncadeada):
    base = No(0)
    ponteiro = base

    atual1 = lista1.inicio
    atual2 = lista2.inicio

    while atual1 and atual2:
        if atual1.valor < atual2.valor:
            ponteiro.proximo = atual1
            atual1 = atual1.proximo
        else:
            ponteiro.proximo = atual2
            atual2 = atual2.proximo

        ponteiro = ponteiro.proximo

    ponteiro.proximo = atual1 if atual1 else atual2

    resultado = ListaEncadeada()
    resultado.inicio = base.proximo
    resultado.fim = encontrar_fim(resultado.inicio)

    return resultado

def testar():
    lista = ListaEncadeada()
    for numero in [3, 2, 5, 9, 4]:
        lista.inserir(numero)

    print("Lista original:")
    lista.exibir()

    ordenada = ordenar_lista(lista)

    print("\nLista ordenada:")
    ordenada.exibir()

testar()
