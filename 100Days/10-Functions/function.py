def format_name(f_name , l_name):
    if f_name == "" or l_name == "":
        return "flata infomracion"
        return format_name()
    return f"{f_name} {l_name}"


f_name = input('What is your name? : ').title()
l_name = input('What is your last name? : ').title()

print(format_name(f_name , l_name))