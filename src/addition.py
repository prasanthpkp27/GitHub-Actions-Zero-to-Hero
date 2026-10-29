# app.py
def add(a, b):
    return a + b
#this is the testcase
def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
