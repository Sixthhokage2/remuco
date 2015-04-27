"""Miscellaneous tests for stuff used in the generator scripts."""

import unittest
import re

class Test(unittest.TestCase):

    def test_regex_ww(self):
        """Test wiki word detection pattern and replacement."""

        WW = ("SymbianJaMe ", "SymbianJ2me", "WikiWord", "Wiki2Word",
              "MicroEmulator-2.0", "Nokia5220XpressMusic", "Nokia7210Supernova",
              "NokiaE50-2", "NokiaN82", "NokiaE61i-1", "NokiaN85-3",
              "NokiaN95_8GB", "BaBaX2")
        
        NW = ("Normal", "N", "SymbianJ2ME", "SymbianJME", "SymbianJaME",
              "Symbian2me", "Nokia5330c-2", "Nokia5300", "Nokia5500d",
              "NokiaNN82", "BooBooA", "aBooBoo", 'BooBoo"', "SymBianJ2ME")
        
        re_ww_patt = r'(?<![a-z0-9])((?:[A-Z][a-z0-9]+){2,})(?![A-Za-z0-9"])'
        re_ww_repl = r'!\1'

        passed = True
        
        for word in WW:
            repl = re.sub(re_ww_patt, re_ww_repl, word, re.MULTILINE)
            #print ("%s -> %s" % (word, repl))
            if repl != "!%s" % word:
                print ("-> false neg: %s" % word)
                passed = False
                
        for word in NW:
            repl = re.sub(re_ww_patt, re_ww_repl, word, re.MULTILINE)
            #print ("%s -> %s" % (word, repl))
            if repl != "%s" % word:
                print ("-> false pos: %s (%s)" % (word, repl))
                passed = False
        
        assert passed        

if __name__ == "__main__":
    unittest.main()