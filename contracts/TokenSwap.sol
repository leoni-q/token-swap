pragma solidity ^0.8.0;

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title
 *  TokenSwap
 * @notice
 *  TokenSwap is a contract that can be used to exchange two ERC20 tokens for a price set on the contract.
 *  Price can be updated only by the owner of the contract.
 *  Tokens to exchange can be deposited only by the owner of the contract.
 *  Anyone can invoke the exchange method to swap one token for another.
 */
contract TokenSwap is Ownable {

    address public tokenA;
    address public tokenB;
    uint256 public price;

    /**
     * @param _tokenA The address of the first ERC20 token to swap.
     * @param _tokenB The address of the second ERC20 token to swap.
     * @param _price The exchange rate for tokens (how much tokenB will be taken for 1 tokenA).
     */
    constructor(address _tokenA, address _tokenB, uint256 _price) {
        tokenA = _tokenA;
        tokenB = _tokenB;
        price = _price;
    }

    /**
     * @notice
     *  Used to deposit tokens on the contract.
     *
     *  This may only be called by the owner of the contract.
     * @param _address The address of ERC20 token to deposit tokens to. Must be either tokenA or tokenB address.
     * @param _amount The amount of tokens to deposit.
     */
    function deposit(address _address, uint256 _amount) external onlyOwner validateAddress(_address) validateAllowance(_address, _amount) {
        require(IERC20(_address).transferFrom(msg.sender, address(this), _amount), "deposit failed");
    }

    /**
     * @notice
     *  Used to exchange tokenA for tokenB or otherwise.
     *
     *  This may be called by anyone.
     * @param _address The address of ERC20 token which we want to exchange. Must be either tokenA or tokenB address.
     * @param _amount The amount of tokens to exchange.
     */
    function exchange(address _address, uint256 _amount) external validateAddress(_address) validateAllowance(_address, _amount) {
        if (_address == tokenA) {
            uint256 tokenB_amount_to_exchange = _amount * price;
            require(IERC20(tokenB).balanceOf(address(this)) >= tokenB_amount_to_exchange, "there are not enough tokens to exchange in deposit");
            require(IERC20(tokenA).transferFrom(msg.sender, owner(), _amount), "exchange failed");
            require(IERC20(tokenB).transfer(msg.sender, tokenB_amount_to_exchange), "exchange failed");
        } else {
            uint256 tokenA_amount_to_exchange = _amount / price;
            require(IERC20(tokenA).balanceOf(address(this)) >= tokenA_amount_to_exchange, "there are not enough tokens to exchange in deposit");
            require(IERC20(tokenB).transferFrom(msg.sender, owner(), _amount), "exchange failed");
            require(IERC20(tokenA).transfer(msg.sender, tokenA_amount_to_exchange), "exchange failed");
        }
    }

    /**
     * @notice
     *  Used to update price (exchange rate) for tokens.
     *
     *  This may only be called by the owner of the contract.
     * @param _price The price we want to set.
     */
    function updatePrice(uint256 _price) external onlyOwner {
        price = _price;
    }

    modifier validateAddress(address _address) {
        require(_address == tokenA || _address == tokenB, "_address param must represent either tokenA or tokenB address from TokenSwap contract");
        _;
    }

    modifier validateAllowance(address _address, uint256 _amount) {
        require(IERC20(_address).allowance(msg.sender, address(this)) >= _amount, "sender allowance for the contract is too low");
        _;
    }
}
