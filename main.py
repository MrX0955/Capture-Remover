print("Your TXT File has to be in same folder with main.py")
file = input("Enter the file name: ").strip()

with open(file, "r", errors="ignore", encoding="utf-8") as f:
    lines = f.readlines()
    savefile = open(f"noncap.txt", "a")
    for line in lines:
        mrx = line.split("\n")[0].split("|")[0].strip()
        savefile.write(mrx+"\n")
