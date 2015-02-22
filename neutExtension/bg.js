 $("body").append('Test');
function press(){
                alert("You have chosen" + $("input[name=pronoun]:checked").val());
                $('body').append($("input[name=pronoun]:checked").val());
            }