import brownie
from brownie import TokenSwap

from contants import DECIMALS


def test_deposit_tokens_when_has_exact_allowance(alicecoin, bobcoin, owner):
    # given
    amount_to_deposit = 500 * 10 ** DECIMALS
    token_swap = TokenSwap.deploy(alicecoin, bobcoin, 1, {'from': owner})
    alicecoin.approve(token_swap.address, amount_to_deposit, {'from': owner})

    # when
    token_swap.deposit(alicecoin.address, amount_to_deposit, {'from': owner})

    # then
    assert alicecoin.balanceOf(token_swap.address) == amount_to_deposit


def test_deposit_tokens_when_allowance_is_higher_then_amount_to_deposit(alicecoin, bobcoin, owner):
    # given
    amount_to_deposit = 500 * 10 ** DECIMALS
    token_swap = TokenSwap.deploy(alicecoin, bobcoin, 1, {'from': owner})
    alicecoin.approve(token_swap.address, amount_to_deposit + 1000, {'from': owner})

    # when
    token_swap.deposit(alicecoin.address, amount_to_deposit, {'from': owner})

    # then
    assert alicecoin.balanceOf(token_swap.address) == amount_to_deposit


def test_do_not_deposit_tokens_when_call_function_as_not_owner(alicecoin, bobcoin, owner, user):
    # given
    token_swap = TokenSwap.deploy(alicecoin, bobcoin, 1, {'from': owner})

    # then
    with brownie.reverts("Ownable: caller is not the owner"):
        token_swap.deposit(alicecoin.address, 1, {'from': user})


def test_do_not_deposit_tokens_to_unknown_address(alicecoin, bobcoin, owner):
    # given
    token_swap = TokenSwap.deploy(alicecoin, bobcoin, 1, {'from': owner})

    # then
    with brownie.reverts("_address param must represent either tokenA or tokenB address from TokenSwap contract"):
        token_swap.deposit("0xB0Be3cD57f107D45DCF47bDF07ffe5b8d27801D6", 1, {'from': owner})


def test_do_not_deposit_tokens_when_allowance_is_to_low(alicecoin, bobcoin, owner):
    # given
    amount_to_deposit = 500 * 10 ** DECIMALS
    token_swap = TokenSwap.deploy(alicecoin, bobcoin, 1, {'from': owner})
    alicecoin.approve(token_swap.address, amount_to_deposit - 1000, {'from': owner})

    # when
    with brownie.reverts("sender allowance for the contract is too low"):
        token_swap.deposit(alicecoin.address, amount_to_deposit, {'from': owner})
