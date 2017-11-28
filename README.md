# Start Scraping with Python

This repository uses LXML to scrape webpages. [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) is an awesome package, but for those who want more fine-grain control of the pages they scrape, LXML is what runs underneath the hood in Beautiful Soup.

That said, we're going to start with the basics, and add info as requested by users.

## Python Variable Types

#### A quick note about numbers

In programming there are two basic types of numbers, integers and floats. Integers are whole numbers, positive or negative (i.e. 4, 231, -34). Floats are numbers that utilize decimal places (i.e. 3.76, .12, 32.00). 

### Back to Basics

A string is a variable that contains only text

'''
test = 'This is a test variable that we are declaring and defining at the same time'
'''

A list is a collection of variables. Lists can contain strings, numbers, other lists, and dictionaries.

'''
new_list = ['red', 'blue', 12, .3.45,['dog', 'cat', 'taco'], {color: 'red', animal: 'bird', travel_method: 'flight'}]
'''

A dictionary is a collection of key/value items. The last item in our previous list, is a dictionary. There are 3 keys, *color*, *animal*, and *travel_method*. The ':' is used to separate the key, from the value. It is important to note, that this is what a dictionary *may* look like when it is printed out. When creating dictionaries, the format *will* look different.

Just like lists, dictionary values can be strings, numbers, lists, or other dictionaries.

'''
new_dictionary =  {color: 'blue', animal: 'fish', travel_method: 'swim'}
'''



### Future additions

- [ ] Build Development environment
- [ ] How to scrape pages that use JavaScript
