from brownie import TokenSwap


def test_initialize_contract_with_proper_values(alicecoin, bobcoin, owner):
    # given
    initial_price = 1

    # when
    token_swap = TokenSwap.deploy(alicecoin, bobcoin, initial_price, {'from': owner})

    # then
    assert token_swap.tokenA() == alicecoin.address
    assert token_swap.tokenB() == bobcoin.address
    assert token_swap.price() == 1
    assert token_swap.owner() == owner
