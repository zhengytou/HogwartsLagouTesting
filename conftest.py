import pytest
def pytest_configure(config):
    marks_list = ["Web", "Interface"]
    for mark in marks_list:
      config.addinivalue_line("markers", mark)







