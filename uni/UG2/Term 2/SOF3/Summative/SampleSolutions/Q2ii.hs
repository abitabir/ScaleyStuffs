module Q2ii where
{-
In the next group of questions you will build a function that mimics the
way that people prepare the game, by _shuffling_ the pack and then
_dealing_ the pack.

### Q2ii [3 marks]
A stream of pseudorandom natural numbers can be generated by the
_linear congruential method_.  Given any element of the stream, `n`,
the next element is:
```haskell
a*n+c `mod` m
```
for suitable values of `a`, `c`, and `m`.  Picking these values can be
difficult, but one reasonable assignment is `a==7^5`, `c==0`, and
`m=2^31-1`.

Define `psrn` to compute the next element of the stream by the linear
congruential method, using these values.

Your solution should satisfy:
-}
psrnTest :: Bool
psrnTest = psrn 1234567890 == 395529916 && psrn 2468013579 == 1257580448

psrn :: Int -> Int

psrn n = 7^5 * n `mod` (2^31-1)

tests :: [(Int, Bool)] 
tests = zipWith f [0, 999, 9999] [0,16790193,168053193]
  where f i o = (1, psrn i == o)
