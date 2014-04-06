$( document ).ready(function() {
    $('#date').datepicker({autoclose: true});
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

function showFormThanks() {
    $('.form-thanks').show();
}

function submitContactForm(url) {
  $('.has-error').removeClass('has-error');
  $('.contact-submit').addClass('disabled');
  $.ajax({
    url: url,
    type: 'POST',
    data: {
        name: $('#name').val(),
        email: $('#email').val(),
        phone_number: $('#phone_number').val(),
        date: $('#date').val(),
        head_count: $('#head_count').val(),
        location: $('#location').val(),
        additional_info: $('#additional_info').val(),
    },
    dataType: 'json'
  }).fail(function (data, textStatus, jqXHR) {
        for (var key in data.responseJSON.errors) {
           $('#' + key).parent().addClass('has-error');
        }
        $('.contact-submit').removeClass('disabled');
  }).done(function (data, textStatus, jqXHR) {
    $('.full-contact-form').fadeOut("slow", showFormThanks)
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
           $(key).parent().addClass('has-error');
        }
  }).done(function (data, textStatus, jqXHR) {
        var review = $('#id_text').val();
        var author = $('#id_name').val();
        $('.form-horizontal').before("<p>" + review + "</p>" + ((author != "") ? ("<p>– " + author + "</p>") : ''));
        $('.form-horizontal').remove();
  }); 
}