import logging
logging.basicConfig(level=logging.DEBUG,
                    filename="p8_2_logs.log",
                    filemode="w",
                    format="We have message:%(asctime)s:@:%(levelname)s - %(message)s")

try:
    print(10/0)
except Exception:
    logging.exception("Exception")
