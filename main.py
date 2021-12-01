from PIL import Image 
from IPython.display import display 
import random
import json

# Each image is made up a series of traits
# The weightings for each trait drive the rarity and add up to 100%


back = [
    "Alice Blue",
    "Aqua Pear",
    "Beach",
    "Cerulean",
    "Cornflower",
    "Fire Engine Red",
    "Forest Green",
    "Gray",
    "Marine Green",
    "Mustard",
    "Northern Lights",
    "Princeton Orange",
    "Stormcloud",
    "Sunset",
] 
back_weights = [9, 7, 3, 10, 4, 10, 10, 12, 8, 6, 2, 11, 5, 3]

skin = [
    "Breadenza",
    "Damien",
    "Donut",
    "Gold",
    "Marble Rye",
    "Moldy Bread",
    "Multi-Grain",
    "Platinium",
    "Potato",
    "Pumpernicke",
    "Wheat",
    "White",
]
skin_weights = [
    2, 2, 2, 2, 11, 9, 11, 1, 10, 20, 
    20, 10]

shoes = [
    "Breadkicks",
    "Chuck Taylors",
    "Damien",
    "Donut",
    "Dunkz",
    "Gold",
    "High Heels",
    "Platinum",
    "Sneakz",
    "NONE",
]
shoes_weights = [60, 6, 4, 3, 3, 4, 3, 3, 10, 5]

clothes = [
    "Black BW Shirt",
    "Black Hoodie",
    "Black Parka",
    "Black Suit Red Tie",
    "Black Vest",
    "Blue Overalls",
    "Board Shorts",
    "Brown Apron",
    "BW Cycle Shirt",
    "Clown Suit",
    "Donut Dress",
    "Farmer Overalls",
    "Fatigues",
    "Finger Shirt",
    "Firefighter Jacket",
    "gm Shirt",
    "Green BW Shirt",
    "Green Hoodie",
    "Hawaiian Shirt",
    "Judicial Robe",
    "Motorcycle Cut",
    "Nurse Gown",
    "Orange Overalls",
    "PELOMOM Shirt",
    "Pilot Shirt",
    "Police Uniform",
    "Postal Shirt",
    "Red Apron",
    "Red Boxing Robe",
    "Red BW Shirt",
    "Red Parka",
    "Soccer Jersey",
    "Space Suit",
    "Squiggle Shirt",
    "Surgeon Gown",
    "Sweater Vest",
    "Trench Coat",
    "Tuxedo",
    "Tye-Dye Finger Shirt",
    "Tye-Dye Shirt",
    "WAGMI Shirt",
    "White Lab Coat",
    "Zildjan Shirt",
    "NONE",
]

clothes_weights = [
    1, 3, 4, 2, 2, 2, 2, 1, 1, 2, 
    1, 3, 2, 1, 3, 0, 2, 1, 3, 2, 
    2, 2, 3, 3, 2, 4, 2, 2, 2, 2, 
    2, 3, 3, 3, 2, 1, 2, 3, 3, 1, 
    2, 2, 1, 9
]

mouth = [
    "Angry",
    "Beard",
    "Big smile",
    "Vig smile w/Beard",
    "Bored",
    "Bubblegum",
    "Gold tooth",
    "Grumpy",
    "Happy",
    "Hoagie Mouth",
    "Nervous",
    "Red Lipstick",
    "Salivating",
    "Surprised",
    "Tongue out",
    "Wheat Straw",
    "Yawn",
    "NONE",
]

mouth_weights = [
    6, 2, 6, 2, 6, 5, 1, 6, 19, 1,
    6, 6, 6, 9, 6, 7, 6, 0
]

eyes = [
    "Blindfold",
    "Bloodshot",
    "Confused",
    "ETH Eyes",
    "Happy",
    "Lashes",
    "Ski Goggles",
    "Stern Look",
    "Surprised",
    "Verb Glasses",
    "VR Goggles",
    "Wink"
]

eyes_weights = [
    2, 6, 7, 5, 20, 20, 5, 17, 7, 1, 
    2, 8
]


