from project.appliances.appliance import Appliance


class Fridge(Appliance):
    def __init__(self):
        Appliance.__init__(self, 1.2)
