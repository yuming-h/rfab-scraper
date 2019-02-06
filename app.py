import requests
from contextlib import closing
from bs4 import BeautifulSoup
from user import User


# compares 2 lists of hrefs for forum posts and returns the ones from the same thread
def same_threads(l_1, l_2):
    set_1 = set(l_1)
    set_2 = set(l_2)

    common = set_1 & set_2
    return common


def main():
    username_1 = input("First Username: ")
    username_2 = input("Second Username: ")

    user_1 = User(username_1)
    user_2 = User(username_2)

    posts_1 = user_1.get_posts()
    posts_2 = user_2.get_posts()

    common_posts = same_threads(posts_1, posts_2)
    if len(common_posts) > 0:
        print(common_posts)
    else:
        print("No posts found!")
        
    print("Done!")

if __name__ == "__main__":
    main()