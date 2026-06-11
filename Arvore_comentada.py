# arvore_rubro_negra.py

from no import No


class ArvoreRubroNegra:

    def __init__(self):
        # Inicializa a árvore vazia
        self.raiz = None

    # Rotação à esquerda utilizada para balanceamento
    def rotacao_esquerda(self, x):

        # Filho direito sobe para a posição de x
        y = x.direita

        # Subárvore esquerda de y passa a ser direita de x
        x.direita = y.esquerda

        if y.esquerda:
            y.esquerda.pai = x

        # y assume o pai de x
        y.pai = x.pai

        # Se x era a raiz, y passa a ser a nova raiz
        if not x.pai:
            self.raiz = y

        elif x == x.pai.esquerda:
            x.pai.esquerda = y

        else:
            x.pai.direita = y

        # x passa a ser filho esquerdo de y
        y.esquerda = x
        x.pai = y

    # Rotação à direita utilizada para balanceamento
    def rotacao_direita(self, y):

        # Filho esquerdo sobe para a posição de y
        x = y.esquerda

        # Subárvore direita de x passa a ser esquerda de y
        y.esquerda = x.direita

        if x.direita:
            x.direita.pai = y

        # x assume o pai de y
        x.pai = y.pai

        # Se y era a raiz, x passa a ser a nova raiz
        if not y.pai:
            self.raiz = x

        elif y == y.pai.direita:
            y.pai.direita = x

        else:
            y.pai.esquerda = x

        # y passa a ser filho direito de x
        x.direita = y
        y.pai = x

    # Inserção seguindo as regras da árvore binária de busca
    def inserir(self, chave):

        novo = No(chave)

        pai = None
        atual = self.raiz

        # Procura a posição correta para inserir
        while atual:
            pai = atual

            if novo.chave < atual.chave:
                atual = atual.esquerda
            else:
                atual = atual.direita

        novo.pai = pai

        # Caso a árvore esteja vazia
        if pai is None:
            self.raiz = novo

        # Inserção à esquerda
        elif novo.chave < pai.chave:
            pai.esquerda = novo

        # Inserção à direita
        else:
            pai.direita = novo

        # Corrige possíveis violações da árvore rubro-negra
        self.corrigir_insercao(novo)

    # Rebalanceamento após inserção
    def corrigir_insercao(self, z):

        # Executa enquanto houver dois nós vermelhos consecutivos
        while z != self.raiz and z.pai.cor == "VERMELHO":

            # Caso em que o pai está à esquerda do avô
            if z.pai == z.pai.pai.esquerda:

                # Identifica o tio
                tio = z.pai.pai.direita

                # Caso 1: tio vermelho
                if tio and tio.cor == "VERMELHO":

                    # Recoloração
                    z.pai.cor = "PRETO"
                    tio.cor = "PRETO"
                    z.pai.pai.cor = "VERMELHO"

                    # Continua verificando a partir do avô
                    z = z.pai.pai

                else:

                    # Caso 2: nó é filho direito
                    if z == z.pai.direita:
                        z = z.pai
                        self.rotacao_esquerda(z)

                    # Caso 3: rotação e recoloração
                    z.pai.cor = "PRETO"
                    z.pai.pai.cor = "VERMELHO"

                    self.rotacao_direita(z.pai.pai)

            # Caso simétrico: pai está à direita do avô
            else:

                tio = z.pai.pai.esquerda

                # Caso 1: tio vermelho
                if tio and tio.cor == "VERMELHO":

                    z.pai.cor = "PRETO"
                    tio.cor = "PRETO"
                    z.pai.pai.cor = "VERMELHO"

                    z = z.pai.pai

                else:

                    # Caso 2: nó é filho esquerdo
                    if z == z.pai.esquerda:
                        z = z.pai
                        self.rotacao_direita(z)

                    # Caso 3: rotação e recoloração
                    z.pai.cor = "PRETO"
                    z.pai.pai.cor = "VERMELHO"

                    self.rotacao_esquerda(z.pai.pai)

        # Garante que a raiz seja sempre preta
        self.raiz.cor = "PRETO"

    # Percurso em ordem (esquerda -> raiz -> direita)
    def em_ordem(self, no):

        if no:
            self.em_ordem(no.esquerda)
            print(f"{no.chave} ({no.cor})")
            self.em_ordem(no.direita)

    # Exibe a árvore em formato hierárquico
    def mostrar_arvore(self, no, espaco="", ultimo=True):

        if no is not None:

            print(espaco, end="")

            if ultimo:
                print("└── ", end="")
                novo_espaco = espaco + "    "
            else:
                print("├── ", end="")
                novo_espaco = espaco + "│   "

            # Mostra chave e cor do nó
            print(f"{no.chave} ({no.cor[0]})")

            # Exibe recursivamente os filhos
            self.mostrar_arvore(no.esquerda, novo_espaco, False)
            self.mostrar_arvore(no.direita, novo_espaco, True)