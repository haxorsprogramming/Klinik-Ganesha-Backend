from decouple import config

author = config('USER')

print(author)