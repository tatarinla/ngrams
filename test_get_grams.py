import json

from Gram import Gram, GramException
from DataProvider import DataProvider

f = open('test_data.json', 'r')
test_data = json.load(f)


def test_single_word():
    dp = DataProvider(test_data['single_word']['message'])
    gram = Gram(dp.filename)

    assert gram.get_grams(1) == test_data['single_word']['expected_result']

    del dp


def test_one_word_many_times():
    dp = DataProvider(test_data['one_word_many_times']['message'])
    gram = Gram(dp.filename)

    assert gram.get_grams(1) == test_data['one_word_many_times']['expected_result']

    del dp
