#task 4
me = {"name" : 'Tigran',
      "last name" : "Sargsyan",
      "age" : 19,
      "height" : 1.90,
      "weight" : 86,
      "gender" : "male"
     }
name = me.get("name")
print(name)
yngerner = {"Tigran" : {"name" : "Tigran",
                    "last_name" : "Sargsyan",
                    "mid_name" : "Kareni"
                    },
            "Hamlet" : {"name" : "Hamlet",
                    "last_name" : "Ghevondyan",
                    "mid_name" : "Gariki"
                    },
            "Gagik" : {"name" : "Gagik",
                    "last_name" : "Melqonyan",
                    "mid_name" : "Rafiki"
                    },
            "Simon" : {"name" : "Simon",
                       "last_name" : "Mnacakanyan",
                       "mid_name" : "Lerniki"
                    }
            }
simon = yngerner.get("Simon")
simon["age"] = 18
print(simon)