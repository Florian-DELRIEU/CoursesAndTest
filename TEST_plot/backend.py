import matplotlib
import matplotlib.pyplot as plt	

matplotlib.use("agg")
print( matplotlib.get_backend() )

fig1 = plt.figure(1)
plt.plot( [0,1,2,3] , [1,2,1,4] , "b-" )