acc = [
   "Soccer Balls",
   "Stethoscope",
   "Yoga Mat",
   "NONE",
] 
acc_weights = [
   1, 2, 1, 96
]

hair = [
    "Blonde Hair",
    "Brown Hair",
    "NONE",
]

hair_weights =[
    6, 6, 88
]

hat = [
    "Banana",
    "Beanie",
    "Beret",
    "Blue and White cap",
    "Bucket Hat",
    "Carwheel Hat",
    "Chef's Hat",
    "Crown",
    "Deerstalker Hat",
    "Fascinator Hat",
    "Fireman Helmet",
    "Gatsby Cap",
    "gm Cap",
    "Graduation Cap",
    "Hard Hat",
    "Nurse Hat",
    "Panama Hat",
    "Party Hat",
    "Patrol Cap",
    "Pilot Cap",
    "Police Cap",
    "Postal Cap",
    "Sailor Cap",
    "Sombrero",
    "Space Helmet",
    "Sun Hat",
    "Surgeon Cap",
    "Tophat",
    "Trucker Hat",
    "Wizard Hat",
    "NONE",
] 
hat_weights = [
    2, 7, 2, 10, 0, 3, 3, 2, 2, 4, 
    3, 4, 1, 4, 3, 2, 3, 2, 2, 4, 
    2, 3, 1, 1, 4, 2, 4, 3, 2, 2, 
    34,
]

eye_acc = [
    "3D Glasses",
    "Aviators",
    "Black Spectacles",
    "Cat Eye Sunglasses",
    "Eye Patch",
    "Green Spectacles",
    "Green Visor",
    "Groucho Glasses",
    "Monocle",
    "NONE",
]

eye_acc_weights = [
    2, 4, 3, 3, 1, 3, 1, 1, 1, 81
]

lefthand = [
    "Amajawn Box",
    "Balloon",
    "Book",
    "Briefcase",
    "Cloche",
    "Coffee Cup",
    "Coffee Drink",
    "Dog on a Leash",
    "Drumsticks",
    "ETH Coins",
    "Gold Dog on Leash",
    "Lighter",
    "Medical Bag",
    "Microphone",
    "oPhone",
    "Palette",
    "Scales of Justice",
    "Shovel",
    "NONE",
]

lefthand_weights = [
    6, 2, 2, 2, 1, 2, 2, 2, 1, 1, 
    1, 1, 1, 6, 1, 2, 2, 2, 63
]

righthand= [
    "Award",
    "Bacon",
    "Beach Towel",
    "Bottle of Wine",
    "Cane",
    "Creamer",
    "Drumstick",
    "Fire Hydrant",
    "Flag",
    "Gold Watch",
    "Green Syringe",
    "Guitar",
    "Hammer",
    "Magnifying Glass",
    "Mail",
    "Mallet",
    "Paintbrush",
    "Plunger",
    "Pointer",
    "Purple Beaker",
    "Red Syringe",
    "Rolling Pin",
    "Ticket Stub",
    "NONE",
]

righthand_weights = [
    1, 4, 2, 2, 1, 2, 2, 2, 1, 2, 
    1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 
    2, 2, 1, 61, 
]

back_files = {
    "Alice Blue": "1aliceblue",
    "Aqua Pear": "2aquapearl",
    "Beach": "3beach",
    "Cerulean": "4cerulean",
    "Cornflower": "5cornflower",
    "Fire Engine Red": "6fireenginered",
    "Forest Green": "7forestgreen",
    "Gray": "8gray",
    "Marine Green": "9marinegreen",
    "Mustard": "10mustard",
    "Northern Lights": "11northernlights",
    "Princeton Orange": "12orange",
    "Stormcloud": "13stormcloud",
    "Sunset": "14sunset",
}

skin_files = {
    "Breadenza": "1breadenza",
    "Damien": "2damien",
    "Donut": "3donut",
    "Gold": "4gold",
    "Marble Rye": "5marblerye",
    "Moldy Bread": "6moldybread",
    "Multi-Grain": "7multigrain",
    "Platinium": "8platinum",
    "Potato": "9potato",
    "Pumpernicke": "10pumpernickel",
    "Wheat": "11wheat",
    "White": "12white",
}

