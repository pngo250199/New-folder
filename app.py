#restaurant self project of oop
#main page welcome guest
#menu page separate
class Restaurant:
    def __init__(self,FrontPage):
        self.FrontPage = FrontPage
        print(self.FrontPage)


class MotherPage:
    def __init__(self, PageTitle):
        self.PageTitle
    def display(self):
        print(f"displaying the {self.PageTitle} page.")

class PageManager:
    def __init__(self):
        self.pages = []  # List to store pages
        self.current_index = -1  # Keeps track of the current page index
    

    def switch_page(self, index):
        # Switch to a specific page by index
        if 0 <= index < len(self.pages):
            self.current_index = index
            print(f"Switched to the {self.pages[self.current_index].FrontPage} page")
            self.pages[self.current_index].display()
        else:
            print(f"Page index {index} out of range.")

    def add_page(self, page):
        # Add a new page to the list of pages
        self.pages.append(page)
    
    def next_page(self):
        # Move to the next page if possible
        if self.current_index + 1 < len(self.pages):
            self.current_index += 1
            print(f"Next page: {self.pages[self.current_index].FrontPage}")
            self.pages[self.current_index].display()
        else:
            print("No next page available.")
    
    def previous_page(self):
        # Move to the previous page if possible
        if self.current_index - 1 >= 0:
            self.current_index -= 1
            print(self.pages[self.current_index].FrontPage)
            self.pages[self.current_index].display()
        else:
            print("No previous page available.")
    
    def show_current_page(self):
        # Show the current page if there's one
        if self.current_index != -1:
            print(self.pages[self.current_index].FrontPage)
        else:
            print("No page is currently displayed.")

      
class FoodPage(Restaurant):
    def display(self):
        print("pizza, $20")

class DrinkPage(Restaurant):
    def display(self):
        print("sprite, $5")

class SpecialOrderPage(Restaurant):
    def display(self):
        print("pork bread, $20")

class TotalOrderPage(Restaurant):
    def display(self):
        print("$100")



def main():
    

'''
food_menu = FoodPage("Food menu")
drink_menu = DrinkPage ("drink menu")
Special_page = SpecialOrderPage("special menu")
total_sum = TotalOrderPage("")

# Create a PageManager to handle page navigation
manager = PageManager()

# Add pages to the manager
manager.add_page(food_menu)
manager.add_page(drink_menu)
manager.add_page(Special_page)
manager.add_page(total_sum)

# Navigate through the pages using next and previous
manager.switch_page(0)  # Switch to Food Menu page
manager.next_page()  # Next page -> Drinks Menu
manager.next_page()  # Next page -> Today's Specials
manager.previous_page()  # Previous page -> Drinks Menu
manager.next_page()  # Next page -> Order Summary
manager.previous_page()  # Previous page -> Today's Specials
manager.show_current_page()  # Show the current page
myRestaurant = Restaurant("Welcome to my restaurant example")
'''
