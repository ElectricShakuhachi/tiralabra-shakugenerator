import glob
import os
from services.input_converter import ShakuConverter
from entities.trie import TrieTree
from shaku_generator import ShakuGenerator
from services.filing import ShakuFiling

class ShakuGeneratorInterfaceManager:
    """Interface setter that selects correct interface"""
    def __init__(self, interface_type="plugin"):
        self.interfaces = {"cli": Cli, "plugin": NonInteractive}
        if interface_type not in self.interfaces:
            raise ValueError("Unsupported interface type requested")
        self.interface_type = interface_type

    def start(self):
        self.interface = self.interfaces[self.interface_type]()
        self.interface.run()

class Interface:
    """Prototype to be used as parent class of different interface options for shakugenerator"""
    def __init__(self):
        self.generator = ShakuGenerator()

    def _handle_output(self, data: dict, output_type: str):
        if output_type == "wav":
            ShakuFiling().save_wav(data)
        elif output_type == "shaku":
            #data = ShakuConverter().convert_simple_dict_to_shaku(data)
            #ShakuFiling().save_shaku(data)
            print("Saving in .shaku not implemented yet")
            exit()

    def _generate_output(self, output_type: str, measure_count: int=1):
        part = {"pitches": [], "lenghts": []}
        left_in_measure = int(os.getenv("SHAKUGEN_MEASURE_LENGHT"))
        while measure_count > 0:
            note = self.generator.generate_note(part)
            part["pitches"].append(note[0])
            part["lenghts"].append(note[1])
            left_in_measure -= int(note[1])
            if left_in_measure <= 0:
                measure_count -= 1
                left_in_measure = int(os.getenv("SHAKUGEN_MEASURE_LENGHT"))
        print("The following part was generated:")
        print(part)
        self._handle_output(part, output_type)

class Cli(Interface):
    def __init__(self):
        super().__init__()

    def run(self):
        types = {"1": "wav", "2": "csv", "3": "midi"}
        output_type = None
        while output_type not in types:
            print("Choose type of output")
            output_type = input("(1 = wav, 2 = csv, 3 = midi 0 = quit) :").strip()
            if output_type == "0":
                exit()
        output_type = types[output_type]
        count = -1
        while count != 0:
            count = input("How many measures should be generated? (0 to quit)").strip()
            try:
                count = int(count)
            except:
                print("Please input an integer value")
                continue
            if count < 0:
                print("Usage : 0 = quit, 1 or higher = generate measures")
            elif count > 0:
                self._generate_output(output_type, count)
                print("Generation done. Quitting...")
                exit(0)

class NonInteractive(Interface):
    def __init__(self):
        super().__init__()

    def run(self):
        pass # to be developed later