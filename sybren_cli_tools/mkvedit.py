"""Disables all subtitles on given MKV files."""

import argparse
import subprocess

import enzyme


def cli_filenames():
    parser = argparse.ArgumentParser(
        description='Disables all subtitle tracks on all given Matroska (MKV) files.')
    parser.add_argument('filenames', metavar='MKV', type=str, nargs='+',
                       help='Filename of MKV file to operate on')

    args = parser.parse_args()

    yield from args.filenames


def deactivate_subtitles():
    for fname in cli_filenames():
        with open(fname, 'rb') as f:
            try:
                mkv = enzyme.MKV(f)
            except enzyme.exceptions.MalformedMKVError as ex:
                print('Error parsing %s: %s' % (fname, ex))
                continue

        print('%s: %i subtitle tracks' % (fname, len(mkv.subtitle_tracks)))
        for sidx in range(len(mkv.subtitle_tracks)):
            cmd = ['mkvpropedit',
                   '--edit', 'track:s%i' % (sidx+1),
                   '--set', 'flag-default=0',
                   fname]
            subprocess.check_call(cmd)


