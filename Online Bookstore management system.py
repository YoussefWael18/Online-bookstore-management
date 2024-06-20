from isbnlib import is_isbn10, is_isbn13
from abc import ABC,abstractmethod
class items(ABC):
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
        self.cart=[]
    @abstractmethod
    def add_to_cart(self):
        pass
    @abstractmethod
    def view_cart(self):
        pass  
    def clear_Cart(self):
        self.cart=[]
        
class Book(items):
    def __init__(self,title,author,price):
        super().__init__(title,author,price)
        self.Number_of_pages =0
        self.ISBN =0
        self.genre = " "
        self.books = []
    
    
    def print_display(self):
        if not self.books:
            print("No books to display.")
        else:
            for i in range(0, len(self.books), 6):
                if i + 5 < len(self.books):  # Check if there are enough elements for one book
                    print(f"Name: {self.books[i]}, Author: {self.books[i+1]}, Price: {self.books[i+2]}, Pages: {self.books[i+3]}, ISBN: {self.books[i+4]}, Genre: {self.books[i+5]}")
                else:
                    print("There are no more books to display.")

 
    
    def remove_book(self, book_name):
        for i in range(0, len(self.books), 6):
            if self.books[i] == book_name:
                del self.books[i:i+6]
                print(f"{book_name} has been removed from the inventory.")
                
    
    def validate_isbn(self, isbn):
        isbn = isbn.replace("-", "")  # Remove hyphens if present
        if len(isbn) == 10:
            return is_isbn10(isbn)  # Check if it is ISBN-10
        elif len(isbn) == 13:
            return is_isbn13(isbn)  # Check if it is ISBN-13
        else:
            return False

    def available_book(self,name):
        for iterator in self.books:
            if iterator == name:
                print("Book is available")
                return True
        else:
            print("Book is not available")
            return False
                     
    
    def Add_Books(self):
            try:
                N = int(input("What is the number of books you want to insert to the Bookstore: "))
            except ValueError:
                print("Error.")
                return

            x = 0
            while x < N:
                book_name = input("Please enter the book Name that you want to add to the inventory: ")
                book_author = input("Please enter the book author: ")
                if not book_author:
                    print("Author name cannot be empty. Please re-enter all details.")
                    continue
                book_price = None
                while book_price is None:
                    try:
                        book_price = int(input("Please enter the book price: "))
                    except ValueError:
                        print("Please enter a valid price.")
                book_pages = None
                while book_pages is None:
                    try:
                        book_pages = int(input("Please enter the number of pages: "))
                    except ValueError:
                        print("Please enter a valid number of pages.")
                self.ISBN = input("Please enter the ISBN for the book: ")
                if not self.validate_isbn(self.ISBN):
                    print("Invalid ISBN. Book not added.")
                    continue
                book_genre = input("please enter the genre of the book you want add: ")
                
                # Add the book to the list only if all details are valid
                self.books.extend([book_name, book_author, book_price, book_pages, self.ISBN, book_genre])
                x += 1

    def view_book_details(self, book_name):
                for i in range(0, len(self.books), 6):
                    if self.books[i] == book_name:
                        print(f"Title: {self.books[i]}")
                        print(f"Author: {self.books[i+1]}")
                        print(f"Price: {self.books[i+2]}")
                        print(f"Pages: {self.books[i+3]}")
                        print(f"ISBN: {self.books[i+4]}")
                        print(f"Genre: {self.books[i+5]}")
    
    def update_book_details(self, book_name):
        for i in range(0, len(self.books), 6):
            if self.books[i] == book_name:
                print("Select which detail you want to update:")
                print("1. Title")
                print("2. Author")
                print("3. Price")
                print("4. Number of Pages")
                print("5. ISBN")
                print("6. Genre")
                choice = int(input("Enter your choice: "))
                if choice==1:
                    new_title = input("Enter the new author: ")
                    self.books[i] = new_title
                if choice == 2:
                    new_author = input("Enter the new author: ")
                    self.books[i + 1] = new_author
                elif choice == 3:
                    new_price = int(input("Enter the new price: "))
                    self.books[i + 2] = new_price
                elif choice == 4:
                    new_pages = int(input("Enter the new number of pages: "))
                    self.books[i + 3] = new_pages
                elif choice == 5:
                    new_isbn = input("Enter the new ISBN: ")
                    if self.validate_isbn(new_isbn):
                        self.books[i + 4] = new_isbn
                        print("ISBN validated and updated successfully.")
                    else:
                        print("Invalid ISBN. ISBN not updated.")
                elif choice == 6:
                    new_genre = input("Enter the new genre: ")
                    self.books[i + 5] = new_genre
                elif choice<1 or choice>6:
                    print("Invalid choice.")
                print("Book details updated successfully.")
        
    def search_book(self, title):
        found_books = []
        for i in range(0, len(self.books), 6):
            if self.books[i].lower() == title.lower():
                found_books.append({
                    "Title": self.books[i],
                    "Author": self.books[i+1],
                    "Price": self.books[i+2],
                    "Pages": self.books[i+3],
                    "ISBN": self.books[i+4],
                    "Genre": self.books[i+5]
                })
        return found_books    
    
    def add_to_cart(self, book_name):
            if book_name in self.cart:
                print(f"{book_name} is already in the cart.")
            else:
                self.cart.append(book_name)
                print(f"{book_name} has been added to the cart.")
    
    def view_cart(self):
        if not self.cart:
            print("there is no books in the cart")
        else:
            print("Books in cart:")
            for item in self.cart:
                print(item)  
   
    def remove_from_cart(self, book_name):
        if book_name in self.cart:
            self.cart.remove(book_name)
            print(f"{book_name} has been removed from the cart.")
        else:
            print(f"{book_name} is not in the cart.")
    
    def get_item_price(self, item_name):
        for i in range(0, len(self.books), 6):
            if self.books[i] == item_name:
                return self.books[i + 2]  # Price is at index 2
        return 0

    def checkout(self):
        total_price = 0
        for item in self.cart:
            total_price += self.get_item_price(item)
        return total_price
                           
                


