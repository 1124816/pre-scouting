import pickle

try:
    data = pickle.load( open( "jim.p", "rb" ) )
except FileNotFoundError:
    print("Hello")
