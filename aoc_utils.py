from typing import Iterator

import requests


"""
Get problem input for Advent of code
"""
def get_input(input_url) -> Iterator[str]:
    cookies = {}
    
    with open("session.txt", mode="rt", encoding="utf-8") as f:
        cookies["session"] = f.read()
        
    with requests.get(input_url, cookies=cookies) as r:
        if r.status_code != requests.codes["ok"]:
            raise requests.HTTPError(response=r)
        
        return r.iter_lines(decode_unicode=True, delimiter="\n")