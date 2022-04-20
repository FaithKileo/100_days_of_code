print("WELCOME TO HIGHER/LOWER GAME.")

import random 

data = [{'name': 'Instagram',
         'follower_count': 346,
         'description': 'Social media platform',
         'country': 'United states'
         },
        
        {'name': 'Christian Ronaldo',
         'follower_count': 215,
         'description': 'footballer',
         'country': 'Portugal',
        },
        
        {'name': 'Ariana Grande',
         'follower_count': 183,
         'description': 'Musician',
         'country': 'United states',
        },
        
        {'name': 'Dwayne Johnson',
         'follower_count': 181,
         'description': 'Actor and professional wrestler',
         'country': 'United states',
        }]

def format_data( account ):
    """Formatt the data into printable form which does not show the follower count."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr} from {account_country}"


score = 0
game_over = False
account_b = random.choice(data)

while not game_over:
    score += 1
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    print (f"Compare A: {format_data(account_a)}")
    print("VS")
    print (f"Compare B: {format_data(account_b)}")

    choice = input("Who has more followers? Type 'A' or 'B' : ")

    def answer(choice, score):
        """Takes in the choice of the user and compares it with the nummber of followers and returns the score."""
        A = account_a["follower_count"]
        B = account_b["follower_count"]
        
        if choice == "A" and A > B:
            return f"You are right. Current score {score}"
            
        elif choice == "A" and A < B:
            return f"You are wrong. Current score {score - 1}"
            
        elif choice == "B" and B > A:
            return f"You are right. Current score is {score}"
            
        elif choice == "B" and B < A:
            return f"You are wrong. Current score is {score - 1}"
    
    print(answer(choice, score))
# ONE THING THAT HAS REMAINED IN THIS GAME IS HOW TO MAKE THE GAME END.