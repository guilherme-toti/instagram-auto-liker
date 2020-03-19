## Instagram Auto Liker

This is a crawler that likes Instagram posts based on hashtags each 10 seconds

## Setup

This project needs only Selenium to be installed on your Python environment

```
pip install selenium
``` 

## Settings

All you need to do is change the settings:

```
CONFIGS = {
    'USERNAME': 'YOUR_USERNAME',
    'PASSWORD': 'YOUR_PASSWORD',
    'HASHTAGS': [
        'FIRST_HASHTAG', 'SECOND_HASHTAG', 'THIRD_HASHTAG'
    ],
    'TOTAL_LIKES_PER_HASHTAG': 300, # amount of posts to like per hashtag
    'SYSTEM': 'windows/mac/linux'
}
```

## Running

After changing the settings, just run it as:

```
python run.py
```

And let it work :)


## Known Issues

- If you already liked the photo, the crawler will unlike it.