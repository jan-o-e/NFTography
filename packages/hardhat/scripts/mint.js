/* eslint no-use-before-define: "warn" */
const fs = require("fs");
const chalk = require("chalk");
const { config, ethers } = require("hardhat");
const { utils } = require("ethers");
const R = require("ramda");
const ipfsAPI = require('ipfs-http-client');
const ipfs = ipfsAPI({host: 'ipfs.infura.io', port: '5001', protocol: 'https' })
import { AsyncLocalStorage } from "async_hooks";
/*import { reader } from "./fileread";*/
import {getName, getDesc} from "./getnamedescr";

const delayMS = 1000 //sometimes xDAI needs a 6000ms break lol 😅

// ADDRESS TO MINT TO, need to change from hardcode
const toAddress = "0x02c7BFfEDBBaFa1244dBDd5338b303e7DeD4115D"

// This initializes the smart contract
async function init () {
  const { deployer } = await getNamedAccounts();
  const nftograph = await ethers.getContract("NFTograph", deployer);
  return("Contract initialized");
  
}

// This uploads a file to IPFS, and creates the JSON metadata
async function upload () {
  // This needs to have an input of description and name  from the frontend to write into the metadata
  const metadata = {
    "description": getDesc,
    "image": reader.output,
    "name": getName,  
  }
  const uploaded = await ipfs.add(JSON.stringify(metadata));
  return "Uploading to IPFS with hash ("+uploaded.path+")";
}

// Here we would need to call the function which checks for the authenticity of the NFT (i.e. the database search)

//This function uploads and mints the NFT to the Ethereum blockchain, this should only be executed once we have the desired result from the authenticity check and the IPFS upload is complete
 async function mint () {
  await nftograph.mintItem(toAddress,uploaded.path,{gasLimit:400000})
    .catch(e => {
      return "ERROR Couldn't mint NFT" 
    })
  return "Minted to "+toAddress+"...\n";
 }

 //This transfers ownership of the initialized smart contract to the owner of the NFT which is the last thing that is required
 async function transfercontract () {
  await sleep(delayMS)
  await nftograph.transferOwnership(toAddress);
  return "Transferred ownership of contract to "+toAddress+" "
 }


  // const zebra = {
  //   "description": "What is it so worried about?",
  //   "external_url": "https://austingriffith.com/portfolio/paintings/",// <-- this can link to a page for the specific file too
  //   "image": "https://austingriffith.com/images/paintings/zebra.jpg",
  //   "name": "Zebra",
  //   "attributes": [
  //      {
  //        "trait_type": "BackgroundColor",
  //        "value": "blue"
  //      },
  //      {
  //        "trait_type": "Eyes",
  //        "value": "googly"
  //      },
  //      {
  //        "trait_type": "Stamina",
  //        "value": 38
  //      }
  //   ]
  // }
  // console.log("Uploading zebra...")
  // const uploadedzebra = await ipfs.add(JSON.stringify(zebra))

  // console.log("Minting zebra with IPFS hash ("+uploadedzebra.path+")")
  // await yourCollectible.mintItem(toAddress,uploadedzebra.path,{gasLimit:400000})



  // await sleep(delayMS)


  /*


  console.log("Minting zebra...")
  await yourCollectible.mintItem("0xD75b0609ed51307E13bae0F9394b5f63A7f8b6A1","zebra.jpg")

  */


  //const secondContract = await deploy("SecondContract")

  // const exampleToken = await deploy("ExampleToken")
  // const examplePriceOracle = await deploy("ExamplePriceOracle")
  // const smartContractWallet = await deploy("SmartContractWallet",[exampleToken.address,examplePriceOracle.address])



  /*
  //If you want to send value to an address from the deployer
  const deployerWallet = ethers.provider.getSigner()
  await deployerWallet.sendTransaction({
    to: "0x34aA3F359A9D614239015126635CE7732c18fDF3",
    value: ethers.utils.parseEther("0.001")
  })
  */


  /*
  //If you want to send some ETH to a contract on deploy (make your constructor payable!)
  const yourContract = await deploy("YourContract", [], {
  value: ethers.utils.parseEther("0.05")
  });
  */


  /*
  //If you want to link a library into your contract:
  // reference: https://github.com/austintgriffith/scaffold-eth/blob/using-libraries-example/packages/hardhat/scripts/deploy.js#L19
  const yourContract = await deploy("YourContract", [], {}, {
   LibraryName: **LibraryAddress**
  });
  */