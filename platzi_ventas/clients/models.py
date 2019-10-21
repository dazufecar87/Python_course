import uuid # nos permite crear uids unicas

class ClientModel:

  def __init__(self, name, company, email, position, uid=None):
    self.name = name
    self.company = company
    self.email = email
    self.position = position
    self.uid = uid or uuid.uuid4()

  
  def to_dict(self):
    return vars(self)


  @staticmethod # metodo que s epuede ejecutar sin necesidad de una instancia de clase
  def schema():
    return ['name', 'company', 'email', 'position', 'uid']

  