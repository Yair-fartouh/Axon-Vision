# Video Motion Detection Pipeline

## 📋 Overview
Real-time motion detection system using multi-process architecture for high performance video processing.

## 📁 Project Structure
- `main.py` - Main entry point
- `streamer.py` - Video frame reader process
- `detector.py` - Motion detection process  
- `presenter.py` - Video display process
- `logger.py` - Logging system
- `logs/` - Log files directory (auto-generated)

## ⚙️ Installation

1. Install required packages:
```bash
pip install -r requirements.txt
```

2. Place your video file in the project directory (default: People.mp4)

## 🚀 Quick Start
Run the application:

```bash
python main.py
```

## 🔧 Configuration
To use a different video file, edit main.py:

```bash
video_path = "your_video.mp4"
```
