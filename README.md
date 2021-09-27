# Create and Deploy Your Own NFT - Proud Patriot

![Credit card fraudster](https://www.ledgerinsights.com/wp-content/uploads/2021/08/NFT-non-fungible-token.2.jpg)

## NFT Background
Where Bitcoin was hailed as the digital answer to currency, NFTs are now being touted as the digital answer to collectables. In economics, a fungible asset is something with units that can be readily interchanged - like money.

With money, you can swap a $20 note for two $10 notes and it will have the same value. However, if something is non-fungible, this is impossible - it means it has unique properties so it can't be interchanged with something else. It could be a house, or a painting such as the Mona Lisa, which is one of a kind. You can take a photo of the painting or buy a print, but there will only ever be one original painting.

NFTs are "one-of-a-kind" assets in the digital world that can be bought and sold like any other piece of property, but which have no tangible form of their own. The digital tokens can be thought of as certificates of ownership for virtual or physical assets.

Traditional works of art such as paintings are valuable precisely because they are one of a kind. But digital files can be easily and endlessly duplicated. With NFTs, artwork can be "tokenised" to create a digital certificate of ownership that can be bought and sold.

## Getting Started (Project Overview)
1. Artwork 
    * Generate NFT (.py) and create .png 
2. Upload Artwork
    * Upload NFT metadata to IPFS via Pinata
        * Save link to NFT .json as URI will be used in .sol contract deployment
3. Create Smart Contract for NFT Deployment
    * ProudPatriotNFT.sol
    * Need wallet address and .json URI link previously saved
4. Deploy to Rinkby Testnet and OpenSea
5. Create Smart Contract to Split Sales Proceeds from NFT's
    * ProfitSplitter.sol
6. Deploy NFT to Mainnet


### 1. Artwork
Need Josh's input here or see how this was completed?

### 2. Upload Artwork
Need Josh's input here or see how this was completed? Was mint command used? 

### 3. Create Smart Contract for NFT Deployment
* ProudPatriotNFT.sol imports ERC721 for the purposes of demonstrating integration with the OpenSea marketplace. We also include a script for minting the NFT items
* Change environment to Injected Web3 and make sure you are connected to MetaMask Rinkeby Test Network
* Make sure Proud_Patriot contract is selected and click deploy
* Confirm contract deployment on MetaMask

### 4. Deploy to Rinkby Testnet and OpenSea
* After deploying ProudPatriotNFT.sol to Rinkeby network, there will be a contract on Rinkeby that will be viewable on Rinkeby Etherscan. You will aslo be able to see your NFT on your OpenSea profile.
* Click on registerArt tab in the deployed Contract
* Copy your MetaMask account address into the "owner" input box
* Name your NFT in the "description" input box
* Past URI link into the "token_uri" input box (this linke was generated while uploading Artwork - see section above)
* Click the transact button
* Go https://testnets.opensea.io/ and check under your profile to confirm NFT was sucessfully deployed!

### 5. Create Smart Contract to Split Sales Proceeds from NFT's
Need Jon's input here. How will we execute this contract?

### 6. Deploy to NFT to Mainnet
After running your project on a testnet for some time without issues, you will want to deploy it to the main Ethereum network (aka mainnet). Make sure your wallet has at least a few dollars worth of ETH in it.

Please visit the following link for a full guide for preparing to deploy to the mainnet: https://docs.openzeppelin.com/learn/preparing-for-mainnet

Tip 1: OpenSea will automatically pick up transfers on your contract. You can visit an asset by going to https://opensea.io/assets/CONTRACT_ADDRESS/TOKEN_ID.

Tip 2: To load all your metadata on your items at once, visit https://opensea.io/get-listed and enter your address to load the metadata into OpenSea!