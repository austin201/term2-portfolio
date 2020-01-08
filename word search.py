
score = 0
words = ["FLOAT",
         "INTEGER",
         "IMPORT",
         "BREAK",
         "LIST",
         "TUPLE",
         "STRING",
         "VARIABLE",
         "INPUT",
         "LOOP",
         "PRINT",
         "SYNTAXERROR",
         "LOGICALERROR",
         "ARRAY",
         "TRUE",
         "FALSE",
         "CONCATENATE",
         "IFSTATEMENT",
         "RANDOM",
         "CONTINUESTATEMENT"]


questions = ["What are is it called when you have a decimal in your integer?",
             "What are positive or negative whole numbers?",
             "How do you bring in other modules?",
             "How do you exit a loop?",
             "What has square brakets around it([])?",
             "What has parenthesis around them(())?",
             "What is inside double quotes?",
             "What gets asigned a value?",
             "How do you get the users answer?",
             "What is while True?",
             "How do you display something onto the screen?",
             "An error that breaks the program befor it runs?",
             "What results in incorrect or unexpected behavior?",
             "An _____ is a data structure, which can store a fixed-size collection of elements.",
             "What is ____ or false.",
             "That was a _____ statement. Hint(What is the oposite of true)",
             "To ___________ means to merge two things together.",
             "An __ _________ is a programming conditional statement that, if proved true, performs a function or displays information.",
             "What is a module that can be imported?",
             "The ________ _________ in python returns the control to the beginning of the while loop."]



PUZZLE = "RQRTMZFPSAIRWEPABJMNVNSTJKOAKHHMRRMYATXOLEDKAWIGGYVURVYFAIGLPALTOEXRESLAFXCBQBRYNINWENIZFLPFOFZYHXMCTNEMETATSEUNITNOCRAGYRMCLGVAXKLCITNYEQTZZRRIKLCZZGGXGPGBAANKNMUNUCRERQYFTXPLXKQHICCWPMQRYZAIXCCEAASTFFNCKNTXIOUWZTYPHAPTMFOFZURCAOTTJNGATXOKIJTHZKALUHIUECCEQRYJOHUPVYANROZLFYDGRVIQGBQLYILMMIYTYIYSOUGCBTUPLEUFYMOIPSUJLSOFHJAKKEEFHDRYIRIFSTATEMENTQOKAIQXVKHQRYTLEVVZLUUCXLNAIBGMGJAQPZGQUJTOSTRAHQAQNWLVKOYVHLRMERLTSSTBLOFCEDMMOLGDNAWRIKSPBWIQXWMGGPCADQHUDNXRMUNKYPOALCEXBDVWMYMDOONAPIQJKEDTYVUHFTBPBCWBFAYNORAAFMKBRCABJWEMVUZRHIAZRNLLMBUQWICKYKMUMXWIXKYHTTHLTMYLNRMUMMPHRFPZWCXGMGNIRTSBWEALQZRCCJJLWWRMEVDBYSMQVJRSUDQDPTZVSUVUP"

def display_puzzle(PUZZLE):
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"
    F = "F"
    G = "G"
    H = "H"
    I = "I"
    J = "J"
    K = "K"
    L = "L"
    M = "M"
    N = "N"
    O = "O"
    P = "P"
    Q = "Q"
    R = "R"
    S = "S"
    T = "T"
    U = "U"
    V = "V"
    W = "W"
    X = "X"
    Y = "Y"
    Z = "Z"
    print(str.format("""
    0 1 2 3 4 5 6 7 8 9 101112131415161718192021222324
  0 R Q R T M Z F P S A I R W {4} P A B J M N V N S T J 
 25 K O A K H H M R R M Y A {19} X O L E D K A W I G G Y 
 50 V U R V Y F A I G L P {0} L T O E X R {4} {18} {11} {0} {5} X C 
 75 B Q B R Y N I N W E {13} I Z F L P F O F Z Y H X M C 
100 {19} {13} {4} {12} {4} {19} {0} {19} {18} {4} {20} {13} {8} {19} {13} {14} {2} R {0} G Y R M C L 
125 G V A X K L C {8} {19} N Y E Q T Z Z R {17} I K L C Z Z G 
150 G X G P G B A {0} {13} K N M U N U C {17} E R Q Y F {19} X P 
175 L X K Q H I {2} C W {15} M Q R Y Z {0} I X C C E A {0} S T 
200 F F N C {10} {13} T X I O {20} W Z T {24} P H A P T M F {14} F Z 
225 U R C {0} {14} T T J N G A {19} X O K I J T H Z K A {11} U H 
250 I U {4} {2} C E Q R Y J O H U P V Y A N R O Z L {5} Y D 
275 G {17} V I Q G B Q L Y I L M M I Y T Y I Y S O U G C 
300 {1} T U P L E U F Y M O I P S U J L S O F H J A K K 
325 E E F H D R Y I R {8} {5} {18} {19} {0} {19} {4} {12} {4} {13} {19} Q O K A I 
350 Q X V K H Q R Y T L E V V Z L U U C X L N A I B G 
375 M G J A Q P Z G Q U J T O S T R A H Q A Q N W L V 
400 K O Y V H L R M E R L T S S T B L O F C E D M M O 
425 L G D N A W R {8} K S P B W I Q X W M G G P C A D Q 
450 H U D N X R {12} U N K Y P O A L C E X B D V W M Y M 
475 D O O N A {15} I Q J K E D T Y V U H F T B P B C W B 
500 F A Y N {14} R A A F M K B R C A B J W E M V U Z R H 
525 I A Z {17} N L L M B U Q W I C K Y K M U M X W I X K 
550 Y H {19} T H L T M Y L N R M U M M P H R F P Z W C X 
575 G M G N I R T S B W E A L Q Z R C C J J L W W R M 
600 E V D B Y S M Q V J R S U D Q D P T Z V S U V U P""", A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z))

##0 A,1 B,2 C,3 D,4 E,5 F,6 G,7 H,8 I,9 J,10 K,
##11 L,12 M,13 N,14 O,15 P,16 Q,17 R,18 S,19 T,
##20 U,21 V,22 W,23 X,24 Y,25 Z
selected = []
def question_answer(words,questions,selected):
    import random
    while True:
        index = random.randint(0,len(questions)-1)
        while index not in selected:
            word = words[index]
            question = questions[index]
            selected.append(index)
            return word,question

def create_word(PUZZLE):
    num=[]
    coordinate= ""
    find = input("please input your coordinates for the word your looking for\nmake sure you have a comma inbetween coordinates\n")
    for i in find:
        if i != ",":
            coordinate= coordinate + i
        else:
            if coordinate.isdigit():
                num.append(int(coordinate))
                coordinate= ""
    #print(coordinate)
    num.append(int(coordinate))
    
    new_word = ""
    while num:
        x= num.pop(0)
##        y= num.pop(0)
        #add [y] to puzzle when if in a 2d form.
        new_word = new_word + PUZZLE[x]
    #print(word)
    return new_word

display_puzzle(PUZZLE)
##for i in range(len(questions)):
##    question_answer(words,questions,selected)
for i in range(len(questions)):
    word, question = question_answer(words,questions,selected)
    print(question)
    builtWord=create_word(PUZZLE)
    print(builtWord)
    if builtWord == word:
        print("CORRECT")
        score +=1
    else:
        print("INCORRECT")

print("Your score was:",score)
