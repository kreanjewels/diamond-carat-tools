"""Diamond inventory calculations using decimal arithmetic."""
import argparse
from decimal import Decimal, InvalidOperation


def positive(value):
    try:
        number = Decimal(value)
    except InvalidOperation:
        raise argparse.ArgumentTypeError("enter a decimal number") from None
    if not number.is_finite() or number <= 0:
        raise argparse.ArgumentTypeError("enter a finite number greater than zero")
    return number


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)

    total = commands.add_parser("total-weight", help="Sum individual stone weights")
    total.add_argument("weights", nargs="+", type=positive, metavar="CT")

    price = commands.add_parser("price-per-carat", help="Divide price by weight")
    price.add_argument("price", type=positive)
    price.add_argument("carats", type=positive)

    ratio = commands.add_parser("ratio", help="Calculate length-to-width ratio")
    ratio.add_argument("length", type=positive)
    ratio.add_argument("width", type=positive)

    depth = commands.add_parser("depth-percent", help="Calculate depth as a percentage of width")
    depth.add_argument("depth", type=positive)
    depth.add_argument("width", type=positive)

    args = parser.parse_args()
    if args.command == "total-weight":
        print(f"{sum(args.weights):f} ct total")
    elif args.command == "price-per-carat":
        print(f"{args.price / args.carats:.2f} per ct")
    elif args.command == "ratio":
        print(f"{args.length / args.width:.3f}")
    else:
        print(f"{args.depth / args.width * 100:.2f}%")


if __name__ == "__main__":
    main()
