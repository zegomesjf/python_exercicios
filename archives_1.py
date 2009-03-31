def string_address(address):
    var = address[0]
    for  i in range(1, 4):
        var = var + "." + address[i]
    return var

def write_archive(name_archive, string_list):
    archive = open(name_archive, "w")
    for i in range(len(string_list)):
        archive.write(string_list[i])    
    archive.close()    

f = open("addresses.txt", "r")
addresses = f.readlines()

valid_addresses = []
invalid_addresses = []

for i in range(len(addresses)):
    address = addresses[i].split(".")
    valid = 1;
    str_address = ""
    for var in range(len(address)):
        if int(address[var]) > 255:
            valid = 0
    if (valid == 1):
        valid_addresses.append(string_address(address))
    else:
        invalid_addresses.append(string_address(address))
        
f.close()

write_archive("valid_addresses.txt", valid_addresses)
write_archive("invalid_addresses.txt", invalid_addresses)

