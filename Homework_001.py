
# coding: utf-8

# ## Problem 1: De-duplicate a list

# Given the following list,
# 
#     data=[5,4,6,1,9,0,3,9,2,7,10,8,4,7,1,2,7,6,5,2,8,2,0,1,1,1,2,10,6,2]
# 
# remove all the duplicated elements from this list. Note that the **order is preserved.** The order proceeds from smallest list index to greatest (i.e., from left-to-right).

# In[1]:


data=[5,4,6,1,9,0,3,9,2,7,10,8,4,7,1,2,7,6,5,2,8,2,0,1,1,1,2,10,6,2]
answer=[]
for i in data:
    if i not in answer:
        answer.append(i)


# In[2]:


assert answer == [5,4,6,1,9,0,3,2,7,10,8]


# ## Problem 2: Compute the sum

# Write a function that computes the sum of all non-negative integers (i.e. >=0) up to
# and including a specified value, `n`.
# 
# **Hint**: Remember to use all the input/output validation checking techniques we discussed.

# In[3]:


def compute_sum_to_n(n):
   ''' Anh Hoang
   implement a function to compute sum and assert to make sure input n have to be positive and greater than zero
   '''
   assert isinstance(n,int)
   assert n>=0
   return sum(range(n+1))
   raise NotImplementedError()

# delete everything below this line


# In[4]:


assert len(compute_sum_to_n.__doc__)


# ## Problem 3: All sublists

# Generate all sublists of a list. Note there will be `2**len(x)` subsets of the
# list x. For example, the list `[0,1,2]` has seven sublists:
# `[[0],[1],[2],[0,1],[1,2],[0,2],[0,1,2]]`. Note that you don't have to mind the
# ordering of each sublist.  Also, we don't care about the empty list (`[]`). The
# function should accept input consisting of only a list of **unique** items.
# 
# * Hint: use recursion.
# * Hint: You probably want to use `list` instead of `set`.
# 
# Here is the output of `all_sublists(range(4))`:
# 
#     [[0],
#      [1],
#      [2],
#      [3],
#      [2, 3],
#      [1, 2],
#      [1, 3],
#      [1, 2, 3],
#      [0, 1],
#      [0, 2],
#      [0, 3],
#      [0, 2, 3],
#      [0, 1, 2],
#      [0, 1, 3],
#      [0, 1, 2, 3]]

# In[5]:


def all_sublists(x):
    '''find all sublist of the list. There will be 2**len(x) sublist
    '''
    
    def unique(y):
        seen = set()
        return not any(i in seen or seen.add(i) for i in y)
        
    assert isinstance(x,list)
    assert unique(x) is True
    ##assert len(x)>len(set(x))
    if len(x) == 1:
        return [x]
    res = []
    subsets = all_sublists(x[0:-1])
    res = res+subsets
    res.append([x[-1]])
    for sub in subsets:
        res.append(sub+[x[-1]])
    return res
    raise NotImplementedError()


# In[6]:


### BEGIN  TESTS

ans = [[3], [2], [0], [2, 0], [3, 2], [3, 0], [3, 2, 0]]
assert 0 == len(set(map(frozenset,ans)) - set(map(frozenset,all_sublists([3,0,2]))))
ans = [[1], ['a'], [3], ['a', 3], [1, 'a'], [1, 3], [1, 'a', 3]]
assert 0 == len(set(map(frozenset,ans)) - set(map(frozenset,all_sublists([1,3,'a']))))

### END  TESTS


# In[7]:


import pytest
with pytest.raises(AssertionError):
    all_sublists(3)


# In[8]:


with pytest.raises(AssertionError):
    all_sublists([1,1])


# In[9]:


assert len(all_sublists.__doc__)

