import streamlit as st
import openai

# Configuration OpenAI
openai.api_key = "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"  # ⚠️ Remplacez par votre clé personnelle

# Titre de la page
st.set_page_config(page_title="Générateur de Hashtags IA pour Samantha Morgane Auteure", page_icon="📱")
st.title("📱 Générateur de Hashtags Instagram avec IA pour Samantha Morgane Auteure")
st.markdown("Entrez une description de votre vidéo pour obtenir des **hashtags optimisés pour le top 1**. *Développé par Sébastien Bariller*")

# Zone de saisie
description = st.text_area("✍️ Description de la vidéo Instagram :", height=150)

if st.button("🚀 Générer les hashtags"):
    if not description.strip():
        st.warning("Veuillez entrer une description.")
    else:
        with st.spinner("Génération des hashtags en cours..."):
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "Tu es un expert des réseaux sociaux qui génère les meilleurs hashtags Instagram."},
                        {"role": "user", "content": f"Génère les meilleurs hashtags pour cette vidéo : {description}. Donne-les sur une seule ligne, sans explication, uniquement les hashtags séparés par des espaces."}
                    ],
                    temperature=0.7,
                    max_tokens=100
                )
                hashtags = response['choices'][0]['message']['content']
                st.success("🎉 Hashtags générés avec succès !")
                st.text_area("📌 Hashtags suggérés :", value=hashtags.strip(), height=100)
            except Exception as e:
                st.error(f"Erreur lors de l'appel à l'API : {e}")
