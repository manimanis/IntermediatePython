def connection_string(**kwargs):
    res = ""
    for key, value in kwargs.items():
        res += f"{key}={value};"
    return res[:-1]


print(connection_string(Server="localhost", 
                        Uid="salah", 
                        Pwd="1234", 
                        Database="location"))
