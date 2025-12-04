import msvcrt as msv
# COLORS
RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

# ASCII FONT DATA
data = [
    " ***  ****   ***  ****  ***** *****  ***  *   * ***** ***** *   * *     *   * *   *  ***  ****   ***   ****   ****  ***** *    * *   * *   * *   * *   * *****        ***                     ***  ***   ****  ****  *   * *****  ***  *****  ***  ***** ",
    "*   * *   * *   * *   * *     *     *     *   *   *      *  *  *  *     ** ** **  * *   * *   * *   *  *   *  *       *   *    * *   * *   *  * *   * *     *        * ***                   *   *   *       *     * *   * *     *         * *   * *   * ",
    "*   * ****  *     *   * ***   ****  *  ** *****   *      *  ***   *     * * * * * * *   * ****  *   *  ****   *****   *   *    * *   * * * *   *     *     *         * * *       *****       *   *   *       *   **  ***** ****  ****      *  ***  ***** ",
    "***** *   * *   * *   * *     *     *   * *   *   *   *  *  *  *  *     *   * *  ** *   * *     *   *  *  *       *   *   *    *  * *  ** **  * *    *    *          * * *              ***  *   *   *   ***       *     *     * *   *     * *   *     * ",
    "*   * ****   ***  ****  ***** *      ***  *   * *****  ***  *   * ***** *   * *   *  ***  *      *** * *   *  ****    *    *****   *   *   * *   *   *   *****        ***  *****        ***   ***  ***** ***** ****      * ****   ***      *  ***      * "
]

LOGOS = {
    "HEART": [
        " **   ** ",
        "*********",
        " ********",
        "  ****** ",
        "    **   ",
    ],
    "SMILE": [
        "         ",
        "*  *  *  ",
        "         ",
        "*      * ",
        "  ****   ",
    ],
    "DIAMOND": [
        "   *   ",
        "  ***  ",
        " ***** ",
        "  ***  ",
        "   *   "
    ]
}

current_scale = 1          # 1 = small, 2 = medium, 3 = large
last_output = ""           # stores last ASCII art (for saving)

def scale_font(lines, scale):
    """Scale a 5xN ASCII block by 'scale' factor."""
    if scale == 1:
        return lines

    output = []
    for line in lines:
        expanded = "".join(ch * scale for ch in line)
        for _ in range(scale):
            output.append(expanded)
    return output


def display_logo(name, scale=1):
    """Display one of the predefined ASCII logos."""
    name = name.upper()
    if name not in LOGOS:
        print(RED + "Logo not found!" + RESET)
        return ""

    scaled = scale_font(LOGOS[name], scale)
    art = "\n".join(scaled)
    print(CYAN + art + RESET)
    return art


def save(content):
    if not content.strip():
        print(RED + "\nNothing to save! Generate something first.\n" + RESET)
        return

    filename = "ascii_output.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

    print(GREEN + f"\nSaved to {filename}\n" + RESET)

def ooc():
    print(YELLOW + "+-------------------------------+" + RESET)
    print(CYAN   + "| For Printing Single Character |" + RESET)
    print(YELLOW + "+-------------------------------+" + RESET)
    print()
    print(YELLOW + "+-------------------------------+" + RESET)
    print(MAGENTA + "|       Enter Character --      |" + RESET)
    print(YELLOW + "+-------------------------------+" + RESET)
    text = input(MAGENTA + "Enter here: " + RESET).upper()
    if len(text) != 1:
        print("\n\nPlease Enter Only One Letter -- \n\n")
        ooc()
    else:
        print(YELLOW + "+-------------------------------+" + RESET)
        print(GREEN +  "|      You entered:  " + text +"          |" + RESET)
        print(YELLOW + "+-------------------------------+" + RESET)
        n = (ord(text)-17)*6 if ord(text)>=48 and ord(text) <= 57 else 26*6 if text ==" " else 27 * 6 if text == "@" else 28 * 6 if text == "_" else 29 * 6 if text == "-" else 30 * 6 if text == "." else ((ord(text) - 64)-1)*6
        for i in data:
            for j in range(n , n + 6):
                print(i[j],end="")
            print()

def logo():
    global last_output
    print(YELLOW + "+-------------------------------+" + RESET)
    print(CYAN   + "|       ASCII ART LOGOS         |" + RESET)
    print(YELLOW + "+-------------------------------+" + RESET)
    print(GREEN + "Available Logos: HEART, SMILE, DIAMOND" + RESET)

    name = input(MAGENTA + "Enter logo name: " + RESET).upper()
    art = display_logo(name, current_scale)
    if art:
        last_output = art

def wrd():
    print(YELLOW + "+----------------------+" + RESET)
    print(CYAN   + "|   For Printing Words |" + RESET)
    print(YELLOW + "+----------------------+" + RESET)
    print(YELLOW + "+-------------------------------+" + RESET)
    print(MAGENTA + "|        Enter Word --          |" + RESET)
    print(YELLOW + "+-------------------------------+" + RESET)
    text = input(MAGENTA + "Enter here: " + RESET).upper()
    print(GREEN + "You entered: " + text + RESET)
    if not (len(text)>=1 and len(text)<=15):
        print("\n\nPlease Enter Only <=15 Letter -- \n\n")
        wrd()
    else:
        print(YELLOW + "+-------------------------------------------+" + RESET)
        print(GREEN +  "|      You entered:  " + text +"                  |" + RESET)
        print(YELLOW + "+-------------------------------------------+" + RESET)
        for i in data:
            for x in text:
                n =(ord(x)-17)*6 if ord(x)>=48 and ord(x) <= 57 else 26*6 if x ==" " else 27 * 6 if x == "@" else 28 * 6 if x == "_" else 29 * 6 if x == "-" else 30 * 6 if x == "." else ((ord(x) - 64)-1)*6 
                for j in range(n , n + 6):
                    print(i[j],end="")
            print()



