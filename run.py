from Gram import Gram


def run(filename, top):
    gram = Gram(filename)
    gram.print_grams(top)
