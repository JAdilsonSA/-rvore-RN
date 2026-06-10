# no.py

class No:
    def __init__(self, chave):
        self.chave = chave
        self.cor = "VERMELHO"  # Todo novo nó nasce vermelho
        self.esquerda = None
        self.direita = None
        self.pai = None