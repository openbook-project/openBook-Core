module OB_Parser where
import System.IO
import System.IO (isEOF)
import HTMLWriter

translations :: [ (String, String ) ]
translations = [ ("par", par) ]

data Token = Token
        { 
          type_ :: String,
          data_ :: String,
          opts_ :: [ String ],
          prms_ :: [ (String, String) ],
          line_ :: Int
        }
        deriving (Show)


buildEmptyToken :: Token
buildEmptyToken = Token "" "" [""] [("","")] 0

splitOnHelper :: String -> Char -> String -> ( String, String )
splitOnHelper str chr buffer 
    | null str = ( buffer, "" )
    | head str == chr = ( buffer, (tail str) )
    | otherwise = splitOnHelper (tail str) chr (buffer ++ [(head str)])

splitOn :: String -> Char -> (String, String)
splitOn str chr = 
    splitOnHelper str chr ""


data TokenData = TokenData
    {
        type_val :: String,
        opts_val :: [ String ],
        prms_val :: [ (String, String) ]
    }
    deriving (Show)

-- return the token type and any options and parameters
parseTagContents tag = do
    let a = splitOn tag '|'
        t = fst a
        o = [snd a]  --TODO
        p = [("","")]

    TokenData t o p

tokenDebug :: Char -> String -> Char -> String -> IO()
tokenDebug start between end dat
    | foo = print (between ++ " " ++ dat)
    | otherwise = putStr ""
    where foo = and [ (start == '#'), (end == '#') ]


buildToken :: Char -> String -> Char -> String -> Token
buildToken '#' between '#' dat = do  
    let tmp = parseTagContents between
    Token (type_val tmp) dat (opts_val tmp) (prms_val tmp) 0


buildToken _ _ _ _ = buildEmptyToken 
     

getNextTagMark :: String -> Char -> String -> String
getNextTagMark buffer next_char full_word
    | (length full_word) <= 2 = ""
    | next_char == '#' = buffer
    | otherwise = getNextTagMark (buffer ++ [next_char]) (head (tail ( tail full_word))) (tail full_word) 


isEmptyToken :: Token -> Bool
isEmptyToken token = (and [(type_ token == ""), (data_ token == "")  ])


parseHelper :: String -> Token
parseHelper word = do
    let start = head word
        between = getNextTagMark "" (head (tail word)) word 
        tmp = splitAt ((length between) + 2 ) word
        substr = snd tmp
        end = last $ fst tmp
        dat = getNextTagMark "" (head (tail substr)) substr
    
    if (or [length between == 0, length dat == 0])
        then buildEmptyToken
    else
        buildToken start between end dat


updateTokenLine :: Token -> Int -> Token
updateTokenLine old newline = 
    Token (type_ old) (data_ old) (opts_ old) (prms_ old) newline


updateLineCount :: [Char] -> Char -> [Char]
updateLineCount lis '\n' = 
    lis ++ ['\n']
updateLineCount lis chr = 
    lis


--parseByWord :: Handle -> String -> [Token] -> IO [Token]
parseByWord fd string ret lines = do
    isEnd <- hIsEOF fd
    if isEnd
        then return ret
    else do

    next <- hGetChar fd
    let status = updateTokenLine (parseHelper string) ((length lines) - 1)
        -- move the 'pointer' 2 chars back since the #, and next char have been read already
        next_start = (snd (splitAt (length string - 2) string )) ++ [next] 
        line_count = updateLineCount lines next


    -- only append if we got an actual token
    if isEmptyToken status 
        then parseByWord fd (string ++ [next]) ret line_count
    else 
        parseByWord fd next_start (ret ++ [status]) line_count


parse fd = parseByWord fd "" ([] :: [Token]) []

