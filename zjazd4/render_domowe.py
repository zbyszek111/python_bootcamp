class Document:
   def __init__(self):
       self.container = []

   def add_element(self, element):
       self.container.append(element)

   def render(self):
       output = ""
       for el in self.container:
           output += el.render()+"\n"
       return output

class Element:
   def __init__(self, text):
       self.text = text

   def render(self):
       return self.text


class LinkElement(Element):
   def __init__(self, text, url):
       self.url = url
       super().__init__(text)

   def render(self):
       return f"({self.text})[{self.url}]"



class HeaderElement(Element):

   def __init__(self, text, level=1):
       self.level = level
       super().__init__(text)

   def render(self):
       if self.level == 1:
           output = self.text
           output += "\n"
           output += "=" * len(self.text)
       else:
           output = "#" * self.level + " " + self.text
       return output


def test_document():
   doc = Document()
   assert doc.container == []
   doc.add_element("TEXT")
   assert doc.container == ["TEXT"]


def test_document_render():
   document = Document()
   document.add_element(HeaderElement('Header'))
   document.add_element(LinkElement('ABC', 'http://abc.com'))
   document.add_element(Element('Simple'))
   expected = """Header
======
(ABC)[http://abc.com]
Simple
"""
   assert document.render() == expected


def test_element():
   element = Element("Ala ma kota")
   assert element.text == "Ala ma kota"
   assert element.render() == "Ala ma kota"


def test_header_element():
   element = HeaderElement("Ala ma kota")
   assert element.text == "Ala ma kota"
   assert element.render() == "Ala ma kota\n==========="
   element = HeaderElement("Ala ma kota", 3)
   assert element.render() == "### Ala ma kota"


def test_link_element():
   element = LinkElement("ABC", "http://abc.pl")
   assert element.text == "ABC"
   assert element.url == "http://abc.pl"
   assert element.render() == "(ABC)[http://abc.pl]"