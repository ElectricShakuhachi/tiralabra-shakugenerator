
class RuleSet:
    """Wrapper class for additional rules to restrict markov tree music generation"""
    def __init__(self):
        self.prev_data = []

    def repetition_stop(self, data: int) -> int:
        """Returns count of how many times data has been repeated

        Args:
            data (int): data point to compare with preceeding ones

        Returns:
            int: Count of directly preceeding sequence of identical data
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
