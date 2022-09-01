import matplotlib.pyplot as plt

log = open("SPO2_LOG.log", 'r')
new_data_ir = open("IR_DATA.txt", 'w')
new_data_red = open("RED_DATA.txt", 'w')

plot_data_red = []
plot_data_ir = []

while True:
    line = log.readline()
    print("ONE_STRING-->", line)
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
        break

plt.plot(plot_data_red)
# plt.plot(plot_data_ir)
plt.show()
