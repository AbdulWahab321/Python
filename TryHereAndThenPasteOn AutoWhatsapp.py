from datetime import datetime
import pywhatkit

now = datetime.now()
print(now.strftime("Year:%Y %D"))
print(now.strftime("%H:%M:%S"))
print("type G to send message to group and P to send privately")
conf = str(input("To where you want to send message group or private: "))


def ask():
    print("type 0 to not to shutdown your pc")
    shut = int(input("ShutDown your pc in second: "))

    if shut == 0:
        print("Your pc will not shut down")
    else:
        pywhatkit.shutdown(shut)
        print(f"Your pc will shut down in {shut} seconds")
c = 1
num = "+91"


if conf == "P":
    print("Mode: Send Message Private ")
    print("Type your country code down")
    country = str(input("Type your country code: "))
    num = country
    if country.isalpha() or "'" in country or "/" in country or '*' or '"' in country or '!' in country or '@' in country or '#' in country or '$' in country or '%' in country or '^' in country or '&' in country or '*' in country or '(' in country or ')' in country or ';' in country or ':' in country or '<' in country or '>' in country or ',' in country or '.' in country or "?" in country:

        while country.isalpha() or "/" in country or '*' in country  or '!' in country or '@' in country or '#' in country or '$' in country or '%' in country or '^' in country or '&' in country or '*' in country or '(' in country or ')' in country  or ';' in country or ':' in country or '<' in country or '>' in country or ',' in country or '.' in country or "?" in country or "=" in country:
            print("Incorrect Code Please Try Again")
            country = str(input("Type your country code: "))
        else:
            print(f"{num} is added automatically")
            num = country
            n = str(input("Number:"))
            if "+" in n:
                while "+" in n:
                    print(f"{num} is added automatically")
                    n = str(input("Number:"))
                else:
                    if n.isalpha() or "/" in n or '*' in n or '!' in n or '@' in n or '#' in n or '$' in n or '%' in n or '^' in n or '&' in n or '*' in n or '(' in n or ')' in n or ';' in n or ':' in n or '<' in n or '>' in n or ',' in n or '.' in n or "?" in n or "=" in n:
                        while n.isalpha() or "/" in n or '*' in n or '!' in n or '@' in n or '#' in n or '$' in n or '%' in n or '^' in n or '&' in n or '*' in n or '(' in n or ')' in n or ';' in n or ':' in n or '<' in n or '>' in n or ',' in n or '.' in n or "?" in n or "=" in n:
                                 print("Incorrect Code Please Try Again")
                                 n=str(input("Number:"))
            else:
                m = str(input("message: "))

                h = input("24 hour format: ")
                minut = input("minute: ")

                sum = num+n
                ho = int(h)
                mi = int(minut)

                print(" ")
                print(" ")
                print(f"To: {sum}")
                print(f"Message: {m}")
                print(f"Message will be send on: {ho}:{mi} ")

                print("Please wait to open whatsapp web after that a input will appear if you need to shutdown your computer you can type")
                pywhatkit.sendwhatmsg(sum, m, ho, mi)
                print(" ")
                print("Do you want To try more features?")
                fea = str(input("Type Y if you need and N if you don't want: "))
                print(" ")
                if fea == "Y":
                    print("Type Y to go and search on Youtube and G To search on Google")
                    confFea = str(input("Where do you want to Search on youtube or google: "))
                    if confFea == "Y":
                        searc = str(input("What do you want to search: "))
                        pywhatkit.playonyt(searc, True)
                        print("Thank You See You Again")
                        ask()
                    elif confFea == "G":
                        searc1 = str(input("What do you want to search: "))
                        pywhatkit.search(searc1)
                        print("Thank You See You Again")
                        ask()
                elif fea == "N":
                    print("Thank You See You Again")
                    ask()
                else:
                    while fea is not "Y" and "N":
                        print("Sorry unknown command")
                        fea = str(input("Type Y if you need and N if you don't want: "))
                        if fea == "Y":
                            print("Type Y to go and search on Youtube and G To search on Google")
                            confFea = str(input("Where do you want to Search on youtube or google: "))
                            if confFea == "Y":
                                print(" ")
                                searc = str(input("What do you want to search: "))
                                pywhatkit.playonyt(searc, True)
                                print(" ")
                                print("Do you want to try again?")
                                print("Type Y for Yes and N for No")
                                confTry = str(input("Type Y for Yes and N for No"))
                                if confTry == "Y":
                                    print("Type Y to go and search on Youtube and G To search on Google")
                                    confFea = str(input("Where do you want to Search on youtube or google: "))
                                    if confFea == "Y":
                                        searc = str(input("What do you want to search: "))
                                        pywhatkit.playonyt(searc, True)
                                    elif confFea == "N":
                                        print("Thank You See You Again")
                                        ask()
                                    else:
                                        print("Unknown command")
                            elif confFea == "G":
                                searc1 = str(input("What do you want to search: "))
                                pywhatkit.search(searc1)
                        elif fea == "N":
                            print("Thank You See You Again")
                            ask()
