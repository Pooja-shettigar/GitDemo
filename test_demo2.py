import pytest

@pytest.mark.usefixtures("dataload")
class TestExaple:

    def test_demo1(self,dataload):
        print(dataload)

    


