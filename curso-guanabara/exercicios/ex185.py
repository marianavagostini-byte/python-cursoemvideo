# ex185
# Fonte: Curso em Vídeo / prática (seu código)

def producao(*n,opc=false)
    dic={}
    dic['qtd dias']=len(n)
    dic['total']=sum(n)
    dic['maior]=max(n)
    dic['menor]=min(n)
    dic['media]=sum(n)/len(n)


resp = producao(4, 8, 6, 1, 3, 8)
print(resp)
