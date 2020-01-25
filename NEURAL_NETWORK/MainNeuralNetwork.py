import torch
import matplotlib.pyplot as plt

import NeuralNetwork as nn
import ParseParametersNN as pp
import TrainTestDataset as ttd


def predict(net, x, y):
    y_pred = net.forward(x)
    plt.plot(x.numpy(), y.numpy(), 'o', label='Groud truth')
    plt.plot(x.numpy(), y_pred.data.numpy(), 'o', c='r', label='Prediction');
    print(y_pred.data.numpy())
    plt.legend(loc='upper left')
    plt.xlabel('$x$')
    plt.ylabel('$y$')
    plt.show()
    return y_pred

def training_procedure(neural_network, x_tr, y_tr):
    loss_fn = torch.nn.MSELoss()
    optimizer = torch.optim.Adam(neural_network.parameters(), lr=0.01)
    for epoch_index in range(2000):
        optimizer.zero_grad()
        y_pred = neural_network.forward(x_tr)
        loss_val = loss_fn(y_pred, y_tr)
        loss_val.backward()
        optimizer.step()


if __name__ == '__main__':
    print("Hello world!")

    # 1. Parsujemy parametry podane przez uzytkownika do utworzenia Datasetu i Sieci
    parameters = pp.ParseParametersNN('/home/maciek/Siec_neuronowa/XML/ParametersNN.xml')
    parameters.parse_parameters_NN_by_name('NeuralNetwork')
    parameters.parse_parameters_NN_by_name('Dataset')

    # 2. Tworzymy zbior Traingowy i Testowy
    dataset = ttd.DataSet(parameters.train_size, parameters.x_train_scale, parameters.y_train_type, parameters.test_size, parameters.y_test_type)

    # 3. Tworzymy Siec neuronowa
    neural_network = nn.SineNet(parameters.n_hidden_neurons, parameters.fun_activation)

    # 4. Uczymy siec
    training_procedure(neural_network, dataset.x_train, dataset.y_train)

    # 5. WYNIKI
    out_y_predict = predict(neural_network, dataset.x_test, dataset.y_test)
    out_y_test = dataset.y_test
    out_x_test = dataset.x_test