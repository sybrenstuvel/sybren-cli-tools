# sybren-cli-tools

Some random CLI tools I write to scratch my own itch.

## Matroska file support

The `sybren_cli_tools/mkvedit` package contains functions for editing and querying Matroska (MKV) files.
Common to all the tools is that you can either specify the filenames to operate on on the CLI, or specify nothing to have it operate on all MKV files in the current directory.

- *mkv-edit-deactivate-subtitles*: Deactivates, but doesn't remove, all subtitle tracks.
- *mkv-track-info*: Prints a table with a row per file, listing the number of video/audio/subtitle tracks.


