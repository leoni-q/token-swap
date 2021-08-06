import brownie


def test_owner_should_be_able_to_update_price(token_swap, owner):
    # when
    token_swap.updatePrice(2, {'from': owner})

    # then
    assert token_swap.price() == 2


def test_should_throw_exception_when_call_update_price_as_not_owner(token_swap, user):
    with brownie.reverts("Ownable: caller is not the owner"):
        token_swap.updatePrice(2, {'from': user})
