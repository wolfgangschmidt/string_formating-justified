# string_formating-justified

**understanding this code**

  - the first function is responsable for formating the given strings,
  `line_formater()` only formats the lines in order for them not to exeed
  the limit size given by the user. this function can be invoke independently is disired.
  
  - the sencond `line_justified()` is dependent of the first due to the fact that it uses a list of previously
  formated strings. and receives from it also the limit size of the line breaks
  
  **Using the code**
  
    there is a `main()` which orchestrated the the hole process, 
    it passes the the Raw string to the `line_formater()` declared on the top of the code file
    as parameters the functions, it then passes the return values to the second function `line_justified()`.
    
  
