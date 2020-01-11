from xml.dom import minidom


class ParseParametersNN:
    def __init__(self):
        self.xml_ = minidom.parse('NEURAL_NETWORK/ParametersNN.xml')
        self.settings_tree = self.xml_.documentElement
        self.settings = self.settings_tree.getElementsByTagName('Parameter')

    def parse_button_settings_by_name(self, name):
        for setting in self.settings:
            if setting.getAttribute('name') == name and name == 'NeuralNetwork':
                n_hidden = setting.getElementsByTagName('n_hidden_neurons')
                self.n_hidden_neurons = int(n_hidden.childNodes[0].data)
                fun_act = setting.getElementsByTagName('fun_activation')
                self.fun_activation = str(fun_act.childNodes[0].data)




if __name__ == '__main__':
    k = ParseParametersNN()
    k.n_hidden_neurons
    