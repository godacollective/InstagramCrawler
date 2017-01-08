# Description
Selenium-based web Instagram crawler. Used for the [Instarigami](https://vimeo.com/198317130) installation.

This is a forked version of [InstagramCrawler](https://github.com/iammrhelo/InstagramCrawler), updated for Python 3 support and additional functionality. The InstagramCrawler class resides in a separate file, which makes it easier to import into other code. The crawler also stores the names of all the images downloaded in `downloaded_images` which can be cleared by calling the `clear_downloads_list` method of the crawler.

An additional parameter, `allow_duplicates` is added to the constructor (default is `False`). If `False`, an image that has already been downloaded won't be downloaded again.
There's also some Open Sound Control implemented via [python-osc](https://pypi.python.org/pypi/python-osc) (currently for hashtags only). This can be used to send messages when an image is downloaded.

If you're using Firefox 48+, you need to install [GeckoDriver](https://github.com/mozilla/geckodriver/releases) and add it to your system path. (More installation notes can be found [here](https://developer.mozilla.org/en-US/docs/Mozilla/QA/Marionette/WebDriver)).

# Disclaimer
Since Instagram sometimes changes things, this may stop working at any moment. It relies on some regexp-parsing of HTML, too, to [summon Satanic overlords](https://stackoverflow.com/questions/1732348/regex-match-open-tags-except-xhtml-self-contained-tags#1732454).
The code is a bit of a mess, since functionality had to be added quickly 

# InstagramCrawler
A non API python program to crawl public photos, posts or followers.  
Borrowed a lot from [InstaRaider](https://github.com/akurtovic/InstaRaider).
### Example:

Download the first 100 photos and captions(user's posts, if any) from username "instagram"
```
$ python instagramcrawler.py -q 'instagram' -t 'photos' -c -n 100
```

Search for the hashtag "#breakfast" and download first 50 photos
```
$ python instagramcrawler.py -q '#breakfast' -t 'photos' -n 50
```

Record the first 300 followers of the username "instagram", requires log in
```
$ python instagramcrawler.py -q 'instagram' -t 'followers' -n 300
```

### Full usage of the crawler with OSC messages and timed page refresh:

```
  usage: python timed_crawler.py [-q QUERY] [-t TYPE] [-n NUMBER] [-c] [-d DIR] [-r] [-m] [--osc] [--ip] [--port] [--address]
```

Example (download latest 10 images with tag #test_tag every 10 seconds until 40 seconds have passed and send an OSC message with the filename):
```
    python timed_crawler.py -q '#test_tag' -n 10 -r 10 -m 40 --osc 1 --ip 127.0.0.2 --port 5006
```
  - [-q QUERY] : username, add '#' to search for hashtags, e.g. 'username', '#hashtag'
  - [-t TYPE] : specify 'photos','followers' or 'following'
  - [-c]: add this flag to download captions(what user wrote to describe their photos) if TYPE is 'photos'
  - [-n NUMBER]: number of posts, followers, or following to crawl,  
  - [-d DIR]: the directory to save crawling results, default is './data/[query]'
  - [-r]: refresh rate in seconds, default is 25 seconds
  - [-m]: maximum running time in seconds, if -1, will run infinitely, default is 100
  - [--osc]: if 0, won't send OSC messagesm if 1, will send, default is 0
  - [--ip]: IP address of the OSC server, default is 127.0.0.1
  - [--port]: The port the OSC server is listening on, default is 5005
  - [--address]: The address to which the OSC messages will be sent, default is "/image"

### Full usage of the basic crawler:
```
  usage: instagramcrawler.py [-h] [-q QUERY] [-t TYPE] [-n NUMBER] [-c] [-d DIR]
```
  - [-q QUERY] : username, add '#' to search for hashtags, e.g. 'username', '#hashtag'
  - [-t TYPE] : specify 'photos','followers' or 'following'
  - [-c]: add this flag to download captions(what user wrote to describe their photos) if TYPE is 'photos'
  - [-n NUMBER]: number of posts, followers, or following to crawl,  
  - [-d DIR]: the directory to save crawling results, default is './data/[query]'

### Installation

  There are 2 packages : selenium & requests-futures
```
$ pip install -r requirements.txt
```
