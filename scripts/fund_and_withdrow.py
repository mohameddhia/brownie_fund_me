from brownie import FundMe
from scripts.helpful_scripts import get_account


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee() + 50
    print(entrance_fee)
    print(f"the current fee is {entrance_fee}")
    print("funding ...")
    fund_me.fund({"from": account, "value": entrance_fee})


def withdrow():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdrow({"from": account})


def main():
    fund()
    withdrow()
