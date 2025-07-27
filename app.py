# app.py
import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

# Cargar modelo
@st.cache_resource
def cargar_modelo():
    modelo = "mt5_xlsum_prompt_model"
    tokenizer = AutoTokenizer.from_pretrained(modelo)
    model = AutoModelForSeq2SeqLM.from_pretrained(modelo)
    return tokenizer, model

tokenizer, model = cargar_modelo()

# Interfaz
st.title("📰 Generador de resúmenes políticos (mT5 XLSum Prompt)")
texto = st.text_area("Introduce la noticia completa en español")

if st.button("Generar resumen"):
    with st.spinner("✍️ Generando resumen..."):
        entrada = f"resumir: {texto}"
        inputs = tokenizer(entrada, return_tensors="pt", truncation=True, max_length=512)
        output = model.generate(inputs["input_ids"], max_length=60, num_beams=4)
        resumen = tokenizer.decode(output[0], skip_special_tokens=True)
        st.success("✅ Resumen generado:")
        st.write(resumen)
