import csv
import os

from clients.models import ClientModel


class ClientService:
  def __init__(self, table_name):
    self.table_name = table_name


  def create_client(self, client):
    with open(self.table_name, mode='a') as f: # open file in mode append
      writer = csv.DictWriter(f, fieldnames = ClientModel.schema()) # por lo que ClientModel, schema es un static method, entonces no se necesita inicializar ClientModel
      writer.writerow(client.to_dict())


  def list_clients(self):
    with open(self.table_name, mode='r') as f:
      reader = csv.DictReader(f, fieldnames=ClientModel.schema())

      return list(reader)


  def delete_client(self, deleted_client):
    clients = self.list_clients()

    for client in clients:
      if client['uid'] == deleted_client[0]['uid']:
        clients.remove(deleted_client[0])

    self._save_to_disk(clients)


  def update_client(self, updated_client):
    clients = self.list_clients()

    updated_clients = []
    print(updated_client)
    for client in clients:
      if client['uid'] == updated_client.uid:
        updated_clients.append(updated_client.to_dict())
      else:
        updated_clients.append(client)

    self._save_to_disk(updated_clients)


  def _save_to_disk(self, clients):
    tmp_table_name = self.table_name + '.tmp'
    with open(tmp_table_name, mode='w') as f:
      writer = csv.DictWriter(f, fieldnames=ClientModel.schema())
      writer.writerows(clients)

    os.remove(self.table_name)
    os.rename(tmp_table_name, self.table_name)
