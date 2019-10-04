from typing import * #overkill :D

import os
import sys
import ffmpeg

USAGE_TEXT = '''
Batch convert videos or audio files (default: input -> mp3)

Usage:
  tomp3 -i file.webm         # outputs file.mp3
  tomp3 -i my\\dir            # converts all files in \dir to .mp3
  tomp3 -e webm -i file.mkv  # outputs file.mkv
  tomp3 -e webm -i my\\dir    # converts all files in \dir to .webm

Switches:
   -i        input file or directory.
   -e        output extension (without the dot).
'''

def query_file_list(path: str) -> List[str]:
    result: List[str] = []

    try:
        for root, _, files in os.walk( path ):
            for file in files:
                result.append( os.path.join(root, file) )

    except Exception as e:
        print('Failed to query file list.')
        print(e)

    return result


def get_flag_value(flag: str) -> str:
    value: str = ''

    if flag in sys.argv:
        try:
            value = sys.argv[ sys.argv.index(flag) + 1 ]
        except IndexError:
            pass

    return value


def convert(input_path: str, output_ext: str) -> str:
    output_path: str = os.path.splitext(input_path)[0]

    stream: OutputStream = ffmpeg.input(input_path)
    stream = ffmpeg.output(stream, output_path + '.' + output_ext)

    try:
        ffmpeg.run(stream)

    except Exception as e:
        print(f'\nDid not convert: {input_path}\n')
        pass


def main():
    if len(sys.argv) is 1:
        print(USAGE_TEXT)
        return

    input_path: str = get_flag_value('-i')

    if (not input_path):
        print('Missing input file.')
        print('Use -i file or -i \dir.')
        return

    output_ext: str = get_flag_value('-e') or 'mp3'

    if output_ext.startswith('.'):
        output_ext = output_ext[1:]

    print('Converting.\n')

    if ( os.path.isfile(input_path) ):
        convert(input_path, output_ext)

    elif ( os.path.isdir(input_path) ):
        file_list = query_file_list(input_path)

        if (not len(file_list)):
            print('No files found. Exitting.')
            return

        for file_path in file_list:
            convert(file_path, output_ext)

    else:
        print('Error: Invalid input path.\n')
        return

    print('Finished.')
