import json

class ShakuConverter:
    def _convert_file(self, part, type):
        data = []
        for note in part["notes"]:
            data.append(note[type])
        return data

    def _get_data_list(self, filelist, type):
        data_array = []
        for filename in filelist:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
            for part in data["parts"].values():
                data_array.append(self._convert_file(part, type))
        return data_array

    def get_pitch_lists(self, filelist):
        return(self._get_data_list(filelist, "pitch"))

    def get_lenght_lists(self, filelist):
        return self._get_data_list(filelist, "lenght")

    def convert_simple_dict_to_shaku(data: dict):
        for key, pitch in enumerate(data["pitches"]):
            lenght = data["lenghts"][key]
