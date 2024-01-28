'''
Critical power calculation.
'''

import argparse
import pandas as pd
from scipy.optimize import curve_fit


TIME_LOWER_BOUND = 180
TIME_UPPER_BOUND = 1200

def power(time, critical_power, watt_prime) -> float:
    '''
    Calculate the critical power.
    '''
    return critical_power + (watt_prime / time)


def fit_intervals_icu(csv_path: str, plot: bool=False) -> None:
    '''
    Fit the intervals.icu power curve.
    '''
    if plot:
        try:
            import matplotlib.pyplot as plt
        except ImportError:
            print('Matplotlib not installed. Cannot plot.')
            plot = False
    with open(csv_path, 'r') as csv_file:
        df = pd.read_csv(csv_file, index_col='secs')
    roi = slice(TIME_LOWER_BOUND, TIME_UPPER_BOUND)
    if plot:
        fig, ax = plt.subplots()
    for idx, column in enumerate(df.columns):
        p_opt, p_cov = curve_fit(
            power,
            df.loc[roi].index,
            df.loc[roi, column],
            p0=[200, 1.5e4],
        )
        if plot:
            ax.plot(
                df.index,
                df[column],
                'o',
                label=column,
                color=f'C{idx}',
                alpha=0.5,
            )
            ax.plot(
                [df.index[0], df.index[-1]],
                [p_opt[0], p_opt[0]],
                '--',
                label=f'CP={p_opt[0]:.0f} W',
                color=f'C{idx}',
            )
            ax.plot(
                df.loc[roi].index,
                power(df.loc[roi].index, *p_opt),
                label=f'W\'={p_opt[1] * 1e-3:.1f} kJ',
                color=f'C{idx}',
            )
        print(f'{column}: CP={p_opt[0]:.0f} W, W\'={p_opt[1] * 1e-3:.1f} kJ')
    if plot:
        ax.set_xscale('log')
        plt.grid()
        plt.legend()
        plt.show()


def main() -> None:
    '''
    Main function for running the critical power fitting.
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'csv_path',
        help='The path to the CSV export of the intervals.icu power curve.',
    )
    parser.add_argument(
        '-p',
        '--plot',
        action='store_true',
        help='Plot the power curve.',
    )
    args = parser.parse_args()
    fit_intervals_icu(
        csv_path=args.csv_path,
        plot=args.plot,
    )


if __name__ == "__main__":
    main()
