from toto.lib import whats_my_name

def test_whoami():

    res = whats_my_name()

    assert "Gaetan" in res.split()