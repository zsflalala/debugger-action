import os
import time

print("Pushing..")
fn = str(time.time())
with open("pushtime/" + str(fn), 'w') as f:
    f.write("https://github.com/orange2008/debugger-action")

os.system('git add . && git commit -m "Run ' + str(fn) + '" && git push')

print("All done! Please check Action page.")