elif conf=="G":
    print("Mode: Send Message To Group ")
    print("  ")
    print("How to get group id?")
    print("Go to Group info and click invite then copy link and paste it anywhere and copy the suffix")
    print("part of the link and paste it down")
    print("eg: on https://chat.whatsapp.com/KOlwnHs92HBGYT3KKJll1 this is the suffix part 'KOlwnHs92HBGYT3KKJll1'")
    print(" ")
    g = input("Group id: ")

    mess = str(input("message: "))

    hou = int(input("24 hour format: "))
    min = int(input("minute: "))

    sum = g

    print(" ")
    print(" ")
    print(f"To: {sum}")
    print(f"Message: {mess}")
    print(f"Message will be send on: {hou}:{min} ")

    pywhatkit.sendwhatmsg_to_group(sum, mess, hou, min)
    print(" ")
    print("Do you want To try more features?")
    fea = str(input("Type Y if you need and N if you don't want: "))
    print(" ")
    if fea == "Y":
        print("Type Y to go and search on Youtube and G To search on Google")
        confFea = str(input("Where do you want to Search on youtube or google: "))
        if confFea == "Y":
                 searc = str(input("What do you want to search: "))
                 pywhatkit.playonyt(searc, True)
                 print("Thank You See You Again")
                 ask()
        elif confFea == "G":
            searc1 = str(input("What do you want to search: "))
            pywhatkit.search(searc1)
            print("Thank You See You Again")
            ask()
    elif fea == "N":
        print("Thank You See You Again")
        ask()
    else:
        while fea is not "Y" and "N":
            print("Sorry unknown command")
            fea = str(input("Type Y if you need and N if you don't want: "))
            if fea == "Y":
                print("Type Y to go and search on Youtube and G To search on Google")
                confFea = str(input("Where do you want to Search on youtube or google: "))
                if confFea == "Y":
                    print(" ")
                    searc = str(input("What do you want to search: "))
                    pywhatkit.playonyt(searc, True)
                    print(" ")
                    print("Do you want to try again?")
                    print("Type Y for Yes and N for No")
                    confTry = str(input("Type Y for Yes and N for No"))
                    if confTry == "Y":
                        print("Type Y to go and search on Youtube and G To search on Google")
                        confFea = str(input("Where do you want to Search on youtube or google: "))
                        if confFea == "Y":
                            searc = str(input("What do you want to search: "))
                            pywhatkit.playonyt(searc, True)
                            ask()
                        elif confFea == "N":
                            print("Thank You See You Again")
                            ask()
                        else:
                            print("Unknown command")
                elif confFea == "G":
                    searc1 = str(input("What do you want to search: "))
                    pywhatkit.search(searc1)
            elif fea == "N":
                print("Thank You See You Again")
                ask()


else:
    while conf is not "G":
        if conf is not "P":
            print("Invalid Character Please type G or P")
            conf = str(input("To where you want to send message group or private"))

