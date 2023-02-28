// the div where the result is displayed
var result_div = document.getElementById('result_div')

// Program for phone screens
if (window.innerWidth < 768){
    result_div.style.display = "none"
    image = document.createElement('img')
    image.setAttribute('id', 'result_eliminator')
    image.setAttribute('src', '/static/images/eliminate.png')
    image.setAttribute('height', '20px')
    image.setAttribute('width', '20px')
    image.setAttribute('class', 'result_eliminator')
    result_div.append(image)
    //alert(image.getAttribute('id'))

    image.addEventListener('click', e=>{
        result_div.style.display = "none"
    })
}

// When the window is resized
window.addEventListener('resize', e=>{
    let image = document.getElementById('result_eliminator')

    // Provided that the screen-width is greater than 768 remove eliminator
    if (window.innerWidth > 768){
        if (image){
           result_div.style.display = "block"
           image.remove()
        }
    }

    // Else, screen-width is greater, if image is not existing (of course image
    // should not exist if screen is greater than)
    else {
        if (!image){
            image = document.createElement('img')
            image.setAttribute('id', 'result_eliminator')
            image.setAttribute('src', '/static/images/eliminate.png')
            image.setAttribute('height', '20px')
            image.setAttribute('width', '20px')
            image.setAttribute('class', 'result_eliminator')
            result_div.append(image)
            //alert(image.getAttribute('id'))
        }

        if(image){
            image.addEventListener('click', e=>{
                result_div.style.display = "none"
            })
        }
    }
})



submit_button = document.getElementById('form')
submit_button.addEventListener('submit', e=>{

    e.preventDefault()
    if (window.innerWidth < 768){
        if (result_div.style.display == 'none'){
            result_div.style.display = 'block'
            //alert(result_div.style.display)
        }
    }

    var formData = new FormData();
    $.ajax({
        type: 'get',
        url: '/result/',
        data: {
            //formData.append("first_grade", $('first_grade').val()),
             // formData.append("body", $('#create_or_edit_message_body').val())
             first_grade: $('#id_first_grade').val(),
             second_grade: $('#id_first_grade').val(),
             fathers_education: $('#id_fathers_education').val(),
             mothers_education: $('#id_fathers_education').val(),
             study_time: $('#id_study_time').val(),
             sex: $('#id_sex').val()
        },
        success: function(response){
            console.log('result', response.result)
            result = document.getElementById('result')
            percent_result = document.getElementById('percent_result')

            result.innerHTML = 'Score = ' +(response.result['score'])  + ' of 20<br>' +
            '(' + (response.result['score']*100/20).toFixed(2) + '%)'

           // alert(percent_result.innerHTML)
        },
        failure: function(error){

        }

    })
})


