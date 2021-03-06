
<p align="center">
<img src="https://github.com/jan-o-e/NFTography/blob/main/NFTography.png" alt="drawing" width="400"/>
</p>

<h1>NFTography</h1>

NFTography is an image rights management platform for authentic and original photography. This revolutionizes the online photography world which is laden with copyright fraud and data ownership & rights issues. The ownership of images is certified with NFT's. The catch is that the images associated with the NFT's cannot already exist anywhere in the web such that we only allow for NFT based ownership of original work. Algorithmically provable original photos are uploaded and stored on IPFS which is a decentralized file-sharing platform which aims to provide access to data too large to be effectively stored on chain. The userflow is simple as all that is required is a Metamask Wallet and an Ethereum adress. The NFT's are stored through your Ethereum adress and minting is streamlined and made user friendly with the NFTography platform. Key features include auctioning and licensing. One can sell NFTographs over a certain time period through an auction, as well as buying (and of course selling) royalty free permissions (there exist a huge variety of legal image rights frameworks but this seemed to be the most straight forward and logical one for our platform) to one's NFTographs through a simple eth transaction. A complete record of all rights ever granted to any image is visible on the blockchain, as well as the ability to see the full transactional history of any NFT. The aim is to provide an easy to use, decentralized platform to empower content creators and counteract copyright infringements and fraud. This gives smaller creators and amateur photographers a chance to publish their work with secured ownership rights without the need for engaging with agencies often associated with large costs and bureacratic hurdles, particularly for those with little capital.

Our long-term vision is to exist as a browser extension for popular social media platforms which would allow users to upload images, such that those uploading their photographs have a right to prove their ownership of these images. This would - at least in the context of the blockchain - evoke the sense that those who upload their images to social media platforms own their data. Moreover, we would love to implement social features such as the ability to comment and like NFT's, such that  users accrue reputation through NFT ownership and platform activity. This would allow us to implement a scoring framework for NFT's based on user likes weighted by liker reputation as well as the market price and perhaps the number of royalty free licences granted. The possibilities are really endless.

<h2>Technical Details & Documentation</h2>
The Frontend can be viewed in \smash-template-opl\index.html

Key features are handled as follows:

Test Similarity Function \testSimilarity.py function will compare the current given image with a set of images in a fileDB directory and will return TRUE/FALSE indicating that the image is/(not) unique enough to be uploaded.

The functions used to upload, pin and mint NFT's are defined in \packages\hardhat\scripts. Hardhat also contains deployment information for out local Eth node and this is very similar to Scaffold-Eth. The specifications in the hardhatconfig.js file handle the network which we use for minting and also allow us to use Infura to connect to an eth node.

The smart contracts are found in \packages\hardhat\contracts, auction.sol is used for the auction whih unfortunately hasn't been hooked up to the frontend yet and nftography.sol is responsible for minting NFT's with the ERC-721 standard and using OpenZeppelin.
