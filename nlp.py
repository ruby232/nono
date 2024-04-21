from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB


class NLP:
    def __init__(self):
        self.model = MultinomialNB()
        self.vectorizador = TfidfVectorizer()

    def training(self, frases):
        # Conjunto de datos de entrenamiento
        frases = [
            "Hola tío",
            "hola,tío",
            "Hola,tio",
            "hola tio",
            "Hola, tío",
            "hola,tio",
            "Hola,tío",
            "hola, tío",
            "hola, tio",
            "hola tío",
            "Hola,tio",
            "hola,tío",
            "Hola,tio",
            "hola, tío",
            "Hola, tio",
            "Hola tío",
            "hola tio",
            "hola, tio",
            "hola,tío"
        ]
        etiquetas = ["contiene", "no contiene", "no contiene"]

        # Vectorización de las frases
        vectores_frases = self.vectorizador.fit_transform(frases)

        # Entrenamiento del modelo
        self.model.fit(vectores_frases, etiquetas)

    def predict(self, frase):
        # Vectorización de la nueva frase
        vector_nueva_frase = self.vectorizador.transform([frase])

        # Predicción del modelo
        prediccion = self.model.predict(vector_nueva_frase)

        return prediccion[0]
