

def main():
    text = input("Write a message: ")
    message = convert(text)
    print (message)

def convert(text):
    converted = text.replace(":)", "🙂").replace(":(","🙁")
    return converted 

main()