shoes_files = {
    "Breadkicks": "1breadkicks",
    "Chuck Taylors": "2chucktaylors",
    "Damien": "3damien",
    "Donut": "4donut",
    "Dunkz": "5dunkz",
    "Gold": "6gold",
    "High Heels": "7highheels",
    "Platinum": "8platinum",
    "Sneakz": "9sneakz",
    "NONE": "NONE",
}

clothes_files = {
    "Black BW Shirt": "1blackbwshirt",
    "Black Hoodie": "2blackhoodie",
    "Black Parka": "3blackparka",
    "Black Suit Red Tie": "4blacksuitredtie",
    "Black Vest": "5blackvest",
    "Blue Overalls": "6blueoveralls",
    "Board Shorts": "7boardshorts",
    "Brown Apron": "8brownapron",
    "BW Cycle Shirt": "9bwcycleshirt",
    "Clown Suit": "10clownsuit",
    "Donut Dress": "11donutdress",
    "Farmer Overalls": "13farmeroveralls",
    "Fatigues": "14fatigues",
    "Finger Shirt": "15fingershirt",
    "Firefighter Jacket": "16firefighterjacket",
    "gm Shirt": "17gmshirt",
    "Green BW Shirt": "18greenbwshirt",
    "Green Hoodie": "19greenhoodie",
    "Hawaiian Shirt": "20hawaiianshirt",
    "Judicial Robe": "21judicialrobe",
    "Motorcycle Cut": "22motorcyclecut",
    "Nurse Gown": "23nursegown",
    "Orange Overalls": "24orangeoveralls",
    "PELOMOM Shirt": "25pelomomshirt",
    "Pilot Shirt": "26pilotshirt",
    "Police Uniform": "27policeuniform",
    "Postal Shirt": "28postalshirt",
    "Red Apron": "29redapron",
    "Red Boxing Robe": "30redboxingrobe",
    "Red BW Shirt": "31redbwshirt",
    "Red Parka": "32redparka",
    "Soccer Jersey": "33soccerjersey",
    "Space Suit": "34spacesuit",
    "Squiggle Shirt": "35squiggleshirt",
    "Surgeon Gown": "36surgeongown",
    "Sweater Vest": "37sweatervest",
    "Trench Coat": "38trenchcoat",
    "Tuxedo": "39tuxedo",
    "Tye-Dye Finger Shirt": "40tyedyefingershirt",
    "Tye-Dye Shirt": "41tyedyeshirt",
    "WAGMI Shirt": "42wagmishirt",
    "White Lab Coat": "43whitelabcoat",
    "Zildjan Shirt": "45zildjanshirt",
    "NONE": "NONE",
}

mouth_files = {
    "Angry": "1angry",
    "Beard": "2beard",
    "Big smile": "3bigsmile",
    "Vig smile w/Beard": "4bigsmilebeard",
    "Bored": "5bored",
    "Bubblegum": "6bubblegum",
    "Gold tooth": "7goldtooth",
    "Grumpy": "8grumpy",
    "Happy": "9happy",
    "Hoagie Mouth":"10hoagiemouth",
    "Nervous": "11nervous",
    "Red Lipstick": "12redlipstick",
    "Salivating": "13salivating",
    "Surprised": "14surprised",
    "Tongue out": "15tongueout",
    "Wheat Straw": "16wheatstraw",
    "Yawn": "17yawn",
    "NONE": "NONE"
}

eyes_files = {
    "Blindfold": "1blindfold",
    "Bloodshot": "2bloodshot",
    "Confused": "3confused",
    "ETH Eyes": "4etheyes",
    "Happy": "5happy",
    "Lashes": "6lashes",
    "Ski Goggles": "7skigoggles",
    "Stern Look": "8sternlook",
    "Surprised": "9surprised",
    "Verb Glasses": "10verbglasses",
    "VR Goggles": "11vrgoggles",
    "Wink": "12wink",
}

