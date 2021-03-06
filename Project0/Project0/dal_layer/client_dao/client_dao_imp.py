from custom_exceptions.id_not_found import IdNotFound
from dal_layer.client_dao.client_dao_interface import ClientDAOInterface
from entities.client_class_information import Client


class ClientDAOImp(ClientDAOInterface):
    client_List = [Client(1, 1, "Jenny", "Thapa", 12345678)]
    id_generator = 2

    # Create
    def create_client(self, client: Client) -> Client:
        client.client_id = self.id_generator
        self.id_generator += 2
        self.client_List.append(client)
        return client

    # Read
    def get_client_by_id(self, client_id: int) -> Client:
        for client in self.client_List:
            if client.client_id == client_id:
                return client
        raise IdNotFound("No client matches the id given: please try again!")

    # Update
    def update_client_by_id(self, client: Client):
        for old_client in self.client_List:
            if old_client.client_id == client.client_id:
                old_client = client
                return old_client
        raise IdNotFound("No client matches id given: please try again!")

    # Delete
    def delete_client_by_id(self, client_id: int) -> bool:
        for client in self.client_List:
            if client.client_id == client_id:
                self.client_List.remove(client)
                return True
        raise IdNotFound("No client matches the id given: please try again!")
