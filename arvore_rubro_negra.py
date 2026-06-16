# arvore_rubro_negra.py

from no import No


class ArvoreRubroNegra:

    def __init__(self):

      self.NIL = No(None)
      self.NIL.cor = "PRETO"

      self.NIL.esquerda = self.NIL
      self.NIL.direita = self.NIL

      self.raiz = self.NIL

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

        novo.esquerda = self.NIL
        novo.direita = self.NIL

        pai = None
        atual = self.raiz

        while atual != self.NIL:
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

    # Busca um valor na árvore
    def buscar(self, chave):

      atual = self.raiz

      while atual != self.NIL:

        if chave == atual.chave:
            return atual

        elif chave < atual.chave:
            atual = atual.esquerda

        else:
            atual = atual.direita

      return self.NIL

    # Remove um valor da árvore
    def remover(self, chave):

      z = self.buscar(chave)

      if z == self.NIL:
        return False

      y = z

      cor_original = y.cor

      if z.esquerda == self.NIL:

        x = z.direita

        self.substituir(z, z.direita)

      elif z.direita == self.NIL:

        x = z.esquerda

        self.substituir(z, z.esquerda)

      else:

        y = self.minimo(z.direita)

        cor_original = y.cor

        x = y.direita

        if y.pai == z:

            x.pai = y

        else:

            self.substituir(y, y.direita)

            y.direita = z.direita

            y.direita.pai = y

        self.substituir(z, y)

        y.esquerda = z.esquerda

        y.esquerda.pai = y

        y.cor = z.cor

      if cor_original == "PRETO":
        self.corrigir_remocao(x)

      return True

    def corrigir_remocao(self, x):

      while x != self.raiz and x.cor == "PRETO":

        if x == x.pai.esquerda:

            irmao = x.pai.direita

            # Caso 1
            if irmao.cor == "VERMELHO":

                irmao.cor = "PRETO"
                x.pai.cor = "VERMELHO"

                self.rotacao_esquerda(x.pai)

                irmao = x.pai.direita

            # Caso 2
            if (irmao.esquerda.cor == "PRETO" and
                irmao.direita.cor == "PRETO"):

                irmao.cor = "VERMELHO"

                x = x.pai

            else:

                # Caso 3
                if irmao.direita.cor == "PRETO":

                    irmao.esquerda.cor = "PRETO"

                    irmao.cor = "VERMELHO"

                    self.rotacao_direita(irmao)

                    irmao = x.pai.direita

                # Caso 4
                irmao.cor = x.pai.cor

                x.pai.cor = "PRETO"

                irmao.direita.cor = "PRETO"

                self.rotacao_esquerda(x.pai)

                x = self.raiz

        else:

            irmao = x.pai.esquerda

            # Espelho do caso anterior
            if irmao.cor == "VERMELHO":

                irmao.cor = "PRETO"

                x.pai.cor = "VERMELHO"

                self.rotacao_direita(x.pai)

                irmao = x.pai.esquerda

            if (irmao.direita.cor == "PRETO" and
                irmao.esquerda.cor == "PRETO"):

                irmao.cor = "VERMELHO"

                x = x.pai

            else:

                if irmao.esquerda.cor == "PRETO":

                    irmao.direita.cor = "PRETO"

                    irmao.cor = "VERMELHO"

                    self.rotacao_esquerda(irmao)

                    irmao = x.pai.esquerda

                irmao.cor = x.pai.cor

                x.pai.cor = "PRETO"

                irmao.esquerda.cor = "PRETO"

                self.rotacao_direita(x.pai)

                x = self.raiz

      x.cor = "PRETO"

    # Substitui um nó por outro
    def substituir(self, antigo, novo):

      if antigo.pai is None:
        self.raiz = novo

      elif antigo == antigo.pai.esquerda:
        antigo.pai.esquerda = novo

      else:
        antigo.pai.direita = novo

      novo.pai = antigo.pai

    # Retorna o menor nó de uma subárvore
    def minimo(self, no):

      while no.esquerda != self.NIL:
        no = no.esquerda

      return no      
    
    # Percurso em ordem
    def em_ordem(self, no):

        if no:
            self.em_ordem(no.esquerda)
            print(f"{no.chave} ({no.cor})")
            self.em_ordem(no.direita)


    def mostrar_arvore(self, no, espaco="", ultimo=True):

        if no != self.NIL:

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
    def mostrar(self):
      self.mostrar_arvore(self.raiz)
