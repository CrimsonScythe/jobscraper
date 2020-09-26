import pickle

with open('listings.pkl', 'rb') as f:
    newlst = pickle.load(f)

print(len(newlst))

keywords = ['limit', 'search']
translst = [item for item in newlst if ('limit' not in item and 'search' not in item)]


final_lst = list(set(translst))

print(len(final_lst))

print(final_lst)
