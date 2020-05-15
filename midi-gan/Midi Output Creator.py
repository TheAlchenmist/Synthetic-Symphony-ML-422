from visual_midi import Plotter
import magenta.music as mm
import os
import sys
import glob

f = '*.mid'
d = os.getcwd()
for file in glob.glob(os.path.join(d,f)):
    sequence = mm.midi_io.midi_file_to_note_sequence(os.path.join("simplemidi", file))
    plot_filename = "%s.html" % (file)
    plot_path = os.path.join("output", plot_filename)
    pretty_midi = mm.midi_io.note_sequence_to_pretty_midi(sequence)
    plotter = Plotter()
    plotter.show(pretty_midi, plot_path)
    plotter.save(pretty_midi, plot_path)
    print("Generated plot file: " + str(os.path.abspath(plot_path)))
