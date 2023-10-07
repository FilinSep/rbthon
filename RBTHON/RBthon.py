# RBThon - BEST ROBLOX API MODULE!

import requests
from bs4 import BeautifulSoup as bs

# ERRORS

class IDNotFoundError(Exception):
    pass

class NotFoundError(Exception):
    pass

class AuthorizationDeniedError(Exception):
    pass

class PostError(Exception):
    pass

# API GET METHODS
class RobloxUserGET():

    Nickname = 'Roblox'
    Cookie = None
    Id = 1

    def __init__(self, nickname='Roblox', cookie=None, id=1) -> None:
        self.Nickname = nickname
        self.Cookie = cookie
        self.Id = id

    def user(self):

        # uses ID
        # answer:
        # description, created, isBanned, externalAppDisplayName, hasVerifiedBadge, id, name, displayName

        jsonanswer = requests.get('https://users.roblox.com/v1/users/'+str(self.Id)).json()

        if "errors" in jsonanswer:
            
            raise IDNotFoundError
        
        else:

            class UserAPIdata():
                
                answer = jsonanswer
                description = jsonanswer["description"]
                created = jsonanswer["created"]
                isBanned = jsonanswer["isBanned"]
                externalAppDisplayName = jsonanswer["externalAppDisplayName"]
                hasVerifiedBadge = jsonanswer["hasVerifiedBadge"]
                id = jsonanswer["id"]
                name = jsonanswer["name"]
                displayName = jsonanswer["displayName"]

            return UserAPIdata
        
    def birthdate(self):

        # uses .ROBLOSECURITY COOKIE
        # answer:
        # birthMonth, birthDay, birthYear

        jsonanswer = requests.get('https://users.roblox.com/v1/birthdate', cookies={".ROBLOSECURITY": self.Cookie}).json()

        if "errors" in jsonanswer:
            
            raise NotFoundError
        
        else:

            class BirthAPIdata():
                
                answer = jsonanswer
                birthMonth = jsonanswer["birthMonth"]
                birthDay = jsonanswer["birthDay"]
                birthYear = jsonanswer["birthYear"]

            return BirthAPIdata
        
    def gender(self):

        # uses .ROBLOSECURITY COOKIE
        # answer:
        # gender

        jsonanswer = requests.get('https://users.roblox.com/v1/gender', cookies={".ROBLOSECURITY": self.Cookie}).json()

        if "errors" in jsonanswer:
            
            raise NotFoundError
        
        else:

            class GenderAPIdata():
                
                answer = jsonanswer
                gender = jsonanswer["gender"]

            return GenderAPIdata
        
    def countrycode(self):

        # uses .ROBLOSECURITY COOKIE
        # answer:
        # countryCode

        jsonanswer = requests.get('https://users.roblox.com/v1/users/authenticated/country-code', cookies={".ROBLOSECURITY": self.Cookie}).json()

        if "errors" in jsonanswer:
            
            raise AuthorizationDeniedError
        
        else:

            class CountryCodeAPIdata():
                
                answer = jsonanswer
                countryCode = jsonanswer["countryCode"]

            return CountryCodeAPIdata
        
    def roles(self):

        # uses .ROBLOSECURITY COOKIE
        # answer:
        # roles

        jsonanswer = requests.get('https://users.roblox.com/v1/users/authenticated/roles', cookies={".ROBLOSECURITY": self.Cookie}).json()

        if "errors" in jsonanswer:
            
            raise AuthorizationDeniedError
        
        else:

            class CountryCodeAPIdata():
                
                answer = jsonanswer
                roles = jsonanswer["roles"]

            return CountryCodeAPIdata
        
    def agebracket(self):

        # uses .ROBLOSECURITY COOKIE
        # answer:
        # ageBracket

        jsonanswer = requests.get('https://users.roblox.com/v1/users/authenticated/age-bracket', cookies={".ROBLOSECURITY": self.Cookie}).json()

        if "errors" in jsonanswer:
            
            raise AuthorizationDeniedError
        
        else:

            class ageBracketAPIdata():
                
                answer = jsonanswer
                ageBracket = jsonanswer["ageBracket"]

            return ageBracketAPIdata
        
    def authenticated(self):

        # uses .ROBLOSECURITY COOKIE
        # answer:
        # id, name, displayName

        jsonanswer = requests.get('https://users.roblox.com/v1/users/authenticated', cookies={".ROBLOSECURITY": self.Cookie}).json()

        if "errors" in jsonanswer:
            
            raise AuthorizationDeniedError
        
        else:

            class ageBracketAPIdata():
                
                answer = jsonanswer
                id = jsonanswer["id"]
                name = jsonanswer["name"]
                displayName = jsonanswer["displayName"]

            return ageBracketAPIdata
        

# API POST METHODS
class RobloxUserPOST():

    Cookie = None
    CSRF = None

    def __init__(self, cookie) -> None:
        self.Cookie = cookie

        http = requests.get("https://www.roblox.com/home", cookies={".ROBLOSECURITY":cookie})
        html = bs(http.text, "html.parser")
        csrf_tag = html.find("meta", {"name": "csrf-token"})
        self.CSRF = csrf_tag["data-token"]

    def description(self, json):
        answer = requests.post('https://users.roblox.com/v1/description', 
                                json=json, 
                                cookies={".ROBLOSECURITY": self.Cookie},
                                headers={'X-CSRF-TOKEN':self.CSRF})

        return answer.json()
    
    def birthdate(self, json):
        answer = requests.post('https://users.roblox.com/v1/birthdate', 
                                json=json, 
                                cookies={".ROBLOSECURITY": self.Cookie},
                                headers={'X-CSRF-TOKEN':self.CSRF})

        return answer.json()
    
    def gender(self, json):
        answer = requests.post('https://users.roblox.com/v1/gender', 
                                json=json, 
                                cookies={".ROBLOSECURITY": self.Cookie},
                                headers={'X-CSRF-TOKEN':self.CSRF})

        return answer.json()
