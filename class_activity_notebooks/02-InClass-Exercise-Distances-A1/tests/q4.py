from otter.test_files import test_case

OK_FORMAT = False

name = "q4"
points = 5

@test_case(points=None, hidden=False)
def test_scaler_is_fitted_and_matches(scaler, err_scaler, X):
    import numpy as np
    assert hasattr(scaler, 'mean_'), 'scaler must be a FITTED StandardScaler (call .fit(X))'
    assert np.allclose(scaler.mean_, X.mean(axis=0)) and np.allclose(scaler.scale_, X.std(axis=0))
    assert err_scaler < 1e-09, "sklearn's StandardScaler should reproduce your hand standardization"

@test_case(points=None, hidden=False)
def test_pipeline_matches_hand(pipe, nn_pipe, nn_std):
    from sklearn.pipeline import Pipeline
    assert isinstance(pipe, Pipeline), 'pipe must be a sklearn Pipeline'
    assert list(pipe.named_steps) == ['scale', 'nn'], "steps must be named 'scale' then 'nn'"
    assert list(nn_pipe) == list(nn_std), 'the pipeline should reproduce your Part 3 neighbors'

