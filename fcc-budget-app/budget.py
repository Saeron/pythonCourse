import math
class Category():
    num_stars = 30

    def __init__(self, name):
        self.ledger = list()
        self.name = name

    def deposit(self, amount, description=''):
        self.ledger.append({
                "amount": amount,
                "description": description
            })

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({
                "amount": -amount,
                "description": description
            })
            return True
        return False

    def get_balance(self):
        balance = 0
        for ticket in self.ledger:
            balance += ticket['amount']
        return balance
    # wha other category?

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + category.name)
            category.deposit(amount, "Transfer from " + self.name)
            return True
        return False

    def check_funds(self, amount):
        funds = self.get_balance()
        if funds < amount:
            return False
        return True

    def __get_star_name(self):
        lname = len(self.name)
        stars_ini = (self.num_stars - lname) // 2
        stars_fin = self.num_stars - stars_ini - lname
        title = ''

        for i in range(0, stars_ini):
            title += '*'
        title += self.name
        for i in range(0, stars_fin):
            title += '*'

        return title

    def __get_short_desc(self, desc):
        if len(desc) > 23:
            return desc[0:23]
        return desc

    def __str__(self):

        star_name = self.__get_star_name()
        deposits = ''
        amount_desp = 0
        for item in self.ledger:
            description = self.__get_short_desc(item['description'])
            amount_desp = self.num_stars - len(description)
            deposits += description + \
                str("{:.2f}".format(float(item['amount']))).rjust(
                    amount_desp) + '\n'

        return star_name + '\n' + deposits + 'Total: ' + str(self.get_balance())


def __add_withdraw(categories_dic, categories):
    total = 0
    for category in categories:
        name = category.name
        categories_dic[name] = 0
        for item in category.ledger:
            if item['amount'] < 0:
                categories_dic[name] += item['amount']
        total += categories_dic[name]
    categories_dic = calc_percent(categories_dic, total)

def __print_axis(categories_dic):
    chart = ''
    for i in range(100, -10, -10):
        snum = str(i)
        shift = 4
        chart +=(str(i) + '|').rjust(4) +' '
        for value in categories_dic.values():
            if value >= i:
                chart += 'o  '
            else:
                chart += '   '
        chart+='\n'
    return chart

def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper

def calc_percent(categories_dic, total):
    # Calculating the percent
    for category, value in categories_dic.items():
        categories_dic[category] = int(truncate(abs(value) / abs(total), 1)*100)

    return categories_dic


def __print_cover(categories_dic):
    lcategories = len(categories_dic)
    num_cover = 1 + lcategories + 2*lcategories

    cover = ''
    for i in range(0, num_cover):
        cover += '-'
    return '    ' + cover

def __get_names(names, categories_dic):
    max_name = ''
    for name in categories_dic:
        names.append(name)
        if len(name) > len(max_name):
            max_name = name
    return max_name

def __print_names(names, max_name):
    chart = ''
    for index in range(0, len(max_name)):
        chart += '     '
        for n in names:
            if index < len(n):
                chart += n[index] + '  '
            else:
                chart += '   '
        chart += '\n'

    return chart.rstrip() + '  '


def create_spend_chart(categories):
    categories_dic = dict()
    chart = ''
    # Adding all withdraw
    __add_withdraw(categories_dic, categories)

    chart = 'Percentage spent by category' + '\n'
    chart += __print_axis(categories_dic)

    chart +=__print_cover(categories_dic) + '\n'

    names = list()
    max_name = __get_names(names, categories_dic)
    
    chart += __print_names(names, max_name)

    return chart
