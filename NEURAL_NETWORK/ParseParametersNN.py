from xml.dom import minidom
import torch


class ParseParametersNN:
    """
    Klasa do parsowania i sprawdzenia poprawnosci parametrow podanych w XML, ktore wykorzystywane do tworzenia sieci
    neuronowej i zbioru uczacego i testowego.
    """

    def __init__(self, xml_path):
        self.xml_ = minidom.parse(xml_path)
        self.settings_tree = self.xml_.documentElement
        self.settings = self.settings_tree.getElementsByTagName('Parameter')
        self.message = None
        self.status = None

    def parse_parameters_NN_by_name(self, name):
        accept_fun_activation = {'Sigmoid': torch.nn.Sigmoid(), 'Tanh': torch.nn.Tanh, 'ReLU': torch.nn.ReLU}
        for setting in self.settings:
            if setting.getAttribute('name') == name and name == 'NeuralNetwork':
                try:
                    par_n_hidden = setting.getElementsByTagName('n_hidden_neurons')[0]
                    self.n_hidden_neurons = int(par_n_hidden.childNodes[0].data)
                    par_fun_act = setting.getElementsByTagName('fun_activation')[0]
                    par_fun_act = str(par_fun_act.childNodes[0].data)
                    self.fun_activation = accept_fun_activation[par_fun_act]
                    self.message = f'xml load succesfully .'
                    self.status = 1
                except KeyError:
                    self.message = 'Niepoprawna wartosc nazwy funkcji aktywacji. Do wyboru: Sigmoid, Tanh, ReLU'
                    self.status = 2
                    print(self.message)
                except TypeError:
                    self.message = 'Ilosc neuronow w ukrytej warstwie powinna byc typu int'
                    self.status = 3
                    print(self.message)
                except ValueError:
                    self.message = 'Niepoprawny typ jednego z parametrow: n_hidden_neurons.'
                    self.status = 3
                    print(self.message)

            elif setting.getAttribute('name') == name and name == 'Dataset':
                try:
                    accept_y_train_test_type = {'Sin': 'Sin', 'Cos': 'Cos', 'Tan': 'Tan'}
                    par_train_size = setting.getElementsByTagName('train_size')[0]
                    self.train_size = int(par_train_size.childNodes[0].data)
                    par_x_train_scale_0 = setting.getElementsByTagName('x_train_scale_0')[0]
                    par_x_train_scale_1 = setting.getElementsByTagName('x_train_scale_1')[0]
                    par_x_train_scale_2 = setting.getElementsByTagName('x_train_scale_2')[0]
                    self.x_train_scale = [int(par_x_train_scale_0 .childNodes[0].data), int(par_x_train_scale_1.childNodes[0].data), int(par_x_train_scale_2.childNodes[0].data)]
                    par_y_train_type = setting.getElementsByTagName('y_train_type')[0]
                    par_y_train_type = str(par_y_train_type.childNodes[0].data)
                    self.y_train_type = accept_y_train_test_type[par_y_train_type]
                    par_test_size = setting.getElementsByTagName('test_size')[0]
                    self.test_size = int(par_test_size.childNodes[0].data)
                    par_y_test_type = setting.getElementsByTagName('y_test_type')[0]
                    par_y_test_type = str(par_y_test_type.childNodes[0].data)
                    self.y_test_type = accept_y_train_test_type[par_y_test_type]
                    self.message = f'xml load succesfully.'
                    self.status = 1
                except KeyError:
                    self.message = 'Niepoprawna wartosc parametru "y_train_type" lub "y_test_type". Do wyboru: Sin, Cos, Tan.'
                    self.status = 3
                    print(self.message)
                except ValueError:
                    self.message = 'Niepoprawny typ jednego z parametrow: train_size, x_train_scale_0, x_train_scale_1, x_train_scale_1, test_size. '
                    self.status = 3
                    print(self.message)
