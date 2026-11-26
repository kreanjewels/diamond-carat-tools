# Diamond inventory calculators

Run these commands with Python 3 from the repository directory. Use the same measurement unit for both dimensions.

| Command | Result |
|---|---|
| `python inventory.py total-weight 1.25 0.35` | 1.60 ct total |
| `python inventory.py price-per-carat 900 1.50` | 600.00 per ct in the input currency |
| `python inventory.py ratio 9 6` | 1.500 length-to-width ratio |
| `python inventory.py depth-percent 4 6` | 66.67% depth relative to width |

For depth percentage, use the reference width or diameter appropriate to your reporting convention.
