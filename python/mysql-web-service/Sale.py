class Sale(object):
    def __init__(self, date, amount, currency):
        self.date = date
        self.amount = amount
        self.currency = currency

    def __str__(self):
        return f'<li>date: {self.date}, amount: {self.amount}, currency: {self.currency}</li>'


class Currency(object):
    def __init__(self, source, target, rate, start_date):
        self.source = source
        self.target = target
        self.rate = rate
        self.start_date = start_date

    def __str__(self):
        return f'<li>source: {self.source}, target: {self.target}, rate: {self.rate}, start_date: {self.start_date}</li>'

