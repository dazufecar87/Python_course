#Lectura en documentacion de este curso

from setuptools import setup


setup(
  name='pv', #definimos como invocamos a nuestra linea de comandos, se llama pv
  version='0.1', # version 0.1
  py_modules=['pv'], #Se llama el modulo pv
  intall_requires=[
    'Click',
  ], # necesitamos como requisito modulo o libreria click
  entry_points='''
  [console_scripts]
  pv=pv:cli
  ''',  # punto de entrada de nuestra app metodo cli declarado en pv.py
)