import unittest
from blocks import BlockType, block_to_block_type



class test_blocks(unittest.TestCase):
    def test_block_to_block_type(self):
        self.assertEqual(block_to_block_type("# Heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("## Subheading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("### Sub-subheading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("####### Not a heading"), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("> Quote"), BlockType.QUOTE)
        self.assertEqual(block_to_block_type("> Quote\n> Quote line 2\n> Quote line 3"), BlockType.QUOTE)
        self.assertEqual(block_to_block_type("- Unordered list item"), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type("1. Ordered list item\n2. Another ordered list item\n3. Yet another ordered list item"), BlockType.ORDERED_LIST)
        self.assertEqual(block_to_block_type("```Code block```"), BlockType.CODE)
        self.assertEqual(block_to_block_type("```Code block'''"), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("Regular paragraph text."), BlockType.PARAGRAPH)







if __name__ == "__main__":
    unittest.main()