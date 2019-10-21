import click

from clients.services import ClientService
from clients.models import ClientModel

@click.group() # Este decorador convierte a clients en otro decorador
def clients():
  """Manages the clients lifecycle"""
  pass


@clients.command() # este es un comando
@click.option('-n', '--name',
              type=str,
              prompt=True,
              help='The clients name')
@click.option('-c', '--company',
              type=str,
              prompt=True,
              help='The clients company')
@click.option('-e', '--email',
              type=str,
              prompt=True,
              help='The clients email')
@click.option('-p', '--position',
              type=str,
              prompt=True,
              help='The clients position')
@click.pass_context # necesitamos el contexto
def create(ctx, name, company, email, position):
  """Creates a new client"""
  client = ClientModel(name, company, email, position)
  client_service = ClientService(ctx.obj['clients_table'])

  client_service.create_client(client)


@clients.command()
@click.pass_context
def list(ctx):
  """List all clients"""
  client_service = ClientService(ctx.obj['clients_table'])

  clients_list = client_service.list_clients()

  click.echo(' ID  |  NAME  |  COMPANY  |  EMAIL  |  POSITION')
  click.echo('*' * 100)

  for client in clients_list:
    print ('{uid}  |  {name}  |  {company}  |  {email}  |  {position}'.format(
      uid=client['uid'],
      name=client['name'],
      company=client['company'],
      email=client['email'],
      position=client['position']
    ))


@clients.command()
@click.argument('client_uid', type=str)
@click.pass_context
def update(ctx, client_uid):
  """Updates a client"""
  client_service = ClientService(ctx.obj['clients_table'])

  client_list = client_service.list_clients()

  client = [client for client in client_list if client['uid'] == client_uid]

  if client:
    client = _update_client_flow(ClientModel(**client[0]))
    client_service.update_client(client)

    click.echo('Client updated')
  else:
    click.echo('Client not found')


def _update_client_flow(client):
  click.echo('Leave it empty if you do not want to modify the value')

  client.name = click.prompt('New name', type=str, default=client.name)
  client.company = click.prompt('New company', type=str, default=client.company)
  client.email = click.prompt('New email', type=str, default=client.email)
  client.position = click.prompt('New position', type=str, default=client.position)

  return client


@clients.command()
@click.argument('client_uid', type=str)
@click.pass_context
def delete(ctx, client_uid):
  """Deletes a client"""
  client_service = ClientService(ctx.obj['clients_table'])

  client_list = client_service.list_clients()

  client = [client for client in client_list if client['uid'] == client_uid]

  if client:
    click.echo(client)
    if click.confirm('Are you sure you want to delete the client with uid: {}'.format(client_uid)):
        client_service.delete_client(client)
    #client_service.delete_client(client)

    click.echo('Client deleted')
  else:
    click.echo('Client not found')

# alias de clients, all apunta a funcion clients
all = clients

