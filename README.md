# SCB - Sistema de Controle Bancário

Projeto em Python para simular um sistema simples de controle bancário pelo terminal. O sistema permite criar contas, listar registros, buscar titulares, alterar dados, realizar depósitos, saques, transferências e consultar o extrato das movimentações.

## Funcionalidades

- Criar conta bancária com número, agência, titular, senha e saldo inicial.
- Listar todas as contas cadastradas.
- Buscar contas pelo nome do titular.
- Alterar nome do titular e senha da conta.
- Depositar valores em uma conta.
- Sacar valores com validação de saldo disponível.
- Transferir valores entre contas.
- Remover contas cadastradas.
- Consultar extrato de transações.
- Salvar e carregar os dados em arquivo JSON.

## Estrutura do projeto

```text
SCB/
+-- dados/
|   +-- accounts.json
+-- main.py
+-- persistence.py
+-- utils.py
+-- README.md
```

## Arquivos principais

| Arquivo | Responsabilidade |
| --- | --- |
| `main.py` | Exibe o menu principal e chama as funções do sistema. |
| `utils.py` | Contém as regras de negócio, validações e operações bancárias. |
| `persistence.py` | Faz a leitura e gravação dos dados em JSON. |
| `dados/accounts.json` | Armazena as contas cadastradas e seus extratos. |

## Requisitos

- Python 3.10 ou superior.

O projeto usa apenas bibliotecas padrão do Python, então não é necessário instalar dependências externas.

## Como executar

No terminal, dentro da pasta do projeto, execute:

```bash
python main.py
```

## Menu do sistema

Ao iniciar o programa, o sistema exibe as opções:

```text
1 - Criar conta no banco
2 - Listar contas registradas no banco
3 - Buscar conta pelo nome do titular
4 - Alterar os dados da conta
5 - Depositar dinheiro
6 - Sacar dinheiro
7 - Transferir dinheiro
8 - Excluir conta do banco
9 - Mostrar extrato
0 - Salvar e sair
```

Para manter os dados atualizados no arquivo `dados/accounts.json`, use a opção `0 - Salvar e sair` antes de encerrar o sistema.

## Validações implementadas

- IDs, números de conta e agência não podem ser negativos.
- Operações como depósito, saque e transferência exigem valores maiores que zero.
- O titular da conta não pode ficar vazio na criação.
- A senha precisa ter pelo menos 4 dígitos.
- O sistema não permite criar duas contas com o mesmo número e agência.
- Saques e transferências só são realizados quando há saldo suficiente.
- Transferências não podem ser feitas para a mesma conta de origem.
- O sistema valida se a conta existe antes de alterar, remover ou movimentar valores.

## Persistência dos dados

As informações são armazenadas no arquivo:

```text
dados/accounts.json
```

Cada conta possui dados básicos e uma lista de transações no extrato. Exemplo simplificado:

```json
{
  "id": 1,
  "number_account": 251,
  "number_agency": 361,
  "name": "Maria",
  "password": 1234,
  "balance_account": 120.0,
  "extract": [],
  "date": "2026-07-07"
}
```

## Observações

Este projeto tem fins de estudo e prática com Python, entrada de dados pelo terminal, funções, listas, dicionários, validações e persistência com JSON.
