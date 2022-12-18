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
    const fieldName = document.querySelector('.nav-main-2')
    function filter(category,items){
        items.forEach((item) => {
            const isItemFiltered = !item.classList.contains(category)
            const isShowAll = category.toLowerCase() === 'all'
            if(isItemFiltered && !isShowAll){
                item.classList.add('hide')
            }else{
                item.classList.remove('hide')
            }
        })
    }

    buttons.forEach((button)=>{
        button.addEventListener('click',() => {
            const currentCategory = button.dataset.filter
            filter(currentCategory,cards)
            if(currentCategory == 'all'){
                fieldName.innerHTML = 'Категории игр'
            }else{
                fieldName.innerHTML = `Категория:${currentCategory}`
            }

        })
    })
}


app()