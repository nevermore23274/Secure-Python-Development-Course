#Import(s)
import sys
from io import BytesIO
import requests
from PIL import Image
import matplotlib.pyplot as plt

# List for state information
state_info = []
state_info.append(['Alabama', 'Montgomery', 4887681, 'Camellia', "https://statesymbolsusa.org/\
                    sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/\
                    camellia-flower.jpg?itok=K1xKDUI5"])
state_info.append(['Alaska', 'Juneau', 735139, 'Forget-Me-Not', "https://statesymbolsusa.org/\
                    sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/\
                    Alpineforgetmenot.jpg?itok=VxF44TUl"])
state_info.append(['Arizona', 'Phoenix', 7158024, 'Suguaro Catus Blossom',
                    "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/\
                    symbol_thumbnail__medium/public/saguaroflowersFlickr.jpg?itok=DxWnZav5"])
state_info.append(['Arkansas', 'Little Rock', 3009733, 'Apple Blossom', "https://statesymbolsusa.\
                    org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/\
                    primary-images/AppletreeblossomArkansasflower.JPG?itok=HRX6pZyN"])
state_info.append(['California', 'Sacramento ', 39461588, 'California Poppy',
                    "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/\
                    symbol_thumbnail__medium/public/primary-images/\
                    CAflowerCaliforniaPoppy.jpg?itok=62onOuJf"])
state_info.append(['Colorado', 'Denver', 5691287, 'Rocky Mountain Columbine',
                    "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/\
                    symbol_thumbnail__medium/public/Colorado_columbine2.jpg?itok=3bfYnk5Y"])
state_info.append(['Connecticut', 'Hartford', 3571520, 'Mountain Laurel', "https://statesymbolsusa.\
                    org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/\
                    primary-images/Mountain-Laural-flowers2.jpg?itok=b7tlfk4G"])
state_info.append(['Delaware', 'Dover', 965479, 'Peach Blossom', "https://statesymbolsusa.org/\
                    sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/\
                    peachblossomspeachflowers.jpg?itok=Lx-fzlgl"])
state_info.append(['Florida', 'Tallahassee', 21244317, 'Orange Blossom', "https://statesymbolsusa.\
                    org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/\
                    primary-images/OrangeBlossomsFloridaFlower.jpg?itok=SK-Tp-rH"])
state_info.append(['Georgia', 'Atlanta', 10511131, 'Cherokee Rose', "https://statesymbolsusa.org/\
                    sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/\
                    primary-images/CherokeeRoseFlower.jpg?itok=TKWxpzcw"])
state_info.append(['Hawaii', 'Honolulu', 1420593, 'Hinahina', "https://statesymbolsusa.org/sites/\
                    statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/\
                    HinahinaKahoolaweLei3.jpg?itok=Gnp45FQB"])
state_info.append(['Idaho', 'Boise', 1750536, 'Syringa', "https://statesymbolsusa.org/sites/\
                    statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/\
                    syringaPhiladelphuslewisiiflower.jpg?itok=BKOaOXs0"])
state_info.append(['Illinois', 'Springfield', 12723071, 'Violet', "https://statesymbolsusa.org/\
                    sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/\
                    primary-images/singlebluevioletflower.jpg?itok=8i1uQHwg"])
state_info.append(['Indiana', 'Indianapolis', 6695497, 'Peony', "https://statesymbolsusa.org/sites/\
                    statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/\
                    PeonyPaeoniaflowers.jpg?itok=IrFIQ9ZF"])
state_info.append(['Iowa', 'Des Moines', 3148618, 'Wild Rose', "https://statesymbolsusa.org/sites/\
                    statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/\
                    WildPrairieRose.jpg?itok=zyo0qIMG"])
state_info.append(['Kansas', 'Topeka', 2911359, 'Wild Native Sunflower', "https://statesymbolsusa.\
                    org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/\
                    primary-images/native-sunflowers.jpg?itok=PB8Qq-IC"])
