document.getElementById('GNsubmit').addEventListener('click', neutralize);

chrome.tabs.executeScript({ file: 'jquery-2.1.3.js'}); 
//$("#GNsubmit").click(function( event ){
    //event.preventDefault();
    
    
function neutralize(){
    console.log("hey! listen!");
    var pro = $('input[name=pronoun]:checked', '#choosePls').val(); 
    var pd; 
    if (pro == 'f'){ 
        chrome.tabs.executeScript({ file: 'f.js'}); 
    } else if (pro == 'm'){ 
        chrome.tabs.executeScript({ file: 'm.js' }); 
    } else { 
        chrome.tabs.executeScript({ file: 't.js' }); 
    }     
    
    
};
         