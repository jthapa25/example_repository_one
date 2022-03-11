"""
What do client when they create an account?
they have client_id
account_id
first_name
last_name
account_number
"""


class Client:
    def __init__(self, client_id: int, account_id: int, first_name: str, last_name: str, account_number: int):
        self.client_id = client_id
        self.account_id = account_id
        self.first_name = first_name
        self.last_name = last_name
        self.account_number = account_number
