function clubsavings() {
    	var pv = parseInt(document.getElementById("amount").value);
    	var i = parseFloat(document.getElementById("rate").value)/100;
    	var n = parseInt(document.getElementById("period").value);
    	var fv; var fvifa;
    	fvifa = (( 1 + (i / 12)) * (Math.pow(( 1 + (i / 12)), n)-1)) / ( i / 12);
    	fv = fvifa * pv;    	
    	document.getElementById("result").innerHTML = "本利和 = $" + fv.toFixed(2);  
}