import string

class Filters:
    class HasBody:
        name = 'Has Body'
        id_name = 'hasbody'

        @staticmethod
        def match(inp):
            return inp.body == ''
    
    class SpecialChar:
        name = 'Special Characters'
        id_name ='specchar'

        @staticmethod
        def match(inp):
            valid_chars = [e for e in string.ascii_letters + ''.join(['\\' + f for f in string.punctuation]) + string.digits + '\n\r ']
            check_string = inp.title + inp.body

            for i in check_string:
                if i in valid_chars:
                    return False
            return True
    
    class Over18:
        name = 'Over 18'
        id_name = 'over18'

        @staticmethod
        def match(inp):
            return inp.over_18

class PostList:
    def __init__(self, posts):
        self.posts = posts
    
    def filter(self, include = [], exclude = []):
        outputs = []

        for i in self.posts:
            for f in include:
                if f.match(i):
                    outputs.append(i)
        
        for i in self.posts:
            for f in exclude:
                if f.match(i):
                    outputs.remove(i)
        
        return outputs