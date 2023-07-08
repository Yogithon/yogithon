$('#create-data').submit((e) => {
    event.preventDefault()

    $.ajax({
        url : '/',
        method:'POST',
        data : {
            csrfmiddlewaretoken : $('input#csrfmiddlewaretoken').val(),
            title : $('input#title').val(),
            p_name : $('input#p_name').val(),
            school : $('input#school').val(),
            author : $('input#image').val(),
            insta_url : $('input#insta_url').val(),
            description : $('textarea#description').val(),
        },
        dataType : "json",
        success(response){
            console.log(response)
            window.location.href = '/'
        },
        error(response, status, error){
            console.log(response, status, error);
        }
    })
})