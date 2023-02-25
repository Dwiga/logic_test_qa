from main import logic


def test_logic_five(capfd):
    # assert logic(5) == "Odd 2 Odd 4 Odd"
    logic(5)
    captured = capfd.readouterr()
    assert captured.out == "Odd 2 Odd 4 Odd\n"


def test_logic_ten(capfd):
    logic(10)
    captured = capfd.readouterr()
    result = ''
    for i in range(1, 10 + 1):
        if i % 2 == 0:
            result += str(i) + " "
        else:
            result += "Odd "

    final = result.strip() + "\n"
    assert captured.out == final


def test_logic_more_than_five_oh(capfd):
    logic(51)
    captured = capfd.readouterr()
    assert captured.out == "Max. input is 50\n"
