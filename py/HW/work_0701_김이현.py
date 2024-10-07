#-------------------딕셔너리dict----------------
#p149------
camille={'health':575.6,
         'health_regen':1.7,
         'mana': 338.8,
         'mana_regen':1.63,
         'melee': 125 ,
         'attack_damage':60,
         'attack_speed': 0.625,
         'armor':26,
         'magic_ resistance':32.1,
         'movement_speed':340}
print(camille['health'])
print(camille['movement_speed'])

#p150---------------------------------------
a=dict(zip(["health" ,"health_regen" ,"mana" ,"mana_rehen"],[575.6, 1.7, 338.8, 1.63]))
print(a)

#P164-------------------------------------------------------------
x=5

if x != 10 :
    print('ok')

#p174------------------------------------

tast=80
t=True

if tast >=80 and t == True:
    print('합격')
else :
    print('불합')

