from arvore_rubro_negra import ArvoreRubroNegra

arvore = ArvoreRubroNegra()

valores = [10, 20, 30, 15, 5, 25]

for valor in valores:
    print(f"\nInserindo {valor}...")
    arvore.inserir(valor)

print("\nÁrvore final:\n")
arvore.mostrar_arvore(arvore.raiz)



