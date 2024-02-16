import os
paths = list(os.walk("."))
for path in os.walk("."):
    print(path)
