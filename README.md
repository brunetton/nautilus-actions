# Nautilus actions

Actions for Nautilus I made, based on the excellent [actions-for-nautilus](https://github.com/bassmanitram/actions-for-nautilus).

## Actions list

This file groups similar actions by their base label. When an action applies only to a specific file type or target, it's noted in parentheses.

- 🪄 Convert to webp: lossless, 80%, 60%, 30%
- 🪄 Convert to jpg
- 🪄 Convert to PNG (two variants):
  - Convert PDF files to PNG (300 dpi) (applies to PDF files)
  - Convert image files to PNG
- Extract images from PDF files (applies to PDF files)
- ⏬ Layer images: (up down), (up down) - REVERSED, (2 by 2)
- ❌ Remove EXIF data
- 🎥 Extract audio from video files
- 🎥 Convert video files to mp4
- 🎥 Recompress video files to h264
- 🎥 Create GIF from video files
- 🎥 Merge video and audio (mkv or mp4) (requires a video and an audio file)
- 🔇 Remove audio from video files (keeps original file)
- ➡️ Convert audio files to FLAC
- ➡️ Convert audio files to WAV
- ➡️ Convert audio files to AAC: 96k, 128k, 192k
- ➡️ Convert audio files to MP3: 96 kbps (mono), 96 kbps, 128 kbps, 192 kbps, 256 kbps
- ▶️◀️ Resize image files: 1200px, 1500px, 2000px, 70%, 50%
- Folder Actions (applies to directories)
  - Remove "node modules" dirs recursively
  - Execute command here (runs in selected directory)
  - Start HTTP server here (runs in selected directory)
- 📝 Copy details (generic)
  - Copy full path (~/truc.pdf)
  - Copy basename (truc.pdf)
  - Copy path only (~/)
  - Copy URI
- 📥 Move last downloaded file here (moves file into selected directory)


## Install

- install [actions-for-nautilus](https://github.com/bassmanitram/actions-for-nautilus)
- clone this repo
- make a link from actions-for-nautilus config file location to this project `config.json` file:

    ```bash
    mkdir -p ~/.local/share/actions-for-nautilus
    ln -s $PWD/config.json ~/.local/share/actions-for-nautilus/
    ```

    => replace $PWD by the folder you cloned this repo onto, if you're not inside this folder when you type this command
- restart Nautils
    `nautilus -q; nautilus`
