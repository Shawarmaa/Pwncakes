// const hre = require("hardhat");

// async function main() {
//   const QuantSignals = await hre.ethers.getContractFactory("QuantSignals");
//   const quantSignals = await QuantSignals.deploy();
  
//   // Wait for the contract to be deployed
//   await quantSignals.waitForDeployment();
  
//   // Get the contract address
//   const address = await quantSignals.getAddress();
//   console.log("QuantSignals deployed to:", address);
// }

// main().catch((error) => {
//   console.error(error);
//   process.exitCode = 1;
// });

async function main() {
const [deployer] = await ethers.getSigners();

console.log("Deploying contracts with the account:", deployer.address);

const PriceFeed = await ethers.getContractFactory("FtsoV2FeedConsumer");
const priceFeed = await PriceFeed.deploy();

// Wait for the deployment transaction to be mined
await priceFeed.waitForDeployment();

// Get the deployed contract address
const address = await priceFeed.getAddress();

console.log("PriceFeed deployed to:", address);
}

main()
.then(() => process.exit(0))
.catch((error) => {
    console.error(error);
    process.exit(1);
});