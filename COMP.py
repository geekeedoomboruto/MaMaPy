from jsonUtils import readJson
def stringbefore(string, indexof):
    if not '"' in string:
        return False
    else:
        for i in string:
            if i == '"' and string.index(i) < indexof:
                return True
        return False
def isfunction(string):
    if "(" in string and ")" in string and ("def" in string or "commande" in string or "definit" in string):
        return True
    return False
def isclass(string):
    if "fabrique" in string or "class" in string:
        return True
    return False
def isloop(string):
    cond1 = "pour" in string or "tant que" in string or "while" in string or "for" in string
    cond12 = (">=" in string or "<=" in string or "<" in string or ">" in string or "!=" in string or "==" in string or "est" in string or "dans" in string or "True" in string or "False" in string or "Vrai" in string or "Faux" in string)
    cond2 = ("in" in string or cond12) and cond1
    if cond2:
        return True
    return False
def iscondition(string):
    cond1 = ("si" in string or "encore si" in string or "sinon" in string)
    cond2 = (">=" in string or "<=" in string or "<" in string or ">" in string or "!=" in string or "==" in string or "est" in string or "dans" in string)
    if "sinon" in string:
        if string == "sinon":
            return True
        else:
            ss = string
            try:
                ss = ss.replace("\t", "")
                if ss == "sinon":
                    return True
                else:
                    return False
            except:
                return False
    else:
        if cond1 and cond2:
            return True
        else:
            return False
def mamapy_comp(code):
    grammar = readJson("grammar.json")
    mmpcode = grammar.keys
    pycode = grammar.values
    new_code = ""
    if "\n" in code:
        code = code.split("\n")
        for line in code:
            for i in mmpcode:
                if i in line:
                    ttr = pycode[mmpcode.index(i)]
                    tryline = line.replace(i, "~"+ttr)
                    if stringbefore(tryline, tryline.index("~")):
                        line = line
                    else:
                        line = line.replace(i, ttr)
                if (isfunction(line) and not ":" in line) or (isclass(line) and not ":" in line) or (iscondition(line) and not ":" in line) or (isloop(line) and not ":" in line):
                    line += ":"
                else:
                    line += ""
            new_code += line

    return new_code
def pyfile(code, ofn):
    ofn = ofn.split(".")
    filename = ofn[0]+'.py'
    f = open(filename, "w")
    f.write(code)
    f.close()