state_info.append(['Kentucky', 'Frankfort', 4461153, 'Goldenrod', "https://statesymbolsusa.org/\
                    sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/\
                    primary-images/stateflowergoldenrod-bloom.jpg?itok=CCLZ4eiV"])
state_info.append(['Louisiana', 'Baton Rouge', 4659690, 'Magnolia', "https://statesymbolsusa.org/\
                    sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/\
                    primary-images/MagnoliagrandifloraMagnoliaflower.jpg?itok=LQ7y9QJk"])
state_info.append(['Maine', 'Augusta', 1339057, 'Pine Cone & Tassel',
                    "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/\
                    symbol_thumbnail__medium/public/primary-images/\
                    whitepinemalecones.jpg?itok=cscy757F"])
state_info.append(['Maryland', 'Annapolis', 6035802, 'Black-eyed Susan', "https://statesymbolsusa.\
                    org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/\
                    primary-images/FlowerMDBlack-eyedSusan.jpg?itok=I8jYSvFl"])
state_info.append(['Massachusetts', 'Boston', 6882635, 'Mayflower', "https://statesymbolsusa.org/\
                    sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/\
                    primary-images/MayflowerTrailingArbutus.jpg?itok=uIQd8O6F"])
state_info.append(['Michigan', 'Lansing', 9984072, 'Apple Blossom', "https://statesymbolsusa.org/\
                    sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/\
                    primary-images/appleblossombeauty.jpg?itok=HxWn6VHl"])
state_info.append(['Minnesota', 'St.Paul', 5606249, 'Lady-Slipper', "https://statesymbolsusa.org/\
                    sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/\
                    primary-images/pinkwhiteladysslipperflower1.jpg?itok=LGYZFl26"])
state_info.append(['Mississippi', 'Jackson', 2981020, 'Magnolia', "https://statesymbolsusa.org/\
                    sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/\
                    primary-images/magnoliablossomflower01.jpg?itok=xlIoba-H"])
state_info.append(['Missouri', 'Jefferson City', 6121623, 'Hawthorne Blossom',
                    "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/\
                    symbol_thumbnail__medium/public/primary-images/hawthornflowersblossoms1.jpg\
                    ?itok=LOrlsJ3L"])
state_info.append(['Montana', 'Helena', 1060665, 'Bitterroot', "https://statesymbolsusa.org/sites/\
                    statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images\
                    /bitterrootfloweremblem.jpg?itok=SnCwy78x"])
state_info.append(['Nebraska', 'Lincoln', 1925614, 'Goldenrod', "https://statesymbolsusa.org/sites/\
                    statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/\
                    goldenrodflowersyellow4.jpg?itok=6X5qpm4c"])
state_info.append(['Nevada', 'Carson City', 3027341, 'Sagebrush', "https://statesymbolsusa.org\
                    /sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/\
                    primary-images/Nevada-Sagebrush-Artemisia-tridentata.jpg?itok=ij6RMnom"])
state_info.append(['New Hampshire', 'Concord', 1353465, 'Purple Lilac',
                   "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_\
                    thumbnail__medium/public/primary-images/lilacflowerspurplelilac.jpg?\
                    itok=GM5URJEO"])
state_info.append(['New Jersey', 'Trenton', 8886025, 'Violet', "https://statesymbolsusa.org/sites/\
                    statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/\
                    wood-violet.jpg?itok=IJ0ft_8r"])
state_info.append(['New Mexico', 'Santa Fe', 2092741, 'Yucca', "https://statesymbolsusa.org/sites/\
                    statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/\
                    YuccaFlowersclose.jpg?itok=jCUN8toc"])
state_info.append(['New York', 'Albany', 19530351, 'Rose', "https://statesymbolsusa.org/sites/\
                    statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/\
                    redrosebeautystateflowerNY.jpg?itok=LDcB_Vc_"])
state_info.append(['North Carolina', 'Raleigh', 10381615, 'Dogwood',
                   "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_\
                    thumbnail__medium/public/primary-images/floweringdogwoodflowers2.jpg?\
                    itok=p_1PGcNk"])
