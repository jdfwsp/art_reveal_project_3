pragma solidity ^0.5.0;
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/drafts/Counters.sol";
contract Proud_Patriot is ERC721Full {
    constructor() ERC721Full("PATRIOT", "PP") public { }
    using Counters for Counters.Counter;
    Counters.Counter token_ids;
    struct Nft_image {
        string description;
        uint copy;
    
    }
    mapping(uint => Nft_image) public art;
    event Itemsold(uint token_id, string report_uri);
    function registerArt(address owner, string memory description, string memory token_uri) public returns(uint) {
        token_ids.increment();
        uint token_id = token_ids.current();
        _mint(owner, token_id);
        _setTokenURI(token_id, token_uri);
        art[token_id] = Nft_image(description, 0);
        return token_id;
    }
    function reportArtsale(uint token_id, string memory report_uri) public returns(uint) {
        art[token_id].copy += 1;
        emit Itemsold(token_id, report_uri);
        return art[token_id].copy;
    }
}

