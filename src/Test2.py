'''
Created on Mar 29, 2018
@author: tjcoo
'''
#change it from looking for a set to looking for a class. 
import urllib2
import json
import sys

#setting up my keys
bliz_api = '7qugbcvt9pd4aqs2kbwwwvxa'
bliz_api2 = '65xvm5ftx3gvtckbewhkgbmmbrcvgb79'

name = raw_input("What set are you looking for in the top 20 (case-sensitive): ")

#initializing needed variables
playerBattleTag = ''
num = 0
numFound = 0.0
heroID = 0
setName = ''
answer = ''
#getting the url for the Diablo 3 leaderboards
urlLeaderBoard = 'https://us.api.battle.net/data/d3/season/13/leaderboard/achievement-points?access_token=' + bliz_api

#setting up and loading the json objects
json_obj = urllib2.urlopen(urlLeaderBoard)
data = json.load(json_obj)

#gets the player battle tag from leaderboards
for item in data['row']:
    try:
        if(num >= 30):
            num = 0
            break
        #gets and sets up the player battletag
        playerBattleTag = item["player"][0]['data'][0]['string']
        playerBattleTag = playerBattleTag.replace('#', '%23')
        num += 1
        #print(num)
        urlHeroList = 'https://us.api.battle.net/d3/profile/' + playerBattleTag +'/?locale=en_US&apikey=' + bliz_api2
        json_obj2 = urllib2.urlopen(urlHeroList)
        data2 = json.load(json_obj2)
        
        for item in data2['heroes']:
            #getting the hero ID's for the battletags and sets up the url for the hero sets
            heroID = item['id']
            urlHeroSetList = 'https://us.api.battle.net/d3/profile/' +playerBattleTag+ '/hero/' +str(heroID)+ '/items?locale=en_US&apikey=' + bliz_api2
            json_obj3 = urllib2.urlopen(urlHeroSetList)
            data3 = json.load(json_obj3)
            
            try:   
                #getting the names of the sets and printing them to the screen.
                setName = data3['head']['set']['name']
                # print(setName)
                if(name == setName):
                    numFound += 1
                break
            except:
                num += 1                
    except:
        print "name can't convert"
        
percent = numFound/20

if(percent == 0.0):
    print("Sorry, seems like that set isnt used in Top 20.")
    sys.exit()

percent = percent*100

