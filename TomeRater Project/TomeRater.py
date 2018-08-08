class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.user_books = {}
        #print("A user has been created with the name of: " + str(self.name) + " and the email address: " + str(self.email)+"\n")
        # Print function above took too much space, so decided to leave it out. It is nice to have when checking if users are created correctly.


    def get_email(self):
        return self.email


    def change_email(self, address):
        self.email = address
        print("The email for user " + str(self.name) + " has been changed to: " + str(self.email))


    def __repr__(self):
        return ("User: " + str(self.name) + ", email: " + str(self.email) + ", Books read: " + str(len(self.user_books))+"\n" )

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            return True
        else:
            return False

    def read_book(self, book, rating = None):
        self.user_books[book] = rating

    def average_rating(self):
        return sum([rating for rating in self.user_books.values() if rating is not None]) / len(self.user_books)


#Defining the book object.
class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def __repr__(self):
        return ("Book: " + str(self.title) + ", ISBN: " + str(self.isbn))

    def __hash__(self):
        return hash((self.title, self.isbn))

    def __eq__(self, other):
        if self.title == other.title and self.isbn == other.isbn:
            return True
        else:
            return False

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print("The ISBN for the book: " + str(self.title) + " has been changed to: " + str(new_isbn)+"\n")

    def add_rating(self, rating=None):
        if rating is None:
            pass
        elif 0 <= rating <= 4:
            (self.ratings).append(rating)
        else:
            print("Invalid Rating")

    #Function could be simplified with the removal of variables, but I think the code is more readable with more variables.
    def get_average_rating(self):
        number_of_reviews = len(self.ratings)
        total_score = sum(self.ratings)
        average_score = total_score / number_of_reviews
        return average_score



#Subclass fiction will inherit most of Book constructor, with the added element of an author.
class Fiction(Book):
    def __init__(self, title, author, isbn):
        super(Fiction, self).__init__(title, isbn)
        self.author = author

    def __repr__(self):
        return str(self.title) + " by " + str(self.author)

    def get_author(self):
        return str(self.author)

#Creating subclass with inheritance from Book class while adding subject and level.
class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super(Non_Fiction, self).__init__(title, isbn)
        self.subject = subject
        self.level = level

    def __repr__(self):
        return str(self.title) + ", a " + str(self.level) + " manual on " + str(self.subject)

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

class TomeRater():
    def __init__(self):
        self.users = {}
        self.books = {}
        self.total_books = {}

    #Representation of the amount of users and books within the TomeRater object.
    def __repr__(self):
        return ("The Tomerater program contains " + str(len(self.users.keys())) + " users" + " and " + str(len(self.books.keys())) + " books.")


    def create_book(self, title, isbn):
        return Book(title, isbn)

    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)


    def add_book_to_user(self, book, email, rating=None):
        user = self.users.get(email, "No user with email: {email}".format(email=email))

        if user:
            user.read_book(book, rating)
            book.add_rating(rating)

        if book in self.books:
            self.books[book] += 1

        if book not in self.books:
            self.books[book] = 1


    def add_user(self, name, email, user_books=None):
        new_user = User(name, email)
        self.users[email] = new_user
        if user_books is not None:
            for book in user_books:
                self.add_book_to_user(book, email)

    def print_catalog(self):
        print("These are the books currently in the catalog:")
        for item in self.books:
            print(str(item) + "\n")

    def print_users(self):
        for user in self.users:
            print(user)

#checking if any book has a higher read count than the existing book.
    def get_most_read_book(self):
        highest_read = 0
        book_name = ""
        for book in self.books:
            if self.books[book] > highest_read:
                highest_read = self.books[book]
                book_name = book
        print("The most read book is: " + str(book_name) +". It has been read " + str(highest_read) + " times.\n" )

    #Checking if any book as a value higher than the current variable. If true, then book will be stored in the highest key variable.
    def highest_rated_book(self):
        highest_value = 0.0
        highest_key = ""
        for book in self.books.keys():
            if book.get_average_rating() > highest_value:
                highest_value = book.get_average_rating()
                highest_key = book.title
        return ("The highest rated book is: " + str(highest_key) + " with an average score of: " + str(highest_value)+"\n")

    #Checking for highest average rating, stored in variable of same name.
    def most_positive_user(self):
        highest_average_score = 0.0
        name_of_user = ""
        for item in Tome_Rater.users:
            if Tome_Rater.users[item].average_rating() > highest_average_score:
                highest_average_score = Tome_Rater.users[item].average_rating()
                name_of_user = item
        return ("The most positive user is: " + str(name_of_user) + ". His average review score is: " + str(highest_average_score)+"\n")



#End of program code: The following elements will add data to Tome_Rater as well as  test the functionality of the code.


Tome_Rater = TomeRater()


#Create some books:
book1 = Tome_Rater.create_book("Society of Mind", 12345678)
novel1 = Tome_Rater.create_novel("Alice In Wonderland", "Lewis Carroll", 12345)
novel1.set_isbn(9781536831139)
nonfiction1 = Tome_Rater.create_non_fiction("Automate the Boring Stuff", "Python", "beginner", 1929452)
nonfiction2 = Tome_Rater.create_non_fiction("Computing Machinery and Intelligence", "AI", "advanced", 11111938)
novel2 = Tome_Rater.create_novel("The Diamond Age", "Neal Stephenson", 10101010)
novel3 = Tome_Rater.create_novel("There Will Come Soft Rains", "Ray Bradbury", 10001000)

#Create users:
Tome_Rater.add_user("Alan Turing", "alan@turing.com")
Tome_Rater.add_user("David Marr", "david@computation.org")

#Add a user with three books already read:
Tome_Rater.add_user("Marvin Minsky", "marvin@mit.edu", user_books=[book1, novel1, nonfiction1])



#Add books to a user one by one, with ratings:
Tome_Rater.add_book_to_user(book1, "alan@turing.com", 1)
Tome_Rater.add_book_to_user(novel1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction2, "alan@turing.com", 4)
Tome_Rater.add_book_to_user(novel3, "alan@turing.com", 1)
Tome_Rater.add_book_to_user(novel2, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "david@computation.org", 4)



"""
print(Tome_Rater.users["marvin@mit.edu"].user_books)
Tome_Rater.print_catalog()
Tome_Rater.print_users()
print("Most positive user:")
print(Tome_Rater.most_positive_user())
print(Tome_Rater.highest_rated_book())
print("Most read book:")
print(Tome_Rater.get_most_read_book())
print(Tome_Rater.__repr__())
"""








