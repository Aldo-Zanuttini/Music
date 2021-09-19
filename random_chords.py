"""
Generate a number of random chords: basic triads (complexity==0), 
seventh chords (complexity==1) or sixth, seventh and upper extension chords 
(complexity==2).
"""
import random as rd
def chords(number_of_chords,complexity=0):
    roots=["A ","A# ","B ","C ","C# ","D ","D# ","E ","F ","F# ","G ","G# "];
    third_qualities=["","m"];
    sixth_qualities=["6","6","b6"];
    seventh_qualities=["maj7","maj7","maj7","7","7","7","bb7"];
    ninth_qualities=["9","9","9","b9","#9"];
    eleventh_qualities=["11","#11","b11"];
    thirteenth_qualities=["13","b13","#13"];
    placeholder_list_1=[];
    placeholder_list_2=[];
    placeholder_list_3=[];
    placeholder_list_4=[];
    placeholder_list_5=[];
    placeholder_list_6=[];
    placeholder_list_7=[];
    placeholder_list_8=[];
    chords=[];
    for i in range(number_of_chords):
        placeholder_list_1.append(roots[rd.randint(0,11)]);
        placeholder_list_2.append(third_qualities[rd.randint(0,1)]);
        placeholder_list_4.append(seventh_qualities[rd.randint(0,6)]);
        if complexity==0:
            fifth_qualities=["halfdim","aug","","","","",""];
            placeholder_list_3.append(fifth_qualities[rd.randint(0,4)]);
            chord=placeholder_list_1[i]+placeholder_list_2[i]+placeholder_list_3[i];
            chords.append(chord)
        elif complexity==1:
            fifth_qualities=["b5","#5","","","","",""];
            placeholder_list_3.append(fifth_qualities[rd.randint(0,4)]);
            chord=placeholder_list_1[i]+placeholder_list_2[i]+placeholder_list_4[i]+placeholder_list_3[i];
            chords.append(chord)
        elif complexity==2:
            placeholder_list_5.append(sixth_qualities[rd.randint(0,2)]);
            placeholder_list_6.append(ninth_qualities[rd.randint(0,5)]);
            placeholder_list_7.append(eleventh_qualities[rd.randint(0,2)])
            placeholder_list_8.append(thirteenth_qualities[rd.randint(0,2)])
    return chords