acc_files = {
    "Soccer Balls": "3soccerballs",
    "Stethoscope": "4stethoscope",
    "Yoga Mat": "5yogamat",
    "NONE": "NONE",
}

hat_files = {
    "Banana": "1bandana", 
    "Beanie": "2beanie",
    "Beret": "3beret", 
    "Blue and White cap": "4blueandwhitehat", 
    "Bucket Hat": "5buckethat",
    "Carwheel Hat": "6cartwheelhat",
    "Chef's Hat": "7chefhat",
    "Crown": "8crown",
    "Deerstalker Hat": "9deerstalkerhat",
    "Fascinator Hat": "10fascinatorhat",
    "Fireman Helmet": "11firemanhelmet",
    "Gatsby Cap": "12gatsbycap",
    "gm Cap": "13gmcap",
    "Graduation Cap": "14graduationcap", 
    "Hard Hat": "15hardhat",
    "Nurse Hat": "16nursehat", 
    "Panama Hat": "17panamahat", 
    "Party Hat": "18partyhat", 
    "Patrol Cap": "19patrolcap",
    "Pilot Cap": "20pilotcap",
    "Police Cap": "21policecap",
    "Postal Cap": "22postalcap",
    "Sailor Cap": "23sailorcap",
    "Sombrero": "24sombrero",
    "Space Helmet": "25spacehelmet",
    "Sun Hat": "26sunhat",
    "Surgeon Cap": "27surgeoncap",
    "Tophat": "28tophat",
    "Trucker Hat": "29truckerhat", 
    "Wizard Hat": "30wizardhat",
    "NONE": "NONE"
}

hair_files = {
    "Blonde Hair": "1blondehair",
    "Brown Hair": "2brownhair",
    "NONE": "NONE", 
}

eye_acc_files = {
    "3D Glasses": "1threedimensionglasses",
    "Aviators": "2aviators",
    "Black Spectacles": "3blackspectacles",
    "Cat Eye Sunglasses": "4cateyesunglasses",
    "Eye Patch": "5eyepatch",
    "Green Spectacles": "6greenspectacles",
    "Green Visor": "7greenvisor",
    "Groucho Glasses": "8grouchoglasses",
    "Monocle": "9monocle",
    "NONE": "NONE",
}

lefthand_files = {
    "Amajawn Box": "1amajawnbox",
    "Balloon": "2balloon",
    "Book": "3book",
    "Briefcase": "4briefcase",
    "Cloche": "5cloche",
    "Coffee Cup": "6coffeecup",
    "Coffee Drink": "7coffeedrink",
    "Dog on a Leash": "8dogonaleash",
    "Drumsticks": "9drumsticks",
    "ETH Coins": "10ethcoins",
    "Gold Dog on Leash": "11golddogonleash",
    "Lighter": "12lighter",
    "Medical Bag": "13medicalbag",
    "Microphone": "14microphone",
    "oPhone": "15ophone",
    "Palette": "16palette",
    "Scales of Justice": "17scalesofjustice",
    "Shovel": "18shovel",
    "NONE": "NONE",
}

righthand_files = {
    "Award": "1award",
    "Bacon": "2bacon",
    "Beach Towel": "3beachtowel",
    "Bottle of Wine": "4bottleofwine",
    "Cane": "5cane",
    "Creamer": "6creamer",
    "Drumstick": "7drumstick",
    "Fire Hydrant": "8firehydrant",
    "Flag": "9flag",
    "Gold Watch": "10goldwatch",
    "Green Syringe": "11greensyringe",
    "Guitar": "12guitar",
    "Hammer": "13hammer",
    "Magnifying Glass": "14magnifyingglass",
    "Mail": "15mail",
    "Mallet": "16mallet",
    "Paintbrush": "17paintbrush",
    "Plunger": "18plunger",
    "Pointer": "19pointer",
    "Purple Beaker": "20purplebeaker",
    "Red Syringe": "21redsyringe",
    "Rolling Pin": "22rollingpin",
    "Ticket Stub": "23ticketstub",
    "NONE": "NONE",
}

