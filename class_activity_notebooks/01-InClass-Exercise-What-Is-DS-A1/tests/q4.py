from otter.test_files import test_case

OK_FORMAT = False

name = "q4"
points = 2

@test_case(points=None, hidden=False)
def test_filter_format(subset, n_subset, subset_survival_rate, df):
    import pandas as pd
    assert isinstance(subset, pd.DataFrame), 'subset must be a DataFrame (rows of df)'
    assert list(subset.columns) == list(df.columns), 'keep all the columns; only filter rows'
    assert isinstance(n_subset, int) and n_subset == len(subset)
    assert 0 < n_subset < len(df), 'the filter should keep some rows and drop some'
    assert isinstance(subset_survival_rate, float) and 0.0 <= subset_survival_rate <= 1.0

