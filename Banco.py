class Bank_Account:
    def __init__(self):
        self.balance=0
        print("HOLA BIENVENIDO, AL BANCO ESTADO")
 
    def deposit(self):
        amount=float(input("Ingrese el saldo a depositar: "))
        self.balance += amount
        print("\n Saldo depositado:",amount)
 
    def withdraw(self):
        amount = float(input("Ingrese el saldo para ser retirado: "))
        if self.balance>=amount:
            self.balance-=amount
            print("\n tu saldo retirado:", amount)
        else:
            print("\n Saldo insuficiente  ")
 
    def display(self):
        print("\n nuevo saldo disponible =",self.balance)
 

  
# Objeto de la clase
s = Bank_Account()
  
# Llamar a las funciones 
s.deposit()
s.withdraw()
s.display()