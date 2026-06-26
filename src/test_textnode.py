from platform import node
import unittest
from htmlnode import LeafNode
from textnode import TextNode, TextType



class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_str(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertEqual(node, node2)
    
    def test_repr(self):
        node = TextNode("This is a text node", TextType.CODE)
        node2 = TextNode("This is a text node", TextType.CODE)
        self.assertEqual(node, node2)
    
    def test_link(self):
        node = TextNode("This is a link", TextType.LINK, "https://www.example.com")
        node2 = TextNode("This is a link", TextType.LINK, "https://www.example.com")
        self.assertEqual(node, node2)
    
    def text_node_to_html_node(self, text_node: TextNode) -> LeafNode:
        if text_node.text_type == TextType.TEXT:
            return LeafNode("" ,text_node.text)
        elif text_node.text_type == TextType.BOLD:
            return LeafNode("b", text_node.text)
        elif text_node.text_type == TextType.ITALIC:
            return LeafNode("i", text_node.text)
        elif text_node.text_type == TextType.CODE:
            return LeafNode("code", text_node.text)
        elif text_node.text_type == TextType.LINK:
            return LeafNode("a", text_node.text, props={"href": text_node.text})
        elif text_node.text_type == TextType.IMAGE:
            return LeafNode("img", "", props={"src": text_node.text, "alt": text_node.text})
        else:
            raise ValueError(f"Unknown TextType: {text_node.text_type}")
        
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = self.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "")
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bold text node", TextType.BOLD)
        html_node = self.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold text node")

    def test_italic(self):
        node = TextNode("This is an italic text node", TextType.ITALIC)
        html_node = self.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic text node")

    def test_code(self):
        node = TextNode("This is a code text node", TextType.CODE)
        html_node = self.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code text node")



if __name__ == "__main__":
    unittest.main()