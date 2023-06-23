def insert_command(tablename, **values):
    colnames, colvalues = "", ""
    for key, val in values.items():
        if colnames != "":
            colnames += ", "
            colvalues += "', '"
        colnames += key
        colvalues += val
    cmd = f"INSERT INTO {tablename} ({colnames}) VALUES ('{colvalues}')"
    return cmd


print(insert_command('clients', nomprenom="Mohamed Ali", numtel="23456789"))