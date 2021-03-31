from matplotlib import pyplot as plt

# read and format timestamps
sources = {}
diffs = {}

for i in range(1,5):
	fname = "../data/00" + str(i) + "_timedata.txt"
	trial = open(fname, "r")
	timestamps = trial.read()
	offset = float(timestamps[0])
	timestamps = [float(i) - offset for i in timestamps.split("\n") if i != '']

	cam1 = timestamps[0::2]
	cam2 = timestamps[1::2]

	sz1 = len(cam1)
	if sz1 != len(cam2):
		cam1 = cam1[:-1]
		sz1 -= 1

	difference = []
	for j in range(sz1):
		difference.append(cam2[j] - cam1[j])

	offst = cam1[0]
	cam1 = [i - offst for i in cam1]

#	sources["source{0}".format(i)] = cam1
#	diffs["diff{0}".format(i)] = difference




# plot
	plt.loglog(cam1,difference)

plt.title("Difference in camera timestamps - graphics configurations")
plt.ylabel("milliseconds (ms)")
plt.xlabel("camera1 timestamp")
plt.legend(["001", "002", "003", "004"])

plt.savefig("graphics_diff.png")
plt.show()
