from custom_exceptions.id_not_found import IdNotFound
from dal_layer.account_dao.account_dao_interface import AccountDAOInterface
from entities.account_class_information import Account

"""
This module implement the account data access object interface. These methods only interact with the database, 
they do not validate the information being passed into them, since that is handled by the service layer. The only checks
these methods make are on data inside (or not inside) the database

"""


class AccountDAOImp(AccountDAOInterface):

    def __init__(self):
        account_needed_for_id_catch = Account(1, "Saving", 2)
        self.account_List = []
        self.id_generator = 2

        self.account_List.append(account_needed_for_id_catch)

    def create_account(self, account: Account) -> Account:
        # account needs to be given an Id, and it needs to be added to the list
        account.account_id = self.id_generator  # thus changes the account's Id to whatever the id generator is set to
        self.id_generator += 1  # this ensures that the next account will have a newly generated Id
        self.account_List.append(account)  # this adds the new account to my account database
        return account  # this returns the account object with its newly generated Id

    def get_account_by_id(self, account_id: int) -> Account:
        for account in self.account_List:
            if account.account_id == account_id:
                return account
        raise IdNotFound("No bank matches the id given: please try again!")

    def update_account_by_id(self, account: Account):
        for old_account in self.account_List:
            if account.account_id == old_account.account_id:
                old_account = account
                return old_account
        raise IdNotFound("No bank matches the id given: please try again!")

    def delete_account_by_id(self, account_id: int) -> bool:
        for account in self.account_List:
            if account.account_id == account_id:
                self.account_List.remove(account)
                return True
        raise IdNotFound("No bank matches the id given: please try again!")

    def deposit_amount_by_id(self, value: float, account_id: int):
        for account in self.account_List:
            if account.account_id == account_id:
                return True
            raise IdNotFound("No bank matches the id given: please try again!")

    def withdraw_amount_by_id(self, value: float, account_id: int):
        for account in self.account_List:
            if account.account_id == account_id:
                return True
            raise IdNotFound("No bank matches the id given: please try again!")

    def transfer_amount_by_id(self, value: float, transfer_account_id: int, account_id: int):
        for account in self.account_List:
            if account.account_id == account_id:
                return True
            raise IdNotFound("No bank matches the id given: please try again!")

    def get_all_accounts_information(self):
        pass
