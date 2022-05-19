# RedditTTS
For lazily creating the reddit videos you see all over youtube. This entire thing was made to spite the people who make those videos :)

## Dependencies
* moviepy
* requests
* gtts

## Installation
Ensure that the dependencies listed above are installed. You can do this with the `pip3 install <package name>` command (on Windows, run `py -m pip install <package name>`)

Example (Windows):
```cmd
py -m pip install moviepy
```

Example (Linux/MacOS):
```cmd
pip3 install moviepy
```

## Video Creator
Video creation will be handled by the `videogen.py` script. This script, however, is a sample script that is used as a demo but it still works. You can modify the subreddit that it pulls data from, the way the data is sorted, and how many posts are put into the video.

You can modify the `sub` variable to change the subreddit listing / sorting. You can do this by changing the first few lines of the code.
```python
# videogen.py
sub = reddit.Subreddit('<subreddit'>, reddit.Listing.<Listing>) # See below for reddit.Listing properties
```
### Run
Now that you have modified the video creator file, you can run the script with...
```cmd
python3 videogen.py
```
Windows:
```cmd
py videogen.py
```

## reddit.Listing
The reddit.Listing class is where the enum values for different sorting functions.
* `HOT`
* `NEW`
* `Top`
  * `PAST_YEAR`
  * `PAST_24`
  * `PAST_WEEK`
  * `ALL_TIME`
