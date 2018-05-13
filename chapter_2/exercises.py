# R-2.4
from chapter_1.exercises import calculate_product


class Flower:
    def __init__(self, name: str, number_of_petals: int, price: float) -> None:
        self._name = name
        self._number_of_petals = number_of_petals
        self._price = price

    def get_name(self):
        return self._name

    def get_number_of_petals(self):
        return self._number_of_petals

    def get_price(self):
        return self._price

    def set_name(self, name: str):
        self._name = name

    def set_number_of_petals(self, number_of_petals: int):
        self._number_of_petals = number_of_petals

    def set_price(self, price: float):
        self._price = price


class CreditCard:
    # R-2.7
    def __init__(self, customer, bank, acnt, limit, balance=0):
        self._balance = balance
        self._limit = limit
        self._account = acnt
        self._bank = bank
        self._customer = customer

    def get_customer(self):
        return self._customer

    def get_bank(self):
        return self._bank

    def get_account(self):
        return self._account

    def get_limit(self):
        return self._limit

    def get_balance(self):
        return self._balance

    # R-2.5
    def charge(self, price):
        if price <= 0:
            raise ValueError('price is lower or 0!')
        # if charge would exceed limit,
        if price + self._balance > self._limit:
            raise ValueError('Limit exceeded!')
        else:
            self._balance += price
        return True

    # R-2.6
    def make_payment(self, amount):
        if amount <= 0:
            raise ValueError('amount is lower or 0!')
        self._balance -= amount


def main_functon_credit_card():
    wallet = list()
    wallet.append(CreditCard(
        customer='John Bowman',
        bank='CaliforniaSavings',
        acnt='5391 0375 9387 5309',
        limit=2500)
    )
    wallet.append(CreditCard('JohnBowman', 'CaliforniaFederal', '3485 9999 3395 1954', 3500))
    wallet.append(CreditCard('JohnBowman', 'CaliforniaFinance', '5391 0375 9387 5309', 5000))

    for val in range(1, 17):
        wallet[0].charge(val)
        wallet[1].charge(2 * val)
        wallet[2].charge(3 * val)

    for c in range(3):
        print('Customer=', wallet[c].getcustomer())
        print('Bank=', wallet[c].getbank())
        print('Account=', wallet[c].getaccount())
        print('Limit=', wallet[c].getlimit())
        print('Balance=', wallet[c].getbalance())
        while wallet[c].get_balance() > 100:
            wallet[c].makepayment(100)
            print('Newbalance =', wallet[c].getbalance())
        print()


class Vector:
    # R-2.15
    def __init__(self, d: int = None, numbers=list):
        if not d:  # or d isinstance(d, collections.Iterable):
            self.coords = numbers
        else:
            self.coords = [0] * d

    def __len__(self):
        return len(self.coords)

    def __getitem__(self, j):
        return self.coords[j]

    def __setitem__(self, j, val):
        self.coords[j] = val

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))

        for j in range(len(self)):
            result[j] = self[j] + other[j]

        return result

    def __eq__(self, other):
        return self.coords == other.coords

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return '<' + str(self.coords)[1:-1] + '>'

    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))

        for j in range(len(self)):
            result[j] = self[j] - other[j]

        return result

    def __neg__(self):
        result = Vector(len(self))

        for j in range(len(self)):
            result[j] = -self[j]

        return result

    # R-2.11
    def __radd__(self, other):
        return self.__add__(other)

    # R-2.12
    def __mul__(self, obj):
        result = Vector(len(self))

        if isinstance(obj, Vector):
            data = calculate_product(self.coords, obj.coords)
            result.coords = data
        else:
            for j in range(len(self)):
                result[j] = self[j] * obj

        return result

    # R-2.13
    def __rmul__(self, other):
        return self.__mul__(other)


class SequenceIterator:
    def __init__(self, sequence):
        self._seq = sequence
        self._k = -1

    def next(self):
        self.k += 1
        if self.k < len(self.seq):
            return (self.seq[self.k])
        else:
            raise StopIteration()

    def iter(self):
        return self


# C-2.26
class ReverseSequenceIterator:
    def __init__(self, sequence):
        self._seq = sequence
        self._index = len(sequence)

    def __next__(self):
        self._index += -1
        if self._index >= 0:
            return self._seq[self._index]
        else:
            raise StopIteration()

    def __iter__(self):
        return self


class Range:
    def __init__(self, start, stop=None, step=1):
        if step == 0:
            raise ValueError('step cannot be 0')
        if stop is None:
            start, stop = 0, start
            self._length = max(0, (stop - start + step - 1) // step)
            self._start = start
            self._step = step

    def __contains__(self, item):
        return 0 <= item < self._length

    def __len__(self):
        return self._length

    def __getitem__(self, k):
        if k < 0:
            k += len(self)
        if not 0 <= k < self._length:
            raise IndexError('index out of range')

        return self._start + k * self._step


class PredatoryCreditCard(CreditCard):
    def __init__(self, customer, bank, acnt, limit, apr):
        super().__init__(customer, bank, acnt, limit)
        self._apr = apr
        self._number_charges_in_month = 0

    def charge(self, price):
        success = super().charge(price)
        if not success:
            self._balance += 5
        return success

    def process_month(self):
        self._number_charges_in_month += 1
        self._balance -= 1
        if self._balance > 0:
            monthly_factor = pow(1 + self._apr, 1/12)
            self._balance *= monthly_factor
