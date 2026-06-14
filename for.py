#counting from 1 to 10
#for i in range(1, 11):
   # print("Number " + str(i))

color =  input("Enter a color(red,yellow,greeen): ").lower()
match color:
    case "red" | "yellow":
        print("stop!!")
    case "green":
        print("go!!")
    case _:
        print("invalid color")    