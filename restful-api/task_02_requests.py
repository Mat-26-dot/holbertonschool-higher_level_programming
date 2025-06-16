

import requests

def fetch_and_print_posts():
    
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url) # parse the json to parse response data
    print(f"Status Code:", {response.status_code})
    if response .status_code == 200: # print status code if ok = 200
        posts = response.json() # Convert JSON to python list of dicts
        for post in posts: # iterate through posts and print each title
            print("Title:", post['title'])
    else:
        print("Failed to fetch posts")


import csv
import requests

def fetch_and_save_posts():
    
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url) #Parse the JSON to parse response data

    if response.status_code == 200:
        posts = response.json() # Convert JSON to list of dict
        
        post_data = []

        for post in posts:
            post_info = {
            "id": post["id"],
            "title": post["title"],
            "body": post["body"]
        }
        post_data.append(post_info)

        with open ("posts.csv", mode="w", newline="", encoding= "utf-8") as f: # safely opens a file for writing / "utf-8" proper handling of text characters
            writer = csv.DictWriter(f, fieldnames=["id", "title", "body"]) # helps us write dict into CSV rows
            writer.writeheader() # Write column names id, title, body
            writer.writerows(post_data) # Write all rows
            print("Posts saved to posts.csv")
    else:
        print("Failed to fetch posts")

__name__ == "__main__"
fetch_and_print_posts()
fetch_and_save_posts()
