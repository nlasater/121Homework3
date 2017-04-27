
def get_list():
    return response.json(dict(mylist=['alpha', 'beta', 'gamma', 'delta']))

def get_another_list():
    return response.json({'mylist': ['gamma', 'iota', 'zeta']})


		In[1]: import json
		In[2]: json.dimps('a')
		#OUT[2]: '"a'

		In[3]: print json.dumps('a')
		#"a"

		In[4]: print json.dumps('a"a')
		#"a\"a"

		In[5]: print json.dumps(5)
		#5

		In[6]: print.json.dumps(['cat','dog','deer'])
		#["cat","dog","deer"]

		In[7]: type(json.dumps(['cat','dog','deer']))
		#Out[7]: str

		#In python, there is no ordering...order is not present.
		In[8]: print json.dumps({'cat':4, 'bird':2})
		#{"bird":2, "cat":4}