# Which of the procedures in our search engine
# do we need to change to replace of list index
# with a Dictionary index

# craw_wed, add_to_index, lookup

def get_all_links(page): 
    links = [] 
    while True: 
        url, endpos = get_next_target(page)
        if url: 
            links.append(url) 
            page = page[endpos:] 
        else: 
            break 
    return links

def crawl_web(seed): 
    tocrawl = [seed] 
    crawled = []
    # Modifying index to Dictionary
    index = {}
    while tocrawl: 
        page = tocrawl.pop()
        if page not in crawled: 
            content = get_page(page) 
            add_page_to_index(index, page, content) 
            union(tocrawl, get_all_links(content)) 
            crawled.append(page) 
    return index 

def add_page_to_index(index, url, content): 
    words = content.split() 
    for word in words: 
        add_to_index(index, word, url) 

def add_to_index(index, keyword, url): 
    # List version
    #for entry in index: 
    #    if entry[0] == keyword: 
    #         entry[1].append(url) 
    #         return 
    # not found, add new keyword to index 
    #index.append([keyword, [url]]) 

    # Dictionary version (very simply)
    if keyword in index:
        index[keyword].append(url)
    else:
        #Adding new item to index by this syntax
        index[keyword] = [url]  

def lookup(index, keyword): 
    # List version
    #for entry in index: 
    #    if entry[0] == keyword: 
    #        return entry[1] 
    #return None

    #Dictionary version
    if keyword in index:
        return index[keyword]
    return None

# lookup Testing1
index = {'udacity': ['http://udacity.com', 'http://npr.org']}
print lookup(index, 'computing')
#>>> None

# lookup Testing2 
index2 = {'udacity' : ['http://udacity.com', 'http://npr.org'], 
'computing': ['http://acm.org']}
print lookup(index2, 'computing')
#>>> ['http://acm.org']