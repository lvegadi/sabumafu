window.onload = function() {
    var descripcion = document.getElementById("descripcion").innerHTML;
    var parte1 = descripcion.substring(0,descripcion.length/2);
    var parte2 = descripcion.substring(descripcion.length/2);
    document.getElementById("descripcion").innerHTML = parte1 + "<a id='espacio'> </a><a id='continuar' href='javascript:showAll(\"parte2\")' class='text-white fw-bold stretched-link'>Continuar leyendo...</a>" + "<span id='parte2' style='display:none'>" +parte2+ "</span>"
 }

function showAll(id) {
      document.getElementById(id).style.display = "inline";
      document.getElementById('continuar').innerHTML = '';
      document.getElementById('espacio').innerHTML = '';
}