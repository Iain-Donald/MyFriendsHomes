from email.policy import default
import json, random
from turtle import title
class dbtalk:
    def getListingByID(id):
        f = open('flask_app\controllers\db.json')
        data = json.load(f)
        listingData = "-1"
        for i in data['Listings']:
            if(int(i['id']) == id):
                listingData = i
            
        return listingData

    def updateListingByID(id, newData):
        with open("flask_app\controllers\db.json") as file:
        #with open('flask_app\controllers\db.json','r+') as file:
            file_data = json.load(file)
            for i in file_data['Listings']:
                if(int(i['id']) == int(id)):
                    i['title'] = newData['title']
                    i['description'] = newData['description']
            #file_data["Listings"].append(i)
            #file.seek(0)
            #json.dump(file_data, file, indent = 4)
        
        with open("flask_app\controllers\db.json", 'w', encoding='utf-8') as fa:
            fa.write(json.dumps(file_data, indent=4))

        return -1
    
    def updatePinByGroupID(id, newPin):
        with open("flask_app\controllers\db.json") as file:
            file_data = json.load(file)
            for i in file_data['Groups']:
                if(int(i['GroupID']) == int(id)):
                    #print("TRUE")
                    i['pin'] = newPin
        
        with open("flask_app\controllers\db.json", 'w', encoding='utf-8') as fa:
            fa.write(json.dumps(file_data, indent=4))

        return -1

    def getUserByID(id):
        f = open('flask_app\controllers\db.json')
        data = json.load(f)
        for i in data['Users']:
            if(int(i['userID']) == int(id)):
                return i
            
        return "User not found"

    def getUserByEmail(email):
        f = open('flask_app\controllers\db.json')
        data = json.load(f)
        userData = "-1"
        for i in data['Users']:
            if(i['email'] == email):
                userData = i
            
        return userData

    def getAllListings():
        f = open('flask_app\controllers\db.json')
        data = json.load(f)
        Listings = data['Listings']
            
        return Listings

    def getAllUsers(): #look into deleting this
        f = open('flask_app\controllers\db.json')
        data = json.load(f)

    def deleteListingByID(ID):

        with open("flask_app\controllers\db.json") as f:
            data = json.load(f)

        idx = 0

        for i in data['Listings']:
            #print(i['id'] + "  ID: " + ID)
            if i['id'] == ID:
                #print("TRUE")
                del data['Listings'][idx]
            idx += 1

        with open("flask_app\controllers\db.json", 'w', encoding='utf-8') as fa:
            fa.write(json.dumps(data, indent=4))

    def deleteUserByID():
        return -1
    
    def getImagesByListingID(ListingID):
        f = open('flask_app\controllers\db.json')
        data = json.load(f)
        imagePath = []
        for i in data['ListingImages']:
            #print(i)
            if(i['ListingID'] == ListingID):
                imagePath.append([i['path'], i['PhotoID']])

        return imagePath

    def addImage(fileName, ListingID):
        #replace spaces with _ in filename
        fileNameList = list(fileName)
        fileName = ""
        for i in range(len(fileNameList)):
            if(fileNameList[i] == " "):
                fileNameList[i] = "_"
        fileName = "".join(fileNameList)

        data = {
        "PhotoID": str(random.randrange(11001, 44000)),
        "path": "../static/images/" + fileName,
        "ListingID" : ListingID
        }

        ###print(json.dumps(data))

        #insert object to JSON file

        with open('flask_app\controllers\db.json','r+') as file:
            file_data = json.load(file)
            file_data["ListingImages"].append(data)
            file.seek(0)
            json.dump(file_data, file, indent = 4)

        return -1

    def findGroupsByUserID(userID):
        f = open('flask_app\controllers\db.json')
        data = json.load(f)
        groups = []
        ofThisGroup = False
        for i in data['Groups']:
            #print("I:" + i)
            ofThisGroup = False
            for j in i['UserIDs']:
                #print("J:" + j)
                if(j == userID):
                    ofThisGroup = True
            if(ofThisGroup):
                groups.append(i)
            
        #print("Groups:" + groups[0]['GroupName'])
        return groups
    
    def getGroupByGroupID(GroupID):
        f = open('flask_app\controllers\db.json')
        data = json.load(f)
        group = -1
        for i in data['Groups']:
            if(i['GroupID'] == GroupID):
                group = i
            
        return group

    def getListingsByGroupID(GroupID):
        f = open('flask_app\controllers\db.json')
        data = json.load(f)
        listings = []
        
        for i in data['Groups']:
            #print("I:" + i)
            if(i['GroupID'] == GroupID):
                for j in i['ListingIDs']:
                    listings.append(j)

                break
            
        #print("Groups:" + groups[0]['GroupName'])
        return listings

    def deleteElementByCategory(elementID, category):
        with open("flask_app\controllers\db.json") as f:
            data = json.load(f)
        
        IDVar = '-1'
        if(category == 'Listings'):
            IDVar = 'id'
        elif (category == 'Users'):
            IDVar = 'userID'
        elif (category == 'ListingImages'):
            IDVar = 'PhotoID'
        elif (category == 'Groups'):
            IDVar = 'GroupID'
        else:
            return "no category matched"

        elementIDX = 0

        for i in data[category]: #cats: 'Listings' 'Users' 'ListingImages' 'Groups'
            #print(i['id'] + "  ID: " + ID)
            if i[IDVar] == elementID:
                #print("TRUE")
                del data[category][elementIDX]
            elementIDX += 1

        with open("flask_app\controllers\db.json", 'w', encoding='utf-8') as fa:
            fa.write(json.dumps(data, indent=4))
        return -1
    
    def removeUserFromGroup(userID, groupID):
        with open("flask_app\controllers\db.json") as f:
            data = json.load(f)

        idx = 0
        groupIDX = 0
        for i in data['Groups']:
            if i['GroupID'] == groupID:
                print("FOUND GROUP")
                for j in i['UserIDs']:
                    if j == userID:
                        del data['Groups'][groupIDX]['UserIDs'][idx]
                        with open("flask_app\controllers\db.json", 'w', encoding='utf-8') as fa:
                            fa.write(json.dumps(data, indent=4))
                        return -1
                    idx += 1
                return -1
            groupIDX += 1
        return -1
    
    def addUserToGroup(userID, groupPin, groupID):
        with open("flask_app\controllers\db.json") as f:
            data = json.load(f)
        groupIDX = 0
        for i in data['Groups']:
            if i['GroupID'] == groupID:
                print("FOUND GROUP")
                if(data['Groups'][groupIDX]['pin'] != groupPin):
                    return -1
                data['Groups'][groupIDX]['UserIDs'].append(userID)
                with open("flask_app\controllers\db.json", 'w', encoding='utf-8') as fa:
                    fa.write(json.dumps(data, indent=4))
                return -1
            groupIDX += 1
        return -1
    
    def addListingToGroup(listingID, groupID):
        with open("flask_app\controllers\db.json") as f:
            data = json.load(f)
        groupIDX = 0
        for i in data['Groups']:
            if i['GroupID'] == groupID:
                print("FOUND GROUP")
                data['Groups'][groupIDX]['ListingIDs'].append(listingID)
                with open("flask_app\controllers\db.json", 'w', encoding='utf-8') as fa:
                    fa.write(json.dumps(data, indent=4))
                return -1
            groupIDX += 1
        return -1
    
    def addGroup(groupName, groupPin, userID):
        data = {
            "GroupID": str(random.randrange(11001, 44000)),
            "GroupName": groupName,
            "pin": groupPin,
            "ListingIDs": ["15033"],
            "UserIDs": [userID] 
        }

        if(data['pin'].isdigit()):
            print("Numeric")
        else:
            return -1

        ###print(json.dumps(data))

        #insert object to JSON file

        with open('flask_app\controllers\db.json','r+') as file:
            file_data = json.load(file)
            file_data["Groups"].append(data)
            file.seek(0)
            json.dump(file_data, file, indent = 4)

        return -1