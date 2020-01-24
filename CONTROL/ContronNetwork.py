import NEURAL_NETWORK.NeuralNetwork as nn
import NEURAL_NETWORK.ParseParametersNN as pp
import NEURAL_NETWORK.TrainTestDataset as ttd
from lxml import etree
from pathlib import Path
class Control:
    def __init__(self):

        self.xml_path = None
        self.paramiters = None

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

