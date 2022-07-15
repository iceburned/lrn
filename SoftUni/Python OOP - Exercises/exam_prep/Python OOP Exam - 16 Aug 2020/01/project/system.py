from project.hardware.hardware import Hardware
from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        ph = PowerHardware(name, capacity, memory)
        System._hardware.append(ph)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        hh = HeavyHardware(name, capacity, memory)
        System._hardware.append(hh)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        for h in System._hardware:
            if h.name == hardware_name:
                es = ExpressSoftware(name, capacity_consumption, memory_consumption)
                System._software.append(es)
                return Hardware.install(h, es)
        return "Hardware does not exist"

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        for h in System._hardware:
            if h.name == hardware_name:
                ls = LightSoftware(name, capacity_consumption, memory_consumption)
                System._software.append(ls)
                return Hardware.install(h, ls)
        return "Hardware does not exist"

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        pass

    @staticmethod
    def analyze():
        pass

    @staticmethod
    def system_split():
        pass