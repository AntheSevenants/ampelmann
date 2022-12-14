from ampelmann.CaseStudy import CaseStudy
from tqdm.auto import tqdm
import spacy


class RoodGroen(CaseStudy):
    def __init__(self, sentences, closed_class_items, order):
        super().__init__(sentences, closed_class_items)

        if order not in ["red", "green"]:
            raise Exception(
                "Unrecognised order. Specify either 'red' or 'green' as the requested order.")

        self.order = order

    def filter(self):
        self.nlp = spacy.load("nl_core_news_lg",  disable=[
                              "parser", "attribute_ruler"])

        # List of all raw sentences
        filtered_sentences = []
        # Lists containing participles and lemmas of auxiliaries
        participles = []
        auxiliaries = []
        # Lists containing the indices of the participles and auxiliaries
        # In this way, vectors of these words can be built
        participle_indices = []
        aux_indices = []

        doc = self.nlp.pipe(self.sentences)
        for sentence in tqdm(doc, total=len(self.sentences)):
            pos_tags = []
            pos_tags_fine = []
            tokens = []
            lemmas = []

            for token in sentence:
                pos_tags.append(token.pos_)
                pos_tags_fine.append(token.tag_)
                tokens.append(token.text)
                lemmas.append(token.lemma_)

            indices = [i for i, x in enumerate(pos_tags) if x == "VERB"]
            for index in indices:
                aux_index = -1
                if self.order == "green":
                    aux_index = index + 1
                    if aux_index > len(pos_tags) - 1:
                        continue
                elif self.order == "red":
                    aux_index = index - 1
                    if aux_index < 0:
                        continue

                # No infinitivus pro participio, thank you
                if "inf" in pos_tags_fine[index]:
                    continue

                if pos_tags[aux_index] == "AUX":
                    filtered_sentences.append(sentence)
                    participles.append(tokens[index])
                    auxiliaries.append(lemmas[aux_index])
                    participle_indices.append(index)
                    aux_indices.append(aux_index)
                    break

        to_return = {"filtered_sentences": filtered_sentences,
                     "participles": participles,
                     "auxiliaries": auxiliaries,
                     "participle_indices": participle_indices,
                     "aux_indices": aux_indices}

        return to_return