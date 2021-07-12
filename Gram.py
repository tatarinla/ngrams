
class GramException(Exception):
    pass


class Gram:
    def __init__(self, filename):
        try:
            f = open(filename, 'r')
            message = f.read()
            self.words = message.split()
            self.max_len = len(self.words)
            self.grams = dict()

        except FileNotFoundError:
            raise GramException('File not found')

    def get_grams(self, gram_len):
        n_grams = dict()
        for i in range(self.max_len - gram_len + 1):
            seq = ''
            for j in range(i, gram_len + i - 1):
                seq += self.words[j] + ' '
            seq += self.words[gram_len + i - 1]
            if seq in n_grams.keys():
                n_grams[seq] += 1
            else:
                n_grams[seq] = 1

        self.grams.update({gram_len: n_grams})
        return n_grams

    def print_grams(self, top):
        for i in range(1, top + 1):
            print(f'{i}-length grams:')
            i_grams = self.get_grams(i)
            for seq, num in i_grams.items():
                print(f'{seq} = {num}')
