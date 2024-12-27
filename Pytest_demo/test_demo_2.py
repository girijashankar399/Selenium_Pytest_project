# pytest file name should start with test_ or end with _test.
#pytest methods name should start with test_
import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_firsttest():
    msg = "Hello"
    assert msg == "Hi", "String does not match"

def test_SecondCreditcard():
    a = 4
    b = 2
    assert a+2 == 6, "Addintion correct"