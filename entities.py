class Entity_List:
    def __init__(self):        
        self.list=[]
    def add(self,x,y,mchar,entity):
        self.x=x
        self.y=y
        self.mchar=mchar
        self.entity=entity
        self.list.append([self.x,self.y,self.mchar,self.entity])

    def remove(self,entity):
        i = 0
        for mon in self.list:            
            if mon[3] == entity:
                return self.list.pop(i)
            i += 1

    def return_list(self):
        return self.list
