class Tag(object):
    def __init__(self, tag_name, content):
        self.start_tag = "<{}>".format(tag_name)
        self.end_tag = "</{}>".format(tag_name)
        self.content = content

    def __str__(self):
        return "{0.start_tag}{0.content}{0.end_tag}".format(self)

    def display(self, file=None):
        print(self, file=file)


class Head(Tag):
    def __init__(self, title=None):
        super().__init__("head", "")
        if title:
            self.title = Tag("title", title)
            self.content = str(self.title)


class DocType(Tag):
    def __init__(self):
        super().__init__("!DOCTYPE html", "")
        self.end_tag = ""


class Body(Tag):
    def __init__(self):
        super().__init__("body", "")
        self.body_tag = []

    def add_tag(self, name, contents):
        new_tag = Tag(name, contents)
        self.body_tag.append(new_tag)

    def display(self, file=None):
        for tag in self.body_tag:
            self.content += str(tag)
        super().display(file=file)


class HtmlDoc(object):
    def __init__(self, title=None):
        self._head = Head(title)  # Head is part of HtmlDoc (Composition)
        self._doc = DocType()  # DocType is part of HtmlDoc (Composition)
        self._body = Body()  # Body is part of HtmlDoc (Composition)

    def add_tag(self, name, contents):
        self._body.add_tag(name, contents)

    def display(self, file=None):
        print(self._doc)
        print("<html>")
        print(self._head.display(file=file))
        print(self._body.display(file=file))
        print("</html>")


if "__main__" == __name__:
    # p1 = Body()
    # p1.add_tag("h1", "My name is zannatul")
    # p1.add_tag("p", "My name is zannatul")
    # p1.display()

    html_file = HtmlDoc("This is shit")
    html_file.add_tag("title", "My first website")
    html_file.add_tag("h1", "Main Title")
    html_file.add_tag("h2", "Sub Heading")
    html_file.add_tag("p", "Hello world! Welcome to the making of html doc :/")
    with open("./Section 12_OOP/Polymorphism/test.html", "w") as test_doc:
        html_file.display(file=test_doc)
