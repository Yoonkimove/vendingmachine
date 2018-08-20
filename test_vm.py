from vm import VendingMachine


def test_initial_change_should_be_zero():
    m = VendingMachine()
    assert "잔액은 0원입니다" == m.run("잔액")

def test_insert_coin_and_check():
    m = VendingMachine()
    assert "100원을 넣었습니다" == m.run("동전 100")
    assert "잔액은 100원입니다" == m.run("잔액")

def test_accumulation_of_change():
    m = VendingMachine()
    m.run("동전 100")
    m.run("동전 100")
    assert "잔액은 200원입니다" == m.run("잔액")

def test_I_dont_know():
    m = VendingMachine()
    assert "알 수 없는 명령입니다." == m.run("moony")

def test_short():
    m = VendingMachine()
    m.run("동전 100")
    assert "잔액이 부족합니다." == m.run("음료 커피")
    assert "잔액은 100원입니다" == m.run("잔액")

def test_full():
    m = VendingMachine()
    m.run("동전 500")
    assert "커피가 나왔습니다." == m.run("음료 커피")
    assert "잔액은 350원입니다" == m.run("잔액")

def test_unknown_drink():
    m = VendingMachine()
    m.run("둥전 500")
    assert "알 수 없는 음료입니다." == m.run("음료 맥주")

# def test_valid_coins():
#     m = VendingMachine()
#     valid_coins = ["10", "50", "100", "500"]
#     for coin in valid_coins:
#         assert coin + "원을 넣었습니다" = m.run("동전" + coin)

def test_invalid_coin():
    m = VendingMachine()
    assert "알 수 없는 동전입니다." == m.run("동전 999")
    assert "잔액은 0원입니다" == m.run("잔액")
