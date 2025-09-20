import subprocess

def create_fake_eth(interface="wlan0", ip="192.168.1.60/24"):
    subprocess.run(["ip", "link", "add", "link", interface, "name", "eth-fake", "type", "macvlan"], check=False)
    subprocess.run(["ip", "addr", "add", ip, "dev", "eth-fake"], check=False)
    subprocess.run(["ip", "link", "set", "eth-fake", "up"], check=False)

def apply_killswitch(allowed_if="eth-fake"):
    subprocess.run(["nft", "add", "table", "inet", "filter"], check=False)
    subprocess.run(["nft", "add", "chain", "inet", "filter", "input", "{", "type", "filter", "hook", "input", "priority", "0", ";", "}"], check=False)
    subprocess.run(["nft", "add", "rule", "inet", "filter", "input", "iifname", "!=", allowed_if, "drop"], check=False)
