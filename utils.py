from datetime import datetime


def find_account_by_id(accounts, account_id):
    for account in accounts:
        if account["id"] == account_id:
            return account
    return None


def find_account_by_number_and_agency(accounts, number_account, number_agency):
    for account in accounts:
        if (
            account["number_account"] == number_account
            and account["number_agency"] == number_agency
        ):
            return account
    return None


def next_id(accounts):
    if not accounts:
        return 1
    return max(account["id"] for account in accounts) + 1


def format_currency(value):
    return f"R$ {value:.2f}".replace(".", ",")


def register_transaction(account, transaction_type, value, description=""):
    account.setdefault("extract", []).append(
        {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "type": transaction_type,
            "value": value,
            "description": description,
        }
    )


def read_text_val(prompt, required=True):
    while True:
        value = input(prompt).strip()
        if required and not value:
            print("Este campo é obrigatório.")
            continue
        return value


def read_int_val(prompt, allow_zero=True):
    while True:
        try:
            value = int(input(prompt))
            if value < 0 or (value == 0 and not allow_zero):
                print("Digite um número maior que zero.")
                continue
            return value
        except ValueError:
            print("Digite apenas números inteiros válidos.")


def read_float_val(prompt, allow_zero=True):
    while True:
        try:
            value = float(input(prompt).replace(",", "."))
            if value < 0 or (value == 0 and not allow_zero):
                print("Digite um valor maior que zero.")
                continue
            return value
        except ValueError:
            print("Digite apenas números decimais válidos.")


def read_password(prompt):
    while True:
        password = read_int_val(prompt, allow_zero=False)
        if len(str(password)) < 4:
            print("A senha deve ter pelo menos 4 dígitos.")
            continue
        return password


def create_account(accounts):
    account_id = next_id(accounts)

    while True:
        number_account = read_int_val("Informe o número da conta: ", allow_zero=False)
        agency = read_int_val("Informe o código da agência: ", allow_zero=False)
        if find_account_by_number_and_agency(accounts, number_account, agency):
            print("Já existe uma conta com esse número e agência.")
            continue
        break

    name = read_text_val("Nome do titular da conta: ")
    password = read_password("Senha da conta: ")
    balance = read_float_val("Saldo inicial da conta: ")

    new_account = {
        "id": account_id,
        "number_account": number_account,
        "number_agency": agency,
        "name": name,
        "password": password,
        "balance_account": balance,
        "extract": [],
        "date": datetime.now().strftime("%Y-%m-%d"),
    }

    if balance > 0:
        register_transaction(new_account, "Depósito inicial", balance)

    accounts.append(new_account)
    print(
        f"Conta {number_account} pertencente ao titular {name} "
        "foi registrada com sucesso!"
    )


def list_accounts(accounts):
    if not accounts:
        print("Nenhuma conta registrada.")
        return

    print("ID | Número da Conta | Agência | Nome do Titular | Saldo")
    print("-" * 62)
    for account in accounts:
        print(
            f"{account['id']} | {account['number_account']} | "
            f"{account['number_agency']} | {account['name']} | "
            f"{format_currency(account['balance_account'])}"
        )


def search_account(accounts):
    search_term = read_text_val(
        "Informe o nome do titular da conta que você deseja buscar: "
    ).lower()
    found_accounts = [
        account for account in accounts if search_term in account["name"].lower()
    ]

    if not found_accounts:
        print("Nenhuma conta encontrada com este nome.")
        return

    for account in found_accounts:
        print_account(account)
        print("-" * 30)


def update_account(accounts):
    account_id = read_int_val("ID da conta para alteração: ", allow_zero=False)
    account = find_account_by_id(accounts, account_id)
    if not account:
        print("Conta não encontrada.")
        return

    print_account(account)
    new_name = read_text_val(
        "Informe o novo nome do titular da conta (Enter para manter): ",
        required=False,
    )
    if new_name:
        account["name"] = new_name

    change_password = read_text_val(
        "Deseja alterar a senha? (s/n): ",
        required=False,
    ).lower()
    if change_password == "s":
        account["password"] = read_password("Informe a nova senha da conta: ")

    print("Dados atualizados com sucesso!")