state_info.append(['North Dakota', 'Bismark', 758080, 'Prairie Rose',
                   "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/\
                    symbol_thumbnail__medium/public/primary-images/flowerwildprairierose.jpg?\
                    itok=j5Retaxz"])
state_info.append(['Ohio', 'Columbus', 11676341, 'Red Carnation', "https://statesymbolsusa.org/\
                    sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/\
                    primary-images/redcarnationOhioflower.jpg?itok=oCdw9u6V"])
state_info.append(['Oklahoma', 'Oklahoma City', 3940235, 'Mistletoe',
                   "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/\
                   symbol_thumbnail__medium/public/primary-images/mistletoe_phoradendron_\
                   serotinum.jpg?itok=7W9kY8YB"])
state_info.append(['Oregon', 'Salem', 4181886, 'Oregon Grape', "https://statesymbolsusa.org/sites/\
                    statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/\
                    Oregongrapeflowers2.jpg?itok=lVSJoqCE"])
state_info.append(['Pennsylvania', 'Harrisburg', 12800922, 'Mountain Laurel',
                   "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/\
                   symbol_thumbnail__medium/public/Mt_Laurel_Kalmia_Latifolia.jpg?itok=8VhW2Sms"])
state_info.append(['Rhode Island', 'Providence', 1058287, 'Violet', "https://statesymbolsusa.org/\
                    sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/\
                    primary-images/violetsflowers.jpg?itok=KNMrrLfu"])
state_info.append(['South Carolina', 'Columbia', 5084156, 'Yellow Jessamine',
                   "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/\
                   symbol_thumbnail__medium/public/primary-images/CarolinaYellowJessamine101.jpg?\
                   itok=1tgcX6mj"])
state_info.append(['South Dakota', 'Pierre', 878698, 'American Pasque',
                   "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/\
                   symbol_thumbnail__medium/public/primary-images/Pasqueflower-03.jpg?\
                   itok=vMlGt_qW"])
state_info.append(['Tennessee', 'Nashville', 6771631, 'Iris', "https://statesymbolsusa.org/\
                   sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/\
                   purpleirisflower.jpg?itok=ZJjHu7Lb"])
state_info.append(['Texas', 'Austin', 28628666, 'Bluebonnet', "https://statesymbolsusa.org/sites/\
                   statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/\
                   BluebonnetsBlueRed.jpg?itok=taqKfWDs"])
state_info.append(['Utah', 'Salt Lake City', 3153550, 'Sego Lily',
                   "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/\
                   symbol_thumbnail__medium/public/SegoLily.jpg?itok=Hxt3DOTq"])
state_info.append(['Vermont', 'Montpelier', 624358, 'Red Clover', "https://statesymbolsusa.org/\
                    sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/\
                    primary-images/redcloverstateflowerWV.jpg?itok=wvnkPA4C"])
state_info.append(['Virginia', 'Richmond', 8501286, 'American Dogwood', "https://statesymbolsusa\
                    .org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/\
                    public/primary-images/floweringDogwoodSpring.jpg?itok=DFuNFYgS"])
state_info.append(['Washington', 'Olympia', 7523869, 'Coast Rhododendron',
                   "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/\
                   symbol_thumbnail__medium/public/primary-images/flower_rhododendronWeb.jpg?\
                   itok=0Xl911Zf"])
state_info.append(['West Virginia', 'Charleston', 1804291, 'Rhododendron',
                   "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/\
                   symbol_thumbnail__medium/public/primary-images/rhododendronWVstateflower.jpg\
                   ?itok=7lJaeqWT"])
state_info.append(['Wisconsin', 'Madison', 5807406, 'Wood Violet', "https://statesymbolsusa.org/\
                    sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/\
                    wood-violet.jpg?itok=IJ0ft_8r"])
