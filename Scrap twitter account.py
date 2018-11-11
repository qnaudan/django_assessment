"""
Here follows the pertinent HTML code sample to find the # of followers on Twitter :



<li class="ProfileNav-item ProfileNav-item--followers">
<a class="ProfileNav-stat ProfileNav-stat--link u-borderUserColor u-textCenter js-tooltip js-openSignupDialog js-nonNavigable u-textUserColor" data-nav="followers" href="/KMbappe/followers" title="2,141,177 Followers">
<span aria-hidden="true" class="ProfileNav-label">Followers</span>
<span class="u-hiddenVisually">Followers</span>
<span class="ProfileNav-value" data-count="2141177" data-is-compact="true">2.14M</span>
</a>
</li>
"""

import requests
from bs4 import BeautifulSoup

def get_followers():
    twit_url = input("Input Twitter account's URL : ")
    webpage = requests.get(twit_url)
    data = webpage.text
    html_code = BeautifulSoup(data)
    return html_code.select('li[class="ProfileNav-item ProfileNav-item--followers"]')[0].select('span[class="ProfileNav-value"]')[0].get('data-count')

get_followers() # https://twitter.com/KMbappe