def deposit_value(accounts):
    account_id = read_int_val(
        "ID da conta em que será realizado o depósito: ",
        allow_zero=False,
    )
    account = find_account_by_id(accounts, account_id)

    if not account:
        print("Nenhuma conta encontrada com este ID.")
        return

    print_account(account)
    deposit_amount = read_float_val(
        "Informe o valor que será depositado: ",
        allow_zero=False,
    )

    account["balance_account"] += deposit_amount
    register_transaction(account, "Depósito", deposit_amount)
    print(
        f"Depósito de {format_currency(deposit_amount)} realizado com sucesso "
        f"para a conta de ID {account['id']}."
    )


def withdraw_value(accounts):
    account_id = read_int_val(
        "ID da conta em que será realizado o saque: ",
        allow_zero=False,
    )
    account = find_account_by_id(accounts, account_id)

    if not account:
        print("Nenhuma conta encontrada com este ID.")
        return

    print_account(account)
    withdraw_amount = read_float_val(
        "Informe o valor que será sacado: ",
        allow_zero=False,
    )

    if withdraw_amount > account["balance_account"]:
        print("Saldo insuficiente.")
        return

    account["balance_account"] -= withdraw_amount
    register_transaction(account, "Saque", withdraw_amount)
    print(
        f"Saque de {format_currency(withdraw_amount)} realizado com sucesso "
        f"para a conta de ID {account['id']}."
    )


def transfer_value(accounts):
    origin_id = read_int_val("ID da conta de origem: ", allow_zero=False)
    origin_account = find_account_by_id(accounts, origin_id)
    if not origin_account:
        print("Conta de origem não encontrada.")
        return

    destination_id = read_int_val("ID da conta de destino: ", allow_zero=False)
    destination_account = find_account_by_id(accounts, destination_id)
    if not destination_account:
        print("Conta de destino não encontrada.")
        return

    if origin_id == destination_id:
        print("A conta de origem e destino não podem ser a mesma.")
        return

    transfer_amount = read_float_val(
        "Informe o valor que será transferido: ",
        allow_zero=False,
    )

    if transfer_amount > origin_account["balance_account"]:
        print("Saldo insuficiente para realizar a transferência.")
        return

    origin_account["balance_account"] -= transfer_amount
    destination_account["balance_account"] += transfer_amount

    register_transaction(
        origin_account,
        "Transferência enviada",
        transfer_amount,
        f"Para conta ID {destination_account['id']}",
    )
    register_transaction(
        destination_account,
        "Transferência recebida",
        transfer_amount,
        f"Da conta ID {origin_account['id']}",
    )

    print(
        f"Transferência de {format_currency(transfer_amount)} realizada com sucesso."
    )


def remove_account(accounts):
    account_id = read_int_val("ID da conta que será removida: ", allow_zero=False)
    account = find_account_by_id(accounts, account_id)

    if not account:
        print("Nenhuma conta encontrada com este ID.")
        return

    accounts.remove(account)
    print(f"Conta de ID {account['id']} removida com sucesso!")


def print_account(account):
    print(f"ID: {account['id']}")
    print(f"Número da Conta: {account['number_account']}")
    print(f"Agência: {account['number_agency']}")
    print(f"Nome do Titular: {account['name']}")
    print(f"Saldo: {format_currency(account['balance_account'])}")
    print(f"Data de Criação: {account['date']}")


def show_extract(account):
    if not account.get("extract"):
        print("Nenhuma transação registrada no extrato.")
        return

    print("Extrato da Conta:")
    for transaction in account["extract"]:
        description = transaction.get("description", "")
        if description:
            description = f", Descrição: {description}"
        print(
            f"Data: {transaction['date']}, Tipo: {transaction['type']}, "
            f"Valor: {format_currency(transaction['value'])}{description}"
            f"\nSaldo atual: {format_currency(account['balance_account'])}"
        )
