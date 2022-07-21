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
                answer = Hardware.install(h, es)
                if answer.__class__.__name__ == "Exception":
                    return answer
                System._software.append(es)
                return
        return "Hardware does not exist"

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        for h in System._hardware:
            if h.name == hardware_name:
                ls = LightSoftware(name, capacity_consumption, memory_consumption)
                answer = Hardware.install(h, ls)
                if answer.__class__.__name__ == "Exception":
                    return answer
                System._software.append(ls)
                return
        return "Hardware does not exist"

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        for p in System._hardware:
            if p.name == hardware_name:
                for n in p.software_components:
                    if n.name == software_name:
                        p.software_components.remove(n)
                        return
        return "Some of the components do not exist"

    @staticmethod
    def analyze():
        return f"System Analysis\n" \
               f"Hardware Components: {len(System._hardware)}\n" \
               f"Software Components: {len(System._software)}\n" \
               f"Total Operational Memory: {sum(_.memory_consumption for _ in System._software)} / {sum(_.memory for _ in System._hardware)}\n" \
               f"Total Capacity Taken: {sum(_.capacity_consumption for _ in System._software)} / {sum(_.capacity for _ in System._hardware)}"

    @staticmethod
    def system_split():
        answer = ''
        for p in System._hardware:
            express = len([p for p in p.software_components if p.__class__.__name__ == 'ExpressSoftware'])
            light = len([p for p in p.software_components if p.__class__.__name__ == 'LightSoftware'])
            memory = f'{sum(_.memory_consumption for _ in p.software_components)} / {p.memory}'
            capacity = f"{sum(_.capacity_consumption for _ in p.software_components)} / {p.capacity}"
            all_components = [_.name for _ in p.software_components]
            answer += f"Hardware Component - {p.name}\n" \
                      f"Express Software Components: {express}\n" \
                      f"Light Software Components: {light}\n" \
                      f"Memory Usage: {memory}\n" \
                      f"Capacity Usage: {capacity}\n" \
                      f"Type: {p.hardware_type}\n" \
                      f"Software Components: {', '.join(all_components) if any(all_components) else None}\n"
        return answer
