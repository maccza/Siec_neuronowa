import NEURAL_NETWORK.NeuralNetwork as nn
import NEURAL_NETWORK.ParseParametersNN as pp
import NEURAL_NETWORK.TrainTestDataset as ttd
from lxml import etree
from pathlib import Path
import torch
class Control:
    def __init__(self):

        self.xml_path = None
        self.paramiters = None
        self.dataset = None
        self.neural_network = None
    def load_xml(self,xml_path):
        self.xml_path = xml_path
        status = self.valid_settings_xml

        if status:
            return 1,"valid xml"
        else:
            return 3,"invalid xml"
        
    
    @property
    def valid_settings_xml(self):

        path = Path().resolve()/'XML/validation_xml.xsd'

        xml_settings_schema_doc = etree.parse(str(path))
        xml_settings_schema = etree.XMLSchema(xml_settings_schema_doc)

        xml_doc = etree.parse(self.xml_path)
        result = xml_settings_schema.validate(xml_doc)
        
        return result


    @property
    def parse_setting_xml(self):

        if self.xml_path is None:
            return (3,"load xml first")
        else:
            self.paramiters = pp.ParseParametersNN(self.xml_path)
            self.paramiters.parse_parameters_NN_by_name('NeuralNetwork')
            self.paramiters.parse_parameters_NN_by_name('Dataset')

    def to_lern_network(self):

        if self.paramiters.status == 1:
            self.dataset = ttd.DataSet(self.paramiters.train_size, 
                                         self.paramiters.x_train_scale, 
                                         self.paramiters.y_train_type, 
                                         self.paramiters.test_size, 
                                         self.paramiters.y_test_type)
            

            self.neural_network = nn.SineNet(self.paramiters.n_hidden_neurons, 
                                            self.paramiters.fun_activation)

            
            self.training_procedure(self.neural_network, 
                                    self.dataset.x_train, 
                                    self.dataset.y_train)

        else:
            return(self.paramiters.status,
                    self.paramiters.message)
        return(self.paramiters.status,
                    self.paramiters.message)
        
    def predict(self):
        # self.y_pred = net.forward(x)

        self.neural_network.forward(self.dataset.x_test)

    def training_procedure(self,neural_network, x_tr, y_tr):
        loss_fn = torch.nn.MSELoss()
        optimizer = torch.optim.Adam(neural_network.parameters(), lr=0.01)
        for epoch_index in range(2000):
            optimizer.zero_grad()
            y_pred = neural_network.forward(x_tr)
            loss_val = loss_fn(y_pred, y_tr)
            loss_val.backward()
            optimizer.step()

    @property
    def return_train_dataset_to_plot(self):
        return self.dataset.x_train,self.dataset.y_train
    @property
    def return_test_dataset_to_plot(self):
        return self.dataset.x_test,self.dataset.y_test