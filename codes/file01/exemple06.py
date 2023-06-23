def connection_string(**options):
    res = ""
    for key, value in options.items():
        res += f"{key}={value};"
    return res[:-1]


print(connection_string(Server="localhost", 
                        Uid="salah", 
                        Pwd="1234", 
                        Database="location"))
