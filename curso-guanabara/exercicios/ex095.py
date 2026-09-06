# ex095
# Fonte: Extra - fora do curso (seu código / variação)

usuario = ('Mari', 'jv', 'barbs')
senha = ('0502', '0000', '1234')
while True:
    login = input('Digite seu usuario: ')
    password = input('Digite sua senha: ')
    if login in usuario:
        pos = usuario.index(login)
        if password == senha[pos]:
            print(f'Acesso liberado! Bem-vindo(a), {login}!')
            break
        else:
            print('Senha incorreta! Tente novamente.')
    else:
        print('Usuário não encontrado! Tente novamente.')