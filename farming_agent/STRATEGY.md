# Kaggriculture — Strategy Notes

## Economic analysis (from rules; verify against engine source)

### Price glut behavior (how much can we sell before price crashes)
price(inv) = base − amp·f(inv − I0) on the glut side, amp = above_target·base/f(T)

| Product | Base | Above func/target | Approx. units to $1 floor | Notes |
|---|---|---|---|---|
| WHEAT | 25 | log 0.20 | never (≈$17 even at +10k) | infinite-scale staple |
| EGG | 50 | log 0.20 | never (≈$35–40 at huge glut) | infinite-scale staple |
| CARROT | 35 | sqrt 0.70 | ~870 | large capacity |
| TOMATO | 60 | sqrt 0.60 | ~2000+ | large capacity |
| FERTILIZER | 100 | linear 0.40 | ~495 | good sink for animal fert |
| MILK | 160 | linear 1.60 | ~76 | tiny capacity ≈ $6k total |
| STRAWBERRY | 120 | linear 1.60 | ~52 | tiny capacity |
| WOOL | 200 | sq 3.20 | ~59 | ≈$8k total |
| MELON | 250 | sq 3.60 | ~158 | ≈$26k total, big early prize |

Town consumption regenerates headroom (esp. shops: wheat/egg-heavy shops are common).
Opponent selling the same product eats shared capacity — sell premium products EARLY.

### Per-tile-day profitability (base prices)
- Melon: 6 units × $250 / 11 occupied days − seed 80 ≈ $125/tile/day — best until glut (~158 units market-wide).
- Goose/egg: 1 egg/day ≈ $40–50 forever, +1 fertilizer/day (~$60–100), −1 wheat feed (~$20 opportunity). Net ≈ $80–120/tile/day steady state. Payback of $300+ in ~4–6 days. THE core late engine. Also glut-proof.
- Wheat: ~4 units/5 days × ~$20 ≈ $14/tile/day (fertilized: 6 units ≈ $22). Needed as animal feed anyway.
- Carrot: ~$20–26/tile/day until glut.
- Cow/Sheep: capped total extraction (~$6–8k each), a handful only, early.
- Strawberry/Tomato: weak per-day, tomato OK as filler (large market capacity, hinge scarcity side can spike with pizza shops).

### Action budget
24 turns/day/unit. Watering a tile costs ~2 actions (move+water). 100 tiles ⇒ ~9 units for watering alone. Hand hire cost = fib: 13 hands/day ≈ 609 coins — trivial vs income. Hands spawn at shed, vanish at end of day (inventory auto-dropped to shed).

### Capital plan (start $3000)
1. Day 0: buy NE land ($1000) early (also unlocks hand spawn tile 5,4), plant melons (~10 × $80) + wheat/carrots with the rest. Hire ~4–6 hands immediately.
2. Days 1–8: scale planting; buy SW ($2000) then SE ($4000) as cash allows. Start geese ASAP (300 each + coop build).
3. Mid game: convert most tiles to geese (eggs+fertilizer are glut-proof); keep 1–2 quadrants wheat (feed + sales); a few cows/sheep/strawberries up to their market caps; fertilize wheat/melon via animal fertilizer.
4. Sell: melons/milk/wool/strawberry with price floors (stop selling below threshold, wait for town regen); wheat/eggs continuously; keep shed <100.
5. Endgame: stop planting anything that can't mature (melon by day ~19, wheat by day ~25); last day(s) dump ALL inventory; don't waste feed wheat on final day if production won't land (yield ticks at end of day — check engine).

## Key rules gotchas
- New plant starts consecutive_unwatered=1 ⇒ MUST water same day it's planted.
- Animals: consecutive_unfed=0 on placement; escape after 2 unfed days.
- PLANT with insufficient seeds for simultaneous plants ⇒ ALL fail. Coordinate.
- Shed cap 100 non-seed items; overflow discarded at end-of-day. Sell aggressively.
- Max 10 market orders/turn.
- Buy price quoted post-buy, sell price pre-sell (no arbitrage).
- Hands spawn NWSE adjacent to shed; first spawn tile (5,4) is in NE quadrant (locked until bought) but passable.
- CARE: banks +1/day (if fed+cared) paid on next production tick — good for cows/sheep (multi-day intervals), marginal for geese (daily prod, extra action/day for +1 egg/day... actually CARE costs 1 action and yields +1 egg = same as harvest value; do it when idle).

## Roadmap
1. v0: read engine source, verify all above numbers/mechanics.
2. v1: scheduler agent (job list → greedy assignment → move/act), wheat+melon+geese plan.
3. Simulate vs "starter" baseline and self-play; tune crop mix, land timing, hand count.
4. Submit, monitor episodes, iterate against real opponents' replays.