class Magazines(items):
         def __init__(self,title,author,price):
            super().__init__(title,author,price)
            self.pages=0
            self.issue_number = 0
            self.publication_date =0
            self.magazines = []
           
         def Add_Magazine(self):
            try:
                N = int(input("What is the number of magazines you want to insert to the Bookstore: "))
            except ValueError:
                print("Error.")
                return

            x = 0
            while x < N:
                magazine_title = input("Please enter the magazine Title that you want to add to the inventory: ")
                magazine_publisher = input("Please enter the magazine editor: ")
                if not magazine_publisher:
                    print("Publisher name cannot be empty. Please re-enter all details.")
                    continue
                magazine_price = None
                while magazine_price is None:
                    try:
                        magazine_price = int(input("Please enter the magazine price: "))
                    except ValueError:
                        print("Please enter a valid price.")
                magazine_pages = None
                while magazine_pages is None:
                    try:
                        magazine_pages = int(input("Please enter the number of pages for the magazine: "))
                    except ValueError:
                        print("Please enter a valid number of pages.")
                magazine_issue_number = input("Please enter the issue number for the magazine: ")
                magazine_publication_date = input("Please enter the publication date for the magazine: ")
                magazine_genre = input("Please enter the genre of the magazine you want add: ")

                # Add the magazine to the list only if all details are valid
                self.magazines.extend([magazine_title, magazine_publisher, magazine_price, magazine_pages, magazine_issue_number, magazine_publication_date, magazine_genre])
                x += 1

         
         def available_magazine(self,M):
                for iterator in self.magazines:
                    if iterator == M:
                        print("magazine is available")
                        return True
                else:
                    print("Magazine is not available") 
                    return False  
        
        
         def print_display(self):
                if not self.magazines:
                    print("No magazines to be display.")
                else:
                    for i in range(0, len(self.magazines), 7):
                        if i + 5 < len(self.magazines):  # Check if there are enough elements for one magazine
                            print(f"Name: {self.magazines[i]}, Author: {self.magazines[i+1]}, Price: {self.magazines[i+2]}, Pages: {self.magazines[i+3]} , Issue number: {self.magazines[i+4]},  Publication date:{self.magazines[i+5]},genre:{self.magazines[i+6]}")
                        else:
                            print("There are no more magazines to display.")
                            
         def update_magazine_details(self, magazine_title):
                for i in range(0, len(self.magazines), 6):
                    if self.magazines[i] == magazine_title:
                        print("Select which detail you want to update:")
                        print("1. Title")
                        print("2. Editor")
                        print("3. Price")
                        print("4. Number of Pages")
                        print("5. Issue Number")
                        print("6. Publication Date")
                        choice = int(input("Enter your choice: "))
                        if choice==1:
                            new_title = input("Enter the new title: ")
                            self.magazines[i] = new_title
                        if choice == 2:
                            new_editor = input("Enter the new editor: ")
                            self.magazines[i + 1] = new_editor
                        elif choice == 3:
                            new_price = int(input("Enter the new price: "))
                            self.magazines[i + 2] = new_price
                        elif choice == 4:
                            new_pages = int(input("Enter the new number of pages: "))
                            self.magazines[i + 3] = new_pages
                        elif choice == 5:
                            new_issue_number = input("Enter the new issue number: ")
                            self.magazines[i + 4] = new_issue_number
                        elif choice == 6:
                            new_publication_date = input("Enter the new publication date: ")
                            self.magazines[i + 5] = new_publication_date
                        elif choice<1 or choice>6:
                            print("Invalid choice.")
                        print("Magazine details updated successfully.")
                                               

         def remove_magazine(self, magazine_title):
                        for i in range(0, len(self.magazines), 6):
                            if self.magazines[i] == magazine_title:
                                del self.magazines[i:i+6]
                                print(f"{magazine_title} has been removed from the inventory.")
                                return
                        print(f"{magazine_title} is not found in the inventory.")                    
         def view_magazine_details(self, magazine_title):
                        for i in range(0, len(self.magazines), 6):
                            if self.magazines[i] == magazine_title:
                                print(f"Title: {self.magazines[i]}")
                                print(f"Editor: {self.magazines[i+1]}")
                                print(f"Price: {self.magazines[i+2]}")
                                print(f"Pages: {self.magazines[i+3]}")
                                print(f"Issue Number: {self.magazines[i+4]}")
                                print(f"Publication Date: {self.magazines[i+5]}")
                                return
                        print(f"{magazine_title} is not found in the inventory.")
         def search_magazine(self, title):
                    found_magazines = []
                    for i in range(0, len(self.magazines), 6):
                        if self.magazines[i].lower() == title.lower():
                            found_magazines.append({
                                "Title": self.magazines[i],
                                "Editor": self.magazines[i+1],
                                "Price": self.magazines[i+2],
                                "Pages": self.magazines[i+3],
                                "Issue Number": self.magazines[i+4],
                                "Publication Date": self.magazines[i+5]
                            })
                    return found_magazines
         def get_item_price(self, item_name):
                    for i in range(0, len(self.magazines), 6):
                        if self.magazines[i] == item_name:
                            return self.magazines[i + 2]  # Price is at index 2
                    return 0
         
         def add_to_cart(self, magazine_title):
            if magazine_title in self.cart:
                print(f"{magazine_title} is already in the cart.")
            else:
                self.cart.append(magazine_title)
                print(f"{magazine_title} has been added to the cart.")
         def view_cart(self):
            if not self.cart:
                print("there is no magazine in the cart")
            else:
                print("Magazines in cart:")
                for item in self.cart:
                    print(item)
         def remove_from_cart(self, magazine_name):
            if magazine_name in self.cart:
                self.cart.remove(magazine_name)
                print(f"{magazine_name} has been removed from the cart.")
            else:
                print(f"{magazine_name} is not in the cart.") 
         def checkout(self):
            total_price = 0
            for item in self.cart:
                total_price += self.get_item_price(item)
            return total_price                   
