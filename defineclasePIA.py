# Define una clase.
 
# La clase tiene las siguientes propiedades.
# telefono: loutilizamos para contactar a la persona, y actúa como PK.
# nombre: Es como se identifica la persona.
# correo: Es otro metodo para contactar a la persona.
# registro: Sirve para saber el dia de registro exacto.

# Se nececita una librería requerida ya que se usa la variable Date.
import datetime

# Se tiene que declarar una clase para la obtencion de los datos.
# De las cuales usaremos solo propiedades
class Contacto:
  # Se declara un procedimiento constructor.
  # Los argumentos se declaran como propiedades.
  # La propiedad registro es opcional, ya que la fecha del sistema es 
  # variable.
  def __init__(self, telefono, nombre,correo,registro=datetime.datetime.now(),UIValido=False):
    self.telefono=telefono
    self.nombre=nombre
    self.correo=correo
    self.registro=registro
    self.UIValido=UIValido