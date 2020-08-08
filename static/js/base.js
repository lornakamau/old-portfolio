$(document).ready(function(){
    /* change color of navbar when toggle is clicked */
    $('.navbar-toggle').click(function() {
        $(".navbar").addClass('navbar-scroll');
        $('.navbar-brand').show(100);
    })
    $('.nav-link').click(function() {
        $(".navbar").addClass('navbar-scroll');
        $('.navbar-brand').show(100);
    })
    /* change color of navbar on scroll */
    $(window).scroll(function(){
        var scroll = $(window).scrollTop();
        if (scroll > 300) {
          $(".navbar").addClass('navbar-scroll');
          $('.navbar-brand').show(100);
        }
        else{
            $('.navbar-brand').hide(100);
            $(".navbar").removeClass('navbar-scroll');
            $(".navbar").addClass('navbar-transparent');	
        }
    })

  }) // End of document ready function

 