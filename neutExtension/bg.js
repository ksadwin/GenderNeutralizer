//chrome.tabs.executeScript({ file: 'jquery-2.1.3.js'}); 
document.getElementById('GNsubmit').addEventListener('click', neutralize);

//$("#GNsubmit").click(function( event ){
    //event.preventDefault();
    
    
function neutralize(){
    console.log("hey! listen!");
    var pro = $('input[name=pronoun]:checked', '#choosePls').val(); 
    //alert(pro);
    
    //calls a different .js file for each pronoun choice
    //the evaluation is done on a page-by-page level, not directly in this file for the extension
    if (pro == "m"){ 
        console.log("m chosen");
        chrome.tabs.executeScript( { file: 'm.js'}); 
    } else{
        if (pro == "f"){ 
            console.log("f chosen");
            chrome.tabs.executeScript( { file: 'f.js' }); 
        } else{ 
            if (pro == "t") { 
                console.log("t chosen");
                chrome.tabs.executeScript( { file: 't.js' }); 
            }     
        }
    }
    
    
};
         