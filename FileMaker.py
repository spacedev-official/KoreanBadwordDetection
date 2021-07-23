Base_layer = {'ㄱ':100,'ㄲ':101,'ㅋ':102,'ㄴ':110,'ㄹ':120,'ㄷ':130,'ㄸ':131,'ㅌ':132,'ㅂ':140,'ㅃ':141,'ㅍ':142,'ㅅ':150,'ㅆ':151,'ㅎ':160,'ㅈ':170,
              'ㅉ':171,'ㅊ':172,'ㅇ':180,'ㅁ':190,'ㅡ':300,'ㅣ':300,'ㅏ':301,'ㅗ':301,'ㅜ':302,'ㅓ':302,'ㅑ':303,'ㅛ':303,'ㅕ':304,'ㅠ':304,'ㅐ':300.5,
                          'ㅒ':301.5,'ㅔ':301,'ㅖ':302,'ㅘ':301,'ㅙ':300.75,'ㅚ':300.5,'ㅝ':302,'ㅞ':301.5,'ㅟ':301,'ㅢ':300}
Seem_layer = {'/':300,'|':300,'1':300,'r':301,'^':150,'•':180,'○':180,'●':180,'0':180,'O':180,'o':180,'@':183,'°':180,'¤':180,'□':190,'■':190,
              '◇':180,'H':300.5,'F':303,'l':300,'*':182,'n':151}
KeyBorad_layer = {'q': 140, 'Q': 141, 'w': 170, 'W': 171, 'e': 130, 'E': 131, 'r': 100, 'R': 101, 't': 150, 'T': 151, 'y': 303, 'Y': 303, 'u': 304,
                                 'U': 304, 'i': 303, 'I': 303, 'o': 300.5, 'O': 301.5, 'p': 301, 'P': 302, 'a': 190, 'A': 190, 's': 110, 'S': 110, 'd': 180, 
                                 'D': 180, 'f': 120, 'F': 120, 'g': 160, 'G': 160, 'h': 301, 'H': 301, 'j': 302, 'J': 302, 'k': 301, 'K': 301, 'l': 300, 'L': 300,
                                 'z': 102, 'Z': 102, 'x': 132, 'X': 132, 'c': 172, 'C': 172, 'v': 142, 'V': 142, 'b': 304, 'B': 304, 'n': 302, 'N': 302, 'm': 300,
                                 'M': 300}
Pro_layer = {'a': 301, 'A': 301, 'o': 301, 'O': 301, 'u': 302, 'U': 302, 'i': 300, 'I': 300, 'e': 301, 'E': 301, 'g': 100, 'G': 100, 'k': 102, 'K': 102, 'd': 130,
             'D': 130, 't': 132, 'T': 132, 'b': 140, 'B': 140, 'p': 142, 'P': 142, 'j': 170, 'J': 170, 's': 150, 'S': 150, 'h': 160, 'H': 160, 'n': 110, 'N': 110,
             'm': 190, 'M': 190, 'r': 120, 'R': 120, 'l': 120, 'L': 120}

import pickle

with open('WDLD.txt', 'wb') as file:
        pickle.dump(Base_layer, file)
        pickle.dump(Seem_layer, file)
        pickle.dump(KeyBorad_layer, file)
        pickle.dump(Pro_layer, file)
