single_match = {'AO':'ɔ', 	
                    'AA':'ɑ', 	
                    'IY':'i',	
                    'UW':'u', 	
                    'EH':'ɛ', 	
                    'IH':'ɪ', 	
                    'UH':'ʊ', 	
                    'AH':'ʌ',	 
                    'AX':'ə', 
                    'AE':'æ',
                    'EY':'eɪ', 	
                    'AY':'aɪ', 	
                    'OW':'oʊ', 	
                    'AW':'aʊ', 	
                    'OY':'ɔɪ', 	
                    'ER':'ɝ', 	
                    'AXR':'ɚ',  
                    'P':'p', 	
                    'B':'b', 	
                    'T':'t', 	
                    'D':'d', 	
                    'K':'k', 	
                    'G':'ɡ', 	
                    'F':'f', 	
                    'V':'v', 	
                    'TH':'θ', 	
                    'DH':'ð', 	
                    'S':'s', 	
                    'Z':'z', 	
                    'SH':'ʃ', 	
                    'ZH':'ʒ', 	
                    'HH':'h', 	
                    'M':'m', 	
                    'EM':'m̩', 	
                    'N':'n', 	
                    'EN':'n̩', 	
                    'NG':'ŋ', 	
                    'ENG':'ŋ̍', 	
                    'L':'ɫ', 	
                    'EL':'ɫ̩', 	
                    'R':'r', 	
                    'DX':'ɾ', 	
                    'NX':'ɾ̃', 	
                    'Y':'j', 	
                    'W':'w', 	
                    'Q':'ʔ'}	
r_colored = {'EH':'ɛr', 	
             'UH':'ʊr', 	
             'AO':'ɔr', 	
             'AA':'ɑr', 	
             'IH':'ɪr',
             'IY':'ɪr',	
             'AW':'aʊr'}

def arpabet_to_ipa(arpabet_list):
    """ Converts a list of ARPABET phoemes into a list of IPA phoemes. Does not handle syllabe stresses """
    arpabet_list = [phoeme.rstrip('012') for phoeme in arpabet_list] #No stresses till I get how they work in IPA 
    IPA_list = []
    for  index  in  range(len(arpabet_list)):
        phoeme = arpabet_list[index]
        if phoeme in r_colored and index < len(arpabet_list)-1 and arpabet_list[index + 1] == 'R':
            IPA_list.append(r_colored[phoeme]) 
        elif phoeme in single_match:
            IPA_list.append(single_match[phoeme])
        #else: invalid ARPABET phoeme 
    return IPA_list


"""
# Because I don't know how to write test cases 
test_strings = [
'P EY1 JH IY0',
'P AE2 JH EH1 Z IY0',
'P AE2 JH AH0 N EY1 SH AH0 N',
'P EY1 JH IH0 NG',
'P AE1 G L IY0 AH0',
'P AE2 G L IY0 AA1 R OW0',
'P AE2 G L IY0 ER0 UW1 L OW0',
'P AE2 G L IY0 UW1 K AH0',
'P AE2 G L IY0 UW1 K AH0 Z',
'P AE1 G N IY0',
'P  AA0 G N OW1 T AH0',
'P AH0 G OW1 D AH0',
'P AH0 G OW1 D AH0 Z',
'P AH0 G OW1 D AH0 Z',
'P AA2 G OW0 P AA1 G OW0',
'P AH0 G Y UH1 R IY0 AH0 N'
] 
for test_string in test_strings:
    print(''.join(arpabet_to_ipa(test_string.split())))
        
"""
