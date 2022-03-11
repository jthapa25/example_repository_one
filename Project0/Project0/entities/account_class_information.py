"""
account have account_id
account_balance
client_id

accounts are going to be their own entities, So I don't need to put their information inside of the account class

"""


class Account:
    def __init__(self, account_id: int, account_type: str, balance: float):
        self.account_id = account_id
        self.account_type = account_type
        self.balance = balance

    def convert_to_dictionary(self):
        return {
            "accountId": self.account_id,
            "accountType": self.account_type,
            "Balance": self.balance

        }
