import speech_recognition as sr 
import moviepy.editor as mp
clip = mp.VideoFileClip(r"project_audio.mp4")
clip.audio.write_audiofile(r"converted_audio.wav")
r = sr.Recognizer()
audio = sr.AudioFile("converted_audio.wav")
with audio as source:
    r.adjust_for_ambient_noise(source)
    audio_file = r.record(source,offset=4)
    result = r.recognize_google(audio_file)


with open('recognized.txt',mode ='w') as file: 
   file.write("Recognized Speech:") 
   file.write("\n") 
   file.write(result) 
   print("text is ready!")
