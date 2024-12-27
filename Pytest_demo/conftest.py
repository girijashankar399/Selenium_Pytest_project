import pytest

@pytest.fixture()
def setup():
    print("I will be execute first")
    yield
    print("I will be execute at last")

@pytest.fixture()
def dataload():
    print("user profile data is being created ")
    return ["Rahul", "Shetty", "rahulsetty.com"]

# @pytest.fixture(params=["chrome","FireFox","IE"])
# def crossbrowser(request):
#     return request.param

@pytest.fixture(params=[("Rahul","chrome"),"FireFox","IE"])
def crossbrowser(request):
    return request.param