from otter.test_files import test_case

OK_FORMAT = False

name = "q3"
points = 2

@test_case(points=None, hidden=False)
def test_inspect_format(n_rows, n_cols, n_missing_age, value_col_mean):
    assert isinstance(n_rows, int) and isinstance(n_cols, int), 'n_rows and n_cols must be ints'
    assert isinstance(n_missing_age, int), 'n_missing_age must be an int'
    assert isinstance(value_col_mean, float), 'value_col_mean must be a float'
    assert n_rows == 891 and n_cols == 12, 'check df.shape'
    assert 0 < n_missing_age < n_rows, 'some — not all, not none — ages are missing'

