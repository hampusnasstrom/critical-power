'''
Critical power calculation.
'''

import argparse


def fit_intervals_icu(csv_path: str) -> None:
    '''
    Fit the intervals.icu power curve.
    '''
    raise NotImplementedError


def main() -> None:
    '''
    Main function for running the critical power fitting.
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'csv_path',
        help='The path to the CSV export of the intervals.icu power curve.',
    )
    args = parser.parse_args()
    fit_intervals_icu(
        csv_path=args.csv_path,
    )


if __name__ == "__main__":
    main()
