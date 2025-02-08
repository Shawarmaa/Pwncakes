# backend/api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from web3 import Web3
from decimal import Decimal

class PriceFeedView(APIView):
    # Complete mapping of feed IDs with additional information
    FEED_INFO = {
        "0x01464c522f55534400000000000000000000000000": {"name": "FLR/USD", "base_asset": "Flare", "status": "🟢"},
        "0x015347422f55534400000000000000000000000000": {"name": "SGB/USD", "base_asset": "Songbird", "status": "🟡"},
        "0x014254432f55534400000000000000000000000000": {"name": "BTC/USD", "base_asset": "Bitcoin", "status": "🟢"},
        "0x015852502f55534400000000000000000000000000": {"name": "XRP/USD", "base_asset": "XRP", "status": "🟢"},
        "0x014c54432f55534400000000000000000000000000": {"name": "LTC/USD", "base_asset": "Litecoin", "status": "🟢"},
        "0x01584c4d2f55534400000000000000000000000000": {"name": "XLM/USD", "base_asset": "Stellar", "status": "🟡"},
        "0x01444f47452f555344000000000000000000000000": {"name": "DOGE/USD", "base_asset": "Dogecoin", "status": "🟡"},
        "0x014144412f55534400000000000000000000000000": {"name": "ADA/USD", "base_asset": "Cardano", "status": "🟢"},
        "0x01414c474f2f555344000000000000000000000000": {"name": "ALGO/USD", "base_asset": "Algorand", "status": "🟡"},
        "0x014554482f55534400000000000000000000000000": {"name": "ETH/USD", "base_asset": "Ethereum", "status": "🟢"},
        "0x0146494c2f55534400000000000000000000000000": {"name": "FIL/USD", "base_asset": "Filecoin", "status": "🟢"},
        "0x014152422f55534400000000000000000000000000": {"name": "ARB/USD", "base_asset": "Arbitrum", "status": "🟢"},
        "0x01415641582f555344000000000000000000000000": {"name": "AVAX/USD", "base_asset": "Avalanche", "status": "🟢"},
        "0x01424e422f55534400000000000000000000000000": {"name": "BNB/USD", "base_asset": "BNB", "status": "🟢"},
        "0x01504f4c2f55534400000000000000000000000000": {"name": "POL/USD", "base_asset": "POL (ex-MATIC)", "status": "🟢"},
        "0x01534f4c2f55534400000000000000000000000000": {"name": "SOL/USD", "base_asset": "Solana", "status": "🟢"},
        "0x01555344432f555344000000000000000000000000": {"name": "USDC/USD", "base_asset": "USDC", "status": "🟢"},
        "0x01555344542f555344000000000000000000000000": {"name": "USDT/USD", "base_asset": "Tether", "status": "🟢"},
        "0x015844432f55534400000000000000000000000000": {"name": "XDC/USD", "base_asset": "XDC Network", "status": "🟡"},
        "0x015452582f55534400000000000000000000000000": {"name": "TRX/USD", "base_asset": "TRON", "status": "🟢"},
        "0x014c494e4b2f555344000000000000000000000000": {"name": "LINK/USD", "base_asset": "Chainlink", "status": "🟢"},
        "0x0141544f4d2f555344000000000000000000000000": {"name": "ATOM/USD", "base_asset": "Cosmos Hub", "status": "🟢"},
        "0x01444f542f55534400000000000000000000000000": {"name": "DOT/USD", "base_asset": "Polkadot", "status": "🟢"},
        "0x01544f4e2f55534400000000000000000000000000": {"name": "TON/USD", "base_asset": "Toncoin", "status": "🟢"},
        "0x014943502f55534400000000000000000000000000": {"name": "ICP/USD", "base_asset": "Internet Computer", "status": "🟢"},
        "0x01534849422f555344000000000000000000000000": {"name": "SHIB/USD", "base_asset": "Shiba Inu", "status": "🔴"},
        "0x014441492f55534400000000000000000000000000": {"name": "DAI/USD", "base_asset": "Dai", "status": "🟢"},
        "0x014243482f55534400000000000000000000000000": {"name": "BCH/USD", "base_asset": "Bitcoin Cash", "status": "🟢"},
        "0x014e4541522f555344000000000000000000000000": {"name": "NEAR/USD", "base_asset": "NEAR Protocol", "status": "🟢"},
        "0x014c454f2f55534400000000000000000000000000": {"name": "LEO/USD", "base_asset": "LEO Token", "status": "🔴"},
        "0x01554e492f55534400000000000000000000000000": {"name": "UNI/USD", "base_asset": "Uniswap", "status": "🟢"},
        "0x014554432f55534400000000000000000000000000": {"name": "ETC/USD", "base_asset": "Ethereum Classic", "status": "🟡"},
        "0x015749462f55534400000000000000000000000000": {"name": "WIF/USD", "base_asset": "dogwifhat", "status": "🔴"},
        "0x01424f4e4b2f555344000000000000000000000000": {"name": "BONK/USD", "base_asset": "Bonk", "status": "🔴"},
        "0x014a55502f55534400000000000000000000000000": {"name": "JUP/USD", "base_asset": "Jupiter", "status": "🟢"},
        "0x0145544846492f5553440000000000000000000000": {"name": "ETHFI/USD", "base_asset": "Ether.fi", "status": "🟡"},
        "0x01454e412f55534400000000000000000000000000": {"name": "ENA/USD", "base_asset": "Ethena", "status": "🟡"},
        "0x01505954482f555344000000000000000000000000": {"name": "PYTH/USD", "base_asset": "Pyth Network", "status": "🟢"},
        "0x01484e542f55534400000000000000000000000000": {"name": "HNT/USD", "base_asset": "Helium", "status": "🟡"},
        "0x015355492f55534400000000000000000000000000": {"name": "SUI/USD", "base_asset": "Sui", "status": "🟢"},
        "0x01504550452f555344000000000000000000000000": {"name": "PEPE/USD", "base_asset": "Pepe", "status": "🔴"},
        "0x01514e542f55534400000000000000000000000000": {"name": "QNT/USD", "base_asset": "Quant", "status": "🟡"},
        "0x01414156452f555344000000000000000000000000": {"name": "AAVE/USD", "base_asset": "Aave", "status": "🟢"},
        "0x0146544d2f55534400000000000000000000000000": {"name": "FTM/USD", "base_asset": "Fantom", "status": "🔴"},
        "0x014f4e444f2f555344000000000000000000000000": {"name": "ONDO/USD", "base_asset": "Ondo", "status": "🟡"},
        "0x0154414f2f55534400000000000000000000000000": {"name": "TAO/USD", "base_asset": "Bittensor", "status": "🟡"},
        "0x014645542f55534400000000000000000000000000": {"name": "FET/USD", "base_asset": "Artificial Superintelligence Alliance", "status": "🟢"},
        "0x0152454e4445522f55534400000000000000000000": {"name": "RENDER/USD", "base_asset": "Render", "status": "🟢"},
        "0x014e4f542f55534400000000000000000000000000": {"name": "NOT/USD", "base_asset": "Notcoin", "status": "🟡"},
        "0x0152554e452f555344000000000000000000000000": {"name": "RUNE/USD", "base_asset": "THORChain", "status": "🟡"},
        "0x015452554d502f5553440000000000000000000000": {"name": "TRUMP/USD", "base_asset": "Official Trump", "status": "⚫"}
    }

    def get(self, request):
        try:
            # Connect to Coston2 testnet
            w3 = Web3(Web3.HTTPProvider('https://coston2-api.flare.network/ext/C/rpc'))
            
            # Your deployed contract address
            contract_address = '0x00cFaAC5f5b85880484fd676E36760b98A24fd9d'  # Replace with your contract address
            
            # Contract ABI
            abi = [
                {
                    "inputs": [],
                    "name": "getFtsoV2CurrentFeedValues",
                    "outputs": [
                        {
                            "internalType": "uint256[]",
                            "name": "_feedValues",
                            "type": "uint256[]"
                        },
                        {
                            "internalType": "int8[]",
                            "name": "_decimals",
                            "type": "int8[]"
                        },
                        {
                            "internalType": "uint64",
                            "name": "_timestamp",
                            "type": "uint64"
                        },
                        {
                            "internalType": "bytes21[]",
                            "name": "_feedIds",
                            "type": "bytes21[]"
                        }
                    ],
                    "stateMutability": "nonpayable",
                    "type": "function"
                }
            ]
            
            # Create contract instance
            contract = w3.eth.contract(address=contract_address, abi=abi)
            
            # Call the contract function
            feed_values, decimals, timestamp, feed_ids = contract.functions.getFtsoV2CurrentFeedValues().call()
            
            # Process the values with complete information
            processed_feeds = []
            for feed_id, value, decimal in zip(feed_ids, feed_values, decimals):
                feed_id_hex = feed_id.hex()
                # Add '0x' prefix to match our mapping
                feed_id_lookup = f"0x{feed_id_hex}"
                actual_value = Decimal(value) / Decimal(10 ** abs(decimal))
                
                feed_info = self.FEED_INFO.get(feed_id_lookup, {
                    "name": "Unknown",
                    "base_asset": "Unknown",
                    "status": "⚫"
                })
                
                processed_feeds.append({
                    'pair': feed_info['name'],
                    'base_asset': feed_info['base_asset'],
                    'status': feed_info['status'],
                    'feed_id': feed_id_lookup,
                    'value': str(actual_value),
                    'decimals': decimal
                })
            
            return Response({
                'status': 'success',
                'timestamp': timestamp,
                'feeds': processed_feeds
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response({
                'status': 'error',
                'message': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
