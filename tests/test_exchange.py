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
