let counter = 1;
setInterval(function(){
  document.getElementById('radio' + counter).checked = true;
  counter++;
  if(counter > 4){
    counter = 1;
  }
}, 5000);
setInterval()
//Scroll

window.onscroll = function() {scrollFunction()};

function scrollFunction(evt) {
  evt.preventDefault();
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    document.getElementById("navbar").style.top = "16px";
  }
}



let search = document.querySelector('search-js');

search.addEventListener('click', (evt) =>{
  if (search.onmouseover ){

  }
})


