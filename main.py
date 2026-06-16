from arvore_rubro_negra import ArvoreRubroNegra

arvore = ArvoreRubroNegra()

# Inserção dos valores
valores = [10, 20, 30, 15, 5, 25]

for valor in valores:
    arvore.inserir(valor)

print("Árvore antes da remoção:")
arvore.mostrar_arvore(arvore.raiz)

# Remoção de um valor
arvore.remover(10)

print("\nÁrvore depois da remoção do 10:")
arvore.mostrar_arvore(arvore.raiz)


