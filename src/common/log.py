import logging
import sys

root = logging.getLogger()
root.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(levelname)s] [%(asctime)s] - %(name)s - %(message)s')
handler.setFormatter(formatter)
root.addHandler(handler)

default_logger = logging.getLogger()
