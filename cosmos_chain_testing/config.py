from cosmpy.aerial.client import  NetworkConfig
from wallet import get_mnemonic_wallet
from cosmpy.aerial.wallet import LocalWallet


#CONFIG for tests to be run

#list of chains to be tested, name only needs to match that in chain_config
chains_to_test = ["symphony_testnet","osmosis"]

##CosmPy endpoints to be tested - only allows rest and grpc
endpoints=["rest","grpc"]

#chain_config - relevant configuration for each of the chains in chains_to_test
chain_config = {
    "symphony_testnet": {
        "endpoints" : {
            "grpc": "https://grpc.testnet.symphonychain.org/",
            "rpc" : "https://rpc.testnet.symphonychain.org/",
            "rest" : "https://lcd.testnet.symphonychain.org/",
        },
        "chain_id":"symphony-testnet-1",
        "fee_minimum_gas_price":0.05,
        "fee_denomination":"note",
        "staking_denomination":"note",
        "bech32_prefix" : "symphony"
    },
    "osmosis" :{
        "endpoints" : {
            "grpc": "https://grpc.testnet.osmosis.zone/",
            "rpc" : "https://rpc.osmotest5.osmosis.zone/",
            "rest" : "https://lcd.osmotest5.osmosis.zone/",
        },
        "chain_id":"osmo-test-5",
        "fee_minimum_gas_price":0.04,
        "fee_denomination":"uosmo",
        "staking_denomination":"uosmo",
        "bech32_prefix" : "osmo"
    },

    "fetch" :{
        "endpoints": {
            "grpc": "https://grpc-dorado.fetch.ai:443/",
            "rpc": "https://rpc-dorado.fetch.ai:443/",
            "rest": "https://rest-dorado.fetch.ai/",
        },
        "chain_id": "dorado-1",
        "fee_minimum_gas_price": 0.035,
        "fee_denomination": "atestfet",
        "staking_denomination": "atestfet",
        "bech32_prefix": "fetch"
    }
}

#rpc_test_queries = queries for comet BFT Endpoint tests
rpc_test_queries = [
    {"name":"dump_consensus_state", "desired_response" : 403},
    {"name":"genesis", "desired_response" : 200}
]

def get_network_cfg(endpoint_type: str, chain : str) -> NetworkConfig:
    """
    Get the CosmPy NetworkConfig

    :param endpoint_type: relevant NetworkConfig endpoints - either "grpc" or "rest"
    :type endpoint_type: str
    :param chain: name of chain to test - must be same name as defined in chain_config and chains_to_test
    :type chain: str
    :return: Cosmpy Network config for use with LedgerClient
    :rtype: NetworkConfig
    """

    endpoint=chain_config[chain]["endpoints"][endpoint_type]
    url=f"{endpoint_type}+{endpoint}"

    cfg = NetworkConfig(
        chain_id=chain_config[chain]["chain_id"],
        url=url,
        fee_minimum_gas_price=chain_config[chain]["fee_minimum_gas_price"],
        fee_denomination=chain_config[chain]["fee_denomination"],
        staking_denomination=chain_config[chain]["staking_denomination"],
    )
    return cfg

def get_chain_wallet(dotenv_variable_name: str, chain: str)-> LocalWallet:
    prefix=chain_config[chain]["bech32_prefix"]
    wallet = get_mnemonic_wallet(dotenv_variable_name, prefix)
    return wallet