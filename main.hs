import System.Environment
import System.Directory
import System.Exit
import System.FilePath
import System.IO

import OB_Parser 
import HTMLWriter
import HTMLUtils
-- Ask user for a target .book file to parse
-- if no arguments are given
askFileName args 
    | length args == 0 = do
        putStrLn "Enter a .book file to parse"
        name <- getLine
        return name
    | otherwise =
        return (head args)


-- Check if a given file exists,
-- If it doesn't display an error and exit
checkFileExists :: String -> IO()
checkFileExists fname = do
    b <- doesFileExist fname
    if not b
        then do 
            putStrLn ("Cannot open file \"" ++ fname ++ "\"")
            exitWith (ExitFailure 1)
    else 
        putStr ""


-- Move the current working directory of the location of the outputfiles
-- Will create required directories if it doesn't exist
moveToTgtDir :: String -> IO()
moveToTgtDir dir = do
    b <- doesDirectoryExist dir
    if b
        then setCurrentDirectory dir 
    else do
        createDirectory dir
        setCurrentDirectory dir


-- create the media directory if it doesn't exist
initMedia :: IO()
initMedia = do
    b <- doesDirectoryExist "media"
    if b
       then putStr ""
    else
       createDirectory "media"


-- Parse given args if a target dir is given
-- otherwise give the current
getCurrentDir :: [String] -> String
getCurrentDir args 
    | length args > 1 = head (tail args)
    | otherwise = "."



main = do
    args <- getArgs
    fpath <- (askFileName args)

    checkFileExists fpath
    fd <- openFile fpath ReadMode

    let fname = takeBaseName fpath
        tgt_path = combine (getCurrentDir args) fname
        
    moveToTgtDir tgt_path

    -- create initial files --
    html <- openFile (fname ++ ".html") ReadWriteMode
    js <- openFile (fname ++ ".js") ReadWriteMode
    css <- openFile (fname ++ ".css") ReadWriteMode

    initMedia

    lexed <- parse fd
    print lexed

    writeFile (fname ++ ".html") (initFile fname)
    writeFile (fname ++ ".css") (initCSS)
    writeFile (fname ++ ".js") (initJS)