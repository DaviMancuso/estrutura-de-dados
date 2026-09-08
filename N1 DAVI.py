class no_lista:
    def __init__(self, v):
        self.valor = v
        self.ant = None
        self.prox = None

class Lista:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def mostrar(self):
        aux = self.inicio
        while aux != None:
            print(aux.valor, end=" -> ")
            aux = aux.prox
        print("FIM")

    def insere_comeco(self, x):
        novo = no_lista(x)
        if self.inicio == None:
            self.inicio = novo
            self.fim = novo
        else:
            novo.prox = self.inicio
            self.inicio.ant = novo
            self.inicio = novo

    def insere_fim(self, x):
        novo = no_lista(x)
        if self.fim == None:
            self.inicio = novo
            self.fim = novo
        else:
            novo.ant = self.fim
            self.fim.prox = novo
            self.fim = novo

    def insere_posicao(self, x, pos):
        if pos < 0:
            print("erro na posicao")
            return

        if pos == 0:
            self.insere_comeco(x)
            return

        novo = no_lista(x)
        aux = self.inicio
        
        cont = 0
        while aux != None and cont < pos - 1:
            aux = aux.prox
            cont = cont + 1

        if aux == None:
            print("posicao nao existe na lista!!!")
            return

        if aux.prox == None:
            self.insere_fim(x)
            return

        novo.prox = aux.prox
        novo.ant = aux
        aux.prox.ant = novo
        aux.prox = novo

    def remove_primeiro(self):
        if self.inicio != None:
            self.inicio = self.inicio.prox
            if self.inicio != None:
                self.inicio.ant = None
            else:
                self.fim = None

    def remove_ultimo(self):
        if self.fim != None:
            self.fim = self.fim.ant
            if self.fim != None:
                self.fim.prox = None
            else:
                self.inicio = None

L = Lista()
L.insere_comeco(10)
L.insere_fim(20)
L.insere_fim(30)
L.mostrar()

L.insere_posicao(15, 1)
L.mostrar()

L.remove_primeiro()
L.remove_ultimo()
L.mostrar()
