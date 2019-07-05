import pickle

# name = "이정일"
# email = "jungil.lee@kt.com"
#
# person = (name, email)
#
# with open('./pickle_test.pkl', 'wb') as f:
#     pickle.dump(person, f)

with open('./pickle_test.pkl', 'rb') as f:
    name, email = pickle.load(f)
    print(name, email)