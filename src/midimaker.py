class MidiMaker:
    """Class to convert midi integer list into a .mid file
    """
    def __init__(self, notes: list, tempo=65, volume=100):
        """Class constructor

        Args:
            notes: List of notes as midi integers to convert to MIDI
            tempo (int, optional): Tempo for MIDI. Defaults to 65.
            volume (int, optional): Volume for MIDI. Defaults to 100.
        """
        self.notes = notes
        self.tempo = tempo
        self.volume = volume
