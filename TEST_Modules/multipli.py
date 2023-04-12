def table(nb, max=10):
    i = 0
    while i < max:
        i += 1
        print("{}x{} = {}".format(i,nb,i*nb))

if __name__ == "__main__":  #Ne s'excute pas si le module est importer mais lancé.
    table(8)