## Generate Traits
TOTAL_IMAGES = 7018 # Number of random unique images we want to generate

all_images = [] 

# A recursive function to generate unique image combinations
def create_new_image():
    
    new_image = {} #

    # For each trait category, select a random trait based on the weightings 
    new_image ["Back"] = random.choices(back, back_weights)[0]
    new_image ["Skin"] = random.choices(skin, skin_weights)[0]
    new_image ["Shoes"] = random.choices(shoes, shoes_weights)[0]
    new_image ["Clothes"] = random.choices(clothes, clothes_weights)[0]
    new_image ["Mouth"] = random.choices(mouth, mouth_weights)[0]
    new_image ["Eyes"] = random.choices(eyes, eyes_weights)[0]
    new_image ["Acc"] = random.choices(acc, acc_weights)[0] 
    new_image ["Eyeacc"] = random.choices(eye_acc, eye_acc_weights)[0]   
    new_image ["Hat"] = random.choices(hat, hat_weights)[0]
    new_image ["Hair"] = random.choices(hair, hair_weights)[0]
    new_image ["Lefthand"] = random.choices(lefthand, lefthand_weights)[0]
    new_image ["Righthand"] = random.choices(righthand, righthand_weights)[0]
    

    # rule 1
    if 'Space Helmet' in new_image ['Hat']:
        if 'Green Visor' in new_image ['Eyeacc'] or 'Book' in new_image ['Lefthand']:
            return create_new_image()
            
        mouth_arr = [
            "Angry",
            "Big smile",
            "Vig smile w/Beard",
            "Bored",
            "Gold tooth",
            "Grumpy",
            "Happy",
            "Nervous",
            "Red Lipstick",
            "Salivating",
            "Tongue out",
            "Yawn",
        ]
        new_image ["Mouth"] = random.choice(mouth_arr)
        
        eyes_arr = [
            "Bloodshot",
            "Confused",
            "ETH Eyes",
            "Happy",
            "Lashes",
            "Stern Look",
            "Wink"
        ]
        new_image ["Eyes"] = random.choice(eyes_arr)

    # rule 2
    if 'Sun Hat' in new_image ['Hat']:   
        if '3D Glasses' in new_image ['Eyeacc'] or 'Aviators' in new_image ['Eyeacc'] or 'Green Visor' in new_image ['Eyeacc']:
            return create_new_image()     
        eyes_arr_2 = [          
            "Confused",
            "ETH Eyes",
            "Happy",
            "Lashes",
            "Stern Look",
            "Wink"
        ]
        new_image ["Eyes"] = random.choice(eyes_arr_2)

    # rule 3
    if 'Blonde Hair' in new_image ['Hair'] or 'Brown Hair' in new_image ['Hair']:    
        new_image ['Eyes'] = 'Lashes'

        temp_hat = [           
            "Chef's Hat",
            "Crown",
            "Fascinator Hat",
            "Nurse Hat",
            "Patrol Cap",
            "Sailor Cap",
            "Trucker Hat",
            "NONE",
        ] 
        new_image ['Hat'] = random.choice(temp_hat)
        # ruke 4
        if 'Guitar' in new_image ['Righthand']:
            return create_new_image()
    
    # rule 6
    if 'Hoagie Mouth' in new_image ['Mouth'] and 'Clothe' in new_image ['Acc']:  
        return create_new_image()

    # rule 7
    if 'Beanie' in new_image ['Hat'] and 'Award' in new_image ['Righthand']:  
        return create_new_image()

    # rule 8  
    eyes_ban_arr = [
        "Blindfold",
        "Lashes",
        "Ski Goggles",
        "Surprised",
        "Verb Glasses",
        "VR Goggles",
    ]
    if 'Aviators' in new_image ['Eyeacc'] or 'Cat Eye Sunglasses' in new_image ['Eyeacc']:
        for i in eyes_ban_arr:
            if i == new_image ['Eyes']:
                return create_new_image()

    
    eye_acc_temp = [
        "3D Glasses",
        "Black Spectacles",
        "Eye Patch",
        "Green Spectacles",
        "Green Visor",
        "Groucho Glasses",
        "Monocle"
    ]

    eyes_temp = [
        "Surprised",
        "Blindfold",
        "Ski Goggles",
        "Stern Look",
        "Verb Glasses",
        "VR Goggles",
    ]
    
    for j in eye_acc_temp:
        for k in eyes_temp:
            if j == new_image ['Eyeacc'] and k == new_image ['Eyes']:
                return create_new_image()

    # rule 9
    if 'Wheat Straw' in new_image ['Mouth']:
        if 'Soccer Balls' in new_image ['Acc'] or 'Book' in new_image ['Lefthand']:
            return create_new_image()
    
    # rule 12
    if 'VR Goggles' in new_image ['Eyes']:
        if 'Hoagie Mouth' in new_image ['Mouth']:
            return create_new_image()


    # if 'Lashes' in new_image ['Eyes']:
    #     if not ('Blonde Hair' in new_image ['Hat'] or 'Brown Hair' in new_image ['Hat']):
    #         return create_new_image()

    # rule 13
    if 'Ski Goggles' in new_image ['Eyes']:
        if 'Surgeon Cap' in new_image ['Hat']:
            return create_new_image()

    # rule 14
    if 'Eye Patch' in new_image ['Eyeacc']:
        if 'Blindfold' in new_image ['Eyes']:
            return create_new_image()
               
    # rule 15
    if 'Mail' in new_image ['Righthand']:
        if 'Sun Hat' in new_image ['Hat']:
            return create_new_image()

    # rule 16
    if 'Trucker Hat' in new_image['Hat'] or 'Beanie' in new_image['Hat']:
        if 'Cane' in new_image ['Righthand']:
             return create_new_image()

    # rule 16
    if 'Sombrero' in new_image['Hat'] or 'Beanie' in new_image['Hat']:
        if 'Cane' in new_image ['Righthand'] or 'Rolling Pin' in new_image ['Righthand']:
             return create_new_image()

    # rule 16
    if 'Trucker Hat' in new_image['Hat'] or 'Beanie' in new_image['Hat']:
        if 'Cane' in new_image ['Righthand'] or 'Drumstick' in new_image ['Righthand'] or 'Paintbrush' in new_image ['Righthand']:
             return create_new_image()

    # rule 18
    if 'Sun Hat' in new_image ['Hat']:
        if 'Balloon' in new_image ['Lefthand']:
            return create_new_image()

    if 'Dog on a Leash' in new_image ['Lefthand'] or 'Gold Dog on Leash' in new_image ['Lefthand']:
        if 'Bottle of Wine' in new_image ['Righthand']  or 'Fire Hydrant' in new_image ['Righthand']  or 'Guitar' in new_image ['Righthand'] or 'Yoga Mat' in new_image ['Acc'] or 'Soccer Balls' in new_image ['Acc']:
            return create_new_image()

    # rule 20
    if 'Drumsticks' in new_image ['Lefthand'] or 'ETH Coins' in new_image ['Lefthand']:       
        new_image ['Righthand'] = 'NONE'     
    

    # rule 21
    if 'Red Syringe' in new_image['Righthand'] or 'Green Syringe' in new_image['Righthand']:
        if 'Bloodshot' in new_image['Eyes'] or 'Finger Shirt' in new_image ['Clothes'] or 'Tye-Dye Shirt' in new_image ['Clothes'] or 'Zildjan Shirt'  in new_image ['Clothes']:
            return create_new_image()

    # rule 22
    if 'Surprised' in new_image ['Eyes']:
        if '8grouchoglasses' in new_image['Eyeacc'] or 'Eye Patch' in new_image ['Eyeacc'] or 'Bubblegum' in new_image ['Mouth'] or 'Verb Glasses' in new_image ['Eyes']: 
            return create_new_image()
    
    # rule 23
    if 'Bubblegum' in new_image ['Mouth']:
        if 'Blindfold' in new_image ['Eyes'] or 'VR Goggles' in new_image ['Eyes'] or 'Ski Goggles' in new_image ['Eyes'] or 'Verb Glasses' in new_image ['Eyes'] or 'Green Spectacles'  in new_image ['Eyeacc'] or 'Green Visor'  in new_image ['Eyeacc'] or 'Groucho Glasses'  in new_image ['Eyeacc'] or 'Cat Eye Sunglasses'  in new_image ['Eyeacc'] or '3D Glasses' in new_image ['Eyeacc'] or 'Bubblegum' in new_image ['Mouth']: 
            return create_new_image()


    if 'Soccer Balls' in new_image ['Acc']:
        new_image ['Lefthand'] = 'NONE'
        new_image ['Righthand'] = 'NONE'
 
    if 'Yoga Mat' in new_image ['Acc']:
        if 'Bottle of Wine' in new_image ['Righthand']  or 'Fire Hydrant' in new_image ['Righthand']  or 'Guitar' in new_image ['Righthand']  or 'Soccer Balls' in new_image ['Acc']:
            return create_new_image()

    if 'Groucho Glasses' in new_image ['Eyeacc']:
        if 'Surprised' in new_image ['Eyes']:
            return create_new_image()


    if 'Soccer Balls' in new_image ['Acc']:
        if 'Bubblegum' in new_image ['Mouth']:
            return create_new_image()

    if 'Gold' in new_image ['Skin']:
        new_image ['Shoes'] = 'Gold'

    if new_image in all_images:
        return create_new_image()
    else:
        return new_image
    
    
