import System.IO
    ( hClose, openFile, hGetContents, IOMode(ReadMode) )
import Data.List.Split ( splitOn )

main :: IO ()
main = do
        let list = []
        handle <- openFile "input" ReadMode
        contents <- hGetContents handle
        let singlelines = contents
            list = map (read :: String -> Integer) (splitOn "," singlelines)
        print $ step 0 80 (group list) []
        print $ step 0 256 (group list) []
        hClose handle

group :: [Integer] -> [(Integer, Integer)]
group xs = group_it 0 xs

group_it :: Integer -> [Integer] -> [(Integer, Integer)]
group_it n xs | n == 7     = []
              | otherwise  = (n, toInteger $ length $ filter (== n) xs) : group_it (n+1) xs

step :: Integer -> Integer -> [(Integer, Integer)] -> [(Integer, Integer)] -> Integer 
step s u kinds cache | s == u    = foldr ((+) . snd) 0 (kinds ++ (filter ((>=s) . fst) cache))
                     | otherwise = step (s+1) u kinds' cache'
    where
        x       = s `mod` 7
        kinds_x = filter ((== x) . fst) kinds
        cache_s = filter ((== s) . fst) cache
        n       = if kinds_x == [] then 0 else snd $ head $ kinds_x
        m       = if cache_s == [] then 0 else snd $ head $ cache_s
        kinds'  = (x, n + m) : filter ((/= x) . fst) kinds
        cache'  = (:) (s + 9, n+m) cache
