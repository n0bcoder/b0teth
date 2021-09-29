from web3 import Web3
import json
import time
from eth_account import Account
import secrets
import akun

priv = secrets.token_hex(32)
private_key = priv
#print ("SAVE BUT DO NOT SHARE THIS:", private_key)
acct = Account.from_key(private_key)
#print("Address:", acct.address)

#alamatRPC
rpc = 'https://api.avax-test.network/ext/bc/C/rpc'
web3 = Web3(Web3.HTTPProvider(rpc))
balance = web3.eth.get_balance(acct.address)

humanReadable = web3.fromWei(balance,'ether')
print (private_key)
print(acct.address)
input('SIMPAN ADDRESS LALU TEKAN ENTER')

humanReadable = web3.fromWei(balance,'ether')

while True:
	balance =  web3.eth.get_balance(acct.address)
	baca = web3.fromWei(balance,'ether')
	print(baca)
	if( baca > 0):
		break

nonce = web3.eth.getTransactionCount(acct.address)

tx = {
    'nonce': nonce,
	'chainId': 43113,
    'to': akun.penerima,
    'value': web3.toWei(9.999475, 'ether'),
    'gas': 21000,
    'gasPrice': web3.toWei('25', 'gwei'),
}


#sign the transaction
signed_tx = web3.eth.account.sign_transaction(tx, private_key)

#send transaction
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

#get transaction hash
print('Saldo Terkirim !')
trx = web3.toHex(tx_hash)
print('https://cchain.explorer.avax-test.network/tx/'+trx)