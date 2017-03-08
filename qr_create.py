#!/usr/bin/env python

import pyqrcode
import credentials
from bitcoinrpc import connection

rpcworker = connection.BitcoinConnection(credentials.rpcuser, credentials.rpcpassword, host='localhost', port=8332, use_https=False)
new_bitcoin_address = rpcworker.getnewaddress()
new_qr_code = pyqrcode.create(new_bitcoin_address, version=5)

#Displays the QR code in the terminal, useful for sending small test transfers on mainnet
print(new_qr_code.terminal())

#Displays the corresponding public key, just so you know where it's going!
print(new_bitcoin_address)

# examples
# rawtxn = rpcworker.createrawtransaction(
#                 [{"txid": "a9d4599e15b53f3eb531608ddb31f48c695c3d0b3538a6bda871e8b34f2f430c",
#                   "vout": 0}],
#                 {"1B9nCoZxEdKspVJ3xxqUN97FtgqGzLY9Ba":50})
# print(rpcworker.getconnectioncount())
# print(rpcworker.getdifficulty())
# print(rpcworker.getinfo())
# print(rpcworker.getbalance())

exit()
