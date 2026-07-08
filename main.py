import persistence
import utils


DATA_FILE = "dados/accounts.json"
accounts = persistence.load_json(DATA_FILE) or []


while True:
    print("\n=>> Sistema de Controle Bancário <<=")
    print("1 - Criar conta no banco")
    print("2 - Listar contas registradas no banco")
    print("3 - Buscar conta pelo nome do titular")
    print("4 - Alterar os dados da conta")
    print("5 - Depositar dinheiro")
    print("6 - Sacar dinheiro")
    print("7 - Transferir dinheiro")
    print("8 - Excluir conta do banco")
    print("9 - Mostrar extrato")
    print("0 - Salvar e sair")

    op = utils.read_int_val("Informe a opção desejada: ")

    match op:
        case 1:
            utils.create_account(accounts)
        case 2:
            utils.list_accounts(accounts)
        case 3:
            utils.search_account(accounts)
        case 4:
            utils.update_account(accounts)
        case 5:
            utils.deposit_value(accounts)
        case 6:
            utils.withdraw_value(accounts)
        case 7:
            utils.transfer_value(accounts)
        case 8:
            utils.remove_account(accounts)
        case 9:
            account_id = utils.read_int_val(
                "ID da conta para mostrar extrato: ",
                allow_zero=False,
            )
            account = utils.find_account_by_id(accounts, account_id)
            if account:
                utils.show_extract(account)
            else:
                print("Conta não encontrada.")
        case 0:
            persistence.save_json(accounts, DATA_FILE)
            print("Salvando as informações...\nEncerrando o sistema...")
            break
        case _:
            print("Opção informada é inválida. Verifique as opções disponíveis.")
