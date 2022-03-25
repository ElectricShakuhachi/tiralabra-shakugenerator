import json

class ShakuConverter:
    def _convert_file(self, part, data_type):
        data = []
        for note in part["notes"]:
            data.append(note[data_type])
        return data

    def _get_data_list(self, filelist, data_type) -> list:
        data_array = []
        for filename in filelist:
            with open(filename, "r", encoding="utf-8") as file:
                data = json.load(file)
            for part in data["parts"].values():
                data_array.append(self._convert_file(part, data_type))
        return data_array

    def get_pitch_lists(self, filelist) -> list:
        """Return lists of note pitches, one list per file in given list"""
        return self._get_data_list(filelist, "pitch")

    def get_lenght_lists(self, filelist) -> list:
        """Return lists of note lenghts, one list per file in given list"""
        return self._get_data_list(filelist, "lenght")
