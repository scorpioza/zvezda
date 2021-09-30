(function () {
  'use strict';

    $('a[href="#"]').click(function (event) {
      event.preventDefault();
    })
    $(".to_anchor").click(function(e){
      e.preventDefault();
      $('html,body').animate({scrollTop: $('body').offset().top},'slow');
    });
    $("#zvezdaShowToast").click(function(){
      if($("#zvezdaToast").hasClass("show")){
        $("#zvezdaToast").toast('hide');
      }else{
        $("#zvezdaToast").toast('show');
      }
    });
    $('body').on('click','.close',function(){
      $(this).closest('.toast').toast('hide')
    })
    $("#zvezda-btn-groups .btn-cat-group, #zvezda-link-groups .link-cat-group, .zvezda-cat-select").click(function(){
      var lbl = $(this).attr("role");
      $(".zvezda-cat").hide();      
      $(".zvezda-cat-"+lbl).show();
      $("#zvezdaFilter").attr("class", "card mb-3 border-"+lbl).show();
      $("#zvezdaFilterLabel").attr("class", "badge rounded-pill bg-"+lbl).text($(this).text());
      $('html,body').animate({scrollTop: $('#zvezdaFilter').offset().top},'fast');
      $('.link-cat-group').removeClass("active");
      $('.link-cat-group.link-'+lbl).addClass("active");
    });      

    $("#zvezdaFilterClean").click(function(){
      $("#zvezdaFilter").hide();
      $(".zvezda-cat").show();
      $('.link-cat-group').removeClass("active");
    });


    if($("#zv-share-comics")[0]){
      var ylink = window.location.href;
      var ytitle = "ПАК Звезда: "+ $("#zvezda-buklet-title").text();
      var ycat = $("#zvezda-page-cat").text();
      var yimg = $(this).closest(".container").find(".zvezda-img").attr("src");

      createYaShare( $("#zv-share-comics")[0], ylink, ytitle, ycat, yimg);
    }
    $(".zvezda-share").click(function(){
      var zvShare = $(this).closest(".zvezda-cat").find(".zv-share")[0];
      var link = $(this).closest(".zvezda-cat").
                    find('.zvezda-img-link').attr("href");
      var title = "ПАК Звезда: "+
        $(this).closest(".zvezda-cat").find('.card-text').text();

      var cat = $(this).closest(".zvezda-cat").find('.zvezda-cat-select').text();
      var img = $(this).closest(".zvezda-cat").find('.card-img-top').attr("src");

      createYaShare(zvShare, link, title, cat, img);

    });

    function createYaShare(cont, link, title, cat, img){

      let dir = window.location.href.substring(0, window.location.href.lastIndexOf('/'))
      link = link.replace("./", dir+"/");

      var share = Ya.share2(cont, {
        content: {
          title: title,
          description: cat,
          url: link,
          image: img,
          hashtags: 'ПАК Звезда, криптография, MERI, NIIME, НИИМЭ'  
        },
        theme: {
          services: 'vkontakte,facebook,odnoklassniki,telegram,whatsapp,twitter,pinterest,pocket,lj'
        }/*,
        hooks: {
          onready: function () {
              alert('блок инициализирован');
          },
  
          onshare: function (name) {
              alert('нажата кнопка' + name);
          }
      }*/
    });
    }
})();


