# Citations at the top. Or rather, we're going to declare
# what other packages/libraries/resources we will use in
# our script


# We'll use this library to convert dates and times as needed.

from datetime import datetime

# We'll use the 'pretty print' package to make that which we
# print out, more readable. We are also 'renaming' the function
# we are importing from the package so we have less to type
# when we want to use the function.

from pprint import pprint as ppr


# the requests package is what retrieves the webpage we want to scrape

import requests

# LXML is a 'core' package. Many people will use a package called
# Beautiful Soup to scrape websites. LXML is what runs under the hood.
# Once you can read HTML (not difficult) and know how to 'inspect'
# websites, you'll be able to scrape anything (more on this later).


from lxml import html


# Here we use a 'function' we gained acces to by importing the 
# requests package; the 'get' function. We use this to get
# our website by inputing the URL as a string.

root = requests.get('https://stpaul.legistar.com/Calendar.aspx')

# Now that we have the webpage, there are quite a few components
# to what we actually recieved, we need to separate out the portion
# we will use for scraping. 

base = html.fromstring(root.text)

# Enter LXML
# We are using something called Xpath; sounds complicated, and it isn't.

# What we are doing here is locating every single table row located 
# in the parent object with 'class' of 'rgMasterTable'. The results
# will be put into the object 'items', as a list. 

# Everything Xpath returns will be in a 'list'.

# Let's go through each part of the code.

# items variable we are declaring and assigning so we can use it later.

# base is defined earlier, and is the product of html function we
# pulled in from the LXML package. It returns an object that has
# properties we can use.

# xpath is one of those properties we are able to use. Within the
# parenthesis we define the path to the object we want to scrape.
# We are going to input a string, using single quotations on the
# outside for every XPath call, FYI.
# We use a '.' to tell XPath that we want to only look within
# the object being called; it sounds redundant perhaps, but is 
# necessary. 
# The '//' let's XPath  know that we are about to start telling it
# what types of HTML tags we want to access.
# The '*' is commonly used character that means 'anything'; what we're
# saying here is we want any HTML tag that has a class of 'rgMasterTable'.
# After XPath has found that item, we want it to find the 'tbody' tag
# within our 'MasterTable' tag. And once we've got that 'tbody' item
# we want to grab every single row in that table.

items = base.xpath('.//*[@class="rgMasterTable"]/tbody/tr')

# We got our items, now lets get the data!
# We are going to use a for-loop to go through each of our items
# and parse them further using XPath. 

for i in items[:5]:
    d = {}
    title = i.xpath('.//td[1]/*/a/font/text()')
    d['desc'] = i.xpath('.//description/text()')
    place = i.xpath('.//td[5]/font/text()')
    d['link'] = i.xpath('.//td[1]/*/a/@href')
    date = i.xpath('.//td[2]/font/text()')
    time = i.xpath('.//td[4]/font/span/font/text()')
    d['title'] = title[0].strip()
    d['loc'] = place[0].strip()
    d['url'] = "https://stpaul.legistar.com/" + d['link'][0]
    time = " ".join(date + time)
    format_date = '%m/%d/%Y %I:%M %p'
    d['real_date'] = datetime.strptime(time, format_date)
    d['desc_xtra'] = i.xpath('.//td[5]/font/*/text()')
    d['deets'] = i.xpath('.//td[6]/*/a/@href')
    d['agenda'] = i.xpath('.//td[7]/font/span/a/@href')
    ppr(d)

