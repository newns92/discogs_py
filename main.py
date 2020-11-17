import os
import discogs_client
import oauth2 as oauth


def read_keys():
    print(os.getcwd())
    file = open('..\discogs_keys.txt', 'r')
    lines = file.readlines()
    # for line in file:
    consumer_key = lines[0].split(":")[1]
    consumer_secret = lines[1].split(":")[1]
    print(consumer_key)
    print(consumer_secret)


if __name__ == '__main__':
    read_keys()
