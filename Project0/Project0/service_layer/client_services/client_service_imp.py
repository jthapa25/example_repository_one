from custom_exceptions.bad_client_info import BadClientInfo
from entities.client_class_information import Client
from service_layer.client_services.client_service_interface import ClientServiceInterface


class ClientServiceImp(ClientServiceInterface):

    def service_create_client(self, client: Client) -> Client:
        if len(client.first_name) > 20:
            raise BadClientInfo("First name is too long")
        elif len(client.last_name) > 20:
            raise BadClientInfo("Last name is too long")
        for c in self.client_dao.client_List:
            if c.account_id == client.account_id and c.account_number == client.account_number:
                raise BadClientInfo("account number already exist")
        return self.client_dao.create_client(client)

    def service_get_client_by_id(self, client_id: int) -> Client:
        if type(client_id) == int:
            return self.client_dao.get_client_by_id(client_id)
        else:
            raise BadClientInfo("Please provide a valid Id")

    def service_update_client_information(self, client: Client) -> Client:
        if len(client.first_name) > 20:
            raise BadClientInfo("First name is too long")
        elif len(client.last_name) > 20:
            raise BadClientInfo("Last name is too long")
        for c in self.client_dao.client_List:
            if c.account_id == client.account_id and c.account_number == client.account_number:
                raise BadClientInfo("account number already exist")
        return self.client_dao.update_client_by_id(client)

    def service_delete_client_by_id(self, client_id: int) -> bool:
        if type(client_id) == int:
            return self.client_dao.delete_client_by_id(client_id)
        else:
            raise BadClientInfo("Please provide a valid Id")
