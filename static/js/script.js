$( function() {
    $("#submit").prop('disabled', true);
    $( "#vocabulary, #tweet-composer" ).sortable({
        connectWith: ".connectedSortable",
        revert: true,
        update: function(e,ui) {
            if (this === ui.item.parent()[0]) {
                letter_count();
            }
        }
    }).disableSelection();

    $("#tweet-composer").trigger("sortupdate"); // trigger the update from sortable

    $( "#submit" ).click(function() {
        $( "#tweet-composer li" ).each(function() {
            $("#final-tweet").append($(this).text() + " " );
        });
        $("#submit").prop('disabled', true);
        //$('form#submit-tweet').submit();
    });

    function letter_count() {
        var char_count = 140;
        $( "#tweet-composer li" ).each(function() {
            char_count -= $(this).text().length;
        });
        $("#characters").text(char_count);
        if (char_count < 0) {
            $("#submit").prop('disabled', true);
            $("#characters").css("color", "red");
        } else {
            $("#submit").prop('disabled', false);
            $("#characters").css("color", "black");
        }
    }
} );