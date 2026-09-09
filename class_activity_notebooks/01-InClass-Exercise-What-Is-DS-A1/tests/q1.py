from otter.test_files import test_case

OK_FORMAT = False

name = "q1"
points = 5

@test_case(points=None, hidden=False)
def test_classification_format(classification, TYPES, SCENARIOS):
    assert isinstance(classification, dict), 'classification must be a dict'
    missing = [n for n in SCENARIOS if n not in classification]
    assert not missing, f'scenarios not classified: {missing}'
    bad = {n: v for n, v in classification.items() if v not in TYPES}
    assert not bad, f'these values are not one of the six types in TYPES: {bad}'

