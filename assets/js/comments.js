$( document ).ready(function() {

    var disqus_public_key = $('#disqus_thread').data('pub-key');
    var disqus_shortname = $('#disqus_thread').data('shortname');
    var disqus_url = window.location.href;
    var disqus_identifier = window.location.pathname;
    var thread_identifier = "ident:" + disqus_identifier;

    $.ajax({
        type: 'GET',
        url: 'https://disqus.com/api/3.0/threads/set.jsonp',
        data: { api_key: disqus_public_key, forum: disqus_shortname, thread: thread_identifier },
        cache: false,
        dataType: 'jsonp',
        success: function(result) {
            if (result.response.length === 1) {
                btnText = 'Show comments (' + result.response[0].posts + ')';
                $('.show-comments').html(btnText);
            }
        }
    });

    $('.show-comments').on('click', function() {
        $.ajaxSetup({cache:true});
        $.getScript('//' + disqus_shortname + '.disqus.com/embed.js');
        $.ajaxSetup({cache:false});
        $(this).remove();
    });

    if(/\#comment/.test(location.hash)){
        $('.show-comments').trigger('click');
    }

});
