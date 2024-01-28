import pytest
from critical_power import fit_intervals_icu

def test_fit_intervals_icu() -> None:
    '''
    Test the fit_intervals_icu function.
    '''
    with pytest.raises(Exception):
        fit_intervals_icu('tests/data/intervals.icu.csv')
