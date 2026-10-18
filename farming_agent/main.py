"""Kaggriculture agent — scheduler-based economy bot.

Architecture:
  - Parse observation into a State.
  - Market layer: land purchases, hiring, seed purchases, price-aware selling.
  - Job layer: enumerate tile jobs (water/feed/harvest/plant/build/place/fertilize/
    care/collect/dig) with priorities.
  - Assignment: greedy nearest-unit matching; units move Manhattan-style (no obstacles).
"""

CROPS = {
    # crop: (seed_cost, base_price, first_yield_day, max_yield_day, ongoing)
    "WHEAT": (10, 25, 2, 4, False),
    "CARROT": (20, 35, 2, 3, False),
    "TOMATO": (50, 60, 8, 11, True),
    "STRAWBERRY": (100, 120, 10, 16, True),
    "MELON": (80, 250, 10, 10, False),
}

ANIMALS = {
    # animal: (cost, product, structure, prod_interval_days)
    "GOOSE": (300, "EGG", "COOP", 1),
    "COW": (400, "MILK", "PASTURE", 2),
    "SHEEP": (500, "WOOL", "PASTURE", 3),
}

# Sell price floors: don't sell below these (wait for town demand to regen), except endgame.
SELL_FLOOR = {
    "WHEAT": 12, "CARROT": 15, "TOMATO": 25, "STRAWBERRY": 40,
    "MELON": 60, "EGG": 25, "MILK": 50, "WOOL": 60, "FERTILIZER": 40,
}

QUADRANT_ORDER = ["NE", "SW", "SE"]  # NW is free


def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def step_toward(src, dst):
    """One-step move op from src toward dst, x first."""
    if src[0] < dst[0]:
        return "EAST"
    if src[0] > dst[0]:
        return "WEST"
    if src[1] < dst[1]:
        return "SOUTH"
    if src[1] > dst[1]:
        return "NORTH"
    return None


def agent(obs, config=None):
    # placeholder — replaced by full implementation
    return {"farmer": ["PASS"], "hands": [], "market": []}
