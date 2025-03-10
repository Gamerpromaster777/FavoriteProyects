#https://chatgpt.com/share/67816f2e-4ef0-8006-bdb4-a621046f07dc 
# Here Up you can see how I used Chatgpt
def main():
    list = []
    sterlinpounds = 0  
    
    print("Welcome to Your Walmart Shop")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" )
    
    while True:
        print("\n What would you like to do?")
        print("1. Add stuff to your cart ")
        print("2. See what's in your cart ")
        print("3. Remove stuff on your cart")
        print("4. Remove EVERYTHING that is on your cart ")
        print("5. Set your budget(Pls more than 100$) ")
        print("6. I'm done shopping")
        
        choice = input("\nSo what are you choosing (1-6): ")
        
        if choice == '1':
            while True:
                new = input("\nWhat do you need to buy? You can just type the word leave to leave ")
                if new == 'leave':
                    print("Alright, lets go back to the menu")
                    break
                elif new:
                    list.append(new)
                    print(f" Nice, its added {new} to your list!")
                else:
                    print("OMG whats wrong with you, you didn't type anything, get off")
                    
        elif choice == '2':
            if list:
                print("\n Here's what you're planning to buy:")
                for i, item in enumerate(list, 1):
                    print(f"{i}. {item}")
                if sterlinpounds > 0:
                    print(f"\nYour money is: ${sterlinpounds}")
            else:
                print("\n Are you dumb!!!, Theres nothing here, Buy stuff, i need the money")
                
        elif choice == '3':
            if list:
                print("\nHere's your list:")
                for i, item in enumerate(list, 1):
                   print(f"{i}. {item}")
                try:
                    remove = input("\nWhat number do you want to remove? ")
                    popo = int(remove) - 1
                    if 0 <= popo < len(list):  
                        removed = list[popo]
                        del list[popo] 
                        print(f"Removed {removed} from your list!")
                    else:
                       print("That is not a valid number, just go back to Kindergarden")
                except ValueError:
                    print("try again !")
            else:
              print("\nYou got nothing on your cart, you broke")

                
        elif choice == '4':
            if list:
                confirm = input("Are you sure you want to clear everything??: ")
                if confirm== 'yes':
                    list.clear()
                    print("Poof! Your list is now empty!")
                else:
                    print("Okay, keeping your items")
            else:
                print("\nYour cart is already empty, you are suck an broke.")
                
        elif choice == '5':
            try:
                sterlinpounds = float(input("How much do you want to spend? $$"))
                print(f" Money set to ${sterlinpounds}")
            except:
                print("Enter an valid number, and it better be more than 100$ ")

        elif choice == '6':
            print("I dont get paid enough, just go!")
            break
            
        else:
            print("\n I dont get paid enough for this, choose an option 1-6")


if __name__ == "__main__":
    main()