from fairsharer.fair_sharer import fair_sharer

def test_fair_sharer_example_1():
    result = fair_sharer([0, 1000, 800, 0], 1)
    expected = [100.0, 800.0, 900.0, 0.0]
    assert result == expected

def test_fair_sharer_example_2():
    result = fair_sharer([0, 1000, 800, 0], 2)
    expected = [100.0, 890.0, 720.0, 90.0]
    assert result == expected