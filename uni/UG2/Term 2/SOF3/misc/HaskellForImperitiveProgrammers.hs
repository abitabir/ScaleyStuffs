-- creating a function elem (based on the inbuilt function) which returns True if an element is in a given list, otherwise returning false

elemmy :: (Eq a) => a -> [a] -> Bool
elemmy a (x:xs)
 | a == x = True
 | null xs = False
 | otherwise = elemmy a xs

elem_2 :: Eq t => t -> [t] -> Bool
elem_2 a [] = False
elem_2 a (x:xs)
 | a == x = True
 | otherwise = elem_2 a xs

elemSolution :: (Eq a) => a -> [a] -> Bool
elemSolution _ [] = False
elemSolution e (x:xs) = (e == x) || elemSolution e xs

-- creating a function nub which removes all duplicates from a given list

nubby_2 :: Eq a1 => [a1] -> [a2]
nubby_2 [] = []
--nubby_2 [a] = [a]
nubby_2 lstt = setCreation lstt []
    where
    setCreation (x:xs) sett
     | x `elem` xs = setCreation xs (x:sett)
     | otherwise = setCreation xs sett

nubbySimpleSolution :: Eq a => [a] -> [a]
nubbySimpleSolution [] = []   -- this is also base case
nubbySimpleSolution (x:xs)
 | x `elem` xs = nubbySimpleSolution xs
 | otherwise = x : nubbySimpleSolution xs

-- creating a function isAsc which returns True if the input list is ascending

isAscMulti :: Ord a => [a] -> Bool
isAscMulti [] = True
isAscMulti [_] = True
isAscMulti (x:y:xs)
 | x < y = isAscMulti (y:xs)
 | otherwise = False

isAscSimpleSolution [] = True 
isAscSimpleSolution [a] = True 
isAscSimpleSolution (x:y:xs) = (x <= y) && isAscSimpleSolution (y:xs)
-- yeehawww

-- creating a function which can determine if a path exists from one node to another in a directed graph inputted ~ beware cyclic routes
directedGraph = [(1, 2), (2, 3), (3, 2), (4, 3), (4, 5)]
fromNode = 1
toNode = 3

-- hasNode :: [(Int, Int)] -> Int -> Int -> Bool
-- hasNode directedGraph fromNode toNode 
--  = not ((fromNode, _) `notElem` directedGraph)
-- hasNode ((currentNode, nextNode):directedGraph) fromNode toNode
--  | (currentNode, nextNode) == (fromNode, toNode) = True
--  | otherwise = hasNode directedGraph nextNode toNode

hasPath :: [(Int, Int)] -> Int -> Int -> Bool
hasPath directedGraph@((currentNode, nextNode):tailGraph) fromNode toNode
 | (fromNode, _) `notElem` directedGraph = False
 | (currentNode, nextNode) == (fromNode, toNode) = True
 | otherwise = hasPath tailGraph nextNode toNode

hasPathSolution :: [(Int, Int)] -> Int -> Int -> Bool
hasPathSolution [] x y = x == y
hasPathSolution xs x y
 | x == y = True 
 | otherwise = 
  let xs' = [(n, m) | (n, m) <- xs, n /= x] in
  or [hasPathSolution xs' m y | (n, m) <- xs, n == x]