import json
import copy
class UserManage:
    def __init__(self):
        self._users=[]
        self._userid=1
    def add_user(self,name,age):
        user={"name":name,"age":age,"id":self._userid}
        self._users.append(user)
        self._userid+=1
        return copy.deepcopy(user)
    def get_user(self,user_id):
        for i in self._users:
            if i.get("id")==user_id:
                return copy.deepcopy(i)
        return None
    def update_age(self,user_id,updated_age):
        for i in self._users:
            if i.get("id")==user_id:
                i["age"]=updated_age
                return True
        return False
    def remove_user(self,user_id):
        for i in self._users:
            if i.get("id")==user_id:
                self._users.remove(i)
                return True
        return False