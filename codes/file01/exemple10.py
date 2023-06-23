# file01/exemple10.py
def select_command(tablename, *cols):
    colnames = ""
    for col in cols:
        if colnames != "":
            colnames += ", "
        colnames += col
    if colnames == "":
        colnames = "*"
    cmd = f"SELECT {colnames} FROM {tablename}"
    return cmd

print(select_command("clients"))
print(select_command("eleves", "nomprenom", "datenaiss"))