# Generate the unique combinations based on trait weightings
for i in range(TOTAL_IMAGES): 
    
    new_trait_image = create_new_image()
    
    all_images.append(new_trait_image)


# Returns true if all images are unique
def all_images_unique(all_images):
    seen = list()
    return not any(i in seen or seen.append(i) for i in all_images)

# print("Are all images unique?", all_images_unique(all_images))

# Add token Id to each image
i = 0
for item in all_images:
    item["tokenId"] = i
    i = i + 1

# print(all_images)

# Get Trait Counts
# acc_count = {}
# for item in acc:
#     acc_count[item] = 0
    
# body_count = {}
# for item in body:
#     body_count[item] = 0

# clothes_count = {}
# for item in clothes:
#     clothes_count[item] = 0

# eye_count = {}
# for item in eye:
#     eye_count[item] = 0

# hand_count = {}
# for item in hand:
#     hand_count[item] = 0

# hat_count = {}
# for item in hat:
#     hat_count[item] = 0

# legs_count = {}
# for item in legs:
#     legs_count[item] = 0 

# mouth_count = {}
# for item in mouth:
#     mouth_count[item] = 0
    
# mouth_count = {}
# for item in mouth:
#     mouth_count[item] = 0

# for image in all_images:
#     acc_count[image["Acc"]] += 1
#     body_count[image["Body"]] += 1
#     clothes_count[image["Clothes"]] += 1
#     eye_count[image["Eye"]] += 1
#     hand_count[image["Hand"]] += 1
#     hat_count[image["Hat"]] += 1
#     legs_count[image["Legs"]] += 1
#     mouth_count[image["Mouth"]] += 1

