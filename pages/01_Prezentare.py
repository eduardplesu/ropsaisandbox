import streamlit as st

def page_prezentare():
    st.title("Prezentare Azure AI Sandbox")

    st.write("""
    **Azure AI Sandbox pentru Sectorul Public din România** este un mediu interactiv care demonstrează puterea tehnologiilor Microsoft Azure AI. Scopul nostru este să sprijinim digitalizarea serviciilor publice prin implementarea de soluții moderne și eficiente.

    ### **Servicii disponibile în Azure AI Sandbox**
    """)

    st.subheader("1. **Azure Document Translation**")
    st.write("""
    Serviciul Azure Document Translation vă permite să traduceți rapid și precis documentele oficiale dintr-o limbă în alta. 

    **Cum funcționează?**  
    - Documentele sunt încărcate într-un spațiu securizat din Azure Blob Storage.  
    - Serviciul traduce automat documentele, păstrând formatarea originală.  

    **Beneficii pentru sectorul public:**  
    - Simplifică comunicarea interinstituțională în mai multe limbi.  
    - Facilitează accesul cetățenilor din comunități diverse la informații oficiale în limba lor nativă.  
    - Crește eficiența proceselor, eliminând nevoia traducerilor manuale.

    """)

    st.subheader("2. **Azure Translator**")
    st.write("""
    Azure Translator este o soluție puternică pentru traducerea textelor și detectarea limbilor.

    **Cum funcționează?**  
    - Textul introdus este analizat automat pentru detectarea limbii.  
    - Se oferă traducere în timp real în peste 90 de limbi.  

    **Beneficii pentru sectorul public:**  
    - Îmbunătățește accesibilitatea și incluziunea pentru cetățeni.  
    - Permite traducerea rapidă a comunicatelor oficiale, regulamentelor sau materialelor educative.  
    - Integrare ușoară în aplicații și sisteme deja existente.
    """)

    st.subheader("3. **Azure Document Intelligence**")
    st.write("""
    Azure Document Intelligence utilizează inteligența artificială pentru a extrage informații din documente structurate și nestructurate, precum formulare, facturi, contracte sau cărți de identitate.

    **Cum funcționează?**  
    - Documentele sunt încărcate și analizate automat.  
    - Datele sunt extrase și organizate într-un format structurat, pregătit pentru utilizare.  

    **Beneficii pentru sectorul public:**  
    - Automatizează procesarea formularelor guvernamentale, economisind timp și reducând erorile.  
    - Simplifică procesul de înregistrare a cetățenilor, fie că este vorba despre eliberarea de documente sau solicitarea de beneficii sociale.  
    - Crește transparența și eficiența administrativă.
    """)

    st.subheader("4. **Azure Speech Services**")
    st.write("""
    Azure Speech Services transformă sunetul în text și invers, oferind funcționalități avansate de transcriere și traducere în timp real.

    **Cum funcționează?**  
    - Poate converti fișiere audio sau conversații live în text.  
    - Oferă opțiuni de traducere vocală în timp real pentru mai multe limbi.  

    **Beneficii pentru sectorul public:**  
    - Permite transcrierea automată a ședințelor și întâlnirilor guvernamentale.  
    - Facilitează accesibilitatea pentru persoanele cu deficiențe auditive.  
    - Sprijină colaborarea internațională prin traducerea instantanee a conversațiilor.
    """)

    st.write("""
    ### **De ce Azure AI Sandbox?**
    - **Tehnologie de ultimă generație:** Soluțiile sunt alimentate de Microsoft Azure, lider global în servicii cloud.  
    - **Securitate garantată:** Respectăm cele mai stricte standarde de securitate și confidențialitate, conform cerințelor GDPR.  
    - **Adaptabilitate pentru sectorul public:** Serviciile Microsoft AI sunt gândite pentru a răspunde nevoilor unice ale instituțiilor publice din România.

    Explorați funcționalitățile disponibile din meniul **Pages** pentru a descoperi cum vă pot ajuta serviciile noastre să modernizați sectorul public!
    """)

if __name__ == "__main__":
    page_prezentare()
