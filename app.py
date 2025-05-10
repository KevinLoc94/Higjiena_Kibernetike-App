import streamlit as st

# Τίτλος και συντελεστές
st.title("Higjiena Kibernetike në Shkolla")
st.subheader("Një Udhëzues Praktik për Sigurinë Online")
st.markdown("**Autorë:** Arlinda Nikolli, Anila Kola, Jonida Prenga  \nNë bashkëpunim me Kevin Locaj")

# Προβολή εξωφύλλου
st.image("ebook-cover.png", use_container_width=True)


with open("Higjiena_Kibernetike.pdf", "rb") as file:
    st.download_button(
        label="📥 Shkarko e-book-un (PDF)",
        data=file,
        file_name="Higjiena_Kibernetike.pdf",
        mime="application/pdf"
    )
with open("Higjiena_Kibernetike.docx", "rb") as file:
    st.download_button(
        label="📄 Shkarko e-book-un (Word)",
        data=file,
        file_name="Higjiena_Kibernetike.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )


# Προαιρετική σύνοψη
st.markdown("### 📝 Përmbledhje")
st.write("""
Ky udhëzues përmbledh praktika, politika dhe shembuj ndërkombëtarë për forcimin e sigurisë digjitale në shkolla.
Përbën një mjet të vlefshëm për mësues, nxënës dhe prindër që kërkojnë të kuptojnë dhe të forcojnë higjienën kibernetike në mjediset arsimore.
""")

