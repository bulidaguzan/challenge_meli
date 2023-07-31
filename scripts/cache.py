import redis

r = redis.Redis(host='localhost', port=6380)

r.set("France","Paris")
r.set("Germany","Berlin")
print(r.get("France"))
print(r.get("Germany"))
