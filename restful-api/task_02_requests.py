#!/usr/bin/python3
"""
Module that def a function

"""
import requests
import json
import csv


def fetch_and_print_posts():
    data = ""
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    print("Status Code:", r.status_code)

    if r.status_code == 200:
        data = r.json()

        for d in data:
            print(f"{d['title']}")


def fetch_and_save_posts():
    data = ""
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    
    if r.status_code == 200:
        data = r.json()

        info = []
        for d in data:
            info.append({
                'id': d['id'],
                'title': d['title'],
                'body': d['body']
                })

        with open("posts.csv", "w", newline="") as file:
            csvR = csv.DictWriter(file, fieldnames=["id", "title", "body"])

            csvR.writeheader()
            csvR.writerows(info)
