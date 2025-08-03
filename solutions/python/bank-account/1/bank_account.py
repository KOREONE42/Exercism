class BankAccount:
    def __init__(self):
        # Indicates whether the account is open
        self._open = False
        # Current balance; valid only when account is open
        self._balance = 0

    def open(self):
        # Cannot open an account that's already open
        if self._open:
            raise ValueError('account already open')
        # Opening a fresh account resets balance to zero
        self._open = True
        self._balance = 0

    def get_balance(self):
        # Cannot check balance if account is not open
        if not self._open:
            raise ValueError('account not open')
        return self._balance

    def deposit(self, amount):
        # Cannot deposit into a closed or unopened account
        if not self._open:
            raise ValueError('account not open')
        # Deposit amount must be positive
        if amount <= 0:
            raise ValueError('amount must be greater than 0')
        self._balance += amount

    def withdraw(self, amount):
        # Cannot withdraw from a closed or unopened account
        if not self._open:
            raise ValueError('account not open')
        # Withdrawal amount must be positive
        if amount <= 0:
            raise ValueError('amount must be greater than 0')
        # Cannot withdraw more than the current balance
        if amount > self._balance:
            raise ValueError('amount must be less than balance')
        self._balance -= amount

    def close(self):
        # Cannot close an account that's not open
        if not self._open:
            raise ValueError('account not open')
        self._open = False
