import os

with open("output.txt", "w") as a:
    for path, subdirs, files in os.walk(r'./test/captured_video'):
       for filename in files:
         f = os.path.join(path, filename)
         f = "video_file=../smart_parkingv1.2/test/captured_video/" + f[22:]
         
         a.write(str(f) + os.linesep) 