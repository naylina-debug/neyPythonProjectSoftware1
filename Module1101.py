class Publication:
    def __init__(self, name):
        self.name = name


class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        print(f"Book: {self.name}")
        print(f"  Author: {self.author}")
        print(f"  Page count: {self.page_count}")
        print()


class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        print(f"Magazine: {self.name}")
        print(f"  Chief editor: {self.chief_editor}")
        print()


if __name__ == "__main__":
    donald_duck = Magazine("Donald Duck", "Aki Hyyppä")
    compartment_no_6 = Book("Compartment No. 6", "Rosa Liksom", 192)

    donald_duck.print_information()
    compartment_no_6.print_information()