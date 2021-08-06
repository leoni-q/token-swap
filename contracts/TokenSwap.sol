pragma solidity ^0.8.0;

import "@openzeppelin/contracts/access/Ownable.sol";


contract TokenSwap is Ownable {

    address public tokenA;
    address public tokenB;
    uint256 public price;

    /// @param _tokenA is an address of the first token to swap
    /// @param _tokenB is an address of the second token to swap
    /// @param _price is an exchange rate for tokens (how much tokenB we will get for 1 tokenA)
    constructor(address _tokenA, address _tokenB, uint256 _price) {
        tokenA = _tokenA;
        tokenB = _tokenB;
        price = _price;
    }

    function updatePrice(uint256 _price) external onlyOwner {
        price = _price;
    }
}
