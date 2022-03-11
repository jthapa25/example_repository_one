from abc import ABC, abstractmethod

from entities.account_class_information import Account

"""
This is the interface for the account data access object. Inside the account I will define the different CRUD operations
that we will need to interact with all account data inside of the database. These methods will be used by the service
layer to make the necessary changes to the database. Note that these methods don't have to fulfill any user stories:
they are a tool used by service layer to be able to fulfill the requirements of the user stories. 

"""


class AccountDAOInterface(ABC):
    # create
    @abstractmethod
    def create_account(self, account: Account):
        pass

    """ this method will be used to handle adding new account data into my database"""

    @abstractmethod
    def get_all_accounts_information(self):
        """ will be used to perform data validation"""
        pass

    # read
    @abstractmethod
    def get_account_by_id(self, account_id: int):
        pass

    """ this method will be used to handle retrieving new account data into my database"""

    # update
    @abstractmethod
    def update_account_by_id(self, account: Account):
        pass

    """ this method will be used to handle updating account data into my database"""

    # delete
    @abstractmethod
    def delete_account_by_id(self, account_id: int) -> bool:
        pass

    """ this method will be used to handle remove account data into my database"""

    # deposit
    @abstractmethod
    def deposit_amount_by_id(self, value: float, account_id: int):
        pass

    """ this method will be used to deposit amount into my database"""

    # withdraw
    @abstractmethod
    def withdraw_amount_by_id(self, value: float, account_id: int):
        pass

    """ this method will be used to withdraw amount into my database"""

    # transfer
    @abstractmethod
    def transfer_amount_by_id(self, value: float, account_id: int):
        pass

    """ this method will be used to transfer amount into my database"""
