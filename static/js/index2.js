
window.onload = function () {


    var button=document.getElementById('addressCopy')
    button.addEventListener('click',()=>{
      var input=document.getElementById('address')
      navigator.clipboard.writeText(input.value);
      alert("Coin's address was copied to your clipboard!")
    })

    var button=document.getElementById('memoCopy')
    button.addEventListener('click',()=>{
      var input=document.getElementById('memo')
      navigator.clipboard.writeText(input.value);
      alert("Memo was copied to your clipboard!")
    })

    var addressBtn=document.getElementById('addressBtn')
    addressBtn.addEventListener('click',()=>{
      var div=document.getElementById('memoQrDiv')
      div.style.display='none';
      var div=document.getElementById('addressQrDiv')
      div.style.display='';
    })

    var memoBtn=document.getElementById('memoBtn')
    memoBtn.addEventListener('click',()=>{
      var div=document.getElementById('memoQrDiv')
      div.style.display='';
      var div=document.getElementById('addressQrDiv')
      div.style.display='none';
    })

  };

function success(user){


    var coinName=document.getElementById('coinName')
    coinName.innerText=user[0]+' address:'
    var address=document.getElementById('address')
    address.value=user[1]
    var addressQr=document.getElementById('addressQr')
    addressQr.src="data:image/png;base64, "+user[6]


    var displayName=document.getElementById('displayName')
    if (displayName !=""){
        displayName.innerText=user[2]
    }

    var description=document.getElementById('description')
    if (description !=""){
    description.innerText=user[5]
    }

    var network=document.getElementById('network')
    if (user[3] !=""){
    network.innerText=user[3]
    }
    else{
        var networkDiv=document.getElementById('networkDiv')
        networkDiv.style.display='none'

    }

    var memo=document.getElementById('memo')
    if (user[4] !=""){
    memo.value=user[4]
    var memoQr=document.getElementById('memoQr')
    memoQr.src="data:image/png;base64, "+user[7]
    }
    else{
        var memoDiv=document.getElementById('memoDiv')
        memoDiv.style.display='none'
        var btnGroup=document.getElementById('btnGroup')
        btnGroup.style.display='none'
    }

}


