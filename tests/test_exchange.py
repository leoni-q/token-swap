import brownie

from contants import DECIMALS


def test_exchange_tokens_from_a_to_b(token_swap, alicecoin, bobcoin, owner, user):
    # given
    bobcoin.approve(token_swap.address, 500 * 10 ** DECIMALS, {'from': owner})
    token_swap.deposit(bobcoin.address, 500 * 10 ** DECIMALS, {'from': owner})
    alicecoin.transfer(user, 1000 * 10 ** DECIMALS, {'from': owner})
    alicecoin.approve(token_swap.address, 200 * 10 ** DECIMALS, {'from': user})

    # when
    token_swap.exchange(alicecoin.address, 200 * 10 ** DECIMALS, {'from': user})

    # then
    assert bobcoin.balanceOf(token_swap.address) == 100 * 10 ** DECIMALS
    assert bobcoin.balanceOf(user) == 400 * 10 ** DECIMALS
    assert alicecoin.balanceOf(owner) == 200 * 10 ** DECIMALS
    assert alicecoin.balanceOf(user) == 800 * 10 ** DECIMALS


def test_exchange_tokens_from_b_to_a(token_swap, alicecoin, bobcoin, owner, user):
    # given
    alicecoin.approve(token_swap.address, 500 * 10 ** DECIMALS, {'from': owner})
    token_swap.deposit(alicecoin.address, 500 * 10 ** DECIMALS, {'from': owner})
    bobcoin.transfer(user, 1000 * 10 ** DECIMALS, {'from': owner})
    bobcoin.approve(token_swap.address, 200 * 10 ** DECIMALS, {'from': user})

    # when
    token_swap.exchange(bobcoin.address, 200 * 10 ** DECIMALS, {'from': user})

    # then
    assert alicecoin.balanceOf(token_swap.address) == 400 * 10 ** DECIMALS
    assert alicecoin.balanceOf(user) == 100 * 10 ** DECIMALS
    assert bobcoin.balanceOf(owner) == 200 * 10 ** DECIMALS
    assert bobcoin.balanceOf(user) == 800 * 10 ** DECIMALS


def test_do_not_exchange_tokens_when_there_are_not_enough_tokens_in_deposit(token_swap, alicecoin, bobcoin, owner, user):
    # given
    bobcoin.approve(token_swap.address, 100 * 10 ** DECIMALS, {'from': owner})
    token_swap.deposit(bobcoin.address, 100 * 10 ** DECIMALS, {'from': owner})
    alicecoin.transfer(user, 1000 * 10 ** DECIMALS, {'from': owner})
    alicecoin.approve(token_swap.address, 200 * 10 ** DECIMALS, {'from': user})

    # then
    with brownie.reverts("there are not enough tokens to exchange in deposit"):
        token_swap.exchange(alicecoin.address, 200 * 10 ** DECIMALS, {'from': user})


def test_do_not_exchange_tokens_when_user_allowance_is_too_low(token_swap, alicecoin, bobcoin, owner, user):
    # given
    alicecoin.transfer(user, 1000 * 10 ** DECIMALS, {'from': owner})

    # then
    with brownie.reverts("sender allowance for the contract is too low"):
        token_swap.exchange(alicecoin.address, 200 * 10 ** DECIMALS, {'from': user})


def test_do_not_exchange_tokens_from_unknown_address(token_swap, alicecoin, bobcoin, owner, user):
    # given
    alicecoin.transfer(user, 1000 * 10 ** DECIMALS, {'from': owner})

    # then
    with brownie.reverts("_address param must represent either tokenA or tokenB address from TokenSwap contract"):
        token_swap.exchange("0xB0Be3cD57f107D45DCF47bDF07ffe5b8d27801D6", 200 * 10 ** DECIMALS, {'from': user})
