import logging

logging.basicConfig(
    filename="/tmp/opsec-hardener.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log(msg):
    logging.info(msg)
