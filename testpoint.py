main_data = {'Ayumu': [['motivation', ':wave:', ':wave:', ':wave:', ':wave:', 'hello', 'I am Ayumu', 'hello-socket-mode', 
'/ hello-socket-mode', 'hello-socket-mode', '/ hello-socket-mode', '/ hello-socket-mode', 'hello', 'motivation', 'ji', 'hello', 'okay sure', 'ok sure', 
'that is a good idea', 'this is so boring job', 'this task is not difficult to do I guess', "I don't like this job."], [0.699999988079071, 0.20000000298023224, 
0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.10000000149011612, 0.0, 0.0, 0.0, 0.0, 0.0, 0.20000000298023224, 0.699999988079071, 
0.10000000149011612, 0.20000000298023224, 0.30000001192092896, 0.5, 0.8999999761581421, -0.8999999761581421, 0.10000000149011612, -0.8999999761581421]], 
'Emma': [['I do not want to go to that meeting because it is always boring', 'I am Emma', 'yea that was hard'], [-0.800000011920929, 0.10000000149011612, -0.30000001192092896]], 
'Bob': [['Tomorrow we have a meeting', 'I am Bob', 'It is so difficult to finish', 'I had a meeting from 6pm', 'Hello'],
 [0.0, 0.10000000149011612, -0.800000011920929, 0.0, 0.20000000298023224]], 
 'Kate': [[':star-struck:', ':smile:', 'Me tooo', 'I am Kate', 'you are fired', 'I hope I can finish this by tomorrow'], [0.0, 0.6000000238418579,
  0.699999988079071, 0.10000000149011612, -0.699999988079071, 0.20000000298023224]]}

strings = "("
for name in list(main_data.keys()):
  strings = strings + "|" + name
strings += ")"

print(strings)