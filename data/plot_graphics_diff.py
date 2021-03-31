from matplotlib import pyplot as plt

# read and format timestamps
graphics = open("timestamps_with_graphics.txt", "r")
nographics = open("timestamps_no_graphics.txt", "r")

times1 = graphics.read()
times2 = nographics.read()

times1 = [int(i) for i in times1.split("\n") if i != '']
offset = times1[0]
times1 = [i - offset for i in times1]

times2 = [int(i) for i in times2.split("\n") if i != '']
offset = times2[0]
times2 = [i - offset for i in times2]

# get first camera for each trial
cam1 = times1[0::2]
cam2 = times2[0::2]

cam1 = cam1[0:len(cam2)]

difference = []
for i in range(min(len(cam1), len(cam2))):
  difference.append(cam2[i] - cam1[i])

index = list(range(len(cam1)))

# plot
plt.plot(index,difference)

plt.title("Difference in camera timestamps [nographics - graphics]")
plt.ylabel("milliseconds (ms)")
plt.xlabel("capture number")

plt.show()
plt.savefig("graphics_diff.png")

# Findings: seems to be an improvement running without graphics, although this is not always the case
