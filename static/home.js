$(document).ready(function() {
    $('.email-dropdown .button-link').click(function(e){
        $('.email-dropdown ul').toggleClass('active')
        e.preventDefault();
    });
});
