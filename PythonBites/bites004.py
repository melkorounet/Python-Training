import os
from collections import Counter
import urllib.request

# prep
tempfile = os.path.join('.', 'feed')
urllib.request.urlretrieve('http://bit.ly/2zD8d8b', tempfile)

with open(tempfile) as f:
    content = f.read().lower()


# start coding

def get_pybites_top_tags(n=10):
    """use Counter to get the top 10 PyBites tags from the feedget_pybites_top_tags
       data already loaded into the content variable"""

    tag_list=[]
    final_list=[]
    lines=content.split("<category>")
    for texte in lines : 
        if "</category>" in texte : 
            tag_list.append(texte.split("</category>"))
    for element in tag_list :
        final_list.append(element[0])
    print(Counter(final_list).most_common(n))

get_pybites_top_tags()