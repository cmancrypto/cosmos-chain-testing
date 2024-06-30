import requests
from config import chain_config,chains_to_test, rpc_test_queries, get_network_cfg, get_chain_wallet, endpoints
from loguru import logger
from cosmpy.aerial.client import LedgerClient, NetworkConfig
import pytest

"""
Test Config 
"""


@pytest.mark.parametrize("chain", chains_to_test)
@pytest.mark.parametrize("query",rpc_test_queries)
def test_rpc_query(chain, query):
    url=chain_config[chain]["endpoints"]["rpc"]
    query_param=query["name"]
    response = requests.get(f"{url}{query_param}")
    desired_response=query["desired_response"]
    assert response.status_code == desired_response , f"response for {query} status should be {desired_response} not {response.status_code} "

@pytest.mark.parametrize("chain", chains_to_test)
@pytest.mark.parametrize("endpoint", endpoints)
def test_query_balances(chain,endpoint):
    wallet1=get_chain_wallet("MNEMONIC_ONE",chain)
    client = LedgerClient(get_network_cfg(endpoint,chain))
    balance = client.query_bank_all_balances(wallet1.address())


##send tests don't seem to work at the moment with cosmpy - removing from tests
"""
@pytest.mark.parametrize("chain", chains_to_test)
@pytest.mark.parametrize("endpoint", endpoints)
def test_send_denom(chain,endpoint):
    cfg = get_network_cfg(endpoint,chain)
    client = LedgerClient(cfg)
    wallet1 = get_chain_wallet("MNEMONIC_ONE", chain)
    wallet2 = get_chain_wallet("MNEMONIC_TWO", chain)
    print(cfg.fee_denomination)
    tx=client.send_tokens(destination=wallet2.address(),amount=1,denom=cfg.fee_denomination,sender=wallet1)
    tx.wait_to_complete()
"""
