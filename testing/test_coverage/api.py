
data={
    "utsav":{
        "age":22,
        "address":"Muragacha",
        "DOB":"11-02-2001"
    },
    "supratim":{
        "age":21,
        "address":"Dunlop",
        "DOB":"06-06-2002"
    }
}

class API:

    def __init__(self,request:dict) -> None:
        self._request=request
        
    
    def get_userFromRequest(self)->str:
        try:
            if self._request.get('user'):
                return self._request.get('user')
            else:
                raise Exception("user is not present in request!")
        except Exception as e:
            raise Exception(e)
    
    def get_userFromRecord(self)->dict:
        try:
            _user=self.get_userFromRequest()
            if data.get(_user):
                return data.get(_user)
            else:
                raise Exception("user is not present in record!")
        except Exception as e:
            raise Exception(e)



