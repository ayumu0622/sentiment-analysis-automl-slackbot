def create_viz(list):
    import matplotlib.pyplot as plt
    #list = [['Ayumu', 'Emma', 'Bob', 'Kate'], [0.13636363805695015, -0.3333333407839139, -0.10000000149011612, 0.15000000471870104]]
    average = sum(list[1]) / len(list[1])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.bar(list[0],list[1])
    ax.axhline(average, label="average",color ="orange")
    ax.axhline(0,color = "black")
    ax.legend(["average"])
    ax.set_title("Everyone")
    ax.set_xlabel("Employee name")
    ax.set_ylabel("Score of positiveness")
    plt.savefig(r'C:\Users\ayumu\Desktop\adobe_project\clone\slack_bot\output.png')
