import matplotlib.pyplot as plt
import re
log = open("SPO2_LOG.log", 'r')
new_data_ir = open("IR_DATA.txt", 'w')
new_data_red = open("RED_DATA.txt", 'w')

plot_data_red = []
plot_data_ir = []

print("START PARSING, LEN ->", len(re.findall(r"[\n']+", open('SPO2_LOG.log').read())))
while True:
    line = log.readline()
    if line != '':
        if line[0] == '1':
            new_data_ir.write(line[8:])
            plot_data_ir.append(int(line[8:13]))
        if line[0] == '2':
            new_data_red.write(line[8:])
            plot_data_red.append(int(line[8:13]))
    if not line:
        log.close()
        new_data_ir.close()
        new_data_red.close()
        print("STOP PARSING-->", line)
        break

plt.plot(plot_data_red, label="RED")
plt.plot(plot_data_ir, label="IR")
plt.legend()
plt.show()
