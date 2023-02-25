from main import logic


def test_logic_five():
    assert logic(5) == "Odd 2 Odd 4 Odd"


def test_logic_ten():
    result = ''
    for i in range(1, 10):
        if i % 2 == 0:
            result += str(i) + " "
        else:
            result += "Odd "

    assert logic(10) == result.strip()


def test_logic_more_than_five_oh():
    assert logic(51) == "Max. input is 50"
