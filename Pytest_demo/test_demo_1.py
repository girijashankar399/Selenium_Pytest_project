# pytest file name should start with test_ or end with _test.
#pytest methods name should start with test_
import pytest


@pytest.mark.smoke
def test_firsttest():
    print("hello")

def test_GreetCreditcard():
    print("Good Morning")