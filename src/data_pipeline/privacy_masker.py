import re
from typing import List
from src.utils.spacy_loader import load_spacy_model

class PrivacyMasker:

    def __init__(self):
        self.nlp = load_spacy_model()
        self.target_entities = {"PERSON", "ORG", "GPE", "FAC", "LOC"}
        
        self.EMAIL_PATTERN = r'\b[\w\.-]+@[\w\.-]+\.\w+\b'
        self.PHONE_PATTERN = r'\b\d{10}\b'

    def mask_pii(self, clauses: List[str]) -> List[str]:
        masked_clauses = []
        
        for text in clauses:
            if not text:
                masked_clauses.append("")
                continue

            text = re.sub(self.EMAIL_PATTERN, "[EMAIL]", text)
            text = re.sub(self.PHONE_PATTERN, "[PHONE]", text)

            doc = self.nlp(text)
            masked_text = text
            
            for ent in reversed(doc.ents):
                if ent.label_ in self.target_entities:
                    placeholder = f"[{ent.label_}]"
                    masked_text = masked_text[:ent.start_char] + placeholder + masked_text[ent.end_char:]
                    
            masked_clauses.append(masked_text)
                
        return masked_clauses