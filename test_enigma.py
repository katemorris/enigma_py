from enigma import Enigma

def test_generating_key():
    enigma = Enigma()
    key = enigma.generate_key()
    assert len(list(key)) == 5

def test_encrypting_message():
    message = 'hello world'
    key = '02715'
    date = '040895'
    enigma = Enigma()

    outcome = enigma.encrypt(message, key, date)

    expected = {
    'encryption': 'keder ohulw',
    'key': '02715',
    'date': '040895'
    }

    assert outcome == expected
