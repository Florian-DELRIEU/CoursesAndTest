import matplotlib.pyplot as plt

label1 = "lol"
label2 = 'test'


plt.figure("test")
plt.title("Ceci est une figure")
plt.plot(1,1,'k*',label = "LOL")
plt.plot(1.1,1,'r*',label = "TEST")
#legend = plt.legend(loc='upper left', shadow=True)# fontsize='x-large')
plt.legend(loc="upper left")
#plt.legend((line1, line2, line3), ('label1', 'label2', 'label3'))

