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
        return copy.deepcopy(self._user)
    