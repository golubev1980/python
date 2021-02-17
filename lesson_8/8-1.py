class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def set_date(cls, set_date):
        set_date = input_date.split('-')
        d, m, y = set_date
        return cls(int(d), int(m), int(y))

    @staticmethod
    def get_date(param):
        return f'{param.day} {param.month} {param.year}' if 1 <= param.day <= 31 and 1 <= param.month <= 12 and 1 <= param.year <= 2021 else 'Дата некорректна'


input_date = "16-02-2021"

param = Date.set_date(input_date)
print(Date.get_date(param))
