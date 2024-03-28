import PyPDF2
import json 

class Document:
    def __init__(self, article_number, article_summary, article_content):
        self.article_number = article_number
        self.article_summary = article_summary
        self.article_content = article_content
    
    def get_article_content(self):
        return self.article_content
        
    def set_article_content(self, new_content):
        self.article_content = new_content

    def to_json(self):
        return self.__dict__
    


def extract_article_number(page_content):
    """
        function that extracts the article number from a title page
        page_content: str -> represents the page content text as it is extracted from the pdf
    """
    page_content_lines = page_content.split('\n')
    article_nb_line = page_content_lines[1]
    if 'Article' in article_nb_line:
        return int(article_nb_line.split()[-1].strip('.'))
    return -1

def is_title_page(page_content):
    """
        function that checks if the given page content is the title page of an article
        page_content: str -> represents the page content text as it is extracted from the pdf
    """
    
    page_content_lines = page_content.split('\n')
    return (all([
        'EN' == page_content_lines[0],
        'Article' in page_content_lines[1],
        'GDPR training, consulting and DPO outsourcing' in page_content_lines[3],
        "www.gdpr-text.cominfo@data-privacy" in page_content_lines[-2],
        "office.eu" in page_content_lines[-1]
    ]))

def extract_summaries(text_content):
    pass

def extract_articles(reader):
    """
        function that checks if the given page content is the title page of an article
        reader: str -> represents the page content text as it is extracted from the pdf
    """
    articles = []
    pages_count = len(reader.pages)

    # extract the first page content for initialization
    page_content = reader.pages[0].extract_text()
    if is_title_page(page_content):
        article_number = extract_article_number(page_content)
        article_obj = Document(article_number,'','')

    for page_index in range(1,pages_count):
        page_content = reader.pages[page_index].extract_text()
        if is_title_page(page_content):
            articles.append(article_obj)
            article_number = extract_article_number(page_content)
            article_obj = Document(article_number,'','')
        else:
            article_obj.set_article_content(
                article_obj.get_article_content()+'\n'+
                page_content
            )

    # print([article.to_json() for article in articles])
if __name__ == '__main__':
    articles_filepath = '/Users/mihai.paul/Desktop/work/rag-GDPR/GDPR Art 1-21.pdf'
    articles_summaries_filepath = '/Users/mihai.paul/Desktop/work/rag-GDPR/summaries.txt'

    reader = PyPDF2.PdfReader(articles_filepath)

    extract_articles(reader)
    # print(is_title_page(reader.pages[5].extract_text()),extract_article_number(reader.pages[5].extract_text()))



    # print(Document(1,'does this', ['content1, content2']).to_json())

# def create_documents()
