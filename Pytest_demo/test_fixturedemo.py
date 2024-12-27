import pytest

# @pytest.fixture()
# def setup():
#     print("I will be execute first")
#     yield
#     print("I will be execute at last")

def test_fixturedemo(setup):
    print("I will be execute in fixture demo")


