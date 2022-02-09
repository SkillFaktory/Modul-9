class Client:
    def __init__(self, name, surname, balance):
        self.name = name
        self.surname = surname 
        self.balance = int(balance)

    def Parameters(self):
        return  f"Клиент {self. name} {self. surname}. Баланс: {self.balance} руб."

    def IncreaseBalance(self, sum):
        self.balance += int(sum)

    def DecreaseBalance(self, sum):
        self.balance += int(sum)

n = Client("Иван", "Петров", 50)
print(n.Parameters())
print(n.IncreaseBalance(100))
print(n.Parameters())