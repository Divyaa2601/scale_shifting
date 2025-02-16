Pitch Shift Audio Script

This Python script allows users to apply a pitch shift effect to an audio file using the `librosa` library. The user provides an audio file, specifies the pitch shift in semitones, and saves the modified audio to a new file.

Features
- Loads an audio file
- Applies a pitch shift effect (up or down in semitones)
- Saves the modified audio file

Requirements
Ensure you have the following dependencies installed:

```bash
pip install librosa numpy
```

Usage
1. Run the script:

```bash
python pitch_shift.py
```

2. Provide the required inputs when prompted:
   - Audio file path (e.g., `input.wav`)
   - Pitch shift amount (in semitones, positive for higher pitch, negative for lower pitch)
   - Output file path (e.g., `output.wav`)

Example
```
Enter the audio file path: input.wav
Enter the pitch shift amount in semitones: 3
Enter the output file path: output.wav
```

This will shift the pitch of `input.wav` up by 3 semitones and save the result as `output.wav`.

Notes
- The script uses `librosa.effects.pitch_shift` for pitch modification.
- Ensure that the input audio file exists before running the script.

License
This project is licensed under the MIT License.


