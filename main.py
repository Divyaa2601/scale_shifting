import librosa
import numpy as np

def my_pitch_shift():
    # Get input from the user
    audio_file = input("Enter the audio file path: ")
    shift = float(input("Enter the pitch shift amount in semitones: "))
    output_file = input("Enter the output file path: ")

    # Load the audio file
    audio, sample_rate = librosa.load(audio_file)

    # Calculate the pitch shift factor
    factor = 2.0 ** (shift / 12.0)

    # Resample the audio to achieve the pitch shift effect
    audio_shifted = librosa.effects.pitch_shift(audio, sample_rate, n_steps=shift)

    # Save the shifted audio to a file
    librosa.output.write_wav(output_file, audio_shifted, sample_rate)

# Run the my_pitch_shift function
my_pitch_shift()
