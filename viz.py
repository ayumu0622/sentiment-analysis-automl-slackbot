import matplotlib.pyplot as plt
value_list = {"Emma":0.899999,"kate":0.2222222,"elen":0.111111111,"ayumu":-0.88888888888,"Bob":-0.22222222222,"Jay":-0.8888888888888}
fig = plt.figure()
ax = fig.add_subplot(111)
ax.bar(value_list.keys(),value_list.values())
plt.savefig(r'C:\Users\ayumu\Desktop\adobe_project\clone\slack_bot\output.png')
