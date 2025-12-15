from hamming_code import hamming_encrypt

def test_encrption():
    assert hamming_encrypt((0, 1, 1, 0, 1, 1, 0, 1)) == [0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1]