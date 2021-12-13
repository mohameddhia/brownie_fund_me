from brownie import FundMe, MockV3Aggregator, network, config
from scripts.helpful_scripts import (
    deploy_mocks,
    get_account,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)


# if we are on a persistent network like rinkeby use this address 0x78F9e60608bF48a1155b4B2A5e31F32318a1d85F
# otherwise deploy mocks
def deploy_fund_me():
    account = get_account()
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )

    print(f"Contract deployed to {fund_me.address}")
    return fund_me


def main():
    deploy_fund_me()
