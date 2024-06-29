from cosmpy.aerial.client import  LedgerClient, NetworkConfig

##todo - fix this so that is more extensible and parameterized
def get_cfg(url_type):

    types={
        "grpc": "grpc+https://grpc.testnet.symphonychain.org/",
        "rest": "rest+https://lcd.testnet.symphonychain.org/"
           }
    url=types[url_type]

    cfg = NetworkConfig(
        chain_id="symphony-testnet-1",
        url=url,
        fee_minimum_gas_price=1,
        fee_denomination="note",
        staking_denomination="note",
    )
    return cfg