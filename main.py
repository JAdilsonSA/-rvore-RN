from arvore_rubro_negra import ArvoreRubroNegra

arvore = ArvoreRubroNegra()

valores = [10, 20, 30, 15, 5, 25]

for valor in valores:
    arvore.inserir(valor)

arvore.mostrar_arvore(arvore.raiz)

valor_procurado = 15

resultado = arvore.buscar(valor_procurado)

if resultado:
    print(f"\nNó {valor_procurado} encontrado!")
    print(f"Cor: {resultado.cor}")
else:
    print(f"\nNó {valor_procurado} não encontrado.")

print("\nÁrvore antes da remoção:")
arvore.mostrar_arvore(arvore.raiz)

arvore.remover(10)

print("\nÁrvore depois da remoção:")
arvore.mostrar_arvore(arvore.raiz)



