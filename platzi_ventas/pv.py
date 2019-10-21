import click

from clients import commands as clients_commands

CLIENTS_TABLE = '.clients.csv'
@click.group()
@click.pass_context #Nos da un Objeto contexto se inicializa como diccionario vacio
def cli(ctx):
  ctx.obj = {}
  ctx.obj['clients_table'] = CLIENTS_TABLE # el nombre del archivo o tabla


cli.add_command(clients_commands.all) # cli hace referencia a la funcion cli
# all viene de commands all=clients alias a funcion clients