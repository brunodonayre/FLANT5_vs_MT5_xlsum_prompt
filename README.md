# FLANT5_vs_MT5_xlsum_prompt
# 📰 Comparación de Modelos de Resumen de Noticias en Español

Este proyecto evalúa y compara el desempeño de modelos de lenguaje basados en T5 y mT5 para la tarea de resumen automático de noticias políticas en español, utilizando métricas como ROUGE y BERTScore.

## 📌 Modelos Evaluados

1. **mT5-base** (`google/mt5-base`)  
   Modelo multilingüe general sin ajuste para resumen.

2. **mT5-XLSum** (`csebuetnlp/mT5_multilingual_XLSum`)  
   Modelo entrenado específicamente para resumen multilingüe de noticias.

3. **mT5-XLSum + Prompt Mejorado**  
   Misma arquitectura que el anterior, pero con ajustes en el prompt para mejorar la calidad del resumen generado.

## 🧪 Dataset

Se utilizó un conjunto de noticias políticas reales en español, con resúmenes de referencia (`resumen_gold`) elaborados manualmente para benchmarking.

## 📈 Métricas de Evaluación

- **ROUGE-1 / ROUGE-2 / ROUGE-L / ROUGE-Lsum**: mide el solapamiento literal de n-gramas entre el resumen generado y el de referencia.
- **BERTScore (Precision / Recall / F1)**: mide similitud semántica usando embeddings de BERT.

## 🧠 Resultados

| Modelo              | ROUGE-1 | ROUGE-2 | ROUGE-L | BERTScore-F1 |
|---------------------|---------|---------|---------|--------------|
| mT5-base            | 0.0553  | 0.0092  | 0.0474  | 0.5655       |
| mT5-XLSum           | 0.2432  | 0.0808  | 0.1607  | 0.6589       |
| mT5-XLSum + Prompt  | 0.2276  | 0.0753  | 0.1581  | 0.6590       |

### 🔍 Interpretación

- **ROUGE** destaca el modelo `mT5-XLSum` como el más fiel al resumen original.
- **BERTScore** muestra que el modelo con prompt mejorado genera resúmenes más naturales y legibles, con una leve mejora en F1 semántico.

📌 En resumen:  
ROUGE mide fidelidad textual, BERTScore mide calidad semántica.  
Si buscas resúmenes más legibles, el prompt mejorado es una excelente opción.

## 🚀 Cómo usar

1. Instala las dependencias:

```bash
pip install -r requirements.txt
