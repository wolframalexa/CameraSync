from matplotlib import pyplot as plt

# read and format timestamps
source = open("../data/008_timedata.txt", "r")
timestamps = source.read()
timestamps = [float(i) for i in timestamps.split("\n") if i != '']
offset = timestamps[0]
timestamps = [i - offset for i in timestamps]

# get odd and even (for first and second cameras)
cam1 = timestamps[0::2]
cam2 = timestamps[1::2]

if len(cam1) != len(cam2):
	cam1 = cam1[:-1]

difference = []
for i in range(len(cam1)):
  difference.append(cam2[i] - cam1[i])

index = list(range(len(cam1)))

offst = cam1[0]
cam1 = [i - offst for i in cam1]

# plot
plt.loglog(cam1,difference)

plt.title("Difference in camera timestamps - test 008")
plt.ylabel("milliseconds (ms)")
plt.xlabel("capture number")

plt.savefig("008_loglog.png")
plt.show()
