
#version 1
# def save_to_log(entry, logfile):
#     f = open(logfile, "a")
#     f.write("\n\r" + entry)
#     f.close()

# save_to_log("hey there", "yada.txt")

def save_to_log(entry, logfile):
    logs = None
    try:
        logs = open(logfile, 'a')
    except IOError as err:
        print(err)
    else:
        logs.write("\n\r" + entry)
    finally:
        if logs != None:
            logs.close()

save_to_log("hey there", "yada.txt")