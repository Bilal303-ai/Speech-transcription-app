# :microphone: Speech Transcription App

## Overview
This application provides an easy-to-use interface for transcribing speech into text. Built using Gradio, Hugging Face's pipeline, and OpenAI's Whisper model, the app allows users to record or upload audio files and instantly receive the corresponding transcription.

## Features
- **Real-time Speech-to-Text:** Record audio directly using your device’s microphone or upload an audio file to transcribe.
- **State-of-the-art Model:** Powered by OpenAI’s Whisper model for accurate transcription across different languages and dialects.
- **User-friendly Interface:** Interactive UI built with Gradio for a smooth user experience.

## How It Works
1. **Recording or Uploading:** Users can either record audio directly via the app or upload pre-recorded audio files.
2. **Transcription:** The audio is processed using the Whisper model, which transcribes the speech into text.
3. **Result:** The transcribed text is displayed on the app for the user to copy or use further.

## Setup Instructions
#### Requirements
- Python 3.8 or above
- Required Python packages (listed in <code>requirements.txt</code>):
  - <code>gradio</code>
  - <code>transformers</code>
  - <code>torchvision</code>
  - <code>numpy</code>
  
#### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Bilal303-ai/Speech-transcription-app
   cd Speech-transcription-app
   ```
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   python app.py
   ```
   
## Using the App
1. **Recording Audio:** Click the Record button to start recording. Once done, the app will automatically process the audio and provide a transcription.
2. **Uploading Audio:** If you have a pre-recorded file, simply upload it using the file input, and the app will transcribe the speech.

## Model Details
This app uses the **Whisper model**, a powerful speech recognition model developed by OpenAI, known for its robustness in various languages and noisy environments. It has been integrated using the **Hugging Face transformers pipeline**, making it easy to apply in real-time applications.

## Demo
You can access the live demo of the app on [GitHub Pages](https://bilal303-ai.github.io/Speech-transcription-app/).

## License
This project is licensed under the MIT License. See the [LICENCE](https://github.com/Bilal303-ai/Speech-transcription-app/blob/main/LICENSE) file for more details.


