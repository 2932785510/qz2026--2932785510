import json
import copy
class UserManage:
    def __init__(self):
        self._user=[]
        self._userid=1
    def add_user(self,name,age):
        user={"name":name,"age":age,"id":self._userid}
        self._user.append(user)
        self._userid+=1
        return copy.deepcopy(user)
    def get_user(self,getid):
        for i in self._user:
            if i.get("id")==getid:
                return copy.deepcopy(i)
        return None