import sys
import os

# Add the project root directory to Python's module path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import streamlit as st

def main():
    st.title("Azure AI Sandbox")
    st.write("""
    **Bine ați venit la Azure AI Sandbox!**

    Acesta este un mediu interactiv creat special pentru sectorul public din România, menit să demonstreze cum tehnologiile avansate bazate pe inteligență artificială pot accelera transformarea digitală și îmbunătăți serviciile publice.

    ### **Ce oferă Azure AI Sandbox?**
    1. **Traducere Documente și Texte**  
       Automatizați traducerea documentelor și conținutului textual folosind servicii AI de ultimă generație. Platforma suportă limbaj natural și detecție automată a limbii.
       
    2. **Analiză Documente**  
       Extrageți informații structurate din documente oficiale precum cărți de identitate, formulare și alte fișiere scanate.

    3. **Transcriere și Traducere Vocală**  
       Transformați conținutul vocal în text și transcrieți conversațiile în timp real, creând accesibilitate și eficiență.

    ### **Cum poate ajuta sectorul public?**
    - **Modernizarea Serviciilor**  
      Simplificați procesele administrative și îmbunătățiți relația cu cetățenii prin automatizare inteligentă.
      
    - **Accesibilitate pentru Toți**  
      Asigurați accesibilitate lingvistică prin traducerea documentelor oficiale în mai multe limbi, inclusiv limba română.
      
    - **Confidențialitate și Securitate**  
      Soluțiile oferite sunt conforme cu cerințele GDPR, oferind siguranță maximă pentru datele sensibile.

    ### **Cum să începeți?**
    Folosiți meniul **Pages** din stânga pentru a explora funcționalitățile Sandbox-ului. Fie că aveți nevoie să analizați documente, să traduceți conținut sau să transcrieți discuții, platforma vă oferă toate aceste opțiuni într-un mod simplu și intuitiv.

    **Pregătiți să transformați digital sectorul public? Să începem!**
    """)

if __name__ == "__main__":
    main()
