# ex087 - Sequência de Tribonacci
# Fonte: Extra - fora do curso (seu código / variação)

n=int(input('Escolha quantos termos para a sequencia de TRIBONACCI:  '))
t1=0
t2=0
t3=1
c=4
print(f'{t1} -- {t2} -- {t3}',end='')
while c <=n:
    t4=t1+t2+t3
    print(f'-- {t4}',end='')
    t1=t2
    t2=t3
    t3=t4
    c+=1
print('--FIM')
