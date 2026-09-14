from otter.test_files import test_case

OK_FORMAT = False

name = "q5"
points = 4

@test_case(points=None, hidden=False)
def test_dtw_basics(dtw_distance, lp_distance, a, b, c, man_ab, man_ac, dtw_ab, dtw_ac):
    import numpy as np
    assert abs(dtw_distance(a, a)) < 1e-12, 'DTW of a series with itself is 0'
    assert abs(dtw_distance([1, 1, 2, 2, 3], [1, 2, 3, 3, 3]) - 0.0) < 1e-12, 'the lecture example aligns perfectly'
    assert dtw_ab <= man_ab + 1e-09 and dtw_ac <= man_ac + 1e-09, 'DTW can never exceed Manhattan'
    assert man_ac < man_ab, 'on the raw index Manhattan should prefer c'
    assert dtw_ab < dtw_ac, 'after warping, b (the shifted bump) should be closer to a than c is'

