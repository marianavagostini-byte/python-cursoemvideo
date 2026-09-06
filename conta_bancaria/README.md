# Sistema de Conta Bancária

Aplicação de terminal para praticar classes, validação e operações com valores monetários em Python.

## Funcionalidades

- Criar contas bancárias
- Depositar e sacar valores
- Impedir saques acima do saldo
- Consultar extrato com data e hora
- Listar contas e saldos

## Como executar

Na raiz do repositório:

```bash
python conta_bancaria/main.py
```

O saldo usa `Decimal`, evitando os arredondamentos inesperados comuns em cálculos com `float`.
