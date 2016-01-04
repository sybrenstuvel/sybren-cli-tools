"""Functions to modify/query Matroska files."""

import argparse
import subprocess
import os.path
import glob
import itertools

import enzyme
from tabulate import tabulate


def cli_filenames(**kwargs):
    parser = argparse.ArgumentParser(**kwargs)
    parser.add_argument('filenames', metavar='MKV', type=str, nargs='*',
                       help='Filename of MKV file')

    args = parser.parse_args()

    if args.filenames:
        yield from args.filenames
    else:
        yield from sorted(itertools.chain(glob.iglob('*.mkv'), glob.iglob('*.MKV')))


def mkv_for_filenames(**kwargs):
    for fname in cli_filenames(**kwargs):
        with open(fname, 'rb') as f:
            try:
                mkv = enzyme.MKV(f)
            except enzyme.exceptions.MalformedMKVError as ex:
                print('Error parsing %s: %s' % (fname, ex))
                continue

            yield (fname, mkv)

def deactivate_subtitles():
    """Disables all subtitle tracks on all given Matroska (MKV) files."""

    for fname, mkv in mkv_for_filenames(description=deactivate_subtitles.__doc__):
        print('%s: %i subtitle tracks' % (fname, len(mkv.subtitle_tracks)))
        for sidx in range(len(mkv.subtitle_tracks)):
            cmd = ['mkvpropedit',
                   '--edit', 'track:s%i' % (sidx+1),
                   '--set', 'flag-default=0',
                   fname]
            subprocess.check_call(cmd)


def track_info():
    """Shows track count of all given Matroska (MKV) files."""

    info = ((os.path.basename(fname),
             len(mkv.video_tracks),
             len(mkv.audio_tracks),
             len(mkv.subtitle_tracks))
            for fname, mkv in mkv_for_filenames(description=track_info.__doc__))

    headers = ['File', 'video', 'audio', 'subtitle']
    print(tabulate(info, headers=headers, tablefmt='fancy_grid'))

