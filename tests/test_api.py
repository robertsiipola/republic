import republic


def test_first():
    api = republic.API(limit=10, offset=0)
    assert api.limit == 10
