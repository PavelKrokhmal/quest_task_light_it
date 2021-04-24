import random


class ActionBase:
    def __init__(self, name, value_range, is_positive):
        self.name = name
        self.value_range = value_range
        self.is_positive = is_positive

    def __str__(self):
        return "{0} (range: {1}-{2})".format(
            self.name, self.value_range["left"], self.value_range["right"]
        )

    def get_random_value(self):
        return self.get_value_sign() * random.randint(
            self.value_range["left"], self.value_range["right"]
        )

    def get_value_sign(self):
        return 1 if self.is_positive else -1