#### Generate Metadata for all Traits 
METADATA_FILE_NAME = './metadata/all-traits.json'; 
with open(METADATA_FILE_NAME, 'w') as outfile:
    json.dump(all_images, outfile, indent=4)

#### Generate Images    
for item in all_images:

   
    im1 = Image.open(f'./trait-layers/12_background/{back_files[item["Back"]]}.png').convert('RGBA')
    im2 = Image.open(f'./trait-layers/11_skin/{skin_files[item["Skin"]]}.png').convert('RGBA')
    im3 = Image.open(f'./trait-layers/10_shoes/{shoes_files[item["Shoes"]]}.png').convert('RGBA')
    im4 = Image.open(f'./trait-layers/9_clothes/{clothes_files[item["Clothes"]]}.png').convert('RGBA')
    im6 = Image.open(f'./trait-layers/8_mouth/{mouth_files[item["Mouth"]]}.png').convert('RGBA')
    im7 = Image.open(f'./trait-layers/7_eyes/{eyes_files[item["Eyes"]]}.png').convert('RGBA')
    im8 = Image.open(f'./trait-layers/6_eyeaccessories/{eye_acc_files[item["Eyeacc"]]}.png').convert('RGBA')
    im9 = Image.open(f'./trait-layers/5_righthand/{righthand_files[item["Righthand"]]}.png').convert('RGBA')
    im10 = Image.open(f'./trait-layers/4_lefthand/{lefthand_files[item["Lefthand"]]}.png').convert('RGBA')
    im5 = Image.open(f'./trait-layers/3_accessories/{acc_files[item["Acc"]]}.png').convert('RGBA')
    im11 = Image.open(f'./trait-layers/2_hair/{hair_files[item["Hair"]]}.png').convert('RGBA')
    im12 = Image.open(f'./trait-layers/1_hat/{hat_files[item["Hat"]]}.png').convert('RGBA')

    #Create each composite 
    com1 = Image.alpha_composite(im1, im2)
    com2 = Image.alpha_composite(im3, im4)
    com3 = Image.alpha_composite(im5, im6)
    com4 = Image.alpha_composite(im7, im8)
    com5 = Image.alpha_composite(im9, im10)
    com6 = Image.alpha_composite(im11, im12)

    com7 = Image.alpha_composite(com1, com2)
    com8 = Image.alpha_composite(com3, com4)
    com9 = Image.alpha_composite(com5, com6)
    com10 = Image.alpha_composite(com7, com8)

    com11 = Image.alpha_composite(com9, com10)
    com12 = Image.alpha_composite(com11, im12)
    com13 = Image.alpha_composite(com12, im9)
    com14 = Image.alpha_composite(com13, im10)


    # # rule 5
    # if 'Hoagie Mouth' in item['Mouth'] and 'Stethoscope' in item['Acc']:
    #     # rule 8
    #     if 'Beanie' in item['Hat'] and 'Award' in item['Acc']:
    #         com3 = Image.alpha_composite(im8, im5)
    #         com4 = Image.alpha_composite(im6, im7)
    #     else:
    #         com3 = Image.alpha_composite(im7, im5)
    #         com4 = Image.alpha_composite(im6, im8)



    # else:
    #     com3 = Image.alpha_composite(im5, im6)
    #     # rule 8
    #     if 'Beanie' in item['Hat'] and 'Award' in item['Acc']:
    #         com4 = Image.alpha_composite(im8, im7)
    #     else:
    #         com4 = Image.alpha_composite(im7, im8)




    #Convert to RGB
    rgb_im = com14.convert('RGBA')
        

    file_name = str(item["tokenId"]) + ".png"
    rgb_im.save("./images/" + file_name)
	
