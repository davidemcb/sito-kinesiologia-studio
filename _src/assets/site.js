(function(){
  var t=document.querySelector('.nav-toggle'),n=document.getElementById('nav');
  if(t&&n){t.addEventListener('click',function(){var o=n.classList.toggle('open');t.setAttribute('aria-expanded',o?'true':'false');});}
  document.querySelectorAll('[data-copy]').forEach(function(b){
    b.addEventListener('click',function(){
      var u=b.getAttribute('data-copy');
      if(navigator.clipboard){navigator.clipboard.writeText(u).then(function(){b.textContent='Link copiato';});}
    });
  });
})();
