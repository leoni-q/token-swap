pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";


contract ERC20Token is ERC20 {

    constructor(string memory _name, uint256 _supply) ERC20("a", "TKN") {
        _mint(msg.sender, _supply);
    }

}
