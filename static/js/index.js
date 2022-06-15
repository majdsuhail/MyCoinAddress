window.onload = function () {


  var button= document.getElementById('button-addon')
  button.addEventListener('click', ()=>{
    var input=document.getElementById('password')
    if (input.type=="password"){
      input.type="text";

    }
    else if(input.type=="text"){
      input.type="password";
    }
  });


        var address=document.getElementById('address').onkeyup=function(e) {
        if (this.value.replaceAll(/\s/g,'').length == 0) {
          this.setCustomValidity('Please enter valid characters');
        } else {
          this.setCustomValidity('');
        }
    };

        var password=document.getElementById('password').onkeyup=function(e) {
        if (this.value.replaceAll(/\s/g,'').length == 0) {
          this.setCustomValidity('Please enter valid characters');
        } else {
          this.setCustomValidity('');
        }
    };

  try {

    var coinName= document.getElementById("name").onkeyup=function(e) {
        if (this.value.replaceAll(/\s/g,'').length == 0) {
          this.setCustomValidity('Please enter valid characters');
        } else {
          this.setCustomValidity('');
        }
    };

    var button=document.getElementById('button-addon2')
    button.addEventListener('click',()=>{
      var input=document.getElementById('copy')
      navigator.clipboard.writeText(input.value);
      alert('your link was copied to you clipboard!')
    })


  } catch (error) {

  }

};

function existing(data){

        var label= document.getElementById('readyLabel');
        label.style= 'color:rgb(255, 57, 22)';
        label.innerText=data.error;

        var input= document.getElementById('copy');
        input.value= data.link;

}

function success(data){

        var label= document.getElementById('readyLabel');
        label.innerText=data.success;

        var input= document.getElementById('copy');
        input.value= data.link;

}

function deleteSuccess(data){
    var label=document.getElementById('deletedLabel')
    label.innerText=data.success;
}

function addressError(data){
    var label=document.getElementById('deletedLabel')
    label.style= 'color:rgb(255, 57, 22)';
    label.innerText=data.aError;
}

function passwordError(data){
    var label=document.getElementById('deletedLabel')
    label.style= 'color:rgb(255, 57, 22)';
    label.innerText=data.pError;
}

