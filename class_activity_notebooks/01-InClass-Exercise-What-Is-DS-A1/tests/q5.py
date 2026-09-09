from otter.test_files import test_case

OK_FORMAT = False

name = "q5"
points = 3

@test_case(points=None, hidden=False)
def test_groupby_format(by_group, survival_by_group, top_group, GROUP_COL, df):
    import pandas as pd
    assert isinstance(by_group, pd.DataFrame), 'by_group should be a DataFrame (two aggregates)'
    assert {'mean', 'count'} <= set(by_group.columns), "by_group needs 'mean' and 'count' columns"
    assert isinstance(survival_by_group, pd.Series), 'survival_by_group should be a Series'
    groups = set(df[GROUP_COL].unique())
    assert set(by_group.index) == groups, f'one row per value of {GROUP_COL}'
    assert set(survival_by_group.index) == groups
    assert top_group in groups, 'top_group must be one of the group labels'
    assert int(by_group['count'].sum()) <= len(df)

