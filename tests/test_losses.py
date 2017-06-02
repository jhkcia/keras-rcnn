import numpy as np
import keras.backend as K
from keras_rcnn import losses


def test_rpn_classification():
    n_anchors = 9
    rpn_cls = losses.classification(n_anchors)
    y_pred = K.variable(0.5 * np.ones((1, 4, 4, n_anchors)))
    y_true = K.variable(np.ones((1, 4, 4, 2 * n_anchors)))
    expected_loss = - np.log(0.5)
    loss = K.eval(rpn_cls(y_true, y_pred))
    assert np.isclose(expected_loss, loss)


def test_rpn_regression():
    n_anchors = 9
    rpn_reg = losses.regression(n_anchors)
    y_pred = K.variable(0.5 * np.ones((1, 4, 4, 4 * n_anchors)))
    y_true = K.variable(np.ones((1, 4, 4, 8 * n_anchors)))
    expected_loss = np.power(0.5, 3)
    loss = K.eval(rpn_reg(y_true, y_pred))
    assert np.isclose(expected_loss, loss)
