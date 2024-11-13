student_data = {
    "id1"  : { 
        "name" : "Jamal", 
        "grade" : "7"
        },
     "id2"  : { 
        "name" : "Jo", 
        "grade" : "7"
        },
    "id3"  : { 
        "name" : "Jo", 
        "grade" : "7"
        },
    "id4"  : { 
        "name" : "Potter", 
        "grade" : "7"
        },
}

result = {}

for key, value in student_data.items():
    if value not in result.values():
        result [key] = value 

print(result)