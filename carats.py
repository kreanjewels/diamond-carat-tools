"""Run python carats.py 2.50 to convert carats to milligrams."""
import argparse
from decimal import Decimal, InvalidOperation


def milligrams(carats):
    weight = Decimal(carats)
    if not weight.is_finite() or weight < 0:
        raise ValueError("weight must be finite and nonnegative")
    return weight * 200


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("carats")
    args = parser.parse_args()
    try:
        print(f"{milligrams(args.carats):f} mg")
    except (InvalidOperation, ValueError) as error:
        parser.error(str(error))
