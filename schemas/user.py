def user(data)->dict:
    return {
        "id":str(data["_id"]),
        "username":data["username"],
        "email":data["email"],
        "password":data["password"]
    }

def userlist(datas)->list:
    return [user(data) for data in datas]