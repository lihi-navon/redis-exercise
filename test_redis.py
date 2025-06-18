import redis
from redis.commands.json.path import Path
r = redis.Redis(host='redis', port=6379, db=0)

r.delete('secret_key')

print(r.set('secret_key', 'passsword1'))

print(r.get('secret_key'))

print(r.set('secret_key', 'passsword_will_expire_boom', ex=5))

# Define JSON object
data = {
    "user": {
        "name": "Alice",
        "age": 30,
        "skills": ["Python", "Redis"]
    }
}

# SET JSON data at root "$"
print(r.json().set("user_1", Path.root_path(), data))



print(r.json().get("user_1"))


print(r.json().get("user_1", Path(".user.name")))




print(r.json().set("user_1", ".user.age", 31))



print(r.json().get("user_1"))


print(r.json().set("user_1", ".user",{'name': 'Lihi', 'age': 19, 'skills': ['Python', 'Redis', 'JS']}))




value = r.json().get("user_1", Path(".user.skills"))
value.append("ubuntu")
print(r.json().set("user_1", ".user.skills ",value))

print(r.json().get("user_1"))


print(r.json().arrappend("user_1", ".user.skills ", "driving"))


print(r.json().get("user_1"))



print(r.json().arrinsert("user_1", ".user.skills ", 1,  "swimming"))




print(r.json().get("user_1"))


print(r.json().set("user_1", ".user.friends ",[]))




print(r.json().get("user_1"))




print(r.json().clear("user_1"))



print(r.json().get("user_1"))



print(r.json().delete("user_1", ".user.age"))


# Define JSON object
data = {
    "user": {
        "name": "Alice",
        "age": 30,
        "skills": ["Python", "Redis"]
    }
}

# SET JSON data at root "$"
print(r.json().set("user_1", Path.root_path(), data))


print(r.json().merge("user_1", Path.root_path(), {"user2":{"playing":True}}))


print(r.json().get("user_1"))



print(r.json().numincrby("user_1",".user.age", 1))

print(r.json().get("user_1"))

print(r.json().objlen("user_1", ".user"))

print(r.json().arrlen("user_1", ".user.skills"))


print(r.json().objkeys("user_1", ".user"))


print(r.json().get("user_1",".user").keys())


print(r.json().strlen("user_1",".user.name"))


print(r.json().get("user_1",".user.name"))




print(r.json().get("user_1"))


print(r.json().strappend("user_1", path=Path(".user.name"), value="lihi"))


