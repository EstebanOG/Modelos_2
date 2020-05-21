{-
Operaciones básicas en matematicas
-}

module Basicas where

--suma
suma::Int->Int->Int
suma a b = a + b

--resta
resta::Int->Int->Int
resta a b = a - b

conteo::Int->Int
conteo n
    | n < 10 = 1
    | otherwise = conteo (div n 10) + 1

digitos_lista:: [Int]-> Int
digitos_lista [] = 0
digitos_lista (x:xs) = conteo x + digitos_lista(xs)