let num = 0;
const recieved_data = location.href.split('?')[1];
const no = recieved_data.split('&')[0];
const comment_method = recieved_data.split('&')[2];
const problem_number = recieved_data.split('&')[1];



function addStudent() {
if(comment_method == 0){
const a = document.getElementById('comment_table');
const new_form_tag = document.createElement('form');

new_form_tag.setAttribute('id', 'form_tag');
new_form_tag.setAttribute('method', 'post');
new_form_tag.setAttribute('action', 'https://script.google.com/macros/s/AKfycby7o6mNDdpuDVxCeTNIKD961M8qvmox4RcpGsLzaBrt5Ya1jE8fb2JPkF1e0FLtcwFN6A/exec');

a.appendChild(new_form_tag);
const new_input_tag_name = document.createElement('input');
new_input_tag_name.setAttribute('class', 'name');
new_input_tag_name.setAttribute('name', 'name');
new_form_tag.appendChild(new_input_tag_name);


const new_input_tag_attendence = document.createElement('input');
new_input_tag_attendence.setAttribute('class', 'input_tag_attendence');
new_input_tag_attendence.setAttribute('type', 'checkbox');
new_input_tag_attendence.setAttribute('checked', 'checked');
new_input_tag_attendence.setAttribute('name', 'attendence');
new_form_tag.appendChild(new_input_tag_attendence);

const new_input_tag_homework= document.createElement('input');
new_input_tag_homework.setAttribute('class', 'input_tag_homework');
new_input_tag_homework.setAttribute('type', 'checkbox');
new_input_tag_homework.setAttribute('checked', 'unchecked');
new_input_tag_homework.setAttribute('name', 'homework');
new_form_tag.appendChild(new_input_tag_homework);

for(var i=1; i <problem_number+1; i++){
    var new_input_tag_score = document.createElement('input');
    new_input_tag_score.setAttribute('class', 'input_tag_score_'+i);
    new_input_tag_score.setAttribute('name', 'score_'+i);
    new_form_tag.appendChild(new_input_tag_score);
    var new_input_tag_comment = document.createElement('input');
    new_input_tag_comment.setAttribute('class', 'input_tag_comment_'+i);
    new_input_tag_comment.setAttribute('name', 'comment_'+i);
    new_form_tag.appendChild(new_input_tag_comment);
}

num++;
}
}
