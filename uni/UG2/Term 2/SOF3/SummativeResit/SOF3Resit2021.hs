module SOF3Resit2021 where


{-
# SOF3 Assessment 2020-21

You may use any values defined in the standard `Prelude`, but you may
not import any other module.  You may use Neil Mitchell's
[Hoogλe](https://hoogle.haskell.org/) to discover useful functions in
the `Prelude`.

Where tests accompany the English description of the problem, it is
not necessarily enough for your implementation to pass the tests to be
correct.

## Question 1 [35 marks]

### Question 1(i) [1 mark]
Write a function `allSoft3` that takes a list of characters and returns `True` if every character is contained in "Software3" and `False` otherwise.

Your solution should satisfy:
-}

allTest :: Bool 
allTest = 
    allSoft3 ""          == True  &&
    allSoft3 " "         == False &&
    allSoft3 "oft3w"     == True  &&
    allSoft3 "ofT3w"     == False &&
    allSoft3 "free"      == True  &&
    allSoft3 "Software3" == True 

allSoft3 :: [Char] -> Bool 

allSoft3 = all (`elem` "Software3")

{-
### Question 1(ii) [1 mark]
Write a function `three4th` that takes a fractional type and returns three-quarters of the input value.

Your solution should satisfy:
-}
testThreeq :: Bool 
testThreeq =
    three4th 0    == 0.0 &&
    three4th 1    == 0.75 &&
    three4th 8.0  == 6.0 &&
    three4th 4.8  == 3.5999999999999996 &&
    three4th (-8) == -6.0


three4th :: Fractional a => a -> a

three4th = (* 0.75)

{-
### Question 1(iii) [1 mark]
Write a function `sqSum` that takes a list of numbers and returns the sum of the square of the numbers.  

Your solution should satisfy:
-}
testSum :: Bool 
testSum = 
     sqSum []                == 0 &&
     sqSum [1, 3, 4]         == 26 &&
     sqSum [1, 3, 4.0]       == 26.0 &&
     sqSum [1, 3, 4.2]       == 27.64 &&
     sqSum [1.0, 3.0, 4.0]   == 26.0 &&
     sqSum [1/2, 3/2, 4.0]   == 18.5 &&
     sqSum[-2, 3.0, 0.2, -1] == 14.04


sqSum :: Num ab => [ab] -> ab

sqSum = sum . map (^2)

{-
### Question 1(iv) [2 marks]

Write a function `same2other` that returns `True` when applied to a list with at 
least three elements of which the first two are the same as each other and at least 
one other element in the list apart from the second element, is also 
the same as the first element. 

Your solution should satisfy:
-}

testsame2other :: Bool
testsame2other =
    (same2other ""                        == False) &&
    (same2other "a"                       == False) &&
    (same2other [2]                       == False) &&
    (same2other "aaa"                     == True)  &&
    (same2other [8, 8, 8]                 == True)  &&
    (same2other [2, 2, 3, 4]              == False) &&
    (same2other [2, 2, 3, 4, 2]           == True)  &&
    (same2other "aatdaya"                 == True)  &&
    (same2other "aatdgyb"                 == False) &&
    (same2other [8, 8, 3, 8, 3, 6, 8, 12] == True)

same2other :: Eq a => [a] -> Bool 
same2other xs = length xs >= 3 && x == y && x `elem` ys
    where (x:y:ys) = xs
{-
### Question 1(v) [2 marks]

Write a function `justVowels` that returns a list of all vowels in a string in the order and case they occur. 
Your solution should satisfy:

-}
testVowels :: Bool
testVowels = 
    justVowels "Hello World!"       == "eoo"  &&
    justVowels "Aaron562qe"         == "Aaoe" && 
    justVowels "sof3isGREATsoenjOY" == "oiEAoeO" &&
    justVowels "numberPLATE2021"    == "ueAE"

justVowels :: String -> String
justVowels = filter (`elem` "aAeEiIoOuU")


{-
### Question 1(vi) [3 marks]

Write a function `revAllLower` that takes a string and returns the elements of the string in reverse order, converting every upper case character into lower case.

Your solution should satisfy:

-}

testRev :: Bool 
testRev = 
    revAllLower ""                            == "" &&
    revAllLower "!reTupmoC"                   == "computer!" &&
    revAllLower "Software3"                   == "3erawtfos" &&
    revAllLower "Software3!"                  == "!3erawtfos" &&
    (revAllLower $  revAllLower "Software3!") == "software3!"

revAllLower letters = reverse $ map toLowercase letters
    where
        toLowercase x
            | x `elem` uppercases = lowercases !! positionFind x uppercases
            | otherwise = x
        lowercases = "abcdefghijklmnopqrstuvwxyz"
        uppercases = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        positionFind :: Eq a => a -> [a] -> Int
        positionFind x = positionFinding 0
            where
                positionFinding n (y:ys)
                    | x == y = n
                    | otherwise = positionFinding (n + 1) ys

{-
### Question 1(vii) [5 marks]
Write a function `findPlurals`, such that given a list over an `Ord` type, `a`, it returns a sorted list of all elements that 
occur at least twice.

Your solution should satisfy: 
-}


testfindPlurals :: Bool 
testfindPlurals =
    (findPlurals ""                             == "") &&
    (findPlurals "THE1SOF1"                     == "1") &&
    (findPlurals "accommodation"                == "acmo") &&
    (findPlurals "Accommodation"                == "cmo") &&
    (findPlurals "THE2SOF2SYS1DAT1HCI1"         == "12HST") &&
    (findPlurals [1, 3, 4, 2, 3, 5, 7, 1, 9, 3] == [1,3]) &&
    (findPlurals [1, 3, 4, 2, 3, 5, 7, 1, 9, 5] == [1,3,5]) &&
    (findPlurals [1, 5, 4, 2, 3, 5, 7, 1, 9, 3] == [1,3,5]) 


findPlurals :: Ord a => [a] -> [a]

findPlurals letters
    | null letters = letters
    | x `elem` ys = x : findPlurals withoutxs
    | otherwise = findPlurals ys
        where
            (x:ys) = sort letters
            withoutxs = filter (/=x) ys
            sort [] = []
            sort (x:xs) = sort [y | y <- xs, y < x]
                ++ x : [y | y <- xs, y == x]
                ++ sort [y | y <- xs, y > x]

{-
### Question 1(viii) [5 marks]


Given the following type `Course` to represent all university courses,
-}

data Course = NICE | EASY | SOFT | HARD | HALF | FULL deriving (Show, Eq)

{-
The rules on prerequisites are as follows:

To study EASY a student must have passed SOFT.
To study HARD a student must have passed both EASY and NICE.
To study FULL a student must have passed both SOFT and HALF.
The rest of the courses do not have any prerequisites. 

Given the type `Student` to represent any student's record, where `CMark` is the list of course and mark pair for the student. 
-}
data Student = Student SName Age College CMark


data College = Halifax | James | Langwith deriving (Show, Eq)

type SName   = String
type Mark    = Int 
type Age     = Int 
type CMark = [(Course, Double)]

benWalker, jBond, yWu, kSong, mGove :: Student
benWalker 
  = Student "Ben Walker" 19 Halifax [(SOFT, 62), (EASY, 42), (FULL, 62)]
jBond = Student "James Bond" 21 Halifax [(SOFT, 42), (EASY, 42)]
mGove = Student "Mike Gove" 21 Halifax [(SOFT, 22), (EASY, 42)]
yWu = Student "Yang Wu" 18 Halifax [(SOFT, 22)]
kSong = Student "Kelly Song" 22 Halifax []

{-
Given a student record `Student`, write a function `checkPrereqs` which returns `True` if the student has the prerequisites for all courses they have studied and `False` otherwise. The pass mark for a course is 40%.


Your solution should satisfy:
-}

testPrereqs :: Bool
testPrereqs = 
  (checkPrereqs benWalker == False) &&
  (checkPrereqs jBond     == True)  &&
  (checkPrereqs yWu       == True)  &&
  (checkPrereqs mGove     == False) &&
  (checkPrereqs kSong     == True)

checkPrereqs :: Student -> Bool

checkPrereqs stu@(Student _ _ _ modules) = modulesCheck modules
    where
        modulesCheck :: [(Course, Double)] -> Bool
        modulesCheck [] = True
        modulesCheck courses@((course, _):remaining) = courses `markCheck` prerequisites course && modulesCheck remaining
        markCheck :: [(Course, Double)] -> [Course] -> Bool
        markCheck _ [] = True
        markCheck examinedcourses (prerequisite:rest) = isvalid prerequisite examinedcourses && markCheck examinedcourses rest
        isvalid :: Course -> [(Course, Double)] -> Bool
        isvalid _ [] = True
        isvalid course ((taken, mark):takens)
            | course == taken = mark >= passingmark
            | otherwise = isvalid course takens
        passingmark = 40
        prerequisites :: Course -> [Course]
        prerequisites EASY = [SOFT]
        prerequisites HARD = [EASY, NICE]
        prerequisites FULL = [SOFT, HALF]
        prerequisites _ = []




{-
### Question 1(ix) [5 marks]

Write a function `numDiff` that computes the difference between the product of all even numbers and the sum of all odd numbers in a string.
Assume every numeric character is an independent number. 
 
Your solution should satisfy:

-}
testND :: Bool
testND = 
   numDiff "soft"               == 1 &&
   numDiff "soft2"              == 2 &&
   numDiff "soft3"              == -2 &&
   numDiff "char27481"          == 56 &&
   numDiff "3to15is117"         == -17 &&
   numDiff "some2743367numbers" == 28


numDiff :: String -> Int

numDiff :: String -> Int
numDiff str = foldr (*) [] evenses - foldr (+) [] oddses
    where
        oddses = filter odd digitising
        evenses = filter even digitising
        digitising = map toint filter (`elem` "0123456789") str 
        positionFind :: Eq a => a -> [a] -> Int
        toint :: [Char] -> [Int]
        toint n = positionFind n "0123456789"
        positionFind x = positionFinding 0
            where
                positionFinding n (y:ys)
                    | x == y = n
                    | otherwise = positionFinding (n + 1) ys


{-
### Question 1(x) [10 marks]
Consider the record of a Computer science student modelled by the type `CSStudent`

-}

data CSStudent = CSStudent {sid :: SID, sname :: SName, stage :: Stage} 
                    deriving (Ord, Eq, Show)

type SID     = Int 

data Stage  = One | Two | Three | Four deriving (Ord, Eq, Show)

{-
[B-Trees](https://ebookcentral.proquest.com/lib/york-ebooks/reader.action?docID=3339142&ppg=1272) are a generalisation of binary sort trees in which each node can have a larger, variable number of children.

[Knuth's](https://en.wikipedia.org/wiki/B-tree#CITEREFKnuth1998) definition, a B-tree of order *m* is a tree which satisfies the following properties:

1. Every node has at most *m* children.
2. Every non-leaf node (except the root) has at least the ceil of *m/2* child nodes.
3. The root has at least two children unless it is a leaf node.
4. A non-leaf node with *k* children contains *k-1* keys.
5. All leaves appear in the same level.

Given the type `DBTreeO` of a B-Tree: 
-}

data DBTreeO a = DBEmp Int | DBLeafO Int [a] | DBNodeO Int [a] [DBTreeO a] deriving (Eq, Show)

{-
`DBEmp m` is an empty tree, `DBLeafO m xs` is a leaf node and `DBNodeO m xs ts` is a non-leaf node, all with order `m`.
-}

csStud, students, csYork, dbThree, stdTest :: DBTreeO CSStudent
students = DBLeafO 4 
  [CSStudent {sid = 2, sname = "Mark Foster", stage = One}, 
  CSStudent {sid = 3, sname = "Juli Smith", stage = Two}]
stdTest  = DBLeafO 4 
  [CSStudent {sid = 1, sname = "Jane Hay", stage = One}, 
  CSStudent {sid = 3, sname = "Mat Bell", stage = Three}]
csStud   = DBEmp 4
csYork   = DBLeafO 3
     [CSStudent {sid = 2, sname = "Mark Foster", stage = One},
     CSStudent {sid = 3, sname = "Juli Smith", stage = Two}]
dbThree  = 
   DBNodeO 3 [CSStudent {sid = 3, sname = "Kriss Wells", stage = One}] 
   [DBLeafO 3 [CSStudent {sid = 2, sname = "Sally Hodge", stage = Two}],
   DBLeafO 3 [CSStudent {sid = 7, sname = "Greg Ovett", stage = Two},
   CSStudent {sid = 20, sname = "Ann Webb", stage = Four}]]
{-
#### Question 1(x)(a) [2 marks]
Consider a database table with records of computer science students organised as a B-Tree of order 4 and `SID` as the keys
 (for example, `students`). Write a function `csFind` which returns `True` if a student with the provided `SID` exists in the database, and `False` otherwise. 

Your solution should satisfy:
-}
testcsFind :: Bool
testcsFind = 
   csFind students 1       == False &&
   csFind students 2       == True &&
   csFind students 3       == True &&
   csFind students 0       == False &&
   csFind students (-13)   == False 


csFind :: DBTreeO CSStudent -> SID -> Bool
csFind (DBEmp _) _ = False
csFind (DBLeafO _ []) _ = False
csFind (DBLeafO _ (stu@(id, _, _):reststus)) isid = id == isid || csFind (DBLeafO _ reststus) isid
csFind (DBNodeO _ ((id, _, _):reststus) (DBTreeO cont)) = id == isid || csFind (DBNodeO _ reststus) isid || csFind (DBTreeO cont) isid


{-
#### Question 1(x)(b) [8 marks]
Consider a database table with records of computer science students organised as a B-Tree of order 4 and `SID` as keys (for example,
 `students`). Write a function `csInsert` which inserts the record of a computer science student into a database organised as a 
 B-Tree. You may assume that the B-tree is either empty, or the root node is a non-full leaf-node.  In all other cases the function
  should return the original database.  

Your solution should satisfy:
-}

testInsert :: Bool
testInsert =
   csInsert students CSStudent {sid =1, sname = "Yi Wu", stage = Four} == 
     DBLeafO 4 [CSStudent {sid = 1, sname = "Yi Wu", stage = Four},
     CSStudent {sid = 2, sname = "Mark Foster", stage = One},
     CSStudent {sid = 3, sname = "Juli Smith", stage = Two}] &&
   csInsert csStud CSStudent {sid =1, sname = "Mike Brown", stage = One} == 
     DBLeafO 4 [CSStudent {sid = 1, sname = "Mike Brown", stage = One}] &&
   csInsert stdTest CSStudent {sid = 1, sname = "Yi Wu", stage = Four} ==
     DBLeafO 4 [CSStudent {sid = 1, sname = "Jane Hay", stage = One},
     CSStudent {sid = 3, sname = "Mat Bell", stage = Three}] &&
   csInsert 
     (csInsert csStud CSStudent {sid = 1, sname = "Mike Brown", stage = One}) 
     CSStudent {sid=2, sname="Georgia Jones", stage=Two} == 
     DBLeafO 4 [CSStudent {sid = 1, sname = "Mike Brown", stage = One},
     CSStudent {sid = 2, sname = "Georgia Jones", stage = Two}] &&
   csInsert 
     (csInsert (csInsert 
     csStud CSStudent {sid = 1, sname = "Mike Brown", stage = One}) 
     CSStudent {sid=2, sname="Georgia Jones", stage=Two}) 
     CSStudent {sid=3, sname="Tamara Berg", stage=Three} == 
     DBLeafO 4 [CSStudent {sid = 1, sname = "Mike Brown", stage = One},
     CSStudent {sid = 2, sname = "Georgia Jones", stage = Two},
     CSStudent {sid = 3, sname = "Tamara Berg", stage = Three}] &&
   csInsert 
     (csInsert (csInsert (csInsert 
     csStud CSStudent {sid = 1, sname = "Mike Brown", stage = One}) 
     CSStudent {sid=2, sname="Georgia Jones", stage=Two}) 
     CSStudent {sid=3, sname="Tamara Berg", stage=Three}) 
     CSStudent {sid=7, sname="Eric Han", stage=Four} == 
     DBLeafO 4 [CSStudent {sid = 1, sname = "Mike Brown", stage = One},
     CSStudent {sid = 2, sname = "Georgia Jones", stage = Two},
     CSStudent {sid = 3, sname = "Tamara Berg", stage = Three}]


csInsert :: DBTreeO CSStudent -> CSStudent -> DBTreeO CSStudent
csInsert (DBEmp stus) inserting = stus
csInsert (DBLeafO stus []) inserting = stus
csInsert (DBLeafO _ (stu@(id, _, _):reststus)) inserting@((isid:rst):rstt) <= id < isid || csInsert (DBLeafO _ reststus) isid
csInsert (DBNodeO _ ((id, _, _):reststus) (DBTreeO cont)) = id <= isid || csFind (DBNodeO _ reststus) isid || csInsert ((DBTreeO cont) isid)

empty :: (Ord a) => DBTreeO CSStudent -> Bool
empty DBEmp = True
empty  _  = False


{-
## Question 2 [25 marks]

-}

{-
In this question you are asked to define types, as well as values.
Each type, *Name*, is given a default implementation as an alias for
the unit type: `type Name = ()`.  You may change the keyword `type` to
either `newtype` or `data` if appropriate, and you should replace the
unit type, `()`, by a suitable type expression.  You may derive any
type classes, such as `Show`, that will be useful.

Marks will be mostly given for how well the type protects the
programmer from mistakes, and also partly for the run-time efficiency
of the type.

Consider the game of
[*Mastermind*](https://en.wikipedia.org/wiki/Mastermind_(board_game)),
where one player constructs a secret, known as a "code", and their
opponent has to guess the secret in a limited number of guesses.  Each
incorrect guess gives information to the guesser that they can use to
refine their guess.

A secret is represented as four distinct colours, in a particular
order, drawn from six possibilities:
-}
data Colour = Red | Orange | Yellow | Green | Blue | Indigo
  deriving (Eq, Show, Read)
{-
A guess is also four distinct colours, in a particular order.

### Question 2(i) [4 marks]

Implement a type, `Code`, to describe values that are secrets and
guesses.  `Code` must be an instance of the `Eq` type class.
-}
newtype Code = Secret [Colour, Colour, Colour, Colour] | Guess [Colour, Colour, Colour, Colour]
instance Eq Code where
  Secret s == Guess g = s == g
{-
### Question 2(ii) [2 marks]

Implement functions to turn a code into a list of length 4, and *vice versa*.

-}
code2List :: Code -> [Colour]
list2Code :: [Colour] -> Code
code2List (Code lstt) = lstt
list2Code = Code

testCodeToFromList :: Bool
testCodeToFromList = let datum = [Red, Orange, Yellow, Green] in
                       code2List(list2Code datum) == datum

{-
### Question 2(iii) [4 marks]

For each guess, the response is a pair of numbers:
1. The number of guess colours in the right position, and
2. The number of guess colours in the wrong position

Implement a type to represent responses to guesses.  `Response` must
be an instance of the `Eq` type class.
-}
type Response = (Int, Int) -- Replace with a suitable definition.

{-
### Question 2(iv) [2 marks]

Implement functions to construct and deconstruct a `Response`.  Given
`r :: Response`, `hits r` should evaluate to the reported number of
right colours in the right location, and `near r` to the reported
number of right colours in the wrong location.
-}
mkResponse :: Int -> Int -> Response
hits, near :: Response -> Int
mkResponse hts msss = Response (hts, msss)
hits (Response (hts, _)) = hts
near (Response (_, mss))  = mss


test_mkResponse :: Bool
test_mkResponse = let r = mkResponse 2 1 in (hits r, near r) == (2, 1)

{-
### Question 2(v) [4 marks]

Implement a function, `oneRound`, that takes a secret (a "code") and a
guess and returns the appropriate response.
-}
oneRound :: Code -> Code -> Response
oneRound scrt gss = Response (hts, msses)
  where
    hts = checkinghts 0 code2List scrt code2List gss
    msses = checkingmss 0 code2List scrt code2List gss - hts
    checkinghts hits [] [] = hits
    checkinghts hits (x:xs) (y:ys)
      | x == y = checkinghts (hits + 1) xs ys
      | otherwise = checkinghts hits xs ys
    checkingmss misses [] _ = misses
    checkingmss misses (x:xs) gss
      | x `elem` gss = checkingmss (misses + 1) xs gss
      | otherwise = checkingmss misses xs gss
   

test_oneRound :: Bool
test_oneRound = oneRound (list2Code [Red, Orange, Yellow, Green]) 
     (list2Code [Green, Blue, Yellow, Orange]) == mkResponse 1 2

{-
### Question 2(vi) [5 marks]

Given a type to represent the two players,
-}
data Player = Encoder | Guesser deriving (Eq, Show)
{-
define a type `Winner` whose values represent whether or not there is
a winner in the current state of a game, and, if there is a winner, the
winner's name.
-}
data Winner
  = Exists Bool
  | Name String

{-
### Question 2(vii) [4 marks]

Implement a function, `winner`, that given a response to the last
guess and the remaining number of guesses reports the current winner,
if any, and a function `ppWinner` that gives the name of the winner
(`"Encoder"` or `"Guesser"`) or "No winner", as appropriate.

The guesser is the winner if the last guess exactly matches the pattern,
and the encoder is the winner the guesser has run out of attempts.

[We have provided a definition, `noWinner :: String`, that you may use.]
-}
winner :: Response -> Int -> Winner
ppWinner :: Winner -> String
noWinner :: String
noWinner = "No winner"
winner 4 0 _ = Guesser
winner _ _ 0 = Encoder
winner _ _ _ = noWinner
ppWinner Guesser = "Guesser"
ppWinner Encoder = "Encoder"


test_winner :: Bool
test_winner = ppWinner (winner (mkResponse 2 1) 2) == noWinner
              && ppWinner (winner (mkResponse 2 1) 0) == "Encoder"


{-
## Question 3 [20 marks]

A new supermarket, *Superior Outlet For Fine Foods*, better known by
its acronym, "SOFFF", or "SOF3", is being set up.

The software team producing the stocking database are trying to choose
between two different representations for the current stock:
-}
newtype StockF item = StockF {getStockF :: item -> Int}
newtype StockL item = StockL {getStockL :: [(item, Int)]} deriving (Eq, Show)
{-
Here `item` is an arbitrary type, whose values are identifiers of the
items stocked.  `StockF` maintains the database as a function that,
given an item identifier, returns the quantity in stock.  `StockL`
maintains the database as a list of pairs where the first element of
each pair is an item identifier, and the second is the quantity in
stock.

A small concrete example of item is `Item`, where
-}
data Item = Loaf_White_Small | Loaf_Brown_Large | Single_Apple | Raisins_1kg
  deriving (Eq, Show)
{-
but any type instantiating type class `Eq` can be used.

To help the software team decide between representations they have
commissioned you to produce pairs of functions for each task of
interest.  For each task below give **two** functions that solve the
problem, one function for each representation.

### Question 3(i) [4 marks]

Report how many instances of a given item are in stock.
-}
countF :: StockF item -> item -> Int
countL :: Eq item => StockL item -> item -> Int
countF (StockF {itm = stock}) itm = stock
countL = countingStocks ((stockeditem, numberof):remaining) searchingitem
    where
        countingStocks :: Eq item => [(item, Int)] -> item -> Int
        countingStocks [] _ = 0
        countingStocks stocks@((stockeditem, numberof):remaining) searchingitem
            | stockeditem == searchingitem = numberof
            | otherwise = countingStocks remaining searchingitem

test_count :: Bool
test_count = let f Single_Apple = 30
                 f Raisins_1kg = 6
                 f _           = 0
          in countF (StockF f) Single_Apple == 30
          &&
          countL (StockL [(Loaf_White_Small, 0), (Single_Apple, 30)]) 
            Single_Apple == 30

{-
### Question 3(ii) [8 marks]

The supermarket can be restocked.  Implement the two operations that
produce the updated database.  Note that the incoming delivery of
stock can also be represented as a value of type `StockF` or `StockL`
as appropriate.  The first parameter to each function is the stock in
the shop, the second is the stock on the lorry bringing the new items.

-}
restockF :: StockF item -> StockF item -> StockF item
restockL :: Eq item => StockL item -> StockL item -> StockL item
restockF = undefined
restockL (StockL ((itm, currstock):rest)) [] = []
restockL (StockL ((itm, currstock):rest)) (StockL ((newitm, newstock):newrest)) = addingStocks ((stockeditem, numberof):remaining) searchingitem
    where
        countingStocks :: Eq item => [(item, Int)] -> item -> Int
        countingStocks [] _ = 0
        countingStocks stocks@((stockeditem, numberof):remaining) searchingitem
            | stockeditem == searchingitem = numberof
            | otherwise = countingStocks remaining searchingitem

test_restock :: Bool
test_restock =
  let f Single_Apple = 30
      f Raisins_1kg  =  6
      f _            =  0
      g Raisins_1kg      = 3
      g Loaf_White_Small = 7
      g _                = 0
      r = restockF (StockF f) (StockF g)
  in countF r Single_Apple == 30 && countF r Raisins_1kg == 9
  &&
  let r = restockL (StockL [(Single_Apple, 30),(Raisins_1kg, 6)]) 
          (StockL [(Raisins_1kg, 3), (Loaf_White_Small, 7)]) 
  in countL r Single_Apple == 30 && countL r Raisins_1kg == 9

{-
### Question 3(iii) [8 marks]

The supermarket receives orders, which it fills as far as it can: for
example, if four apples are requested, but the supermarket only has
two, then only two will be removed from the stock.  Implement the two
operations that produce the updated database.

Note that the order can also be represented as a value of type
`StockF` or `StockL` as appropriate.  The first parameter to each
function is the stock in the shop, the second is the order.

This operation does **not** report the unfulfilled part of the order.

-}
fillOrderF :: StockF item -> StockF item -> StockF item
fillOrderL :: Eq item => StockL item -> StockL item -> StockL item
fillOrderF = undefined
fillOrderL = undefined

test_fillOrder :: Bool
test_fillOrder =
  let f Single_Apple = 30
      f Raisins_1kg  =  6
      f _            =  0
      g Raisins_1kg      = 9
      g Loaf_White_Small = 7
      g _                = 0
      r = fillOrderF (StockF f) (StockF g)
  in countF r Single_Apple == 30 && countF r Raisins_1kg == 0
  &&
  let r = fillOrderL (StockL [(Single_Apple, 30), (Raisins_1kg, 6)]) 
          (StockL [(Raisins_1kg, 9), (Loaf_White_Small, 7)])
  in countL r Single_Apple == 30 && countL r Raisins_1kg == 0

{-
## Question 4 [10 marks]

Recall the definition of the `ProofLayout` type constructor:
-}
infixr 0 :=: -- the fixity and priority of the operator
data ProofLayout a = QED | a :=: ProofLayout a deriving Show
{-
Consider the following definitions from the standard prelude:
```haskell
(.) :: (a -> b) -> (c -> a) -> (c -> b)
(f . g) = f (g x)           -- (.).0

maybe :: a -> (b -> a) -> Maybe b -> a
maybe k f Nothing  = k      -- maybe.0
maybe k f (Just x) = f x    -- maybe.1
```

By exhibiting a suitable value of type `ProofLayout`, prove that
```haskell
∀ g :: a -> b, k :: a, f :: c -> a {g . maybe k f == maybe (g k) (g . f)}
```
Marks will be given for correct annotation, as well as correct proof steps.

#### Hint

Use a case analysis over the structure of values drawn from a `Maybe`
type.
-}
distribMaybe :: (a -> b) -> a -> (c -> a) -> (Maybe c) -> ProofLayout b

distribMaybe x =  -- base case (Nothing as input)
    g . maybe k f Nothing
    :=: -- maybe.0 (from LHS to RHS)
    g . k
    :=: -- maybe.0 (from RHS to LHS, with k' representing (g . k))
    maybe (g . k) _ Nothing  -- cannot determine _ with this case, as when Nothing
    -- is input only the first parameter of the maybe function is dealt with
    :=:
    maybe (g k) _ Nothing
    :=:
    QED

distribMaybe (Just x) =  -- inductive case (Just as input)
    g . maybe k f (Just x)
    :=: -- maybe.1 (from LHS to RHS)
    g . f x
    :=: -- maybe.1 (from RHS to LHS, with k' representing (g . f))
    maybe _ (g . f) (Just x) -- cannot determine _ with this case, as when Just x
    -- is input only the second parameter of the maybe function is used with this input
    :=:  -- without a specific input parameter
    maybe _ (g . f)  
    :=: -- using what we have proven in both cases (where input is Nothing or Just x), we can
-- deduce from both cases that the unknown _ for the base case was found via the
-- inductive case, so we can replace the missing expression here
    maybe (g k) (g . f)  
    :=:
    QED

  
