# SONO VIDZ TRSC

<img width="795" height="637" alt="SONO-VIDZ-TRSC_LOGO" src="https://github.com/user-attachments/assets/642350cb-245b-4f69-bc3f-ac8595ea2cb0" />


Local Mac transcription machine using **faster-whisper**.

## What it does

Drop an audio or video file, press **TRSC**, and get a local transcription.

- Local transcription with Whisper
- White / black SONO VIDZ TRSC interface
- Different sound when transcription starts and ends
- Copy transcript to clipboard
- TXT export automatically named from the source file:
  - `PRECEPT.mp3` -> `PRECEPT_TRSC.txt`
- Runs locally on `127.0.0.1:8777`

- <img width="779" height="769" alt="SONO-VIDZ-TRSC_Shoot_00" src="https://github.com/user-attachments/assets/159df659-aebe-4cea-bc82-c55ff5eb0aac" />
<img width="721" height="486" alt="SONO-VIDZ-TRSC_Shoot_01" src="https://github.com/user-attachments/assets/ea0f8237-4a99-43f6-8385-6685360b4adc" />


## Mac install

Requires Python 3.

1. Clone or download this repository.
2. Double-click `START.command`.
3. On first launch the virtual environment and dependencies are installed.
4. The interface opens in the browser.
5. Drop audio/video -> **TRSC**.

## Stack

- Python
- Flask
- faster-whisper
- CTranslate2
- HTML / CSS / JavaScript
- Web Audio API

## Privacy

Files are processed locally on the Mac. The application does not upload source audio/video to a transcription service.
