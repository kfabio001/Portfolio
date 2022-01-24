function mostrar(elementoM,elemento1,elemento2,elemento3){
    document.getElementById(elementoM).style.display='';
    document. getElementById("p"+elementoM).className = "nav-link active";
    document.getElementById(elemento1).style.display='none';
    document. getElementById("p"+elemento1).className = "nav-link";
    document.getElementById(elemento2).style.display='none';
    document. getElementById("p"+elemento2).className = "nav-link";
    document.getElementById(elemento3).style.display='none';
    document. getElementById("p"+elemento3).className = "nav-link";
    }
