import requests
import config
import wallet
from loguru import logger
from cosmpy.aerial.client import LedgerClient, NetworkConfig
import pytest

"""
Test Config 
"""
##todo - move this to config
prefix="symphony"
wallet1=wallet.get_mnemonic_wallet("MNEMONIC_ONE",prefix)
wallet2=wallet.get_mnemonic_wallet("MNEMONIC_TWO", prefix)
endpoints = ["rest","grpc"]
def test_dump_consensus():
    dump_conensus_response = requests.get("https://rpc.testnet.symphonychain.org/dump_consensus_state")
    assert dump_conensus_response.status_code == 403 or dump_conensus_response.status_code == 404 or not 200, "return consensus - not status 200"

def test_genesis():
    genesis_response = requests.get("https://rpc.testnet.symphonychain.org/genesis")
    assert genesis_response.status_code == 200, "return genesis - should be status 200 success"

@pytest.mark.parametrize("endpoint", endpoints)
def test_query_balances(endpoint):
    client = LedgerClient(config.get_cfg(endpoint))
    balance = client.query_bank_all_balances(wallet1.address())
@pytest.mark.parametrize("endpoint", endpoints)
def test_send_denom(endpoint):
    cfg = config.get_cfg(endpoint)
    client = LedgerClient(cfg)
    client.send_tokens(wallet2.address(),1,cfg.fee_denomination,wallet1)
