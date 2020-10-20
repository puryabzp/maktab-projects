while(True):
        i=int(input("Enter number of disk: "))
        def Hanoi_tower(start="A",middle="B",goal="C",disk=1):
                if disk==1:
                    print("Disk 1 move From {} to {}".format(start,goal))
                else:
                    Hanoi_tower(start,goal,middle,disk-1)
                    print("Disk {} move From {} to {}".format(disk,start,goal))
                    Hanoi_tower(middle,start,goal,disk-1)
        Hanoi_tower("A","B","C",i)