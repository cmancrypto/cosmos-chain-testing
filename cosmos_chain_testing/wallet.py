import base64

from cosmpy.aerial.wallet import LocalWallet
from cosmpy.crypto.keypairs import PrivateKey
from dotenv import load_dotenv
import os
from loguru import logger

def get_mnemonic_wallet(dotenv_varaible,prefix)->LocalWallet:
    load_dotenv()
    try:
        mnemonic = os.getenv(dotenv_varaible)
        assert mnemonic
        wallet = LocalWallet.from_mnemonic(mnemonic,prefix)
        logger.info(f"\n got wallet: {wallet.address()} from .env")
        return wallet
    except AssertionError as e:
        logger.error(f"Error ensure there is a .env with a valid  mnemonic : {e}")
    except ValueError as e:
        logger.error(e)

def get_wallet(private_key = None)->[LocalWallet,str]:
    if private_key == None:
        private_key = PrivateKey()
    elif private_key:
        private_key=PrivateKey(private_key)
    wallet = LocalWallet(private_key)
    logger.info(f"wallet of address {wallet.address()} from key {private_key.private_key}")
    return [wallet , private_key.private_key]

