$( document ).ready(function() {
    $('#id_date').datepicker();
});

function setCSRF() {
    // using jQuery
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        crossDomain: false, // obviates need for sameOrigin test
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type)) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
}

function submitForm(url) {
  $('.has-error').removeClass('has-error');
  $.ajax({
    url: url,
    type: 'POST',
    data: {
        first_name: $('#id_first_name').val(),
        last_name: $('#id_last_name').val(),
        email: $('#id_email').val(),
        phone_number: $('#id_phone_number').val(),
        date: $('#id_date').val(),
        head_count: $('#id_head_count').val(),
        location: $('#id_location').val(),
        additional_info: $('#id_additional_info').val(),
    },
    dataType: 'json'
  }).fail(function (data, textStatus, jqXHR) {
        for (var key in data.responseJSON.errors) {
           $('#id_' + key).parent().addClass('has-error');
        }
  });
}

function submitReviewFormOld(url) {
  $('.has-error').removeClass('has-error');
  $.ajax({
    url: url,
    type: 'POST',
    data: {
        name: $('#id_name').val(),
        text: $('#id_text').val(),
    },
    dataType: 'json'
  }).fail(function (data, textStatus, jqXHR) {
        for (var key in data.responseJSON) {
           $('#id_' + key).parent().addClass('has-error');
        }
  }).done(function (data, textStatus, jqXHR) {
        var review = $('#id_text').val();
        var author = $('#id_name').val();
        $('.form-horizontal').before("<p>" + review + "</p>" + ((author != "") ? ("<p>– " + author + "</p>") : ''));
        $('.form-horizontal').remove();
  }); 
}