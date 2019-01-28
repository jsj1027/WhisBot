txt_file = open("replace_me.txt", "r")
txt_msg = txt_file.read()
txt_file.close()
sf_msg = "What do you want to replace?\n"
rep_msg = "What do you want to replace it with?\n"
searched_for = input(sf_msg)
replace_with = input(rep_msg)
txt_msg = txt_msg.replace(searched_for, replace_with)
f = open('replaced.txt', 'w')
f.write(txt_msg)
print('done')
input('Press ENTER to exit')