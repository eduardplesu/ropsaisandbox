import streamlit as st
from modules.speech_to_text import transcribe_speech_from_file
import os

def page_speech_demo():
    st.title("Speech to Text Demo (Azure)")

    # Language selection
    language = st.selectbox("Selectează limba pentru transcriere:", options=["ro-RO", "en-US"], index=1)

    # Transcribe from audio file
    st.subheader("Transcrie fișier Audio (WAV/MP3)")
    uploaded_audio = st.file_uploader("Încarcă fișierul audio", type=["wav", "mp3"])

    if uploaded_audio is not None:
        temp_file_path = f"temp_audio_file_{uploaded_audio.name}"
        with open(temp_file_path, "wb") as f:
            f.write(uploaded_audio.getvalue())

        if st.button("Transcrie fișier"):
            try:
                with st.spinner("Processing..."):
                    transcription = transcribe_speech_from_file(temp_file_path, language=language)
                st.success("Transcrierea s-a efectuat cu succes!")
                st.text_area("Rezultat transcriere", transcription, height=150)
                st.download_button(
                    label="Descarcă transcrierea",
                    data=transcription,
                    file_name="transcription.txt",
                    mime="text/plain"
                )
            except Exception as e:
                st.error(f"Error: {e}")
            finally:
                os.remove(temp_file_path)

if __name__ == "__main__":
    page_speech_demo()