state_info.append(['Wyoming', 'Cheyenne', 577601, 'Indian Paintbrush',
                   "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/\
                   symbol_thumbnail__medium/public/primary-images/indianpaintbrushWYflower.jpg?\
                   itok=ClQHPA55"])


def display_state_info():
    """
    A function to display state information in alphabetical order
    """
    output_buffer = "-"*65 # Just for nice formatting, my eyes didn't like a wall of text
    info_list = [] # Backup list for enumerate to drop info into

    # Header
    print(f"\n{'State' : <15} {'Capital': <15} {'Population': <15} {'Flower': <20}\n")
    print(output_buffer)

    # Display state info in alphabetical order
    for i, info_list in enumerate(state_info):
        print(f"{state_info[i][0] : <15} {state_info[i][1]: <15} {state_info[i][2]: <15} " +
              f"{state_info[i][3]: <20}")
        info_list.append(state_info)
        print(output_buffer)


def search_state(user_input_state_name):
    """
    A function to find specific information for a state
    """
    # Checksum for users state being found
    state_search = False
    # Header
    print(f"\n{'State' : <15} {'Capital': <15} {'Population': <15} {'Flower': <20}\n")

    # Search through state list
    for i, state_search in enumerate(state_info):
        if user_input_state_name.lower() == (state_info[i][0].lower()):
            # Get flower image and covert to bytes
            flower_link = state_info[i][4].replace(" ",'')
            response = requests.get(flower_link)
            flower_img = Image.open(BytesIO(response.content))

            # Display desired state info
            print(f"{state_info[i][0] : <15} {state_info[i][1]: <15} {state_info[i][2]: <15} " +
                  f"{state_info[i][3]: <20}")

            # Display state flower image
            flower_img.show()
            state_search = True
    return state_search


def bar_graph():
    """
    Function to display top five states graph
    """
    data = []

    for i, list_state in enumerate(state_info):
        # Place state info in list
        data.append([-int(state_info[i][2]),state_info[i][0]])
    data.sort()

    # Create state info
    list_population = []
    list_state = []
    list_len = min(len(data),5)
    for i in range(list_len):
        list_population.append(-data[i][0])
        list_state.append(data[i][1])
        i+=1

    # Create and show graph
    plt.bar(list_state, list_population)
    plt.show()


def update_population_state(name, population):
    """
    Function to update a states population
    """
    # Checksum for users state being found
    state_search = False

    # Look for state
    for i, state_search in enumerate(state_info):
        # Check input vs state name
        if name.lower() == (state_info[i][0].lower()):
            # Update population
            state_info[i][2] = population
            state_search = True
    return state_search


def menu_display():
    """
    This function is for the main menu and its overall functionality
    """
    print("\n") # Put distance between prior output and new generated menu
    print("1. Display U.S. States in alphabetical order with the capital," +
          " state population, and flower")
    print("2. Search a state and display its capital name, state population and flower")
    print("3. Display bar graph of the top 5 populated States showing their overall population")
    print("4. Update overall state population for a specific state")
    print("5. Exit the program" )
    print("\n")

if __name__ == "__main__":
    while True:
        # Main menu function call
        menu_display()

        # User menu input
        choice = input("> ")

        if choice[0] == '1':
            # Function for states in alphabetical order
            display_state_info()

        elif choice[0] == '2':
            state_name = input("Enter state: ")
            # Calls state info display function
            STATE_EXISTS = search_state(state_name)
            if STATE_EXISTS is False:
                print(f"{state_name} doesn't exist, please enter a valid state name.")

        elif choice[0] == '3':
            # Function for bar graph
            bar_graph()

        elif choice[0] == '4':
            state_name = input("Enter state name: ")
            state_pop = input("Enter state population: ")
            STATE_EXISTS = update_population_state(state_name, state_pop)
            if STATE_EXISTS is False:
                print(f"{state_name} doesn't exist, please enter a valid state name.")

        elif choice[0] == '5':
            print("\n" + "Thank you for testing my program, goodbye!")
            sys.exit()

        else:
            print("Invalid input: Please enter a value between 1 and 5.")
