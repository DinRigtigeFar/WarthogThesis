import plot_psmc
import os
import matplotlib.pyplot as plt
import matplotlib

path = "/home/jfl323/pigs/cleanWarts/psmc/results/psmc_output"

psmcs = ["8922.psmc", "7155.psmc", "8627.psmc", "2541.psmc", "1257.psmc",  "2418.psmc"]
countries = ["Desert", "Ghana", "Tanzania", "Zambia", "Zimbabwe", "Namibia"]

first_it = []

for i in psmcs:
    first_it.append(plot_psmc.psmc2fun(os.path.join(path, i)))


X_MIN = 15000
X_MAX = 5*1e6
Y_MIN = 0
Y_MAX = 7e4

cols = ['brown', 'red', 'purple', 'green', 'orange', 'yellow']

fig = plt.figure()
ax = fig.add_subplot(111)

for idx, item in enumerate(first_it):
    (estimated_times, estimated_sizes) = item
    ax.step(estimated_times, estimated_sizes, where='post', lw=2, color=cols[idx], label = countries[idx])

ax.set_xlabel("Years before present starting at 15 Kya")
ax.set_ylabel("Effective population size ($10^4$)")
ax.ticklabel_format(axis='y', style='sci', scilimits=(-2,2))
ax.grid(True)
ax.set_xlim(X_MIN, X_MAX)
ax.set_ylim(Y_MIN, Y_MAX)
ax.set_xscale('log')
ax.set_xticks([1.5*10**4, 10**5, 10**6])
#ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
#ax.xaxis.major.formatter._useMathText = True
#ax.ticklabel_format(axis='x', style='sci', scilimits=(0,0))
plt.legend(loc = 'best')
plt.title("   Demographic history of common and desert warthogs")

plt.savefig("PSMC_with_labels_newOrder.pdf", bbox_inches = 'tight')
