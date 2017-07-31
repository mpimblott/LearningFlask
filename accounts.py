import datetime
from datetime import datetime


class Account(object):
    name = ""
    password = ""
    is_admin = False

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


def create_account(name, password, is_admin):
    account = Account()
    account.name = name
    account.password = password
    account.is_admin = is_admin
    account.creation_date = datetime.now().date()
    return account

