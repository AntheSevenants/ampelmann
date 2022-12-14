from ampelmann.CaseStudy import CaseStudy
from tqdm.auto import tqdm
import spacy

class RoodGroen(CaseStudy):    
    def filter(self, order):
        if order not in ["red", "green"]:
            raise Exception("Unrecognised order. Specify either 'red' or 'green' as the requested order.")
    
        self.nlp = spacy.load("nl_core_news_lg",  disable=["parser", "attribute_ruler"])
        
        filtered_sentences = []
        participles = []
        auxiliaries = []
        
        doc = self.nlp.pipe(self.sentences)
        for sentence in tqdm(doc, total=len(self.sentences)):
            pos_tags = []
            tokens = []
            lemmas = []
            
            for token in sentence:
                pos_tags.append(token.pos_)
                tokens.append(token.text)
                lemmas.append(token.lemma_)
       
            indices = [i for i, x in enumerate(pos_tags) if x == "VERB"]
            for index in indices:
                if order == "green":
                    aux_index = index + 1
                    if aux_index > len(pos_tags) - 1:
                        continue
                elif order == "red":
                    aux_index = index - 1
                    if aux_index < 0:
                        continue
        
                if pos_tags[aux_index] == "AUX":
                    filtered_sentences.append(sentence)
                    participles.append(tokens[index])
                    auxiliaries.append(lemmas[aux_index])
                    break
                    
        return filtered_sentences, participles, auxiliaries