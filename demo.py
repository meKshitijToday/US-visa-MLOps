from us_visa.logger import logging
from us_visa.exception import UsVisaException
import sys

# logging.info("Welcome to our custom log")       # This is log statement

try:
    a=2/0
except Exception as e:
    raise UsVisaException(e,sys)
