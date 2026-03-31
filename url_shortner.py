import pyperclip
import json
import webbrowser
print("welcome to url shortner")
def save_url(short_name, original_url_name):
    file_name = "short_urls.json"

    try:
        with open(file_name, "r", encoding="utf-8") as file:
            url_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        url_data = {}

    if short_name in url_data:
        print("Short URL name is not allowed to be the same.")
        return

    if original_url_name in url_data.values():
        print("Long URL name is not allowed to be the same.")
        return

    url_data[short_name] = original_url_name

    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(url_data, file, indent=4)


def get_url(short_name):
    file_name = "short_urls.json"

    try:
        with open(file_name, "r", encoding="utf-8") as file:
            url_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No URL data found.")
        return

    long_url_name = url_data.get(short_name)

    if long_url_name is None:
        print("Short URL not found.")
        return

    print(f"{short_name}: {long_url_name}")
    
    pyperclip.copy(long_url_name)
    print("The long URL has been copied to your clipboard ")

    print(f"{short_name}: {long_url_name}")
    return long_url_name


def remove_url(short_name):
    file_name = "short_urls.json"

    try:
        with open(file_name, "r", encoding="utf-8") as file:
            url_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No URL data found.")
        return

    if short_name not in url_data:
        print("Short URL not found.")
        return

    del url_data[short_name]

    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(url_data, file, indent=4)
    print(f"deleted {short_name}")
def open_website():
    name = input("enter short name for url to open: ")
    long_url_name = get_url(name)  
    if long_url_name:                 
        try:
            webbrowser.open(long_url_name)
            print(f"Opened {long_url_name} in your browser!")
        except:
            print("Error trying to open website")



while True:
    print("enter 1 for saving new url names")
    print("enter 2 for reading url by short url name")
    print("enter 3 for deleting url")
    print("enter 4 to open website from short name")
    print("\n")
    option = input("please enter one of options above: ")

    if option == "1":
        long_url = input("enter long url name: ")
        short_url_name = input("enter short url name: ")
        save_url(short_url_name, long_url)
    elif option == "2":
        short_url = input("enter short url name: ")
        get_url(short_url)
    elif option == "3":
        name_of_short_url_name = input("enter short url name: ")
        remove_url(name_of_short_url_name)
    elif option == "4":
        open_website()
    else:
        print("invalid option")



    
