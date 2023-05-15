//header
function myHeaderfix() {
    let scroll = window.scrollY;
    let scrollStart = 100;
    let myheader = document.querySelector('#myheader');
    let mybody = document.querySelector('body');
    const changeHeader = () =>  myheader.classList.add('fixhead');
    const changeBody = () => mybody.classList.add('mtbody');
    const removeHeader = () =>  myheader.classList.remove('fixhead');
    const removeBody = () => mybody.classList.remove('mtbody');

    window.addEventListener('scroll' , () =>{
        scroll = window.scrollY;
        if (scroll >= scrollStart) { changeHeader(), changeBody() }
        else{ removeHeader(), removeBody() }
    })
}
myHeaderfix();
//menu
const activePage = window.location.pathname;
const navlinks = document.querySelectorAll('li .nav-link').forEach(link => {
if (link.href.includes(`${activePage}`)) {
    link.classList.add('link-secondary');
    link.classList.remove('link-dark');
}
})
// back top
document.addEventListener('DOMContentLoaded', ()=>{
function mybackTop(){
    let btnBacktop = document.querySelector('#backTop');
    let scrollBack = window.scrollY;
    let backStart = 500;
    
    window.addEventListener('scroll' , () =>{
        scrollBack = window.scrollY;
        if (scrollBack >= backStart) { btnBacktop.style.display = "block" }
        else{ btnBacktop.style.display = "none"}
    })

    btnBacktop.addEventListener('click', ()=>{
        document.body.scrollTop = 0; // For Safari
        document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
    })
}
mybackTop();
})
//news filter
const newsList = document.querySelector('.mylist'),
      newsItems = document.querySelectorAll('.myblocks_item')
      mylistItems = document.querySelectorAll('.mylist_item')

function filerNews() {
    newsList.addEventListener('click', event => { 
        const newstargetId = event.target.dataset.id
        const myTarget = event.target

        if (myTarget.classList.contains('mylist_item')) {
            mylistItems.forEach(mylistItem => mylistItem.classList.remove('activenews'))
            myTarget.classList.add('activenews')    
            
        }

        switch(newstargetId) {
            case 'all':
                getmyItems('myblocks_item')
                break
            case 'business':
                getmyItems(newstargetId)
                break     
            case 'events':
                getmyItems(newstargetId)
                break 
            case 'documentation':
                getmyItems(newstargetId)
                break                                    
        }
    })
}      
filerNews();

function getmyItems(className) {
    newsItems.forEach(item => {
        if (item.classList.contains(className)){
            item.style.display = 'block'
        } else {
            item.style.display = 'none'
        }
    })    
}

    
    
    
    
    
    
    

    
    
    
    
    
    
    
    