import reddit, framegen, tts
from moviepy.editor import ImageSequenceClip, VideoClip, AudioFileClip, VideoFileClip, CompositeVideoClip
from moviepy.editor import concatenate_videoclips

print('Gathering reddit data')
sub = reddit.Subreddit('entitledparents', reddit.Listing.HOT)

frames = []
audio = []

for i in range(3):
    post = sub.posts[i]

    print(f"Generating '{post.title}' frame...'")
    
    frame = framegen.Post(post)
    name = hex(hash(frame)).replace('0x', '') + '.png'

    frame.image.save(name)
    frames.append(name)

    print(f"Generating '{post.title}' audio...'")

    voice = tts.TTS.Post(post)
    name = hex(hash(frame)).replace('0x', '') + '.mp3'

    voice.tts.save(name)
    audio.append(name)

print(frames, audio)


print('Rendering video...')
clips = []

for img, audio in zip(frames, audio):
    clip = ImageSequenceClip([img], fps = 24)
    audio_clip = AudioFileClip(audio)

    clip.audio = audio_clip
    name = 'CLIP_' + hex(hash(img)).replace('0x', '') + '.mp4'
    clips.append(name)

    clip.write_videofile(name)

clip = concatenate_videoclips([VideoFileClip(e) for e in clips])
clip.write_videofile('final.mp4')