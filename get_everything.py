def calc_mean(main_data):
    viz_list = []
    name_list = []
    mean_list = []
    for name, list in main_data.items():
      average = sum(list[1])/len(list[1])
      mean_list.append(average)
      name_list.append(name)
    
    viz_list.append(name_list)
    viz_list.append(mean_list)

    return viz_list
