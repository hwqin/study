/*
* Problem Statement
* ------------------
* Given a String  input, 
* Build substrings for given window size for all possible combination in left to right direction only
* Only consider alphabets and ignore special characters or numbers.
* Print Count of each substring occurance , where as substring must be in a same order as it was processed.
* Print unique substrings where characters of substrings are distinct.
* Discuss Time and Space complexity 

* input s = "abcbcbxa;bcb"
* window = 3
* output: 
*        
        [abc:2 , bcb:3, cbc:1 , cbx:1, bxa:1] //Count of each substring occurance 


*        [cbc, cbx, bxa] //Distinct substring by COUNT/occurance
*
*/

// string input size: could be large
// a $bcdef*cd  szie 4: abcd bcde cdef efcd
// widnow size range: 

function getsubstring(s, window) {
    //check input parameters
    if (s === null || s === "" || window <=0 ) {
        return;
    }
    // remove all non-aplabet chars from input string
    var alphabetstr = "";
    for (var i = 0; i < s.length; i ++) {
        if ((s[i] <= 'z' && s[i] >= 'a') || (s[i] <= 'Z' && s[i] >= 'A')) {
            alphabetstr += s[i];
        }
    }
    console.log(alphabetstr);

    // var resultstring = s.map(c=> filterfunction(c))

    // check window size and alphabetstr length
    if (alphabetstr.length < window) {
        return;
    }
    // retrive substring from alphabetstr and count the occurrences of each substring
    var substringMap = new Map();
    var substringArray = [];
    let substringCount = alphabetstr.length - window + 1;
    for (var i = 0; i < substringCount; i++) {
        let substringi = alphabetstr.substring(i, i+window);
        console.log(substringi);
        if (substringMap.has(substringi)) {
            let count = substringMap.get(substringi);
            substringMap.set(substringi, count + 1);
        } else {
            substringMap.set(substringi, 1);
            substringArray.push(substringi);
        }
    }
    
    // print substring occrences
    var outputstr = "[", outputstr2 = "[";
    const substringResultCount = substringArray.length;
    for (var i = 0; i < substringResultCount; i++){
        const substring = substringArray[i];
        const count = substringMap.get(substring);
        
        outputstr += `${substring}:${count}`;
        if (i < substringResultCount-1)
            outputstr += ",";

        if (count === 1) {
            outputstr2 += `${substring}`;
            if (i < substringResultCount-1)
                outputstr2 += ","
        }
    }
    outputstr += "]";
    outputstr2 += "]"
    console.log(outputstr);
    console.log(outputstr2);
}

getsubstring("abcbcbxa;bcb", 3);
