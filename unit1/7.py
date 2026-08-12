stud = {
        "name": "Prince",
        "rno": 48,
        "uni_name": "Marwadi",
        "is_pass": True
    }

def msg():
    for key, value in stud.items():
        print(key, ": ", value)

msg()

stud["name"] = "Prince Gupta"
print("\nUpdated name: ", stud.get("name"), "\n")

stud.pop("rno")
msg()

stud["rno"] = 48
print()
msg()
