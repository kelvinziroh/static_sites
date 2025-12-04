import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        node = HTMLNode(
            'a', 
            'Game of Thrones', 
            None, 
            {"href": "https://gotfandom.com", "target": "_blank"}
        )
        html_props = node.props_to_html()
        self.assertEqual(html_props, ' href="https://gotfandom.com" target="_blank"')
    
    def test_no_props(self):
        node = HTMLNode('p', 'Winter is coming', None, None)
        html_props = node.props_to_html()
        self.assertEqual(html_props, "")
    
    def test_repr(self):
        node = HTMLNode(
            'a', 
            'You know nothing Jon Snow', 
            None, 
            {"href": "https://gotfandom-characters-igrid.com"}
        )
        self.assertEqual(
            repr(node), 
            "HTMLNode(tag: a, value: You know nothing Jon Snow, children: None, props: {'href': 'https://gotfandom-characters-igrid.com'})"
        )


if __name__ == "__main__":
    unittest.main()