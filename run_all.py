import pytest
if __name__ == '__main__':
    pytest.main(['-s', '-q', '-m',"smoke or Web", '--alluredir','./allure-results'])