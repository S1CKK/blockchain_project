const SHA256 = require('crypto-js/sha256');
class Block{
    constructor(index,timestamp,data,previousHash = ''){
        this.index = index;
        this.timestamp = timestamp;
        this.data = data;
        this.previousHash = previousHash;
        this.hash = this.calculateHash();
    }

    calculateHash(){
        return SHA256(this.index + this.previousHash + this.timestamp + JSON.stringify(this.data)).toString();
    }
}

class Blockchain{
    constructor(){
        this.chain = [this.creatGenesisBlock()];
    }

    creatGenesisBlock(){
        return new Block(0,"02/11/2020","This is Genesis Block","0");
    }

    getLatestBlock(){
        return this.chain[this.chain.length - 1];
    }
    
    addBlock(newBlock){
        newBlock.previousHash = this.getLatestBlock().hash;
        newBlock.hash = newBlock.calculateHash();
        this.chain.push(newBlock);
    }

    isChainValid(){
        for(let i =1; i< this.chain.length; i++){
            const currentBlock = this.chain[i];
            const previousBlock = this.chain[i-1];

            if(currentBlock.hash != currentBlock.calculateHash()){
                return false;
            }
            if (currentBlock.previousHash !== previousBlock.hash){
                return false;
            }
        }
        return true;
    }
}

let test = new Blockchain();
test.addBlock(new Block(1,"10/10/2022",{day:"1",rank1:"BRU", rank2: "PSG", rank3: "BAC"}));
test.addBlock(new Block(2,"10/11/2022",{day:"2",rank1:"BRU" , rank2: "BAC", rank3: "KTN"}));
test.addBlock(new Block(3,"10/11/2022",{day:"3",rank1:"BRU" , rank2: "BAC", rank3: "KOG"}));


//console.log('Is blockchain valid? '+test.isChainValid())

//test.chain[2].data = {rank1:"ART"};
//console.log('Is blockchain valid? '+test.isChainValid())
console.log(JSON.stringify(test,null,4));