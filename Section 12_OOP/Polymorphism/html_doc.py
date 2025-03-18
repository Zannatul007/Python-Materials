class Tag(object):
    def __init__(self, tag_name, content):
        self.start_tag = "<{}>".format(tag_name)
        self.end_tag = "</{}>".format(tag_name)
        self.content = content

    def __str__(self):
        return "{0.start_tag}{0.content}{0.end_tag}".format(self)

    def display(self):
        print(self)


class Head(Tag):
    def __init__(self):
        super().__init__("head", "")


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

    def display(self):
        for tag in self.body_tag:
            self.content += str(tag)
        super().display()


class HtmlDoc(object):
    def __init__(self):
        self._head = Head()  # Head is part of HtmlDoc (Composition)
        self._doc = DocType()  # DocType is part of HtmlDoc (Composition)
        self._body = Body()  # Body is part of HtmlDoc (Composition)

    def add_tag(self, name, contents):
        self._body.add_tag(name, contents)

    def display(self):
        print(self._doc)
        print("<html>")
        print(self._head)
        print(self._body.display())
        print("</html>")


if "__main__" == __name__:
    p1 = Body()
    p1.add_tag("h1", "My name is zannatul")
    p1.add_tag("p", "My name is zannatul")
    p1.display()

    html_file = HtmlDoc()
    html_file.add_tag("h1", "Main Title")
    html_file.add_tag("h2", "Sub Heading")
    html_file.add_tag("p", "Hello world! Welcome to the making of html doc :/")
