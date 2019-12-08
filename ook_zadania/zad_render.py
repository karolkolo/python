# Zaimplementuj klasy odpowiedzialne za tworzenie dokumentów w składni MarkDown.
# Stwórz klasę bazową Element zawierającą podstawową implementację metody render() oraz kilka jej klas pochodnych.
# Stwórz klasę Document umożliwiającą wyrenderowanie dodanych elementów.
# Przykład użycia:
# >>> document = Document()
# >>> document.add_element(HeaderElement('Header'))
# >>> document.add_element(LinkElement('ABC', 'abc.com'))
# >>> document.add_element(Element('Simple'))
# >>> document.render()
# Header
# ======
# (ABC)[http://abc.com]
# Simple


class Element:
    def __init__(self, content: str):
        self._content = content
    def __str__(self):
        return f'{self._content}'

class LinkElement(Element):
    def __init__(self,content,url):
        super().__init__(content)
        self._url = url
    def __str__(self):
        return f'({self._content})[http://{self._url}]'


class HeaderElement(Element):
    def __init__(self,content):
        super().__init__(content)

    def __str__(self):
        return f'{self._content}\n======'
class Document:
    def __init__(self):
        self._elements = []

    def add_element(self,element):
        self.element = element
        self._elements.append(self.element)
    def __str__(self):
        return f'{self._elements}'
    def render(self):
        for el in self._elements:
            print (el)
document = Document()
document.add_element(HeaderElement('Header'))
document.add_element(LinkElement('ABC', 'abc.com'))
document.add_element(Element('Simple'))
document.render()
