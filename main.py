import utils
import persistence
accounts = persistence.load_json('dados/accounts.json') or []




while True:
    print("=>> Sistema de Controle Bancário <<=")
    print("1 - Criar Conta No Banco")
    print("2 - Listas Contas Registradas no Banco")
    print("3 - Salvar e Sair ")
    print("4 - ")
    print("5 - ")
    print("6 - ")
    print("7 - ")


    op = utils.read_int_val(("Informe a Opção desejada: "))

    match(op):
        case 1:
            utils.create_account(accounts)
        case 2:
            utils.list_accounts(accounts)
        case 3:
            persistence.save_json(accounts, 'dados/accounts.json')
            print("Salvando as informações... \n Encerrando o Sistema...")
            break
        
        case _:
            print("Opção informada é inválida, verifique as opções disponivéis !")
        
