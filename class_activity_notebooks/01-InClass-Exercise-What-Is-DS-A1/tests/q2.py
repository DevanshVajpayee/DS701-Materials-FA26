from otter.test_files import test_case

OK_FORMAT = False

name = "q2"
points = 2

@test_case(points=None, hidden=False)
def test_type_error_format(asked, answered, TYPES):
    assert asked in TYPES, 'asked must be one of the six types'
    assert answered in TYPES, 'answered must be one of the six types'
    assert asked != answered, 'if the two were the same there would be no type error'

