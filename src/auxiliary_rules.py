
class RuleSet:
    def __init__(self):
        self.prev_data = []

    def repetition_stop(self, data: int) -> int:
        """_summary_

        Args:
            data (int): _description_

        Returns:
            _type_: _description_
        """
        count = 0
        index = -1
        while len(self.prev_data) >= abs(index) and self.prev_data[index] == data:
            count += 1
            index -= 1
        self.prev_data.append(data)
        return count

    #features planned for future development:
    def repetition_weight(self, data):
        pass

    def applicability_absolute(data):
        pass
