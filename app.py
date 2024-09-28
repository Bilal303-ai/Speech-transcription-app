import gradio as gr
import numpy as np
from transformers import pipeline
transcriber = pipeline("automatic-speech-recognition", model="openai/whisper-base")


def predict(audio):
  sr, y = audio
  y = y.astype(np.float32)
  if y.ndim > 1:
    y = y.mean(axis=1)
  y /= np.max(np.abs(y))

  text = transcriber({"sampling_rate": sr, "raw": y})['text']

  return text


gradio_app = gr.Interface(
    fn=predict,
    inputs=[gr.Audio(sources=["upload", "microphone"], type="numpy")],
    outputs=[gr.Textbox(label="Transcription")],
    title = "Speech transcription"
)
if __name__ == "__main__":
  gradio_app.launch(share=True)
