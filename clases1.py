#Las clases permiten representar los atributos y metodos.

class CuentaBancaria:
   def __init__(self, num_cuenta, nombre_titular, balance): #self instancia actual
      self.num_cuenta= num_cuenta  #Atributos(carateristicas)
      self.nombre_titular= nombre_titular
      self.balance= balance
   
   def generar_balance(self):
      print(self.balance)

   def depositar (self, monto):
      if monto > 0:
        self.balance += monto

#creando las instancias

mi_cuenta= CuentaBancaria("235-556-666", "Mario", 7300)
print(mi_cuenta.balance)

mi_cuenta.generar_balance()

mi_cuenta.depositar(700)
mi_cuenta.generar_balance()

class Person:
   def __init__(self, nombre, edad):
      self.nombre= nombre
      self.edad= edad

   def saludar(self):
      print("Saludando a esta persona {} y tiene {} años" .format(self.nombre, self.edad))
      print(self.nombre, self.edad)

per= Person("Sheilan", 48)
print(per.nombre)
per.saludar()

class Person_2(Person):
    def __init__(self, nombre, edad):
       super().__init__(nombre, edad)
       

    def reir(self, apellido):
       print("Este es el apellido de esa persona sonriendo", apellido)
       self.apellido= apellido
       print("Los nuevos datos son:", self.nombre,self.apellido,"y tiene", self.edad, "años")


perso2= Person_2("Michael", 19)

perso2.reir("Bulgarati")

#ENUNCIADO: crear una clase llamada cuenta que tenga los siguientes atributos: 
# titular y cantidad.
# (puede tener decimales). El titular sera obligatorio y la cantidad opcional, 
#tendra dos metodos especiales:
# 1. Ingresar cantidad: se ingresa una cantidad a la cuenta, si la cantidad introducida 
#es negativa, no se hara nada. 2. Retirar cantidad: se retira una cantidad a la cuenta, 
#si restando la cantidad actual a la que nos pasan es negativa, la cantidad 
#de la cuenta pasa a ser (0).

class Cuenta:
   def __init__(self, titular, cantidad):
      self.titular= titular
      self.cantidad= cantidad
      print("El titular es", titular, "y su cantidad es", cantidad, "$")

   def ingresar (self, cantidad):
      if(cantidad<0):
         print("La cantidad es negativa, no se realizara la operacion")
      else:
         self.cantidad += cantidad
         print("Este es tu nuevo saldo luego de ingresar", self.cantidad,"$")

   def retirar (self, cantidad):
      if(self.cantidad - cantidad < 0):
         cantidad =0
         print("No puede retirar la cantidad, su saldo seria insuficiente", cantidad,"$")
      else:
         print ("El saldo que le queda luego del retiro es:", self.cantidad - cantidad,"$")

persoo= Cuenta ("Nazareth", 3000)

persoo.ingresar(8000)
persoo.retirar(12000)
persoo.retirar(10000)

