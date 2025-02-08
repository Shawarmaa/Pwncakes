from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from web3 import Web3
from decimal import Decimal
import json

class PriceFeedView(APIView):
    def get(self, request):
        try:
            # Connect to Coston2 testnet
            w3 = Web3(Web3.HTTPProvider('https://coston2-api.flare.network/ext/C/rpc'))
            
            # Your deployed contract address
            contract_address = '0xcd47E2F7fE68Df87925D6dDb69e00cF21Bcb5781'  # Replace with your contract address
            
            # Contract ABI - just the function we need
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
                        }
                    ],
                    "stateMutability": "nonpayable",
                    "type": "function"
                }
            ]
            
            # Create contract instance
            contract = w3.eth.contract(address=contract_address, abi=abi)
            
            # Call the contract function
            feed_values, decimals, timestamp = contract.functions.getFtsoV2CurrentFeedValues().call()
            
            # Process the values
            processed_feeds = []
            for value, decimal in zip(feed_values, decimals):
                actual_value = Decimal(value) / Decimal(10 ** abs(decimal))
                processed_feeds.append(str(actual_value))  # Convert to string for JSON serialization
            
            return Response({
                'status': 'success',
                'timestamp': timestamp,
                'feed_values': processed_feeds
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response({
                'status': 'error',
                'message': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)