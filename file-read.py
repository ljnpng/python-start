import os
tokepath = os.path.join(os.environ['HOME'], '.githubtoken')
file = open(tokepath, 'r')
print(file.read())