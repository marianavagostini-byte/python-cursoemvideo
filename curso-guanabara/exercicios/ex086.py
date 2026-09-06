# ex086 - Sequência multiplicativa
# Fonte: Extra - fora do curso (seu código / variação)

n=int(input('Qual quantidade da sequencia?  '))
t1=1
t2=2
c=3
print(f'{t1} -- {t2}  ',end='')
while c <=n:
    t3=t1*t2
    print(f'-- {t3}',end='')
    t1=t2
    t2=t3
    c+=1
print('--FIM')
