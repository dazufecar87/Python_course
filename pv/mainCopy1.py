import sys


clients = [
  {
    'name': 'Daniel',
    'company': 'Google',
    'email': 'daniel@google.com',
    'position': 'Data Scientist',
  },
  {
    'name': 'Pablo',
    'company': 'Facebook',
    'email': 'pablo@facebook.com',
    'position': 'Data Engineer',
  }

]


def create_client(client):
  global clients   #Usar la variable clients global pues variables dentro de la funcion son locales

  if client not in clients:
    clients.append(client)
  else:
    print('Client is already in the client\'s list ')


def list_clients():
  for idx, client in enumerate(clients):
    #print('{}: {}: {}: {}: {}'.format(idx, client['name'], client['company'], client['email'], client['position']))
    print('{uid} | {name} | {company} | {email} | {position}'.format(
      uid=idx, 
      name=client['name'], 
      company=client['company'], 
      email=client['email'], 
      position=client['position']))


def update_client(client, field, updated_client_field):
  global clients
  c = 0
  found = 0
  for clientc in clients:
    if client in clientc['name']:
      found = 1
      clients[c][field] = updated_client_field

    c+=1

  if found == 0:
    print('Client is not in clients list')


def delete_client(client):
  global clients

  c = 0
  found = False

  for clientc in clients:  
    if client in clientc['name']:
      del clients[c]
      found = True
      print('You have deleted\n{idu} | {name} | {company} | {email} | {position}'.format(
        idu=c,
        name=clientc['name'], 
        company=clientc['company'], 
        email=clientc['email'], 
        position=clientc['position']))
    c+=1

  if found == False:
      print('Client is not in clients list')


def search_client(client):
  global clients
  c = 0
  found = False
  for clientc in clients:
    if client in clientc['name']:
      found = True
      print('{idu} | {name} | {company} | {email} | {position}'.format(
        idu=c,
        name=clientc['name'], 
        company=clientc['company'], 
        email=clientc['email'], 
        position=clientc['position']))
    
    c+=1

  if found == False:
      print('Client is not in clients list')

  return found


def _verify_field(field):
  field = field.upper()
  if field == 'N':
    field = 'name'
  elif field == 'C':
    field = 'company'
  elif field == 'E':
    field = 'email'
  elif field == 'P':
    field = 'position'
  else:
    field = 'W'

  return field


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


def _get_client_field(field_name):
  field = None

  while not field:
    field = input('What is the client {}?'.format(field_name))
  
  return field

def _get_field():
  field = input('What field are you willing to update?\n{}: {}: {}: {}'.format(
    '[N]ame', '[C]ompany', '[E]mail', '[P]osition'))
  
  return field


def _get_client_from_user():
  client = {
        'name': _get_client_field('name'),
        'company': _get_client_field('company'),
        'email': _get_client_field('email'),
        'position': _get_client_field('position'),
      }
  return client

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
      client = _get_client_from_user()
      create_client(client)
      list_clients()
    elif command == 'L':
      list_clients()
    elif command == 'D':
      client = _get_client_field('name')
      found = search_client(client)
      if found == True:
        delete_client(client)
        print('The client\'s list has been updated')
        list_clients()
    elif command == 'U':
      list_clients()
      client = _get_client_field('name')
      found = search_client(client)
      if found == True:
        verified_field = 'W'
        while verified_field == 'W':
          field = _get_field()
          verified_field = _verify_field(field)
        updated_client_field = input('What is the updated client {}'.format(verified_field))
        update_client(client, verified_field, updated_client_field)
        list_clients()
    elif command == 'S':
      client = _get_client_field('name')
      found = search_client(client)

      if found:
        print('The client is in the client\'s list')
      else:
        print('The client: {} is not in our client\'s list'.format(client))
    
    elif command == 'E':
      bye = 0
      list_clients()
      print('Thank you for using PV')
      
    else:
      print('Invalid input')

