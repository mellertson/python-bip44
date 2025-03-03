from typing import Tuple

from bip32 import HARDENED_INDEX

__all__ = ("COIN_PATHS",)


def coin_path_by_index(index: int = 0) -> Tuple[int, int]:
    # Full list is at https://github.com/satoshilabs/slips/blob/master/slip-0044.md#registered-coin-types
    return (44 + HARDENED_INDEX, index + HARDENED_INDEX)

def graphene_coin_path_by_index(index: int) -> Tuple[int, int]:
    # Full list is at https://github.com/satoshilabs/slips/blob/master/slip-0048.md#registered-networks
    return (48 + HARDENED_INDEX, index + HARDENED_INDEX)


GRAPHENE_COIN_INDICES = [5000]

COIN_PATHS = {
    "BTC": coin_path_by_index(),
    "TESTNET": coin_path_by_index(1),
    "LTC": coin_path_by_index(2),
    "DOGE": coin_path_by_index(3),
    "ETH": coin_path_by_index(60),
    "ETC": coin_path_by_index(61),
    "DOT": coin_path_by_index(354),
    "SDN": coin_path_by_index(809),
    "ASTR": coin_path_by_index(810),
    "ADA": coin_path_by_index(1815),
    "V12": graphene_coin_path_by_index(5000),
}
