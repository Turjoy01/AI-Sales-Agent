import whisper
import os
import tempfile

# Load model once at startup (CPU only, "base" = fast + accurate for English)
print("Loading OpenAI Whisper model (base) on CPU... (takes ~10-30 seconds first time)")
model = whisper.load_model("base")  # Options: "tiny" (fastest), "small" (better), "medium" (best)

def transcribe_audio(audio_bytes: bytes) -> str:
    """
    Takes raw audio bytes (mp3, wav, m4a, etc.) → returns full transcript
    """
    # Write to temp file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
        tmp.write(audio_bytes)
        tmp_path = tmp.name

    try:
        # Transcribe with English focus, no timestamps (just clean text)
        result = model.transcribe(tmp_path, language="en", verbose=False)
        transcript = result["text"].strip()
        return transcript or "No speech detected."
    finally:
        # Clean up
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)