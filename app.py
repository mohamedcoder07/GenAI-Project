import streamlit as st
import joblib
import numpy as np
import PyPDF2

# Charger le modèle (décommenter si nécessaire)
# model = joblib.load('iris_model.pkl')

# Interface Streamlit
st.title("Chat with your PDFs using IA")
st.write("Utilisez cette application pour chatter avec ton PDF utilisant LLM/RAG.")

# Section d'upload du fichier PDF
uploaded_file = st.file_uploader("📄 Choisissez un fichier PDF", type="pdf")

if uploaded_file is not None:
    st.success("✅ Fichier uploadé avec succès!")

    try:
        # Lecture du fichier PDF
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        text = "\n".join([page.extract_text() for page in pdf_reader.pages if page.extract_text()])

        if text.strip():  # Vérifier si le texte a été extrait
            with st.expander("📃 Contenu du PDF (cliquer pour afficher)"):
                st.text_area("Texte extrait :", text, height=300)
        else:
            st.warning("⚠️ Impossible d'extraire du texte de ce PDF.")

    except Exception as e:
        st.error(f"❌ Erreur lors de la lecture du PDF : {e}")

# Entrée des caractéristiques de la fleur
# st.subheader("🔢 Entrer les caractéristiques de la fleur")
# sepal_length = st.number_input('Longueur du sépale (cm)', min_value=0.0, step=0.1)
# sepal_width = st.number_input('Largeur du sépale (cm)', min_value=0.0, step=0.1)
# petal_length = st.number_input('Longueur du pétale (cm)', min_value=0.0, step=0.1)
# petal_width = st.number_input('Largeur du pétale (cm)', min_value=0.0, step=0.1)

# Faire une prédiction (décommenter si le modèle est chargé)
# if st.button('Faire une prédiction'):
#     features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
#     prediction = model.predict(features)
#     st.write(f"🌼 Le modèle prédit que cette fleur est de la classe : {prediction[0]}")
