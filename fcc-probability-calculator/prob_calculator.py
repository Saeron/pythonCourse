import copy
import random
# Consider using the modules imported above.


class Hat:

    def __init__(self, **kwargs):
        self.contents = list()
        values = dict(**kwargs)
        for item, value in values.items():
            for i in range(0, value):
                self.contents.append(item)

    def draw(self, num):
        draws = list()
        if len(self.contents) >= num:
            for i in range(0, num):
                rnd = random.randint(0, len(self.contents)-1)
                draws.append(self.contents[rnd])
                self.contents.remove(self.contents[rnd])
        else: 
            for i in self.contents:
                draws.append(i)
                self.contents.remove(i)
        return draws

def __compara_dics(dictionary, expected_balls):
    for key, value in expected_balls.items():
        if not dictionary.get(key):
            return False
        elif dictionary[key] < value:
            return False
    return True


def experiment(hat, expected_balls, num_balls_drawn,    num_experiments):
    balls = copy.deepcopy(hat)
    m = 0.0
    for n in range(0, num_experiments):
        result = balls.draw(num_balls_drawn)

        dictionary = dict()
        for item in result:
            if item not in dictionary:
                dictionary[item] = 1
            else:
                dictionary[item] += 1
        # necesita comparar si es subconjunto no esto
        if __compara_dics(dictionary, expected_balls):
            m += 1
        balls = copy.deepcopy(hat)
    pro = float(m / num_experiments) 
    return pro
