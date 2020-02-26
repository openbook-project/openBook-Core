module HTMLUtils where

-- given a src url, and an options string
-- returns a prepared JS tag
initSrcTag :: String -> String -> String
initSrcTag url opts = 
    "<script src = \"" ++ url ++ "\"" ++ opts ++ "></script>" 


-- initialize the header file by creating a header tag & starting the html body
initFile :: String -> String
initFile fname = 
    concat [
    "<!DOCTYPE html>\n",
    "<html lang=\"en\">\n",
    "<head>\n\t",
    ("<title>" ++ fname ++ "</title>\n"),
    "\t<meta charset=\"UTF-8\">\n",
    "\t<link rel = \"stylesheet\" href = \"" ++ fname ++ ".css\">\n",
    "\t" ++ (initSrcTag "https://cdn.jsdelivr.net/gh/google/code-prettify@master/loader/run_prettify.js" ""), "\n",
    "\t" ++ (initSrcTag "https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML" "async"), "\n",
    "</head>\n",
    "<body>\n\n\n",


    "<div class = \"background\" style=\"grid-row-start:1;grid-row-end:100\"></div>\n",
    "<div class = \"background\" style=\"grid-column-start:3;grid-row-start:1;grid-row-end:100\"></div>\n"
    ]

addCSSBlock :: String -> [String]-> String
addCSSBlock name vals = 
    "#" ++ name ++ "{\n\t" ++ (concat vals) ++ "\n}\n"

addCSSMediaQuery :: String -> String -> String -> [String] -> String
addCSSMediaQuery min_size max_size name vals =
    "@media only screen and (min-width: " ++ min_size ++ "px)" ++
    " and (max-width: " ++ max_size ++ "px){\n\t" ++
    "body{\n\t\t" ++
     (concat vals) ++ "\n\t}\n}\n"

initCSS :: String 
initCSS = 
    addCSSBlock "html" [
            "font-family: Arial, Helvetica, sans-serif;",
            "line-height: 2;"
        ] ++
    addCSSBlock ":root" [
        "--primary:#9c84a4;",
        "--highlight:#b597bf;"
        ] ++
    addCSSMediaQuery
        "1600" "10000"
        "body" ["display:grid;",
        "grid-template-columns: auto 800px auto;",
        "margin:0px;",
        "padding:0px;"
        ] ++
    addCSSMediaQuery
        "1280" "1599"
        "body" ["display:grid;",
        "grid-template-columns: 350px auto 350px;"
        ] ++
    addCSSMediaQuery
        "1025" "1280"
        "body" ["display:grid;",
        "grid-template-columns: auto minmax(auto, 800px) auto;"
        ] ++
    addCSSMediaQuery
        "768" "1024"
        "body" [ "display:grid;",
        "grid-template-columns: 50px auto 50px;"
        ] ++
    addCSSMediaQuery
        "481" "767" "body" [ "display:grid;",
        "grid-template-columns: 25px auto 25px"
        ] ++
    addCSSMediaQuery
        "320" "480" "body" [ "display:grid;",
        "grid-template-columns: 10px auto 10px;"
        ] ++
    addCSSBlock
        "p,h2,ul,ol,h1,pre" ["grid-column-start : 2;",
        "grid-column-end : 3;",
        "width:inherit;",
        "margin:15px;"
    ] ++
    addCSSBlock
        "b,i,a" ["grid-column-start : 2;",
        "grid-column-end : 3;",
        "padding-left:15px;",
        "padding-right:15px;"
    ] ++
    addCSSBlock
        "h1,h2"[ "margin-top:0px;",
        "margin-bottom:0px;"
    ] ++
    addCSSBlock
        ".background" ["background-color:rgb(250, 250, 250 );"] ++
    addCSSBlock
        "hr" [
        "height: 1px;",
        "border: 0;",
        "border-top: 1px solid gray;",
        "margin: 2.5px;",
        "padding: 0;",
        "width: 90%;"
    ] ++
    addCSSBlock 
        ".draggable" [
        "position:absolute;",
        "z-index:9;",
        "border:1px solid #d3d3d3;",
        "background-color:white;",
        "max-width:500px;",
        "border-radius: 10px 10px 0px 0px;",
        "box-shadow: 1px 1px 12px grey;"
    ] ++

    addCSSBlock
        ".draggable_content" [
        "max-height:400px;",
        "overflow-y:auto;"
    ] ++
    
    addCSSBlock
        ".ref_header" [
        "cursor:move;",
        "z-index:10;",
        "background-color:#9c84a4;",
        "color:#fff;",
        "display: grid;",
        "grid-template-columns: 10px auto 20px 10px;",
        "grid-column-start: 1;",
        "align-items: center;",
        "border-radius: 10px 10px 0px 0px;"
    ] ++
    addCSSBlock
        ".navbar" [
        "background: white;",
        "position: fixed;",
        "top : 0px;",
        "height:100%;",
        "z-index:100;",
        "-webkit-transition: all 0.3s ease;",
        "-moz-transition: all 0.3s ease;",
        "transition: all 0.3s ease;"
    ] ++
    addCSSBlock 
        ".navbar h3" [
        "color: white;",
        "font-size: 1.9em;",
        "padding: 20px;",
        "margin: 0;",
        "font-weight: 300;",
        "background: var(--primary);",
        "float:left;"
    ] ++
    addCSSBlock
        ".navbar a" [
        "display: block;",
        "color: black;",
        "font-size: 1.1em;",
        "font-weight: 300;"
    ] ++
    addCSSBlock
        ".navbar a:hover" [
        "background: var(--highlight);",
        "color:white;"
    ] ++
    addCSSBlock
        ".navbar a" [
        "padding-top: 5px;",
        "padding-bottom: 5px;"
    ] ++
    addCSSBlock
        ".navbar a:link" [
        "text-decoration:none;"
    ] ++
    addCSSBlock
        ".dropdown-container" [
        "display: none;",
        "padding-left: 8px;"
    ] ++
    addCSSBlock
        "#exitNavBar"[ "float:right;",
        "cursor: pointer;"
    ] ++
    addCSSBlock
        ".navButton" [
        "position: fixed;",
        "top:10px;",
        "background-color: var(--primary);",
        "width: 75px;",
        "height: 75px;",
        "border-radius: 50px;",
        "grid-column-start: 1;",
        "box-shadow:2px 2px 8px 2px  darkgray;",
        "cursor: pointer;"
    ] ++
    addCSSBlock 
        ".bar" [
        "width: 35px;",
        "height: 5px;",
        "background-color: white;",
        "margin: 6px 20px;"
    ]