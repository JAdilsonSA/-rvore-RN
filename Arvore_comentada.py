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


    # Busca um valor específico na árvore
    def buscar(self, chave):

    # Começa a busca pela raiz
        atual = self.raiz

    # Percorre a árvore enquanto existir um nó
        while atual:

        # Se encontrou a chave procurada
            if chave == atual.chave:
                return atual

        # Se a chave procurada é menor,
        # continua a busca pela subárvore esquerda
            elif chave < atual.chave:
                atual = atual.esquerda

        # Se a chave procurada é maior,
        # continua a busca pela subárvore direita
            else:
                atual = atual.direita

    # Se sair do laço, a chave não existe na árvore
        return None

# Remove um valor da árvore
# Remoção simplificada.
# Não realiza o rebalanceamento rubro-negro após a exclusão.
    def remover(self, chave):

        no = self.buscar(chave)

    # Valor não encontrado
        if no is None:
            return False

    # Caso 1: nó sem filhos
        if no.esquerda is None and no.direita is None:

            if no == self.raiz:
                self.raiz = None

            elif no == no.pai.esquerda:
                no.pai.esquerda = None

            else:
                no.pai.direita = None

    # Caso 2: nó possui apenas filho direito
        elif no.esquerda is None:

            self.substituir(no, no.direita)

    # Caso 3: nó possui apenas filho esquerdo
        elif no.direita is None:

            self.substituir(no, no.esquerda)

    # Caso 4: nó possui dois filhos
        else:

            sucessor = self.minimo(no.direita)

            no.chave = sucessor.chave

            if sucessor == sucessor.pai.esquerda:
                sucessor.pai.esquerda = sucessor.direita
            else:
                sucessor.pai.direita = sucessor.direita

        return True

    # Substitui um nó por outro
    def substituir(self, antigo, novo):

        if antigo.pai is None:
            self.raiz = novo

        elif antigo == antigo.pai.esquerda:
            antigo.pai.esquerda = novo

        else:
            antigo.pai.direita = novo

        if novo:
            novo.pai = antigo.pai

    # Retorna o menor nó de uma subárvore
    def minimo(self, no):

        while no.esquerda:
            no = no.esquerda

        return no
    
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