window.onload = function() {
    var descripcion = document.getElementById("descripcion").innerHTML;
    var parte1 = descripcion.substring(0,descripcion.length/2);
    var parte2 = descripcion.substring(descripcion.length/2);
    document.getElementById("descripcion").innerHTML = parte1 + "<span id='parte2' style='display:none'>" +parte2+ "</span>" + "<a id='espacio'> </a><a id='continuar' href='javascript:showAll(\"parte2\")' class='text-white stretched-link fw-bold'><br>Mostrar mas</a>";
    console.log(parte2);
 }

function showAll(id) {
      var estado = document.getElementById(id).style.display;
      if(estado == "inline"){
      document.getElementById(id).style.display = 'none';
      document.getElementById('continuar').innerHTML = '<br>Mostrar mas';    
      }else{
      document.getElementById(id).style.display = "inline";
      document.getElementById('continuar').innerHTML = '<br>Mostrar menos';      
      }
     
}