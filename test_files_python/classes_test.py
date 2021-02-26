
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

arvid = person("Arvid", 17)
conny = person("Conrad", 18)
dj = person("Fatty", 123)

print(arvid.name, arvid.age)
print(conny.name, conny.age)
print(dj.name, dj.age)


del conny
