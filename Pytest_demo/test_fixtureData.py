import pytest

from Pytest_demo.BaseClass import BaseClass


@pytest.mark.usefixture("dataload")
class TestExample(BaseClass):
    def test_editprofile(self,dataload):
        # print(dataload)
        # #we can also break the data into part
        #
        # print(dataload[0])
        # print(dataload[1])
        # print(dataload[2])
        log = self.getlogger()    # logging in log file
        log.info(dataload[0])
        log.info(dataload[2])
        print(dataload[2])


#loading multiple data set on a test case

def test_crossbrowser(crossbrowser):
    print(crossbrowser)