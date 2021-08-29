
data CSStudent = CSStudent {sid :: SID, sname :: SName, stage :: Stage} 
                    deriving (Ord, Eq, Show)

type SID     = Int 

data Stage  = One | Two | Three | Four deriving (Ord, Eq, Show)


data DBTreeO a = DBEmp Int | DBLeafO Int [a] | DBNodeO Int [a] [DBTreeO a] deriving (Eq, Show)

students = DBLeafO 4 
  [CSStudent {sid = 2, sname = "Mark Foster", stage = One}, 
  CSStudent {sid = 3, sname = "Juli Smith", stage = Two}]



