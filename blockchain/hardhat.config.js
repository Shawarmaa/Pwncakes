require("@nomicfoundation/hardhat-toolbox");

/** @type import('hardhat/config').HardhatUserConfig */
module.exports = {
  solidity: {
    version: "0.8.28",  // or whatever version you're using
    settings: {
      evmVersion: "london"
    }
  },
  // ... rest of your config
};