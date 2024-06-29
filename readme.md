Test Cosmos Chain RPC Endpoint Implementation

```pip install -r requirements.txt ```

Rename `.env.sample` to `.env` and include 2x 24 word wallet mnemonics. 

Ensure that wallet 1 has testnet tokens otherwise send tests will fail 

Change the config in `config.py` to suit chain for testing 

In root directory:
```
python -m pytest
```


