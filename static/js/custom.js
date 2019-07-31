let csrfmiddlewaretoken = document.getElementsByName("csrfmiddlewaretoken")[0].value;

$('#register-form').submit(function (e) {
    e.preventDefault();

    $.ajaxSetup({
        headers: {
            'X-CSRFToken': csrfmiddlewaretoken
        }
    });

    let form = $(this);

    // form.find('#please-wait').removeClass('hidden');

    $.ajax({
        type: 'POST',
        url: form.attr('action'),
        data: form.serialize(),
        dataType: 'json',
        success: function (res) {

            // form.find('#please-wait').addClass('hidden');

            if (res.status === false) {
                $('#register-error').text('');
                $.each(res.errors, (index, item) => {
                    $('#register-error').append(item + '<br/>');
                });
            }
            if (res.status === true) {
                $('#register-error').text(res.message);
                // hide register modal and show login modal
                setTimeout(function () {
                    $("#register").modal("hide");
                    $("#login").modal("show");
                }, 2000);
            }
        },
        error: function (err) {
            console.log(err);
        }
    });
});


$('#login-form').submit(function (e) {
    e.preventDefault();

    $.ajaxSetup({
        headers: {
            'X-CSRFToken': csrfmiddlewaretoken
        }
    });

    let form = $(this);

    // form.find('#please-wait').removeClass('hidden');

    $.ajax({
        type: 'POST',
        url: form.attr('action'),
        data: form.serialize(),
        dataType: 'json',
        success: function (res) {

            // form.find('#please-wait').addClass('hidden');

            if (res.status === false) {
                $('#login-error').text('');
                $.each(res.errors, (index, item) => {
                    $('#login-error').append(item + '<br/>');
                });
            } else if (res.status === true) {
                $('#login-error').text(res.message);
                // Redirect to given url
                setTimeout(function () {
                    location.reload();
                }, 2000);
            }
        },
        error: function (err) {
            console.log(err);
        }
    });
});

$(document).ready(function () {

    $('#songFile').on('change', function (e) {
        if ($(this).val().split("\\")[2]) {
            $('#songName').val($(this).val().split("\\")[2]);
            $('#songChoose').text($(this).val().split("\\")[2]);
        }
    });

    $('#audioPlayer').css('visibility', 'hidden');

    $('input[type=radio][name=type]').change(function () {
        if (this.value === 'free') {
            $('#price').find("*").prop('disabled', true);
        } else if (this.value === 'paid') {
            $('#price').find("*").prop('disabled', false);
        }
    });

    // tag-it plugin
    $("#song_tag").tagit();

    // search
    $('#search').on('keyup', function () {
        let keyword = $(this).val();
        if (keyword !== '') {
            $.ajax({
                type: 'GET',
                url: $(this).data('search-url') + '?q=' + keyword,
                dataType: 'json',
                success: function (res) {
                    let search_track = $('#search-track');
                    search_track.empty();
                    if (res.songs.length > 0) {
                        $.each(res.songs, function (index, song) {
                            let artists = "";
                            $.each(song.artists, function (i, artist) {
                                if (i !== 0) artists += ", " + artist.name;
                                else artists += artist.name;
                            });
                            search_track.append('<div class="col-xl-4 col-md-6 col-12">\n' +
                                '                            <div class="custom-card mb-3">\n' +
                                '                                <a href="/track/' + song.audio_id + '" class="text-dark custom-card--inline">\n' +
                                '                                    <div class="custom-card--inline-img">\n' +
                                '                                        <img src="' + song.thumbnail + '" alt=""\n' +
                                '                                             class="card-img--radius-sm">\n' +
                                '                                    </div>\n' +
                                '                                    <div class="custom-card--inline-desc">\n' +
                                '                                        <p class="text-truncate mb-0">' + song.title + '</p>\n' +
                                '                                        <p class="text-truncate text-muted font-sm">' + artists + '</p>\n' +
                                '                                    </div>\n' +
                                '                                </a>\n' +
                                '                            </div>\n' +
                                '                        </div>')
                        });
                    } else {
                        search_track.append('<div class="col-xl-4 col-md-6 col-12"><p>Nothing found with this keyword!</p></div>')
                    }
                },
                error: function (err) {
                    console.log(err);
                }
            });
        }
    });
});