def alp():
    print(YELLOW + "+---------------------------------+" + RESET)
    print(CYAN   + "| For Printing Single Alphabets   |" + RESET)
    print(YELLOW + "+---------------------------------+" + RESET)
    print(YELLOW + "+-----------------------------------------+" + RESET)
    print(MAGENTA + "|        Enter Only Alphabets --          |" + RESET)
    print(YELLOW + "+-----------------------------------------+" + RESET)
    text = input(MAGENTA + "Enter here: " + RESET).upper()
    print(GREEN + "You entered: " + text + RESET)
    if not (len(text)>=1 and len(text)<=15):
        print("\n\nPlease Enter Only <=15 Letter -- \n\n")
        msv.getch()
        alp()
    else:
        if text.isalpha() == False:
            print("\n\nPlease Enter Only Alphabets -- \n\n")
            msv.getch()
            alp()
        else:
            print(YELLOW + "+-------------------------------+" + RESET)
            print(GREEN +  "|      You entered:  " + text +"          |" + RESET)
            print(YELLOW + "+-------------------------------+" + RESET)
            for i in data:
                for x in text:
                    n =((ord(x) - 64)-1)*6
                    for j in range(n , n + 6):
                        print(i[j],end="")
                print()


def num():
    print(YELLOW + "+-------------------------------+" + RESET)
    print(CYAN   + "| For Printing Single Numbers   |" + RESET)
    print(YELLOW + "+-------------------------------+" + RESET)
    print(YELLOW + "+---------------------------------------+" + RESET)
    print(MAGENTA + "|        Enter Numbers Only --          |" + RESET)
    print(YELLOW + "+---------------------------------------+" + RESET)
    text = input(MAGENTA + "Enter here: " + RESET).upper()
    print(GREEN + "You entered: " + text + RESET)
    if not (len(text)>=1 and len(text)<=15):
        print("\n\nPlease Enter Only <=15 Letter -- \n\n")
        msv.getch()
        num()
    else:
        if text.isnumeric() == False:
            print("\n\nPlease Enter Only Numbers -- \n\n")
            msv.getch()
            num()
        else:
            print(YELLOW + "+-------------------------------+" + RESET)
            print(GREEN +  "|      You entered:  " + text +"          |" + RESET)
            print(YELLOW + "+-------------------------------+" + RESET)
            for i in data:
                for x in text:
                    n =(ord(x)-17)*6 if ord(x)>=48 and ord(x) <= 57 else ((ord(x) - 64)-1)*6 
                    for j in range(n , n + 6):
                        print(i[j],end="")
                print()

def ui():
    print(YELLOW + "+----------------------+" + RESET)
    print(CYAN   + "|     ASCII ART MENU   |" + RESET)
    print(YELLOW + "+----------------------+" + RESET)
    
    print(YELLOW + "+--------------------------------+" + RESET)
    print(CYAN   + "|  Options that you can choose:  |" + RESET)
    print(YELLOW + "+--------------------------------+" + RESET)

    print(YELLOW + "+----------------------+" + RESET)
    print(GREEN  + "| 1.Only One Character |" + RESET)
    print(YELLOW + "+----------------------+" + RESET)

    print(YELLOW + "+----------------------+" + RESET)
    print(GREEN  + "|     2.Words          |" + RESET)
    print(YELLOW + "+----------------------+" + RESET)

    print(YELLOW + "+----------------------+" + RESET)
    print(GREEN  + "|    3.Only Alphabets  |" + RESET)
    print(YELLOW + "+----------------------+" + RESET)

    print(YELLOW + "+----------------------+" + RESET)
    print(GREEN  + "|  4.Only Numbbers     |" + RESET)
    print(YELLOW + "+----------------------+" + RESET)

    print(YELLOW + "+----------------------+" + RESET)
    print(GREEN  + "|   5.Art Logos        |" + RESET)
    print(YELLOW + "+----------------------+" + RESET)

    print(YELLOW + "+----------------------+" + RESET)
    print(GREEN  + "|  6.Save Output       |" + RESET)
    print(YELLOW + "+----------------------+" + RESET)

    print(YELLOW + "+----------------------+" + RESET)
    print(RED    + "|   7.Exit             |" + RESET)
    print(YELLOW + "+----------------------+" + RESET)

    press = msv.getch().decode()
    
    if press == "1":
        ooc()
    elif press == "2":
        wrd()
    elif press == "3":
        alp()
    elif press == "4":
        num()
    elif press == "5":
        logo()
    elif press == "6":
        save()
    elif press == "7":
        exit()
    
    print(YELLOW + "+---------------------------------------------------------+" + RESET)
    print(GREEN  +"|Do you want to continue Project.. Press y else any key...|" + RESET)
    print(YELLOW + "+---------------------------------------------------------+" + RESET)
    ch = msv.getch()
    if ch.decode() == "y" or ch.decode() == "Y":
        ui()
ui()
