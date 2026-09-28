pilha = []

pilha.append("Python")
pilha.append("SQL")
pilha.append("Git")

print("Pilha:", pilha)

ultimo = pilha.pop()

print("Elemento removido:", ultimo)
print("Pilha atual:", pilha)

if pilha:
    print("Topo da pilha:", pilha[-1])
else:
    print("A pilha está vazia.")
