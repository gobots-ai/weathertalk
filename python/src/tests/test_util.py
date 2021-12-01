
def test_list(build_list: list):
    assert len(build_list) == 10
    assert all(isinstance(element, int) for element in build_list)
