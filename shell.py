from COMP import *
print("""MaMaPy 0.0.1 sur Windows 10""")
print("""Shell MaMaPy 0.0.1""")
codes = []
codes.append("")
count = 0
while True:
    line = input(">>> ")
    if line == "quit" or line == "exit":
        break
    elif line == "help":
        exec(help())
    elif line == "credits":
        print("""Le createur de MaMaPy est Waaberi, son but etait d'apprendre la programmation a sa mere
        Merci a:
        Waaberi Ibrahim
        """)
    else:
        if not line == "finish":
            codes[count] += line+"\n"
        else:
            exec(mamapy_comp(codes[count]))
            count += 1
            codes.append("")