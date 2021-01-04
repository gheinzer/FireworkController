from lib.nextion import nextion

display = nextion(12, 13, 9600)

print("ERROR")
display.cmd("page ErrorPage")