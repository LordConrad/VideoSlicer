# Shorty

VideoSlicer is a simple GUI app for splitting video files. You can split videos either by a specific duration or into a set number of parts.

## Features
- **Fast splitting:** Uses `ffmpeg -c copy` so videos are split quickly without re-encoding.
- **Two modes:** Split by a fixed duration (e.g., 30-second clips) or into a fixed number of segments (e.g., 4 equal parts).
- **Timeline:** Simple interactive timeline to preview the segments.
- **Progress tracking:** Shows a progress bar while exporting so the app doesn't freeze.

## Made with
- **Python** with **PySide6** for the UI.
- **FFmpeg** for the actual video splitting (make sure you have [FFmpeg](https://www.ffmpeg.org/download.html) installed and in your system PATH).
- **PyInstaller** for building executables.

## Building
You can build a standalone executable using the provided script. Make sure your virtual environment is active.

```bash
python build.py
```

On Linux, it creates a single binary in `dist/VideoSlicer`.
On Windows, it creates a single executable file in `dist/VideoSlicer.exe`.
