import json, requests

REDDIT = 'http://reddit.com/'

class Post:
    def __init__(self, title = '', body = '', author = '', votes = 0, thumbnail = '', over_18 = False, permalink = '', url = '', build_comments = False):
        self.title = title
        self.body = body
        self.author = author
        self.votes = votes
        self.thumbnail = thumbnail
        self.over_18 = over_18,
        self.permalink = permalink,
        self.url = url
        self.build_comments = build_comments
        self.comments = []

        if build_comments:
            # Get the comments
            p = f'{REDDIT}{permalink}.json'
            page = Web.get_json(p)

            comments_dict = page[1]['data']['children']
            
            for i in comments_dict:
                comment = i['data']
                try:
                    append_comment = Comment(
                        body = comment['body'],
                        votes = comment['ups'],
                        author = comment['author'],
                        edited = comment['edited'],
                        stickied = comment['stickied'],
                        permalink = comment['permalink']
                    )
                except KeyError:
                    break
                
                self.comments.append(append_comment)

class Comment:
    def __init__(self, body = '', votes = 0, author = '', edited = False, stickied = False, permalink = ''):
        self.body = body
        self.votes = votes,
        self.author = author
        self.edited = edited
        self.stickied = stickied
        self.permalink = permalink

class Listing:
    HOT = '/.json'
    NEW = '/new/.json'
    class Top:
        PAST_YEAR = '/top/.json?sort=top&t=year'
        PAST_24 = '/top/.json?sort=top&t=day'
        PAST_WEEK = '/top/.json?sort=top&t=week'
        PAST_MONTH = '/top/.json?sort=top&t=month'
        ALL_TIME = '/top/.json?sort=top&t=all'

class Web:
    @staticmethod
    def get_json(page):
        r = requests.get(page, headers = {'User-Agent': 'Reddit TTS Generator (u/NathanBitTheMoon)'})
        return json.loads(r.content)

class Subreddit:
    def __init__(self, subreddit_name, listing, build_comments = False):
        self.subreddit_name = subreddit_name

        self.page_url = f'{REDDIT}r/{subreddit_name}{listing}'
        self.page_content = Web.get_json(page = self.page_url)

        posts = self.page_content['data']['children']
        self.posts = []

        for i in posts:
            post = i['data']
            append_post = Post(
                title = post['title'],
                author = post['author'],
                votes = post['ups'],
                thumbnail = post['thumbnail'],
                over_18 = post['over_18'],
                permalink = post['permalink'],
                url = post['url'],
                build_comments = build_comments,
                body = post['selftext']
            )

            self.posts.append(append_post)