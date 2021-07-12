""" Writes down a string content into a file"""

import os
import random
import string


class DataProvider:

    def __init__(self, message):
        letters = string.ascii_lowercase
        filename = ''.join(random.choice(letters) for i in range(10)) + '.txt'

        with open(filename, 'w') as f:
            f.write(message)

        self.filename = filename

    def __del__(self):
        os.remove(self.filename)
