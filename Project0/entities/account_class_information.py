"""

"""


class Account:
    def __init__(self, account_id: int, account_balance: float, client_id: int):
        self.account_id = account_id
        self.account_balance = account_balance
        self.client_id = client_id


    def convert_to_dictionary(self):
     return {
        "accountId": self.account_id,
        "accountBalance": self.account_balance,
        "clientId": self.client_id

    }
