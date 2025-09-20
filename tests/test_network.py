from src.opsec_hardener import network

def test_fake_eth_function_exists():
    assert callable(network.create_fake_eth)
