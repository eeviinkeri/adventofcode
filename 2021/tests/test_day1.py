from day1 import __version__


def test_version():
    assert __version__ == '0.1.0'


test_data = [
    199,
    200,
    208,
    210,
    200,
    207,
    240,
    269,
    260,
    263,
    ]


def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 5