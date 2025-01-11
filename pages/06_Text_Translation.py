import streamlit as st
import asyncio
from modules.text_translator import detect_language, translate_text

def page_text_translation():
    st.title("Azure Translator Demo - Text Translation")

    # Input text for translation
    st.subheader("Traducere Text Simplu")
    user_text = st.text_area("Introduceți textul de tradus:", "")

    # Language selection
    source_lang = st.selectbox(
        "Alegeți limba sursă (folosiți 'auto' pentru detecție automată):",
        options=["auto", "ro", "en", "de", "fr", "es", "it"],
        index=0
    )
    target_langs = st.multiselect(
        "Selectați una sau mai multe limbi de destinație:",
        options=["ro", "en", "de", "fr", "es", "it"],
        default=["en"]
    )

    # Translation process
    if st.button("Tradu Textul"):
        if not user_text.strip():
            st.warning("Vă rugăm să introduceți textul de tradus.")
        else:
            st.info("Se traduce textul...")
            results = {}
            try:
                with st.spinner("Traducere în curs..."):
                    for target_lang in target_langs:
                        # Handle auto-detection
                        if source_lang == "auto":
                            detected_lang = detect_language(user_text)
                            st.write(f"Limba detectată: **{detected_lang}**")
                        else:
                            detected_lang = source_lang

                        # Translate the text
                        translated_text = asyncio.run(
                            translate_text(
                                text=user_text,
                                from_language=detected_lang,
                                to_language=target_lang
                            )
                        )
                        results[target_lang] = translated_text

                # Display the translations
                st.success("Traducere finalizată!")
                for lang, translation in results.items():
                    st.markdown(f"### Traducere în **{lang.upper()}**")
                    st.text_area(f"Rezultatul în {lang.upper()}:", translation, height=150, key=f"translation_{lang}")

                    # Download button
                    st.download_button(
                        label=f"Descarcă traducere {lang.upper()}",
                        data=translation,
                        file_name=f"translation_{lang}.txt",
                        mime="text/plain",
                        key=f"download_btn_{lang}"
                    )
            except Exception as e:
                st.error(f"Eroare: {e}")

if __name__ == "__main__":
    page_text_translation()
