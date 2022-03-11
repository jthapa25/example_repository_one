from abc import ABC, abstractmethod

from dal_layer.account_dao.account_dao_interface import AccountDAOInterface
from entities.account_class_information import Account

"""
This is interface for the account service object. Inside the class I will define the different User story operation
that we will need to implement. These methods will need to check and validate the data that is being passed into them
to ensure that all business rules and programming logic is being followed. If any business rules or programming logic
are not validated, the data must not be passed into the data access layer, and instead some of error message must be 
returned
"""


class AccountServiceInterface(ABC):

    # create
    @abstractmethod
    def service_create_account(self, account: Account) -> Account:
        """ This method will validate the account information is correct before passing it to the DAL"""
        pass

    # read
    @abstractmethod
    def service_get_account_by_id(self, account_id: int) -> Account:
        """ This method will validate a correct identifier is being used before passing it to the DAL"""
        pass

    # update
    @abstractmethod
    def service_update_account_by_id(self, account: Account) -> Account:
        """ This method will validate the account information is correct before passing it to the DAL"""
        pass

    # delete
    @abstractmethod
    def service_delete_account_by_id(self, account_id: int) -> bool:
        """ This method will validate the account information is correct before passing it to the DAL"""
        pass

    # deposit
    @abstractmethod
    def service_deposit_amount_by_id(self, transaction_type: str, value, account_id: int):
        pass

    """ This method will validate the deposit amount """

    @abstractmethod
    def service_withdraw_amount_by_id(self, transaction_type: str, value, account_id: int):
        pass

    """ This method will validate the withdraw amount """

    @abstractmethod
    def service_transfer_amount_by_id(self, transaction_type: str, transfer_account_id: int, value, account_id: int):
        pass

    """ This method will validate the transfer amount """
