# SONO VIDZ TRSC

**I TRANSCRIBE.**

Local Mac transcription machine using **faster-whisper**.

`AUDIO / VIDEO → TRSC → TEXT`

## WITH / WITHOUT TIME CODE

The interface now offers two modes:

- **WITHOUT TIME CODE** — clean transcription.
- **WITH TIME CODE** — each Whisper segment gets start/end timestamps, e.g. `[00:03:14.120 → 00:03:21.480]`.

Exports keep the source name:

- `PRECEPT.mp4 → PRECEPT_TRSC.txt`
- `PRECEPT.mp4 → PRECEPT_TRSC_TIMECODE.txt`

## Mac

Double-click `START.command`. The interface opens at `http://127.0.0.1:8777/`.

Python 3 is required. First launch creates the virtual environment, installs dependencies and may download the Whisper model. Transcription then runs locally.
