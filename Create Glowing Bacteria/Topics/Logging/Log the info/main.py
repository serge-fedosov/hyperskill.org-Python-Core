import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
log_format = '%(levelname)s -> %(message)s'
console_handler.setFormatter(logging.Formatter(log_format))
logger.addHandler(console_handler)


def hypotenuse(a, b):
    h = round(((a ** 2 + b ** 2) ** 0.5), 2) 
    logging.info("Hypotenuse of %d and %d is %.2f", a, b, h)
    return h
