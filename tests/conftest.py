import pytest
from brownie import accounts

from contants import DECIMALS


@pytest.fixture(autouse=True)
def isolate(fn_isolation):
    pass


@pytest.fixture(scope="module")
def owner():
    return accounts[0]


@pytest.fixture(scope="module")
def user():
    return accounts[1]


@pytest.fixture(scope="module")
def alicecoin(ERC20Token, owner):
    return ERC20Token.deploy("TokenA", 1000 * 10 ** DECIMALS, {'from': owner})


@pytest.fixture(scope="module")
def bobcoin(ERC20Token, owner):
    return ERC20Token.deploy("TokenB", 1000 * 10 ** DECIMALS, {'from': owner})
