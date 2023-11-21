import json


class Pistol:
    def __init__(self):
        self.max_magazines = 10
        self.max_bullets_in_mag = 15
        self.current_magazine = []
        self.magazines = [self.create_magazine() for _ in range(self.max_magazines)]

    def create_magazine(self):
        return [1] * self.max_bullets_in_mag

    def shot(self):
        if not self.current_magazine:
            self.reload()
        self.current_magazine.pop()

    def reload(self):
        if not self.magazines:
            raise OutOfMagazines("Out of magazines.")
        if self.current_magazine:
            self.current_magazine = []
        self.current_magazine = self.magazines.pop()

    def amount(self):
        magazines_left = len(self.magazines)
        bullets_in_current_magazine = len(self.current_magazine)
        return json.dumps({"magazines": magazines_left, "bullets": bullets_in_current_magazine})


class OutOfMagazines(Exception):
    pass


gun = Pistol()
gun.shot()
gun.shot()
gun.reload()
amount_json = gun.amount()
print(amount_json)
