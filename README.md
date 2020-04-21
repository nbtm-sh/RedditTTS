# RedditTTS
For lazily creating the reddit videos you see all over youtube

## Dependencies
* moviepy
* requests
* gtts

## Creating videos
You will use the `videogen.py` script to create the videos. Edit the first few lines of the file and run the script to create the video.
```python
sub = reddit.Subreddit('<subreddit>', reddit.Listing.<Listing>)

for i in range(post_count):
   ....
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
