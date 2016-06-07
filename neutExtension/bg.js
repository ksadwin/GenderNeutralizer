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
    if (pro == 'f'){ 
        
        chrome.tabs.executeScript( { file: 'f.js'}); 
    } if (pro == 'm'){ 
        
        chrome.tabs.executeScript( { file: 'm.js' }); 
    } if (pro == 't') { 
        
        chrome.tabs.executeScript( { file: 't.js' }); 
    }     
    
    
};
         