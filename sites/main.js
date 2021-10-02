Moralis.initialize("52J3xHioTTD7fFGY2uzfzIIyiDOY2LdIGBxwvS1k");
Moralis.serverURL = "https://xe310qxqdkva.moralishost.com:2053/server";
const CONTRACT_ADDRESS = "0xd6ef29f51f57b2d231fbcc79e825372d39367e76";

function fetchNFTMetadata(NFTs) {
    let promises = [];
    for (let i = 0; i < NFTs.length; i++) {
        let nft = NFTs[i];
        let id = nft.token_id;
        //Call Moralis Cloud Function -> Static JSON FILE
        promises.push(fetch("https://xe310qxqdkva.moralishost.com:2053/server/functions/getNFT?_ApplicationId=52J3xHioTTD7fFGY2uzfzIIyiDOY2LdIGBxwvS1k=" + id)
        .then(res => res.json())
        .then(res => {if (typeof res.result !== 'undefined') JSON.parse(res.result)}) 
        .then(res => {(res) ? nft.metadata = res : null})
        .then(res => {
            const options = { address: CONTRACT_ADDRESS, token_id : id, chain: "rinkeby" };
            return Moralis.Web3API.token.getTokenIdOwners(options)
        })
        .then( (res) => {
            nft.owners = [];
            res.result.forEach(element => {
                nft.owners.push(element.ownerOf);
            });

            return nft;
        }))
        
    }
    return Promise.all(promises);
}

function renderInventory(NFTs) {
    const parent = document.getElementById("app");
    for (let i = 0; i < NFTs.length; i++) {
        const nft1 = NFTs[i];
        if(nft1.metadata != null) {
            const nft = JSON.parse(nft1.metadata);
        
            let ipfsImg = nft.image.split('//')[1];
            ipfsImg = "https://ipfs.io/ipfs/"+ipfsImg;
            //console.log();
            //https://ipfs.io/ipfs/QmPyiSrA7Arv2oyuT3U7kx9RX3FES1B6qdhcGqi3iCHYkm
            let htmlString = `
            
            <div class="card">
                <img class="card-img-top" src="${ipfsImg}" alt="Card image cap">
                <div class="card-body" style="margin-top: 25px;">
                    <h5 class="card-title">${nft.name}</h5>
                    <p class="card-text">${nft.description}</p>
                    <p class="card-text">Tokens in circulation: ${nft1.amount}</p>
                    <p class="card-text">Number of Owners: ${nft1.owners.length}</p>
                    <a href="https://testnets.opensea.io/account" class="btn btn-primary">See Details</a>
                </div>
            </div>
            `
            let col = document.createElement("div");
            col.className = "col col-md-3"
            col.innerHTML = htmlString;
            parent.appendChild(col);
        }
    }
}

async function initializeApp() {
    let currentUser = Moralis.User.current();
    console.log(currentUser);
    if(!currentUser) {
        currentUser = await Moralis.Web3.authenticate();
    }
    const options = { address: CONTRACT_ADDRESS, chain: "rinkeby" }
    console.log(options);
    //let NFTs = await Moralis.Web3API.token.getAllTokenIds(options);
    const NFTs = await Moralis.Web3API.token.getAllTokenIds(options);
    let NFTWithMetadata = await fetchNFTMetadata(NFTs.result);
    console.log(NFTWithMetadata);
    renderInventory(NFTWithMetadata);
}

initializeApp();


