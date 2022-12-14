from flashtext import KeywordProcessor
from tqdm.auto import tqdm

class CaseStudy:
    def __init__(self, sentences, closed_class_items):
        # Save all candidate sentences
        self.sentences = sentences
        
        # Keyword processor
        self.keyword_processor = KeywordProcessor()
        self.keyword_processor.add_keywords_from_dict(closed_class_items)
        
        filtered_sentences = []
        for sentence in tqdm(self.sentences):
            if len(self.keyword_processor.extract_keywords(sentence)) > 0:
                filtered_sentences.append(sentence)
                
        self.sentences = filtered_sentences