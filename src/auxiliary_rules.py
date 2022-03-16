from os import getenv
from copy import copy

class RuleSet:
    def __init__(self):
        self.prev_data = []

    def repetition_stop(self, data: int):
        """_summary_

        Args:
            data (int): _description_

        Returns:
            _type_: _description_
        """
        data = copy(data)
        count = 0
        for i in range(len(self.prev_data) - 1, -1, -1):
            if self.prev_data[i] == data:
                count += 1
            else:
                break
        self.prev_data.append(data)
        return count

    #features planned for future development:
    def repetition_weight(self, data):
        pass

    def applicability_absolute(data):
        pass
