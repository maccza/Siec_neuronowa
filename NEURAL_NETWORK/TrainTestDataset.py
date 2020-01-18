import torch


class DataSet:
    def __init__(self, train_size, x_train_scale, y_train_type, test_size, y_test_type):
        self.tr_size = train_size
        self.x_tr_sc = x_train_scale
        self.y_tr_tp = y_train_type
        self.te_size = test_size
        self.y_te_tp = y_test_type

    @property
    def x_train(self):
        _x_train = torch.rand(self.tr_size)
        _x_train = _x_train * self.x_tr_sc[0] + self.x_tr_sc[1] - self.x_tr_sc[2]
        _x_train = _x_train.unsqueeze_(1)
        return _x_train

    @property
    def y_train(self):
        if self.y_tr_tp is 'Sin':
            _y_train = torch.sin(self.x_train)
        elif self.y_tr_tp is 'Cos':
            _y_train = torch.cos(self.x_train)
        elif self.y_tr_tp is 'Tan':
            _y_train = torch.tan(self.x_train)
        noise = torch.randn(_y_train.shape) / 5.
        _y_train = _y_train + noise
        return _y_train

    @property
    def x_test(self):
        _x_test = torch.linspace(min(self.x_train), max(self.x_train), self.te_size)
        _x_test = _x_test.unsqueeze_(1)
        return _x_test

    @property
    def y_test(self):
        if self.y_te_tp is 'Sin':
            _y_test = torch.sin(self.x_test)
        elif self.y_te_tp is 'Cos':
            _y_test = torch.cos(self.x_test)
        elif self.y_te_tp is 'Tan':
            _y_test = torch.tan(self.x_test)
        return _y_test