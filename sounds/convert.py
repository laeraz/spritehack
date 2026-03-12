import base64

file_name = input("enter file name plz $$$: ")

try:
    with open(file_name, "rb") as f:
        encoded = base64.b64encode(f.read())

    with open("output.txt", "wb") as out:
        out.write(encoded)

    print("base64 saved to output.txt")

except Exception as e:
    print("error:", e)

input("press enter to exit...")