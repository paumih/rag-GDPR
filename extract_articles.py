import PyPDF2
import json 
articles_filepath = '/Users/mihai.paul/Desktop/work/rag-GDPR/GDPR Art 1-21.pdf'

reader = PyPDF2.PdfReader(articles_filepath)

print(reader.pages[0].extract_text())

class Document:
    def __init__(self, article_number, article_summary,article_content):
        self.article_number = article_number
        self.article_summary = article_summary
        self.article_content = article_content
    
    def to_json(self):
        return json.dumps(self.__dict__)

print(Document(1,'does this', ['content1, content2']).to_json())
