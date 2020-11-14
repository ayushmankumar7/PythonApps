from moviepy.editor import * 


def output_name(name):
    name = name.split('/')[-1]
    name = name.split('.')[0]
    return name + '.mp3'


# print(output_name(' C:/Users/ayush/Videos/2020-08-11_16-08-20.mp4'))

def convert(mp4_name):
    
    mp3_file = output_name(mp4_name)
    videoclip = VideoFileClip(mp4_name)
    audioclip = videoclip.audio
    audioclip.write_audiofile(mp3_file)
    audioclip.close()
    videoclip.close()




