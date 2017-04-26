import random
import requests

user_agents = []
user_agents_file = open("user_agents.txt", "r") # Text file of user agents

for agents in user_agents_file:
    # cycles through the list adds them to the user_agents array

    user_agents.append(agents)
    random_agents = random.choice(user_agents)[1:-2] # Takes out parens and new line character, also randomizes array choice

url = "http://quotes.toscrape.com"
headers = {"user_agents" : random_agents}

r = requests.get(url, headers=headers)

print r.content