from DAB_Demo.hello_world import hello_world

def test_check_hello():
    message = hello_world()
    assert message
    
def test_hello_return_type():
    message = hello_world()
    assert type(message) == str