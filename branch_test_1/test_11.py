my_dict = { "fruit" : "Grapes",
            "veggie" : "Carrot",
            "nut" : "Almonds"
          }

for key, value in my_dict.items():
    print(key, "--->", value)

my_dict.update({"leaves":"Spinach"})
print(my_dict)



