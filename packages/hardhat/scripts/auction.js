/* eslint no-use-before-define: "warn" */
const fs = require("fs");
const chalk = require("chalk");
const { config, ethers } = require("hardhat");
const { utils } = require("ethers");
const R = require("ramda");


const delayMS = 1000 //

//The bid time needs to be fetched from the frontend as specified by the user
async function auction_init(time) {
    const bidtime = time
  // ADDRESS OWNING NFT need to hardcode:
  const owner = "0xbD451AaCD336a20acb806c499EE431015C3F3594"
  const auction = await ethers.getContractAt('auction', "0xbD451AaCD336a20acb806c499EE431015C3F3594") //<-- if you want to instantiate a version of a contract at a specific address!
    const contract = await auction.deploy(bidtime, owner);
    return ("Auction started at" ("+contract.adress+"))
}    
