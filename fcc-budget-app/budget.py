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


def calc_percent(categories_dic, total):
    # Calculating the percent
    for category, value in categories_dic.items():
        categories_dic[category] = int(round(abs(value) / abs(total), 1)*100)

    return categories_dic


def __print_cover(categories_dic):
    lcategories = len(categories_dic)
    num_cover = 1 + lcategories + 2*lcategories

    cover = ''
    for i in range(0, num_cover):
        cover += '-'
    print('    ' + cover)


def create_spend_chart(categories):
    categories_dic = dict()
    total = 0
    # Adding all withdraw
    for category in categories:
        name = category.name
        categories_dic[name] = 0
        for item in category.ledger:
            if item['amount'] < 0:
                categories_dic[name] += item['amount']
        total += categories_dic[name]
    categories_dic = calc_percent(categories_dic, total)

    print('Percentage spent by category')
    for i in range(100, -10, -10):
        snum = str(i)
        shift = 4
        print((str(i) + '|').rjust(4), end='')
        print(' ', end='')
        for value in categories_dic.values():
            if value >= i:
                print('o  ', end='')
        print('')


    __print_cover(categories_dic)
