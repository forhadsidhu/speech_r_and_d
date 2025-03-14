from spleeter.separator import Separator
from pydub import AudioSegment
import simpleaudio as sa

def music_seperator(audio_file):
    """Separating music and pure audio speech."""
    separator = Separator('spleeter:2stems')
    separator.separate_to_file(audio_file, 'output')

def play_seperator():
    """Function for playing separated audio files."""
    # Load the separated audio files
    vocals = AudioSegment.from_wav('output/song/vocals.wav')
    accompaniment = AudioSegment.from_wav('output/song/accompaniment.wav')
    
    # Play the vocals and accompaniment
    play_audio(vocals)
    play_audio(accompaniment)

def play_audio(audio):
    """Function to play the audio file."""
    # Play audio
    play_obj = sa.play_buffer(audio.raw_data, num_channels=audio.channels, bytes_per_sample=audio.sample_width, sample_rate=audio.frame_rate)
    play_obj.wait_done()

def main():
    # Provide the full path to your MP3 file
    music_seperator('data/song.mp3')
    
    # Play the separated files
    play_seperator()

# Run the main function
if __name__ == "__main__":
    main()
