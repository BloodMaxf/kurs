window.onscroll = function() {scrollFunction()};

function scrollFunction(evt) {
  evt.preventDefault();
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    document.getElementById("navbar").style.top = "16px";
  }
}



function app(){
    const buttons = document.querySelectorAll('.pos')
    const cards = document.querySelectorAll('.product-wrapper')

    function filter(category,items){
        items.forEach((item) => {
            const isItemFiltered = !item.classList.contains(category)
            if(isItemFiltered){
                item.classList.add('hide')
            }
        })
    }

    buttons.forEach((button)=>{
        button.addEventListener('click',() => {
            const currentCategory = button.dataset.filter
            filter(currentCategory,cards)
            console.log(currentCategory)
        })
    })
}


app()