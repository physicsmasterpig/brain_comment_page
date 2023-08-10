var test_no
var school
var grade
var date
var problem_amount
var comment_method


$.get("hhttps://script.google.com/macros/s/AKfycbzUeQPWb22MZT36CKh7abZYz-sJ0fZ-jlvKgrYuDeNAqAXg38UWrqqbvei8GTU9wzhW/exec", {

    action : "getItems"

  }).done(function(data){

   test_no = data.items[data.items.length].No
   school = data.items[data.items.length].school
   grade = data.items[data.items.length].grade
   date = data.items[data.items.length].date
   problem_amount = data.items[data.items.length].problem_amount
   comment_method = data.items[data.items.length].comment_method


  }).fail(function(data){

    //실패시 들어갈 코드

  });