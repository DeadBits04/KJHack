from pydub import AudioSegment
from pydub.silence import split_on_silence
import os

# audio file name, should be in same directory, extension should be ".wav"
filename = input("Enter final name:\t")

sound_file = AudioSegment.from_wav(filename)
audio_chunks = split_on_silence(sound_file, 
    # must be silent for at least half a second
    min_silence_len=500,

    # consider it silent if quieter than -16 dBFS
    silence_thresh=-16
)

for i, chunk in enumerate(audio_chunks):
	if not os.path.exists('splitAudio'):
		os.mkdir('splitAudio')
	out_file = "splitAudio/chunk{}.wav".format(i)
	print("exporting", out_file)
	chunk.export(out_file, format="wav")
