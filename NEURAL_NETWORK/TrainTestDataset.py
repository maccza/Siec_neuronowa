import torch


class DataSet:
    """
    Klasa, ktora tworzy zbior uczacy i testowy wedlug parametrow podanych w pliku XML.
    """

    def __init__(self, train_size, x_train_scale, y_train_type, test_size, y_test_type):
        self.tr_size = train_size
        self.x_tr_sc = x_train_scale
        self.y_tr_tp = y_train_type
        self.te_size = test_size
        self.y_te_tp = y_test_type

        self.x_trains()
        self.y_trains()
        self.x_tests()
        self.y_tests()

    def x_trains(self):
        _x_train = torch.rand(self.tr_size)
        _x_train = _x_train * self.x_tr_sc[0] + self.x_tr_sc[1] - self.x_tr_sc[2]
        _x_train = _x_train.unsqueeze_(1)
        self.x_train = _x_train

    def y_trains(self):
        if self.y_tr_tp is 'Sin':
            _y_train = torch.sin(self.x_train)
        elif self.y_tr_tp is 'Cos':
            _y_train = torch.cos(self.x_train)
        elif self.y_tr_tp is 'Tan':
            _y_train = torch.tan(self.x_train)
        noise = torch.randn(_y_train.shape) / 5.
        _y_train = _y_train + noise
        self.y_train = _y_train

    def x_tests(self):
        _min = int(min(self.x_train))
        _max = int(max(self.x_train))
        _x_test = torch.linspace(_min, _max, self.te_size)
        _x_test = _x_test.unsqueeze_(1)
        self.x_test = _x_test

    def y_tests(self):
        if self.y_te_tp is 'Sin':
            _y_test = torch.sin(self.x_test)
        elif self.y_te_tp is 'Cos':
            _y_test = torch.cos(self.x_test)
        elif self.y_te_tp is 'Tan':
            _y_test = torch.tan(self.x_test)
        self.y_test = _y_test