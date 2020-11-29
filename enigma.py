from datetime import date
import random

class Enigma:
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

    def datekey(self, date):
        return str(int(date) * int(date))[-4:]

    def get_shift(self, key, date):
        datekey = self.datekey(date)
        return [
        int(key[:2]) + int(datekey[:1]),
        int(key[1:3]) + int(datekey[1:2]),
        int(key[2:4]) + int(datekey[2:3]),
        int(key[3:5]) + int(datekey[3:4])
        ]

    def rotate_letter(self, move, char):
        location = self.letters.index(char)
        if ((move % 27) + location) > 27:
            return ((move % 27) + location) - 27
        else:
            return ((move % 27) + location)

    def shift_letter(self, round, char, key, date):
        if round <= 4:
            shift = self.get_shift(key, date)[round - 1]
            return self.rotate_letter(shift, char)
        else:
            shift = self.get_shift(key, date)[(round % 4) - 1]
            return self.rotate_letter(shift, char)

    def presto(self, message, key, date):
        new_msg = []
        round = 0
        for char in list(message.lower()):
            if char in self.letters:
                round += 1
                new_loc = self.shift_letter(round, char, key, date)
                new_msg.append(self.letters[new_loc])
            else:
                new_msg.append(char)
        return "".join(new_msg)

    def generate_key(self):
        digits = random.sample([str(x) for x in range(10)], 5)
        return "".join(digits)

    def encrypt(self, message, key = 'None', date = date.today().strftime("%d%m%y")):
        if key == 'None':
            key = self.generate_key()
        return {
        'encryption': self.presto(message, key, date),
        'key': key,
        'date': date
        }

    # def decrypt(encrypted, key, date = date.today()):
    #     {
    #     decryption: changeo(encrypted),
    #     key: key,
    #     date: date.strftime("%d/%m/%Y")
    #     }

    # def chango(encrypted):
    #     pass
