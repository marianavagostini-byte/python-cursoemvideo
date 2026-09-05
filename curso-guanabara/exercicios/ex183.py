# ex183
# Fonte: Curso em Vídeo / prática (seu código)

def analise(*n,desemp=False):
    dic={}
    dic['qtd']=len(n)
    dic['melhor']=min(n)
    dic['pior']=max(n)
    dic['media']=sum(n)/len(n)


    if desemp:
        if dic['media'] <=25:
            dic['desempenho'] = 'OTIMO'
        elif dic['media'] <=35:
            dic['desempenho'] = 'REGULAR'
        else:
            dic['desempenho'] = 'FRACO'

    return dic

resp=analise(28, 32, 24, 30, desemp=False)
print(resp)
