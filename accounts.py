import datetime
from datetime import datetime


class Account(object):
    name = ""
    password = ""
    permissions = 1


def create_account(name, password, permissions):
    account = Account()
    account.name = name
    account.password = password
    account.permissions = permissions
    account.creation_date = datetime.now().date()
    return account

