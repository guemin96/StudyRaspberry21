
try:

    f = open('./data/readme.txt', mode = 'r',encoding='utf-8') # text file open
    f2 = open('./data/writeme.txt',mode = 'w',encoding='utf-8')

    line = f.readline()
    while line:
        print(line)
        f2.write(line)
        line = f.readline()
    f2.write("\n")
    f2.write("add content")
    f.close() # text file close
    f2.close()

    print("file write complete")
except Exception as e:
    print('exception occur : {0}'.format(e))


