import time
text = "[ ]{}\t{}\t{}\t{}[ ]"
blank = ''
lines = [(blank,blank,blank,blank),(blank,blank,blank,blank),(blank,blank,blank,blank),(blank,blank,blank,blank),(blank,blank,blank,blank),
(blank,blank,blank,blank),(blank,blank,blank,blank),(blank,blank,blank,blank),(blank,blank,blank,blank),(blank,blank,blank,blank)]

k = 0
while k < 10:
    lines[k] = (blank,10 - k,10 - k,blank)
    print("[ ]" * 9)
    print(text.format(lines[0][0],lines[0][1],lines[0][2],lines[0][3]))
    print(text.format(lines[1][0],lines[1][1],lines[1][2],lines[1][3]))
    print(text.format(lines[2][0],lines[2][1],lines[2][2],lines[2][3]))
    print(text.format(lines[3][0],lines[3][1],lines[3][2],lines[3][3]))
    print(text.format(lines[4][0],lines[4][1],lines[4][2],lines[4][3]))
    print(text.format(lines[5][0],lines[5][1],lines[5][2],lines[5][3]))
    print(text.format(lines[6][0],lines[6][1],lines[6][2],lines[6][3]))
    print(text.format(lines[7][0],lines[7][1],lines[7][2],lines[7][3]))
    print(text.format(lines[8][0],lines[8][1],lines[8][2],lines[8][3]))
    print(text.format(lines[9][0],lines[9][1],lines[9][2],lines[9][3]))
    print("[ ]" * 9)
    time.sleep(0.5)
    k += 1
    lines[k-1] = (blank,blank,blank,blank)
    