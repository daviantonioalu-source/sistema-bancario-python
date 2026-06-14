import os

from datetime import datetime


def find_account_by_id(accounts, account_id):      #função
    for account in accounts:
        if account['id'] == account_id:
            return account
    return None

def next_id(accounts):
    if not accounts:
        return 1
    return max(account['id'] for account in accounts) + 1

def create_account(accounts):
    account_id = next_id(accounts)
    number_account = read_int_val(("Informe qual será o número da conta: "))
    agency = read_int_val(("inforne o código da Agência: "))
    name = input("Nome do responsável pela conta: ")
    password = read_int_val(("Senha da Conta: ")) 
    # value = 0
    new_account = {
        'id' : account_id,
        'number_account' : number_account,
        'number_agency' : agency,
        'name' : name,    
        'password' : password,
        # 'value_account' : value,x'
        'date' : datetime.now().strftime ("%Y-%m-%d") 
        }
    accounts.append(new_account)
    print(f"Conta {number_account} pertencente ao responsável {name} foi registrada com sucesso !")

def list_accounts(accounts):
    if not accounts:
        print("Nenhuma Conta Registrada !")
        return
    print (" ID | Número da Conta | Agência | Nome do Responsável | Senha ")
    print(" ------------------------------------------------------------ ")
    for account in accounts:
        print(f"{account['id']} | {account['number_account']} | {account['number_agency']} | {account['name']} | {account['password']}")

def read_int_val (prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Digite apenas números inteiros válidos! ")

def read_float_val(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Digite apenas números decimais válidos! ")

# def deposit_account(accounts):
    

