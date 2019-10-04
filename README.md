# ffmpeg-python-exercise

Batch convert videos or audio files (default: input -> mp3)

```
Usage:
  tomp3 -i file.webm          # outputs file.mp3
  tomp3 -i my\dir            # converts all files in \dir to .mp3 
  tomp3 -e webm -i file.mkv   # outputs file.mkv 
  tomp3 -e webm -i my\dir    # converts all files in \dir to .webm 

Switches:
  -i        input file or directory.
  -e        output extension (without the dot).
```
