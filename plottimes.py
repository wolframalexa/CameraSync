from matplotlib import pyplot as plt

# read and format timestamps
source = open("timestamps.txt", "r")
timestamps = source.read()
timestamps = [int(i) for i in timestamps.split("\n") if i != '']
offset = timestamps[0]
timestamps = [i - offset for i in timestamps]

# get odd and even (for first and second cameras)
cam1 = timestamps[0::2]
cam2 = timestamps[1::2]

index = list(range(len(cam1)))

# plot
plt.plot(index,cam1, label='Camera 1')
plt.plot(index,cam2, label='Camera 2')

plt.title("Difference in camera timestamps")
plt.ylabel("milliseconds (ms)")
plt.xlabel("capture \#")

plt.show()
