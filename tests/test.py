from mypackage import myModule

def test_top_n():
    """
    make sure top_n work correctly
    """

    assert myModule.top_n([8,3,2,7,4],3)==[8,7,3], 'Incorrect'
    assert myModule.top_n([10,1,12,9,2],3)==[12,10], 'Incorrect'
    assert myModule.top_n([1,2,3,4,5,6],3)==[5,4,3,2,1], 'Incorrect'