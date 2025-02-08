# Cross-Chain Liquidity Aggregator by Pwncakes

A decentralized cross-chain liquidity aggregator built on Flare Network that optimizes trading routes across multiple blockchains using FTSO price feeds and FDC for enhanced market data.

## Features

- Smart route optimization across multiple chains
- Real-time price feeds via Flare FTSO
- Automated liquidity rebalancing
- Bridge health monitoring
- Gas optimization across routes
- Single-transaction cross-chain trades
- Dynamic liquidity incentives

## Tech Stack

- **Frontend**: Next.js
- **Backend**: Django + Django REST Framework
- **Blockchain**: Solidity (Hardhat)
- **Network**: Flare (Coston2 Testnet)

## Prerequisites

- Node.js (v16 or higher)
- Python 3.8+
- MetaMask wallet
- Git

## Project Structure

```
project/
├── frontend/           # Next.js frontend application
├── backend/           # Django REST API
└── blockchain/        # Solidity smart contracts
```

## Installation

### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

### Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Blockchain Setup
```bash
cd blockchain
npm install
npx hardhat compile
npx hardhat node  # Start local blockchain
npx hardhat test  # Run tests
```

## Environment Variables

Create `.env` files in each directory:

### Frontend (.env.local)
```
NEXT_PUBLIC_BACKEND_URL=http://localhost:8000
NEXT_PUBLIC_CONTRACT_ADDRESS=your_contract_address
```

### Backend (.env)
```
DEBUG=True
SECRET_KEY=your_secret_key
ALLOWED_HOSTS=localhost,127.0.0.1
CONTRACT_ADDRESS=your_contract_address
```

### Blockchain (.env)
```
PRIVATE_KEY=your_private_key
COSTON2_RPC_URL=https://coston2-api.flare.network/ext/C/rpc
```

## Smart Contract Deployment

1. Configure network in `hardhat.config.js`
2. Deploy to Coston2 testnet:
```bash
npx hardhat run scripts/deploy.js --network coston2
```

## API Endpoints

- GET `/api/routes` - Get optimal trading routes
- POST `/api/execute` - Execute cross-chain trade
- GET `/api/prices` - Get current price feeds
- GET `/api/bridges` - Get bridge health status

## Testing

### Frontend
```bash
cd frontend
npm test
```

### Backend
```bash
cd backend
python manage.py test
```

### Smart Contracts
```bash
cd blockchain
npx hardhat test
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

MIT License - see the [LICENSE](LICENSE) file for details

## Project Resources

- [Flare Documentation](https://docs.flare.network/)
- [FTSO Documentation](https://docs.flare.network/tech/ftso/)
- [FDC Documentation](https://docs.flare.network/tech/data-contracts/)

## Security

This project is in development. Do not use in production without proper security audit.

## Contact

Project Link: [https://github.com/yourusername/project-name](https://github.com/yourusername/project-name)# Cross-Chain Liquidity Aggregator

A decentralized cross-chain liquidity aggregator built on Flare Network that optimizes trading routes across multiple blockchains using FTSO price feeds and FDC for enhanced market data.

## Features

- Smart route optimization across multiple chains
- Real-time price feeds via Flare FTSO
- Automated liquidity rebalancing
- Bridge health monitoring
- Gas optimization across routes
- Single-transaction cross-chain trades
- Dynamic liquidity incentives

## Tech Stack

- **Frontend**: Next.js
- **Backend**: Django + Django REST Framework
- **Blockchain**: Solidity (Hardhat)
- **Network**: Flare (Coston2 Testnet)

## Prerequisites

- Node.js (v16 or higher)
- Python 3.8+
- MetaMask wallet
- Git

## Project Structure

```
project/
├── frontend/           # Next.js frontend application
├── backend/           # Django REST API
└── blockchain/        # Solidity smart contracts
```

## Installation

### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

### Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Blockchain Setup
```bash
cd blockchain
npm install
npx hardhat compile
npx hardhat node  # Start local blockchain
npx hardhat test  # Run tests
```

## Environment Variables

Create `.env` files in each directory:

### Frontend (.env.local)
```
NEXT_PUBLIC_BACKEND_URL=http://localhost:8000
NEXT_PUBLIC_CONTRACT_ADDRESS=your_contract_address
```

### Backend (.env)
```
DEBUG=True
SECRET_KEY=your_secret_key
ALLOWED_HOSTS=localhost,127.0.0.1
CONTRACT_ADDRESS=your_contract_address
```

### Blockchain (.env)
```
PRIVATE_KEY=your_private_key
COSTON2_RPC_URL=https://coston2-api.flare.network/ext/C/rpc
```

## Smart Contract Deployment

1. Configure network in `hardhat.config.js`
2. Deploy to Coston2 testnet:
```bash
npx hardhat run scripts/deploy.js --network coston2
```

## API Endpoints

- GET `/api/routes` - Get optimal trading routes
- POST `/api/execute` - Execute cross-chain trade
- GET `/api/prices` - Get current price feeds
- GET `/api/bridges` - Get bridge health status

## Testing

### Frontend
```bash
cd frontend
npm test
```

### Backend
```bash
cd backend
python manage.py test
```

### Smart Contracts
```bash
cd blockchain
npx hardhat test
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

MIT License - see the [LICENSE](LICENSE) file for details

## Project Resources

- [Flare Documentation](https://docs.flare.network/)
- [FTSO Documentation](https://docs.flare.network/tech/ftso/)
- [FDC Documentation](https://docs.flare.network/tech/data-contracts/)

## Security

This project is in development. Do not use in production without proper security audit.

## Contact

Project Link: [https://github.com/yourusername/project-name](https://github.com/yourusername/project-name)