import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Winter is coming")
        self.assertEqual(node.to_html(), "<p>Winter is coming</p>")
        
    def test_leaf_to_html_rtxt(self):
        node = LeafNode(None, "Hear me roar")
        self.assertEqual(node.to_html(), "Hear me roar")
    
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "King of the Andals", {"href": "https://gotfandom/salutation", "target": "_blank"})
        self.assertEqual(node.to_html(), '<a href="https://gotfandom/salutation" target="_blank">King of the Andals</a>')
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_multiple_children_and_grandchildren(self):
        # great grandchildren
        ggrandchild_node1 = LeafNode(None, "house lannister ")
        ggrandchild_node2 = LeafNode("b", "married to house barathoen")
        ggrandchild_node3 = LeafNode(None, "house lannister ")
        ggrandchild_node4 = LeafNode("b", "married to house stark")
    
        # grandchildren
        grandchild_node1 = LeafNode(None, "Jamie - ")
        grandchild_node2 = LeafNode("span", "house lannister")
        grandchild_node3 = LeafNode(None, "Cersei - ")
        grandchild_node4 = ParentNode("span", [ggrandchild_node1, ggrandchild_node2])
        grandchild_node5 = LeafNode(None, "Tyrion - ")
        grandchild_node6 = ParentNode("span", [ggrandchild_node3, ggrandchild_node4])
        
        # children
        child_node1 = ParentNode("li", [grandchild_node1, grandchild_node2])
        child_node2 = ParentNode("li", [grandchild_node3, grandchild_node4])
        child_node3 = ParentNode("li", [grandchild_node5, grandchild_node6])
        
        # parent
        parent_node = ParentNode("ul", [child_node1, child_node2, child_node3])
        self.assertEqual(
            parent_node.to_html(),
            "<ul><li>Jamie - <span>house lannister</span></li><li>Cersei - <span>house lannister <b>married to house barathoen</b></span></li><li>Tyrion - <span>house lannister <b>married to house stark</b></span></li></ul>"
        )
    
    def test_to_html_with_no_children(self):
        parent_node = ParentNode("p", None)
        self.assertRaises(ValueError, parent_node.to_html)


if __name__ == "__main__":
    unittest.main()
