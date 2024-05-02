import unittest
from chain import rag_chain

class TestRAGChain(unittest.TestCase):

    def test_rag_chain(self):
        ans = rag_chain.invoke("Who are Meta's 'Directors' (i.e., members of the Board of Directors)?")

if __name__ == '__main__':
    unittest.main()