import numpy as np

def r2_score(y_true, y_pred) -> float:
    """
    Compute R² (coefficient of determination) for 1D regression.
    Handle the constant-target edge case:
      - return 1.0 if predictions match exactly,
      - else 0.0.
    """
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    mean_value = np.mean(y_true)
    explained_variance = np.sum(np.square(y_true - mean_value))
    unexplained_variance = np.sum(np.square(y_true - y_pred))

    if np.array_equal(y_true,y_pred) != False:
        return 1.0
    elif explained_variance == 0:
        return 0
    else:
        return  1 - (unexplained_variance / explained_variance)
    
    pass