import streamlit as st

# Τίτλος και συντελεστές
st.title("Higjiena Kibernetike në Shkolla")
st.subheader("Një Udhëzues Praktik për Sigurinë Online")
st.markdown("**Autorë:** Arlinda Nikolli, Anila Kola, Jonida Prenga  \nNë bashkëpunim me Kevin Locaj")

# Προβολή εξωφύλλου
st.image("ebook-cover.png", use_container_width=True)


# 1. PDF version in Albanian
with open("Higjiena_Kibernetike.pdf", "rb") as file:
    st.download_button(
        label="📥 Shkarko e-book-un (PDF) - 🇦🇱 Shqip",
        data=file,
        file_name="Higjiena_Kibernetike.pdf",
        mime="application/pdf"
    )

# 2. Word version in Albanian
with open("Higjiena_Kibernetike.docx", "rb") as file:
    st.download_button(
        label="📄 Shkarko e-book-un (Word) - 🇦🇱 Shqip",
        data=file,
        file_name="Higjiena_Kibernetike.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )

# 3. PDF version in English
with open("Higjiena_Kibernetike_Anglisht.pdf", "rb") as file:
    st.download_button(
        label="📄 Download English Version (PDF) - 🇬🇧 English",
        data=file,
        file_name="Higjiena_Kibernetike_Anglisht.pdf",
        mime="application/pdf"
    )

# 4. Word version in English
with open("Higjiena_Kibernetike_Anglisht.docx", "rb") as file:
    st.download_button(
        label="📝 Download English Version (Word) - 🇬🇧 English",
        data=file,
        file_name="Higjiena_Kibernetike_Anglisht.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )


# 7. Prezantim PowerPoint
with open("Higjiena_Kibernetike_Prezantim.pptx", "rb") as file:
    st.download_button("📊 Shkarko prezantimin (PPT)", file, file_name="Higjiena_Kibernetike_Prezantim.pptx", mime="application/vnd.openxmlformats-officedocument.presentationml.presentation")

# Προαιρετική σύνοψη
st.markdown("### 📝 Përmbledhje")
st.write("""
Ky udhëzues përmbledh praktika, politika dhe shembuj ndërkombëtarë për forcimin e sigurisë digjitale në shkolla.
Përbën një mjet të vlefshëm për mësues, nxënës dhe prindër që kërkojnë të kuptojnë dhe të forcojnë higjienën kibernetike në mjediset arsimore.
""")

