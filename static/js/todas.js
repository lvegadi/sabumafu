window.onload = function() {
    var elementos = document.getElementsByClassName("acortar");
    var i = 0;
    for (i = 0; i < elementos.length; i++) {
        var descripcion = elementos[i].innerHTML;
        var parte1 = descripcion.substring(0,150);
        elementos[i].innerHTML =  parte1 + "...";
      } 
 }
