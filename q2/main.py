import json
import copy
class UserManage:
    def __init__(self):
        self._user=[]
    def add_user(self,name,age):
        userid=1
        user={"name":name,"age":age,"id":userid}
        self._user.append(user)
        userid+=1
        return copy.deepcopy(self._user)
    