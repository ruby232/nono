from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import numpy as np
from typing import List
from ..command.command import Command


class NLP:
    """
    Class to compare similar texts.

    @Todo:
    This has not worked very well for me, I think it is because there is too little data, I need to do better research.
    """
    def __init__(self, _commands: List[Command]):
        self.text_clf = None
        self.commands = _commands
        self.training()

    def training(self):
        """
        Train the model with command phrases.
        """
        phrases = []
        tags = []
        for command in self.commands:
            command_phrases = command.get_phrases()
            phrases.extend(command_phrases)
            tags.extend([command.name] * len(command_phrases))

        self.text_clf = Pipeline([
            ('vect', CountVectorizer()),
            ('tfidf', TfidfTransformer()),
            ('clf', MultinomialNB()),
        ])

        self.text_clf.fit(phrases, tags)

    def predict(self, phrase):
        """
        Predict the command from a phrase.
        """
        predicted_probabilities = self.text_clf.predict_proba([phrase])[0]
        max_probability = np.max(predicted_probabilities)
        print('max_probability', max_probability)
        # 0.2 is the prediction probability of the model, this I believe can be improved and depends on the amount of data.
        if max_probability < 0.2:
            return None
        else:
            predicted_tag = self.text_clf.predict([phrase])
            name = predicted_tag[0]
            for command in self.commands:
                if command.name == name:
                    return command
            return None

