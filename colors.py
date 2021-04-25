import json

with open('colors.json') as f:
    colors = json.loads(f.read())

Home = colors['Home']