import torch


# noinspection SpellCheckingInspection
class SineNet(torch.nn.Module):
    """
    Klasa tworzy siec neuronowa z 1. warstwa ukryta wedlug parametrow podanych przez uzytkownika w ParametersNN.xml.
    """

    def __init__(self, n_hidden_neurons, fun_activation):
        accept_fun_activation = {'Sigmoid': torch.nn.Sigmoid(), 'Tanh': torch.nn.Tanh, 'ReLU': torch.nn.ReLU}
        try:
            super(SineNet, self).__init__()
            self.fc1 = torch.nn.Linear(1, n_hidden_neurons)
            self.act1 = accept_fun_activation[fun_activation]
            self.fc2 = torch.nn.Linear(n_hidden_neurons, 1)
        except KeyError:
            raise print('Zle podana nazwa funkcji aktywacji')
        except TypeError:
            raise print('Ilosc neuronow w ukrytej warstwie powinna byc typu int')

    def forward(self, x):
        """
        Metoda, ktora okresla w jakiej kolejnosci zdefiniowane warstwy w __init__ sa stosowane.
        Przrpuszcza wartosc wejsiowa X przez siec.

        :param x: dane wejsciowe do sieci w postaci tensorowej
        :type x: torch.Tensor
        :return: dane wyjsciowe z sieci
        """
        x = self.fc1(x)
        x = self.act1(x)
        x = self.fc2(x)
        return x