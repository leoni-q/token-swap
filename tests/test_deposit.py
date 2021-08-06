import brownie

from contants import DECIMALS


def test_deposit_tokens_when_has_exact_allowance(token_swap, alicecoin, owner):
    # given
    amount_to_deposit = 500 * 10 ** DECIMALS
    alicecoin.approve(token_swap.address, amount_to_deposit, {'from': owner})

    # when
    token_swap.deposit(alicecoin.address, amount_to_deposit, {'from': owner})

    # then
    assert alicecoin.balanceOf(token_swap.address) == amount_to_deposit


def test_deposit_tokens_when_allowance_is_higher_then_amount_to_deposit(token_swap, alicecoin, owner):
    # given
    amount_to_deposit = 500 * 10 ** DECIMALS
    alicecoin.approve(token_swap.address, amount_to_deposit + 1000, {'from': owner})

    # when
    token_swap.deposit(alicecoin.address, amount_to_deposit, {'from': owner})

    # then
    assert alicecoin.balanceOf(token_swap.address) == amount_to_deposit


def test_do_not_deposit_tokens_when_call_function_as_not_owner(token_swap, alicecoin, user):
    with brownie.reverts("Ownable: caller is not the owner"):
        token_swap.deposit(alicecoin.address, 1, {'from': user})


def test_do_not_deposit_tokens_to_unknown_address(token_swap, owner):
    with brownie.reverts("_address param must represent either tokenA or tokenB address from TokenSwap contract"):
        token_swap.deposit("0xB0Be3cD57f107D45DCF47bDF07ffe5b8d27801D6", 1, {'from': owner})


def test_do_not_deposit_tokens_when_allowance_is_to_low(token_swap, alicecoin, owner):
    # given
    amount_to_deposit = 500 * 10 ** DECIMALS
    alicecoin.approve(token_swap.address, amount_to_deposit - 1000, {'from': owner})

    # when
    with brownie.reverts("sender allowance for the contract is too low"):
        token_swap.deposit(alicecoin.address, amount_to_deposit, {'from': owner})
