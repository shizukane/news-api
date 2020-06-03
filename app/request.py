import urllib.request,json
from .models import Sources,Articles

# Getting api key
api_key = None
# Getting the news sources url
base_url = None
#Getting the news articles url
articles_url = None


def configure_request(app):
    global api_key,base_url,articles_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    articles_url = app.config['NEWS_ARTICLES_URL']
def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results = process_results(get_sources_response['sources'])
    
    return sources_results

def process_results(news_sources_list):
    '''
    Function that processes the json results
    '''
    news_sources_results = []

    for source in news_sources_list:
        id = source.get('id')
        name = source.get('name')
        description = source.get('description')
        url = source.get('url')
        category = source.get('category')
        country = source.get('country')
        if url:
            news_source_object = Sources(id,name,description,url,category,country)
            news_sources_results.append(news_source_object)
    
    return news_sources_results

def get_articles(id):
    '''
    Function that processes the articles and returns a list of articles objects
    '''
    get_news_articles_url = articles_url.format(id,api_key)
    with urllib.request.urlopen(get_news_articles_url) as url:
        get_news_articles_response = json.loads(url.read())
        news_articles_results = None
        if get_news_articles_response['articles']:
            news_articles_results_list = get_news_articles_response['articles']
            news_articles_results = process_articles(news_articles_results_list)
    return news_articles_results

def process_articles(news_articles_list):
	'''
    Function to process Json data
	'''
	news_articles_results = []
	for article_item in news_articles_list:
		id = article_item.get('id')
		author = article_item.get('author')
		title = article_item.get('title')
		description = article_item.get('description')
		url = article_item.get('url')
		urlToImage = article_item.get('urlToImage')
		publishedAt = article_item.get('publishedAt')
		
		if urlToImage:
			news_articles_object = Articles(id,author,title,description,url,urlToImage,publishedAt)
			news_articles_results.append(news_articles_object)	
	return news_articles_results 