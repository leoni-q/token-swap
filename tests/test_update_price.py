import brownie
from brownie import TokenSwap


def test_owner_should_be_able_to_update_price(alicecoin, bobcoin, owner):
    # given
    initial_price = 1
    token_swap = TokenSwap.deploy(alicecoin, bobcoin, initial_price, {'from': owner})

    # when
    token_swap.updatePrice(2, {'from': owner})

    # then
    assert token_swap.price() == 2


def test_should_throw_exception_when_call_update_price_as_not_owner(alicecoin, bobcoin, owner, user):
    # given
    initial_price = 1
    token_swap = TokenSwap.deploy(alicecoin, bobcoin, initial_price, {'from': owner})

    # then
    with brownie.reverts("Ownable: caller is not the owner"):
        token_swap.updatePrice(2, {'from': user})
