$( function() {
    var word_count = 0;
    $( "#vocabulary, #tweet-composer" ).sortable({
        connectWith: ".connectedSortable",
        revert: true
    }).disableSelection();
    word_count += $(this).text().length;
    console.log(word_count);


    $("#submit").click(function() {
        $( "#tweet-composer li" ).each(function() {
            $("#final-tweet").append($(this).text() + " " );
        });
        $("#submit").prop('disabled', true);
        //$('form#submit-tweet').submit();
    });

} );