print "" + str(percent) + "% of players in top 20 use this set. Would you like to see a list of these players? (yes or no)"
answer = raw_input("")
if(answer == "yes"):
    for item in data['row']:
        try:
            if(num >= 30):
                break
            #gets and sets up the player battletag
            playerBattleTag = item["player"][0]['data'][0]['string']
            playerBattleTag = playerBattleTag.replace('#', '%23')
            num += 1
            
            urlHeroList = 'https://us.api.battle.net/d3/profile/' + playerBattleTag +'/?locale=en_US&apikey=' + bliz_api2
            json_obj2 = urllib2.urlopen(urlHeroList)
            data2 = json.load(json_obj2)
            
            for item in data2['heroes']:
                #getting the hero ID's for the battletags and sets up the url for the hero sets
                heroID = item['id']
                urlHeroSetList = 'https://us.api.battle.net/d3/profile/' +playerBattleTag+ '/hero/' +str(heroID)+ '/items?locale=en_US&apikey=' + bliz_api2
                json_obj3 = urllib2.urlopen(urlHeroSetList)
                data3 = json.load(json_obj3)
                
                try:   
                    #getting the names of the sets and printing them to the screen.
                    setName = data3['head']['set']['name']
                    if(name == setName):
                        playerBattleTag = playerBattleTag.replace('%23', '#')
                        print(playerBattleTag)
                    break
                except:
                    num += 1                
        except:
            print "name can't convert"
    print("Would you like to see more information on one of these players? If so type their name (case-sensitive including #), otherwise 'no'")
    answer = raw_input("")
    print("")
    if(answer == "no"):
        print("Goodbye")
    else:
        playerBattleTag = answer.replace('#', '%23')
        urlHeroList = 'https://us.api.battle.net/d3/profile/' + playerBattleTag +'/?locale=en_US&apikey=' + bliz_api2
        json_obj2 = urllib2.urlopen(urlHeroList)
        data2 = json.load(json_obj2)
           
        for item in data2['heroes']:
            #getting the hero ID's for the battletags and sets up the url for the hero sets
            heroID = item['id']
            urlHeroSetList = 'https://us.api.battle.net/d3/profile/' +playerBattleTag+ '/hero/' +str(heroID)+ '/items?locale=en_US&apikey=' + bliz_api2
            json_obj3 = urllib2.urlopen(urlHeroSetList)
            data3 = json.load(json_obj3)   
            
            urlHeroAllData = 'https://us.api.battle.net/d3/profile/'+ playerBattleTag + '/hero/' + str(heroID) + '?locale=en_US&apikey=' + bliz_api2
            json_obj4 = urllib2.urlopen(urlHeroAllData)
            data4 = json.load(json_obj4)
            #getting the names of the sets and printing them to the screen.
            print("General Info: ")
            print("Hero Name: " + item['name'])
            print("Hero Class: " + item['class'])
            print("Hero Level: " + str(item['level']))
            print("Hero ParagonLevel: " + str(item['paragonLevel']))
            print("")
            
            print("Stats: ")
            print("Life:                 " + str(data4['stats']['life']))
            print("Damage:               " + str(data4['stats']['damage']))
            print("Toughness:            " + str(data4['stats']['toughness']))
            print("Healing:              " + str(data4['stats']['healing']))
            print("Attack Speed:         " + str(data4['stats']['attackSpeed']))
            print("Armor:                " + str(data4['stats']['armor']))
            print("Strength:             " + str(data4['stats']['strength']))
            print("Dexterity:            " + str(data4['stats']['dexterity']))
            print("Vitality:             " + str(data4['stats']['vitality']))
            print("Intelligence:         " + str(data4['stats']['intelligence']))
            print("Physical Resistance:  " + str(data4['stats']['physicalResist']))
            print("Fire Resistance:      " + str(data4['stats']['fireResist']))
            print("Cold Resistance:      " + str(data4['stats']['coldResist']))
            print("Lightning Resistance: " + str(data4['stats']['lightningResist']))
            print("Poison Resistance:    " + str(data4['stats']['poisonResist']))
            print("Arcane Resistance:    " + str(data4['stats']['arcaneResist']))
            print("Block Chance:         " + str(data4['stats']['blockChance']))
            print("Block Amount Min:     " + str(data4['stats']['blockAmountMin']))
            print("Block Amaount Max:    " + str(data4['stats']['blockAmountMax']))
            print("Gold Find:            " + str(data4['stats']['goldFind']))
            print("Crit Change:          " + str(data4['stats']['critChance']))
            print("Thorns:               " + str(data4['stats']['thorns']))
            print("LifeSteal:            " + str(data4['stats']['lifeSteal']))
            print("Life Per Kill:        " + str(data4['stats']['lifePerKill']))
            print("Life On Hit:          " + str(data4['stats']['lifeOnHit']))
            print("Primary Resource:     " + str(data4['stats']['primaryResource']))
            print("Secondary Resource    " + str(data4['stats']['secondaryResource']))
            print("")
            #setName = data3['head']['set']['name']
            print("Items: ")
            try:
                print("Head:         " + data3['head']['name'])
            except:
                print("Head:         Empty")
                
            try:
                print("Neck:         " + data3['neck']['name'])
            except:
                print("Neck:         Empty")
            
            try:
                print("Torso:        " + data3['torso']['name'])
            except:
                print("Torse:        Empty")
                   
            try:
                print("Shoulders:    " + data3['shoulders']['name'])
            except:
                print("Shoulders:    Empty")
              
            try:    
                print("Legs:         " + data3['legs']['name'])
            except:
                print("Legs:         Empty")
                
            try:    
                print("Waist:        " + data3['waist']['name'])
            except:
                print("Waist:        Empty")
                
            try:
                print("Hands:        " + data3['hands']['name'])
            except:
                print("Hands:        Empty")
                
            try:
                print("Bracers:      " + data3['bracers']['name'])
            except:
                print("Bracers:      Empty")
                
            try:
                print("Feet:         " + data3['feet']['name'])
            except:
                print("Feet:         Empty")
            
            try:
                print("Left Finger:  " + data3['leftFinger']['name'])
            except:
                print("Left Finger:  Empty")
                
            try:
                print("Right Finger: " + data3['rightFinger']['name'])
            except:
                print("Right Finger: Empty")
                
            try:
                print("Main Hand:    " + data3['mainHand']['name'])
            except:
                print("Main Hand:    Empty")
                
            try:
                print("Off Hand:     " + data3['offHand']['name'])
            except:
                print("Off Hand:     Empty")
                
            print("")
            
            print("Active Skills: ")
            try:
                print("Skill 1: " + data4['skills']['active'][0]['skill']['name'])
            except:
                print("Skill 1: Empty")
                
            try:
                print("Skill 2: " + data4['skills']['active'][1]['skill']['name'])
            except:
                print("Skill 2: Empty")
                
            try:
                print("Skill 3: " + data4['skills']['active'][2]['skill']['name'])
            except:
                print("Skill 3: Empty")
                
            try:
                print("Skill 4: " + data4['skills']['active'][3]['skill']['name'])
            except:
                print("Skill 4: Empty")
                
            try:
                print("Skill 5: " + data4['skills']['active'][4]['skill']['name'])
            except:
                print("Skill 5: Empty")
                
            try:
                print("Skill 6: " + data4['skills']['active'][5]['skill']['name'])
            except:
                print("Skill 6: Empty")
            print("")
            
            print("Passive Skills: ")
            try:
                print("Skill 1: " + data4['skills']['passive'][0]['skill']['name'])
            except:
                print("Skill 1: Empty")
                
            try:
                print("Skill 2: " + data4['skills']['passive'][1]['skill']['name'])
            except:
                print("Skill 2: Empty")
                
            try:
                print("Skill 3: " + data4['skills']['passive'][2]['skill']['name'])
            except:
                print("Skill 3: Empty")
                
            try:
                print("Skill 4: " + data4['skills']['passive'][3]['skill']['name'])
            except:
                print("Skill 4: Empty")
            print("")
            
            print("Legendary Powers")
            try:
                print("Power 1: " + data4['legendaryPowers'][0]['name'])
            except:
                print("Power 1: Empty")
                
            try:
                print("Power 2: " + data4['legendaryPowers'][1]['name'])
            except:
                print("Power 2: Empty")
                
            try:
                print("Power 3: " + data4['legendaryPowers'][2]['name'])
            except:
                print("Power 3: Empty")
            break
else:
    print("Goodbye")