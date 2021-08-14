import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from django.core.management.base import BaseCommand
from tqdm import tqdm as tqdm


def is_title_relevant(title, term):
    title = title.lower()
    if 'definition' not in title:
        return False
    for part in term.lower().split(' '):
        if part == 'pattern':
            continue
        if part not in title:
            return False
    return True


def get_to_article(driver, search_term):    
    driver.get('https://investopedia.com')
    
    # search the term in the main page
    while True:
        try:
            driver.find_element_by_id('header__search_1-0').click()
            break
        except:
            driver.find_element_by_id('onetrust-accept-btn-handler').click()

    driver.find_element_by_class_name('search__input').send_keys(search_term)
    driver.find_element_by_class_name('search__button').click()
    time.sleep(0.5)
    
    # select the first result
    results = driver.find_elements_by_class_name('search-results__link')
    if len(results) == 0:
        raise Exception('Search had no results.')
    
    results_data = []
    
    for result in results:
        result_title = result.find_element_by_class_name('search-results__title').text
        results_data.append([
            result.find_element_by_class_name('search-results__title').text,
            result.get_attribute('href')
        ])
    
    data = []
    relevant_term_found = False
    
    for result in results_data:
        result_title = result[0]
        result_href = result[1]
        if is_title_relevant(result_title, search_term):
            relevant_term_found = True
            driver.get(result_href)
            time.sleep(0.5)
            data.append({
                'href': driver.current_url,
                'title': driver.find_element_by_id('article-heading_3-0').text,
                'author': driver.find_element_by_id('mntl-byline__link_2-0').text,
                'body': driver.find_element_by_id('mntl-sc-page_1-0').get_attribute('innerHTML')
            })
            driver.execute_script("window.history.go(-1)")
            time.sleep(0.5)
            
    if not relevant_term_found:
        raise Exception('Search had no relevant results.')
    
    return data


class Command(BaseCommand):
    help = 'Crawls Investopedia education pages'
    
    
    def add_arguments(self, parser):
        parser.add_argument('--crawl_list', type=str, help='list of items to crawl from Investopedia')
        parser.add_argument('--driver', type=str, help='location of chromedriver')
        parser.add_argument('--save', type=str, help='location to save crawled data json')
        parser.add_argument('--retry', type=int, help='maximum number of retries if a page returns error')
    
    
    def handle(self, *args, **kwargs):
        pattern_names = []
        with open(kwargs.get('crawl_list'), 'r') as f:
            pattern_names = json.load(f)
        
        chrome_options = Options()
        chrome_options.add_argument("--incognito")
        driver = webdriver.Chrome(options=chrome_options, executable_path=kwargs.get('driver'))
        
        driver.get('https://investopedia.com')
        driver.find_element_by_id('onetrust-accept-btn-handler').click()
        
        data = {}

        for pattern in tqdm(pattern_names):
            # attempt 5 times
            for i in range(kwargs.get('retry')):
                try:
                    pattern_data = get_to_article(driver, pattern + ' pattern')
                    data[pattern] = pattern_data
                    break
                except Exception as e:
                    print(e)
                    print('pattern not found:', pattern)
        
        with open(kwargs.get('save'), 'w+') as f:
            json.dump(data, f)