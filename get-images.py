import json
import sys
import requests
import time

def load_tweets(filename='cursed_architecture_archive.json'):
    try:
        with open(filename) as json_file:
            tweets = json.load(json_file)
            return tweets
    except IOError:
        print("no "+filename+" found\ndid you run:\n./build_archive.sh")
        sys.exit(1)

def grab_image(url):
    if url.split('/')[3] != "media":
        return ""

    r = requests.get(url)
    if r.status_code > 299:
        return ""

    return r.content

def save_image(img,url):
    if (len(img) == 0):
        return False
    filename=url.split('/')[-1]
    with open("images/"+filename, 'wb') as f:
        f.write(img)
    return True

def main():
    tweets = load_tweets()
    for tweet in tweets:
        try:
            for pic in tweet['entities']['media']:
                url = pic['media_url_https']
                img = grab_image(url)
                success = save_image(img, url)
                if (success):
                    print("downloaded "+url)
                else:
                    print("could not download"+url)
                # please don't rate limit me
                # time.sleep(10)
        except KeyError:
            pass
            

if __name__ == "__main__":
    main()
