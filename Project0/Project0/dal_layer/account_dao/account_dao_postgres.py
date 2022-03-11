from custom_exceptions.bad_account_info import BadAccountInfo
from custom_exceptions.id_not_found import IdNotFound
from dal_layer.account_dao.account_dao_interface import AccountDAOInterface
from entities.account_class_information import Account
from util.postgress_connection import connection


class AccountDAOImpPostgres(AccountDAOInterface):

    def get_all_accounts_information(self):
        sql = "select * from accounts"
        cursor = connection.cursor()
        cursor.execute(sql)
        account_records = cursor.fetchall()
        account_list = []
        if len(account_records) == 0:
            return account_list
        else:
            for account in account_records:
                account_list.append(Account(*account))
            return account_list

    def create_account(self, account: Account) -> Account:
        sql = "insert into accounts values(default, %s, %s) returning account_id"
        cursor = connection.cursor()
        cursor.execute(sql, (account.account_type, account.balance))
        connection.commit()
        generated_id = cursor.fetchone()[0]
        account.account_id = generated_id
        return account

    def get_account_by_id(self, account_id: int) -> Account:
        sql = "select * from accounts where account_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [account_id])
        account_record = cursor.fetchone()
        if account_record is None:
            raise IdNotFound("No account matches the id given: please try again!")
        account = Account(*account_record)
        return account

    def update_account_by_id(self, account: Account) -> Account:
        sql = "update accounts set account_type = %s, balance = %s where account_id = %s returning *"
        cursor = connection.cursor()
        cursor.execute(sql, (account.account_type, account.balance, account.account_id))
        connection.commit()
        if cursor.rowcount != 0:
            return account
        else:
            raise IdNotFound("No account matches the id given: please try again!")

    def delete_account_by_id(self, account_id: int) -> bool:
        sql = "delete from accounts where account_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [account_id])
        connection.commit()
        if cursor.rowcount != 0:
            return True
        else:
            raise IdNotFound("No account matches the id given: please try again!")

    def deposit_amount_by_id(self, value, account_id: int) -> bool:
        sql = "select balance from accounts where account_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [account_id])
        account_balance = cursor.fetchone()
        old_balance = account_balance['balance']
        new_balance = old_balance + value
        sql = "update into accounts set balance = %s where account_id = %s"
        cursor.execute(sql, (new_balance, account_id))
        connection.commit()

        if cursor.rowcount != 0:
            return True
        else:
            raise IdNotFound("No account matches the id given: please try again!")

    def withdraw_amount_by_id(self, value, account_id: int) -> bool:
        sql = "select balance from accounts where account_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [account_id])
        account_balance = cursor.fetchone()
        old_balance = account_balance['balance']
        new_balance = old_balance - value
        sql = "update into accounts set balance = %s where account_id = %s"
        cursor.execute(sql, (new_balance, account_id))
        connection.commit()

        if cursor.rowcount != 0:
            return True
        else:
            raise IdNotFound("No account matches the id given: please try again!")

    def transfer_amount_by_id(self, value, transfer_account_id, account_id: int) -> bool:
        sql = "select balance from accounts where account_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [account_id])
        account_balance = cursor.fetchone()
        old_balance = account_balance['balance']
        transfer_balance = old_balance - value
        sql = "update into accounts set balance = %s where account_id = %s"
        cursor.execute(sql, (transfer_balance, account_id))
        connection.commit()
        sql = "select balance from accounts where account_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [transfer_account_id])
        account_balance = cursor.fetchone()
        old_balance = account_balance['balance']
        new_balance = old_balance + value
        sql = "update into accounts set balance = %s where account_id = %s"
        cursor.execute(sql, (new_balance, transfer_account_id))
        connection.commit()


        if cursor.rowcount != 0:
            return True
        else:
            raise IdNotFound("No account matches the id given: please try again!")
