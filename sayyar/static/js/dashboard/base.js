const offcanvasBtn = document.querySelector('.offcanvas-open-close')
const offcanvasBtnIco = document.querySelector('.offcanvas-open-close i')
const offcanvasSidbar = document.querySelector('.offcanvas-sidbar')
const sidbarLinks = document.querySelectorAll('.offcanvas-sidbar .nav-link')
const pathname = window.location.pathname

sidbarLinks.forEach(el => {
    if (pathname == el.pathname) {
        el.classList.add('active')
    }
});


function Hideffcanvas() {
    offcanvasSidbar.classList.remove('show')
    offcanvasSidbar.classList.add('hide')
    offcanvasBtnIco.classList.remove('bi-arrow-bar-left')
    offcanvasBtnIco.classList.add('bi-arrow-bar-right')
}
function offcanvasOpenClose() {
    
    if (offcanvasSidbar.classList.contains('show')) {
        Hideffcanvas()
    } else if (offcanvasSidbar.classList.contains('hide')) {
        offcanvasSidbar.classList.remove('hide')
        offcanvasBtnIco.classList.remove('bi-arrow-bar-right')
        offcanvasBtnIco.classList.add('bi-arrow-bar-left')

    }
}

offcanvasBtn.addEventListener('click', offcanvasOpenClose);
window.onresize = Hideffcanvas;

if (window.screen.width <= 578) {
    Hideffcanvas()
}



  // randomGen
function randomGen() {
    let min = 100000
    let max = 1000000
    return (Math.floor((Math.random())*(max-min+1))+min).toString();
  }
  
  
  
  // Toast Alert
  const toastBox = document.querySelector('#toast-box')
  function showToast(toastID, username, msg, img) {
      if (img == '') {
        img = default_img_profile
      }
    html = `
  
      <!-- Then put toasts within -->
      <div class="toast" role="alert" id="toast${toastID}" aria-live="assertive" aria-atomic="true">
        <div class="toast-header">
          <img src="${img}" class="rounded me-2" alt="..." width="50" style="border-radius: 100% !important;">
          <strong class="me-auto">${username}</strong>
          <small class="text-body-secondary">الان</small>
          <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
        </div>
        <div class="toast-body">
          ${msg}
        </div>
      </div>
    `
  
  
    toastBox.insertAdjacentHTML("beforeend", html)
    $(`#toast${toastID}`).toast('show');
  
  };




// Form Bootsrap Validation
(() => {
  'use strict'

  // Fetch all the forms we want to apply custom Bootstrap validation styles to
  const forms = document.querySelectorAll('.needs-validation')

  // Loop over them and prevent submission
  Array.from(forms).forEach(form => {
    form.addEventListener('submit', event => {
      if (!form.checkValidity()) {
        event.preventDefault()
        event.stopPropagation()
      }

      form.classList.add('was-validated')
    }, false)
  })
})()


// Get Request fetch
async function fetchAsync (url) {
  let response = await fetch(url);
  let data = await response.json();
  return data;
  }

// POST Request fetch
async function POSTFetchAsync (url, json_data) {
  let response = await fetch(url, {
    method: 'POST',
    headers: {
      Accept: 'application/json',
      'Content-Type': 'application/json'
      },
    body: JSON.stringify(json_data)
    }
  );

  let data = await response.json();
  return data;
  }


// Notifications Messages Popover
$(document).ready(function() {
  // var optionsNoti = {
  //     sanitize: false,
  //     html: true,
  //     title: "الاشعارات",
  //     customClass: 'MessagesPopover',
  //     //html element
  //     //content: $("#popover-content")
  //     content: $('[data-name="popover-content-noti"]').html(),
  //     //Doing below won't work. Shows title only
  //     //content: $("#popover-content").html()
      
  //     fallbackPlacements : ['bottom']
  // }
  // var exampleElnoti = document.getElementById('noti')
  // var popover = new bootstrap.Popover(exampleElnoti, optionsNoti)


  // Filter Popover
  const filterPopoverBtn = document.getElementById('filter-popover-btn')
  if (filterPopoverBtn) {
    const popover = new bootstrap.Popover(filterPopoverBtn, {    
      placement: 'bottom',
      title: 'Filter',
      sanitize: false,
      html: true,
      content: document.querySelector('#filter-box').innerHTML,
      customClass : 'filter-box-popover',
    })
  }
})


// read all notifi msgs
function ReadMsgs() {
  fetchAsync(`/accounts/read_all_notifi`).then(data => {
      if (data) {
          if (data.status) {
              document.querySelector('.noti-not-readed-box').classList.add('d-none')                    
          }
      }
      })
}



// add bootstrap forms-control
const forms = document.querySelectorAll('.FormAuto')
forms.forEach(form=>{

  if (form) {
    let inputs = form.querySelectorAll('input:not(.exclude):not([type="hidden"]), textarea, select')
    inputs.forEach(el => {
      let label = form.querySelector(`label[for="${el.id}"]`)
      box_class = ''
      help_text = ''
      error_text = ''
      help_text_el = form.querySelector(`#${el.id}_helptext`)
      error_text_el = form.querySelector(`#${el.id}_error`)
      if (help_text_el) {
        help_text_el.remove()
        help_text = help_text_el.outerHTML
      }
      if (error_text_el) {
        error_text_el.remove()
        error_text = error_text_el.outerHTML
      }

      if (label) {
        if (el.tagName == 'SELECT') {
          el.classList.add('form-select')
          label.classList.add('form-label')
          box_class += 'mb-3 '
  
        } else {
          if (el.type == 'checkbox') {
            el.classList.add('form-check-input')
            if (form.classList.contains('check-cols')) {
              box_class += 'form-check form-switch mb-3 col'
            } else {
              box_class += 'form-check form-switch mb-3 w-100'
            }
          } else {
            el.classList.add('form-control')
            label.classList.add('form-label')
            if (el.tagName != 'TEXTAREA') {
              box_class += 'mb-3 col'
            } else {
              box_class += 'mb-3 w-100'
            }
  
          }
        }

        
        label.insertAdjacentHTML('beforebegin', `<div class="${box_class}">${label.outerHTML+error_text+el.outerHTML+help_text}</div>`)
        el.remove()
        label.remove()
      }
  
    })
  }  
})


// enable bootstrap tooltips
var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
  return new bootstrap.Tooltip(tooltipTriggerEl)
})