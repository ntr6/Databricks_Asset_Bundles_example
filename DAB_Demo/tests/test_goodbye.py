from DAB_Demo.goodbye_world import goodbye_world

def test_check_goodbye():
    message = goodbye_world()
    assert message
    
def test_goodbye_return_type():
    message = goodbye_world()
    assert type(message) == str
