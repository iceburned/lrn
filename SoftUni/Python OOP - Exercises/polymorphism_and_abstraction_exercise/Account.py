class Account:
    def __init__(self, owner, amount=0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    @staticmethod
    def validate_transaction(account, amount_to_add):
        new_balance = account.balance + amount_to_add
        if new_balance <= 0:
            raise ValueError("sorry cannot go in debt!")
        account.add_transaction(amount_to_add)
        return f"New balance: {account.balance}"

    @property
    def balance(self):
        return sum(self._transactions) + self.amount

    def add_transaction(self, amount):
        if isinstance(amount, int):
            self._transactions.append(amount)
        else:
            raise ValueError("please use int for amount")

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"

    def __len__(self):
        return len(self._transactions)

    def __reversed__(self):
        return reversed(self._transactions)

    def __add__(self, other):
        result = Account(f"{self.owner}&{other.owner}", self.amount + other.amount)
        for s in self:
            result.add_transaction(s)
        for ss in other:
            result.add_transaction(ss)
        return result

    def __getitem__(self, item):
        return self._transactions[item]

    def __lt__(self, other):
        return self.balance < other.balance

    def __le__(self, other):
        return self.balance <= other.balance

    def __eq__(self, other):
        return self.balance == other.balance
