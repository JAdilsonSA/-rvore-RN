# arvore_rubro_negra.py

from no import No


class ArvoreRubroNegra:

    def __init__(self):
        self.raiz = None

    # Rotação à esquerda
    def rotacao_esquerda(self, x):

        y = x.direita
        x.direita = y.esquerda

        if y.esquerda:
            y.esquerda.pai = x

        y.pai = x.pai

        if not x.pai:
            self.raiz = y

        elif x == x.pai.esquerda:
            x.pai.esquerda = y

        else:
            x.pai.direita = y

        y.esquerda = x
        x.pai = y

    # Rotação à direita
    def rotacao_direita(self, y):

        x = y.esquerda
        y.esquerda = x.direita

        if x.direita:
            x.direita.pai = y

        x.pai = y.pai

        if not y.pai:
            self.raiz = x

        elif y == y.pai.direita:
            y.pai.direita = x

        else:
            y.pai.esquerda = x

        x.direita = y
        y.pai = x

    # Inserção simples
    def inserir(self, chave):

        novo = No(chave)

        pai = None
        atual = self.raiz

        while atual:
            pai = atual

            if novo.chave < atual.chave:
                atual = atual.esquerda
            else:
                atual = atual.direita

        novo.pai = pai

        if pai is None:
            self.raiz = novo

        elif novo.chave < pai.chave:
            pai.esquerda = novo

        else:
            pai.direita = novo

        self.corrigir_insercao(novo)

    # Correção das propriedades rubro-negras
    def corrigir_insercao(self, z):

        while z != self.raiz and z.pai.cor == "VERMELHO":

            if z.pai == z.pai.pai.esquerda:

                tio = z.pai.pai.direita

                if tio and tio.cor == "VERMELHO":

                    z.pai.cor = "PRETO"
                    tio.cor = "PRETO"
                    z.pai.pai.cor = "VERMELHO"

                    z = z.pai.pai

                else:

                    if z == z.pai.direita:
                        z = z.pai
                        self.rotacao_esquerda(z)

                    z.pai.cor = "PRETO"
                    z.pai.pai.cor = "VERMELHO"

                    self.rotacao_direita(z.pai.pai)

            else:

                tio = z.pai.pai.esquerda

                if tio and tio.cor == "VERMELHO":

                    z.pai.cor = "PRETO"
                    tio.cor = "PRETO"
                    z.pai.pai.cor = "VERMELHO"

                    z = z.pai.pai

                else:

                    if z == z.pai.esquerda:
                        z = z.pai
                        self.rotacao_direita(z)

                    z.pai.cor = "PRETO"
                    z.pai.pai.cor = "VERMELHO"

                    self.rotacao_esquerda(z.pai.pai)

        self.raiz.cor = "PRETO"

    # Percurso em ordem
    def em_ordem(self, no):

        if no:
            self.em_ordem(no.esquerda)
            print(f"{no.chave} ({no.cor})")
            self.em_ordem(no.direita)


    def mostrar_arvore(self, no, espaco="", ultimo=True):

        if no is not None:

            print(espaco, end="")

            if ultimo:
                print("└── ", end="")
                novo_espaco = espaco + "    "
            else:
                print("├── ", end="")
                novo_espaco = espaco + "│   "

            print(f"{no.chave} ({no.cor[0]})")

            self.mostrar_arvore(no.esquerda, novo_espaco, False)
            self.mostrar_arvore(no.direita, novo_espaco, True)