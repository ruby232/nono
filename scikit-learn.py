# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
#
# def calcular_similitud(texto1, texto2):
#     # Vectorización de los textos
#     vectorizador = CountVectorizer().fit_transform([texto1, texto2])
#     # Cálculo de la similitud coseno
#     similitud = cosine_similarity(vectorizador)
#     return similitud[0, 1]
#
# texto1 = "Este es un ejemplo de texto"
# texto2 = "Un ejemplo de texto similar"
# similitud = calcular_similitud(texto1, texto2)
# print("Similitud entre los textos:", similitud)
