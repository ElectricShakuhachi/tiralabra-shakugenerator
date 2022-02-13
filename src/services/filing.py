import os
from midiutil import MIDIFile

class ShakuFiling:
    def _generate_midi_track(data):
        file = MIDIFile(1)
        time = 0
        track = 0
        tempo = os.getenv("SHAKUGEN_TEMPO")
        volume = os.getenv("SHAKUGEN_VOLUME")
        file.addProgramChange(1, 0, 0, int(os.getenv("SHAKUGEN_MIDI_INSTRUMENT_NUMBER")))
        file.addTempo(track, time, tempo)
        for key, pitch in enumerate(data["pitches"]):
            vol = 0 if pitch == 0 else volume
            file.addNote(track, track, pitch, time, data["lenghts"][key], vol)
            time + data["lenghts"][key]

    def save_midi(self, data):
        midi = self._generate_midi_track(data)
        with open(os.getenv("SHAKUGEN_TMP_MIDI_FILE"), "wb") as f:
            midi.writeFile(f)

    def save_shaku(data):
        pass