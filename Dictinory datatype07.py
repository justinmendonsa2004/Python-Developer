d = {"key1": "justin", "key2": "hacker"}

print(d.values())
print(d.keys())
print(d["key1"])

# d["key3"] = "shadow"
# del d["key2"]
d2 = d.copy()

d3 = d2.update({"key3": "shadow"})
print(d)
