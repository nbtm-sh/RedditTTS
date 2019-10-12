import gtts

class Format:
    replace = {
        '%t': 'title',
        '%b': 'body',
        '%a': 'author',
        '%u': 'votes'
    }

    def __init__(self, format_string, format_object):
        self.format_string = format_string
        for k, v in zip(Format.replace.keys(), Format.replace.values()):
            self.format_string = self.format_string.replace(k, str(getattr(format_object, v)))

class TTS:
    class Post:
        def __init__(self, post, format = '%t.%b'):
            self.post = post
            self.input_string = Format(format, post)

            self.tts = gtts.gTTS(self.input_string.format_string, lang = 'en')