#### Generate Metadata for each Image    
f = open('./metadata/all-traits.json',) 
data = json.load(f)

IMAGES_BASE_URI = "ADD_IMAGES_BASE_URI_HERE"
PROJECT_NAME = "BreadWinner"

def getAttribute(key, value):
    return {
        "trait_type": key,
        "value": value
    }
for i in data:
    token_id = i['tokenId']
    token = {
        "image": IMAGES_BASE_URI + str(token_id) + '.png',
        "tokenId": token_id,
        "name": PROJECT_NAME + ' ' + str(token_id),
        "attributes": []
    }
    token["attributes"].append(getAttribute("Back", i["Back"]))
    token["attributes"].append(getAttribute("Skin", i["Skin"]))
    token["attributes"].append(getAttribute("Shoes", i["Shoes"]))
    token["attributes"].append(getAttribute("Clothes", i["Clothes"]))
    token["attributes"].append(getAttribute("Mouth", i["Mouth"]))
    token["attributes"].append(getAttribute("Eyes", i["Eyes"]))    
    token["attributes"].append(getAttribute("Acc", i["Acc"]))
    token["attributes"].append(getAttribute("Hat", i["Hat"]))
    
    

    with open('./metadata/' + str(token_id), 'w') as outfile:
        json.dump(token, outfile, indent=4)
f.close()