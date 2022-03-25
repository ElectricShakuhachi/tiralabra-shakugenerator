import os
from midiutil import MIDIFile
from midi2audio import FluidSynth

class ShakuFiling:
    def _generate_midi_track(self, data):
        file = MIDIFile(1)
        time = 0
        track = 0
        channel = 0
        tempo = int(os.getenv("SHAKUGEN_TEMPO"))
        volume = int(os.getenv("SHAKUGEN_VOLUME"))
        file.addProgramChange(0, 0, 0, int(os.getenv("SHAKUGEN_MIDI_INSTRUMENT_NUMBER")))
        file.addTempo(track, time, tempo)
        for key, pitch in enumerate(data["pitches"]):
            vol = 0 if pitch <= 0 else volume
            pitch += int(os.getenv("RO_DAIMERI_PITCH"))
            file.addNote(track, channel, pitch, time, data["lenghts"][key], vol)
            time += int(data["lenghts"][key])
        return file

    def save_wav(self, data):
        print("generating wav")
        synth = FluidSynth()
        self.save_midi(data)
        source = os.getenv("SHAKUGEN_TMP_MIDI_FILE")
        target = source[:-3] + "wav"
        synth.midi_to_audio(source, target)

    def save_midi(self, data):
        midi = self._generate_midi_track(data)
        with open(os.getenv("SHAKUGEN_TMP_MIDI_FILE"), "wb") as file:
            midi.writeFile(file)