class DVD(items):
    def __init__(self, title, author, price):
        super().__init__(title, author, price)
        self.duration = " "
        self.genre = " "
        self.DVDs = []

    def Add_DVD(self):
        try:
            N = int(input("What is the number of DVDs you want to insert to the Bookstore: "))
        except ValueError:
            print("Error.")
            return

        x = 0
        while x < N:
            dvd_title = input("Please enter the DVD Title that you want to add to the inventory: ")
            dvd_director = input("Please enter the DVD director: ")
            if not dvd_director:
                print("Director name cannot be empty. Please re-enter all details.")
                continue
            dvd_price = None
            while dvd_price is None:
                try:
                    dvd_price = int(input("Please enter the DVD price: "))
                except ValueError:
                    print("Please enter a valid price.")
            dvd_duration = input("Please enter the duration of the DVD in minutes: ")
            dvd_genre = input("Please enter the genre of the DVD you want add: ")

            # Add the DVD to the list only if all details are valid
            self.DVDs.extend([dvd_title, dvd_director, dvd_price, dvd_duration, dvd_genre])
            x += 1

    def print_display(self):
        if not self.DVDs:
            print("No DVDs to be display.")
        else:
            for i in range(0, len(self.DVDs), 5):
                if i + 4 < len(self.DVDs):  # Check if there are enough elements for one DVD
                    print(f"Title: {self.DVDs[i]}, Director: {self.DVDs[i + 1]}, Price: {self.DVDs[i + 2]}, Duration: {self.DVDs[i + 3]}, Genre: {self.DVDs[i + 4]}")
                else:
                    print("There are no more DVDs to display.")

    def update_dvd_details(self, dvd_title):
        for i in range(0, len(self.DVDs), 5):
            if self.DVDs[i] == dvd_title:
                print("Select which detail you want to update:")
                print("1. Title")
                print("2. Director")
                print("3. Price")
                print("4. Duration")
                print("5. Genre")
                choice = int(input("Enter your choice: "))
                if choice==1:
                    new_title = input("Enter the new title: ")
                    self.DVDs[i] = new_title
                if choice == 2:
                    new_director = input("Enter the new director: ")
                    self.DVDs[i + 1] = new_director
                elif choice == 3:
                    new_price = int(input("Enter the new price: "))
                    self.DVDs[i + 2] = new_price
                elif choice == 4:
                    new_duration = input("Enter the new duration: ")
                    self.DVDs[i + 3] = new_duration
                elif choice == 5:
                    new_genre = input("Enter the new genre: ")
                    self.DVDs[i + 4] = new_genre
                else:
                    print("Invalid choice.")
                print("DVD details updated successfully.")
                return
        print(f"{dvd_title} is not found in the inventory.")

    def remove_dvd(self, dvd_title):
        for i in range(0, len(self.DVDs), 5):
            if self.DVDs[i] == dvd_title:
                del self.DVDs[i:i + 5]
                print(f"{dvd_title} has been removed from the inventory.")
                return
        print(f"{dvd_title} is not found in the inventory.")

    def view_dvd_details(self, dvd_title):
        for i in range(0, len(self.DVDs), 5):
            if self.DVDs[i] == dvd_title:
                print(f"Title: {self.DVDs[i]}")
                print(f"Director: {self.DVDs[i + 1]}")
                print(f"Price: {self.DVDs[i + 2]}")
                print(f"Duration: {self.DVDs[i + 3]}")
                print(f"Genre: {self.DVDs[i + 4]}")
                return
        print(f"{dvd_title} is not found in the inventory.")

    def search_dvd(self, title):
        found_dvds = []
        for i in range(0, len(self.DVDs), 5):
            if self.DVDs[i].lower() == title.lower():
                found_dvds.append({
                    "Title": self.DVDs[i],
                    "Director": self.DVDs[i + 1],
                    "Price": self.DVDs[i + 2],
                    "Duration": self.DVDs[i + 3],
                    "Genre": self.DVDs[i + 4]
                })
        return found_dvds
    
     
    def available_dvd(self,D):
        for iterator in self.DVDs:
            if iterator == D:
                print("DVD is available")
                return True
        else:
            print("DVD is not available") 
            return False  
    def get_item_price(self, item_name):
        for i in range(0, len(self.DVDs), 5):
            if self.DVDs[i] == item_name:
                return self.DVDs[i + 2]  # Price is at index 2
        return 0
    
    def add_to_cart(self, dvd_title):
        if dvd_title in self.cart:
            print(f"{dvd_title} is already in the cart.")
        else:
            self.cart.append(dvd_title)
            print(f"{dvd_title} has been added to the cart.") 
    def view_cart(self):
        if not self.cart:
            print("there in no DVD in the cart")
        else:
            print("DVDs in cart:")
            for item in self.cart:
                print(item)   
    def remove_from_cart(self, dvd_name):
        if dvd_name in self.cart:
            self.cart.remove(dvd_name)
            print(f"{dvd_name} has been removed from the cart.")
        else:
            print(f"{dvd_name} is not in the cart.")  
    def checkout(self):
        total_price = 0
        for item in self.cart:
            total_price += self.get_item_price(item)
        return total_price                                   


