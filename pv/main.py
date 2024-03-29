import sys


clients = 'pablo,ricardo,'


def create_client(client_name):
  global clients   #Usar la variable clients global pues variables dentro de la funcion son locales

  if client_name not in clients:
    clients += client_name
    _add_comma()
  else:
    print('Client is already in the client\'s list ')


def list_clients():
  global clients

  print(clients)


def update_client(client_name, updated_client_name):
  global clients

  if client_name in clients:
    clients = clients.replace(client_name + ',', updated_client_name + ',')

  else:
    print('Client is not in clients list')


def delete_client(client_name):
  global clients

  if client_name in clients:
    clients = clients.replace(client_name + ',','')
  else:
    print('client is not in clients list')


def search_client(client_name):
  global clients

  clients_list = clients.split(',') # Dividir string por las comas

  for client in clients_list:
    if client != client_name:
      continue
    else:
      return True


def _add_comma():
  global clients

  clients += ','


def _print_welcome():
  print('WELCOME TO PLATZI VENTAS')
  print('*'*50)
  print('What would you like to do today')
  print('[C]reate client')
  print('[L]ist client')
  print('[U]pdate client')
  print('[D]elete client')
  print('[S]earch client')
  print('[E]xit')


def _get_client_name():
  client_name = None

  while not client_name:
    client_name = input('What is the client name?')
  
    if client_name == 'exit':
      client_name = None
      break

  if not client_name:
    sys.exit()

  return client_name


if __name__ == '__main__':

  bye = 1

  _print_welcome()

  while bye:

    command = input()
    command = command.upper()

    if command == 'C':
      client_name = _get_client_name()
      create_client(client_name)
      list_clients()
    elif command == 'L':
      list_clients()
    elif command == 'D':
      client_name = _get_client_name()
      delete_client(client_name)
      list_clients()
    elif command == 'U':
      client_name = _get_client_name()
      updated_client_name = input('What is the updated client name')
      update_client(client_name, updated_client_name)
      list_clients()
    elif command == 'S':
      client_name = _get_client_name()
      found = search_client(client_name)

      if found:
        print('The client is in the client\'s list')
      else:
        print('The client: {} is not in our client\'s list'.format(client_name))
    
    elif command == 'E':
      bye = 0
      list_clients()
      print('Thank you for using PV')
      
    else:
      print('Invalid input')

