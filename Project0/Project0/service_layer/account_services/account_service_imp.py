from custom_exceptions.bad_account_info import BadAccountInfo
from dal_layer.account_dao.account_doa_imp import AccountDAOImp
from entities.account_class_information import Account
from service_layer.account_services.account_service_interface import AccountServiceInterface

"""
This module implement the account service interface. Here is where we define how the data being worked with is validated,
and we define what needs to happen if the data is not validated. This could be because the data type provided is wrong,
Business Rules are not being adhered to, or any other reason why the data should not be passed into the data access
layer.

Another thing to note is that it is ok if there is overlap in the names of the different methods between the service
layer and the data access layer, but the ideal is that your method names in your service layer should reflect the
particular user story that they are meant to implement. 
"""


class AccountServiceImp(AccountServiceInterface):

    def __init__(self, account_dao: AccountDAOImp):
        self.account_dao = account_dao

    def service_create_account(self, account: Account) -> Account:
        if type(account.account_type) != str:  # this is checking that the account type is string
            raise BadAccountInfo("Please pass a valid account type") # raise exception if we are not working with a string
        for existing_account in self.account_dao.account_List: # here we need to loop through existing teams to validate business rules
            if existing_account.account_id == account.account_type: # here we are checking for duplicate account type
                raise BadAccountInfo("This account type is already exists in the database") # raise exception if their are duplicates
        return self.account_dao.create_account(account) # assuming all validation checked out, we pass sata into DAL

    def service_get_account_by_id(self, account_id: int) -> Account:
        try:
            return self.account_dao.get_account_by_id(int(account_id))
        except ValueError:
            raise BadAccountInfo("please pass a valid account id")

    def service_update_account_by_id(self, account: Account) -> Account:
        if type(account.account_type) != str:  # this is checking that the account type is string
            raise BadAccountInfo("Please pass a valid account type")
        for existing_account in self.account_dao.account_List:
            if existing_account.account_id == account.account_type:
                raise BadAccountInfo("This account type is already exists in the database")
        return self.account_dao.update_account_by_id(account)

    def service_delete_account_by_id(self, account_id: int) -> bool:
        if type(account_id) == int:
            return self.account_dao.delete_account_by_id(account_id)
        else:
            raise BadAccountInfo("Please provide a valid account Id")

    def service_deposit_amount_by_id(self, transaction_type: str, value, account_id: int):
        if transaction_type == "deposit":
            return self.account_dao.deposit_amount_by_id(value, account_id)

    def service_withdraw_amount_by_id(self, transaction_type: str, value, account_id: int):
        if transaction_type == "withdraw":
            return self.account_dao.withdraw_amount_by_id(value, account_id)

    def service_transfer_amount_by_id(self, transaction_type: str, value, account_id: int):
        if transaction_type == "transfer":
            return self.account_dao.transfer_amount_by_id(value, account_id)