book=Book("","","")
magazine=Magazines("","","")
dvd=DVD("","","")
admin_pass="admin123"
while True:
        print("Welcome to our bookstore")        
        I=input("For Admin mode: \n enter 1 \n  for user mode: \n enter 2:\n")
        if I=="1":
            print("welcome to the Admin mode:")
            password=input("Please enter the password for admin mode:")
            if password=="admin123":
                print(" please enter to add: \n 1-Books \n 2-magazine \n 3-DVD \n 4-for items managment")
                choice = int(input("Enter your choice: "))

                if choice == 1:
                    book.Add_Books()
                elif choice == 2:
                    magazine.Add_Magazine()
                elif choice == 3:
                    dvd.Add_DVD()
                elif choice==4:
                    print("")
                elif choice>4 or choice<1:
                    print("Invalid choice.")

                #978-0061120084
                while True:
                    print("Please enter:\n1-Books management\n2-Magazine management\n3-DVDs management\n4-Exit")
                    choice1 = int(input("Enter your choice: "))
                    
                    if choice1 == 1:
                        # Book management
                        while True:
                            print("Please enter:\n1-Display Books on display\n2-Update books\n3-Search for a book by name\n4-Remove a book\n5-Display book details\n6-add book\n7-Exit\n")
                            choice = int(input("Enter your choice: "))
                            if choice == 1:
                                # Display Books on display
                                book.print_display()
                            elif choice == 2:
                                # Update Books
                                new = input("please enter the name of the book you want to update:")
                                if book.available_book(new):
                                    book.update_book_details(new)
                            elif choice == 3:
                                # Search for a book by name
                                book_name = input("Enter the name of the book you want to search: ")
                                if book.available_book(book_name):
                                    print(book.search_book(book_name))
                            elif choice == 4:
                                # Remove a book
                                book_name = input("Enter the name of the book you want to remove: ")
                                book.remove_book(book_name)
                            elif choice == 5:
                                # Display Book Details
                                book_name = input("Enter the name of the book you want to display details for: ")
                                book.view_book_details(book_name)
                            elif choice ==6:
                                book.Add_Books()
                            elif choice == 7:
                                # Exit from book management
                                break
                            elif choice<1 or choice>7:
                                print("Invalid choice.")
                                
                    elif choice1 == 2:
                            while True:
                                print("Please enter:\n1-Display Magazines on display\n2-Update magazines\n3-Search for a magazine by name\n4-Remove a magazine\n5-Display magazine details\n6-add magazine\n7-Exit")
                                choice = int(input("Enter your choice: "))
                                
                                if choice == 1:
                                    # Display Magazines on display
                                    magazine.print_display()
                                elif choice == 2:
                                    # Update Magazines
                                    magazine_title = input("Enter the name of the magazine you want to update: ")
                                    if magazine.available_magazine(magazine_title):
                                        magazine.update_magazine_details(magazine_title)
                                elif choice == 3:
                                    # Search for a magazine by name
                                    magazine_title = input("Enter the name of the magazine you want to search: ")
                                    if magazine.available_magazine(magazine_title):
                                        print(magazine.search_magazine(magazine_title))
                                elif choice == 4:
                                    # Remove a magazine
                                    magazine_title = input("Enter the name of the magazine you want to remove: ")
                                    magazine.remove_magazine(magazine_title)
                                elif choice == 5:
                                    # Display Magazine Details
                                    magazine_title = input("Enter the name of the magazine you want to display details for: ")
                                    magazine.view_magazine_details(magazine_title)
                                elif choice==6:
                                    magazine.Add_Magazine()
                                elif choice == 7:
                                    # Exit from magazine management
                                    break
                                elif choice<1 or choice>7:
                                    print("Invalid choice.")


                    elif choice1 == 3:
                        while True:
                            print("Please enter:\n1-Display DVD on display\n2-Update DVD\n3-Search for a DVD by name\n4-Remove a DVD\n5-Display DVD details\n6-Add DVD\n7-Exit")
                            choice = int(input("Enter your choice: "))

                            if choice == 1:
                                # Display DVDs on display
                                dvd.print_display()
                            elif choice == 2:
                                # Update DVD
                                dvd_title = input("Enter the name of the DVD you want to update: ")
                                dvd.update_dvd_details(dvd_title)
                            elif choice == 3:
                                # Search for a DVD by name
                                dvd_title = input("Enter the name of the DVD you want to search: ")
                                if dvd.available_dvd(dvd_title):
                                    print(dvd.search_dvd(dvd_title))
                            elif choice == 4:
                                # Remove a DVD
                                dvd_title = input("Enter the name of the DVD you want to remove: ")
                                dvd.remove_dvd(dvd_title)
                            elif choice == 5:
                                # Display DVD details
                                dvd_title = input("Enter the name of the DVD you want to display details for: ")
                                dvd.view_dvd_details(dvd_title)
                            elif choice == 6:
                                # Add DVD
                                dvd.Add_DVD()
                            elif choice == 7:
                                # Exit
                                break
                            elif choice>7 or choice<1:
                                print("Invalid choice.")

                        
                    elif choice1 == 4:
                        # Exit from admin mode
                        break
                    else:
                        print("Error invalid input")
            else:
                print("invalid password")            
        elif I=="2":
             print("welcome to user mode:")
             while True:
                choice = int(input("Please enter:\n1-print items on display\n2-Add Book to Cart\n3-Add Magazine to Cart\n4-Add DVD to Cart\n5-View Cart\n6-Remove Book from Cart\n7-Remove Magazine from Cart\n8-Remove DVD from Cart\n9-checkout\n10-exit \n"))
                
                if choice==1:
                    print("Books on display:")
                    book.print_display()
                    print("magazine on display:")
                    magazine.print_display()
                    print("DVDS on display:")     
                    dvd.print_display()
                if choice == 2:
                    book_name = input("Enter the name of the book you want to add to the cart: ")
                    if book.available_book(book_name):
                        book.add_to_cart(book_name)
                elif choice == 3:
                    magazine_name = input("Enter the name of the magazine you want to add to the cart: ")
                    if magazine.available_magazine(magazine_name):
                        magazine.add_to_cart(magazine_name)
                elif choice == 4:
                    dvd_name = input("Enter the name of the DVD you want to add to the cart: ")
                    if dvd.available_dvd(dvd_name):
                        dvd.add_to_cart(dvd_name)
                elif choice == 5:
                    print("View Cart:")
                    book.view_cart()
                    magazine.view_cart()
                    dvd.view_cart()
                elif choice == 6:
                    book_name = input("Enter the name of the book you want to remove from the cart: ")
                    book.remove_from_cart(book_name)
                elif choice == 7:
                    magazine_name = input("Enter the name of the magazine you want to remove from the cart: ")
                    magazine.remove_from_cart(magazine_name)
                elif choice == 8:
                    dvd_name = input("Enter the name of the DVD you want to remove from the cart: ")
                    dvd.remove_from_cart(dvd_name)
                elif choice == 9:
                    total_price = book.checkout() + magazine.checkout() + dvd.checkout()
                    print(f"Total price : {total_price}")
                    if total_price > 1000:
                        discount = total_price * 0.1
                        total_price -= discount
                        print(f"Discount applied: 10% ({discount})")
                        print(f"Total price after discount: {total_price}")
                        confirmation = input("Do you want to checkout? (yes/no): ")
                        if confirmation.lower() == 'yes':
                            print("Thank you for shopping with us!")
                            book.cart=[]
                            magazine.cart=[]
                            dvd.cart=[]
                        else:
                            print("Your items are still in the cart.")
                    else:
                        confirmation = input("Do you want to checkout? (yes/no): ")    
                        if confirmation.lower() == 'yes':
                            print("Thank you for shopping with us!")
                            book.cart=[]
                            magazine.cart=[]
                            dvd.cart=[]
    
                        else:
                            print("Your items are still in the cart.")
                elif choice==10:
                    break               
                elif choice>10 or choice<1:
                    print("Invalid choice. Please try again.")
        else:
            print("Error please enter 1 or 2")
            
                        

                                    
                
            
    
  
                        

        
          
    
    
      
        
    
    


