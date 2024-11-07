from utils_logger import log_decorator
from loguru import logger

@log_decorator
def soma(x,y):
    return x+y

soma(2,3)
soma(5,3)
soma(7,3)