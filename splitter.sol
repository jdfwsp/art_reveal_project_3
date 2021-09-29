

pragma solidity ^0.5.0;


library SafeMath {
  function mul(uint256 a, uint256 b) internal pure returns (uint256 c) {
    if (a == 0) {
      return 0;
    }
    c = a * b;
    assert(c / a == b);
    return c;
  }
  function div(uint256 a, uint256 b) internal pure returns (uint256) {
    assert(b > 0);
    return a / b;
  }
  function sub(uint256 a, uint256 b) internal pure returns (uint256) {
    assert(b <= a);
    return a - b;
  }
  function add(uint256 a, uint256 b) internal pure returns (uint256 c) {
    c = a + b;
    assert(c >= a);
    return c;
  }
}

contract splitter {
    
    uint public contractbalance;
    
    address payable[] fourpeople = [0xd5e9ddeF40A999C25E3B84134e94b2960461BAaE, 0x540375Ec8F949B5263840120eC1d06a498eE9b69, 0xda3f9De9142ccf4BbB3d8787754B31AF5eB2C274, 0xE8ED7a9A7D0e9d2Aad0f855CB3179B5D5B117e56];

    function deposit() public payable {
        contractbalance = SafeMath.add(contractbalance,msg.value);
    }
    
    function _split_() public payable {
        
        uint amount = SafeMath.div(address(this).balance, 4);
        
        contractbalance = SafeMath.sub(contractbalance,address(this).balance);
        
       fourpeople[0].transfer(amount);
       fourpeople[1].transfer(amount);
       fourpeople[2].transfer(amount);
       fourpeople[3].transfer(amount);
   
   
    }
    