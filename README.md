## About

This repository contains TokenSwap contract which can be used to exchange two ERC20 tokens (18-decimals)
for given price.

## Prerequisites

Please install or have installed the following:

- [docker](https://docs.docker.com/get-docker/)
- [python](https://www.python.org/downloads/)

## Installation

1. Install requirements

```bash
pip install -r requirements.txt
```

2. Run ganache in docker

```bash
docker-compose -up
```

## Tests

```bash
brownie test
```
