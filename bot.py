#!/usr/bin/env python3

"""
A crypto bot to send a message on telegram if there is a movement in the price of the cryptocurrency.

/alert BTC > 50000

/alert : command
BTC    : cryptocurrency
>      : operation
50000  : target price
"""

from coinbase.wallet.client import Client
from telegram import ParseMode
