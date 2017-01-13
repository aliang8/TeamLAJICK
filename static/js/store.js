var headerChange = function(e){
    var h = document.getElementById('h');
    h.innerHTML = this.innerHTML;
}

var restoreHead = function(e){
    var h = document.getElementById('h');
    h.innerHTML = "Hello World!";
}

var purchase = function(price, e){
    var p = document.getElementById('balance');
    var i = parseInt(p.innerHTML);
    var f = i - parseInt(price);
    p.innerHTML = f.toString(); 
}

var addItem = function(e){
    var li = document.createElement("li");
    var name = prompt("Reward Name:");
    var cost = prompt("Reward Value:");
    //var button = "<button id=\"obtain\">purchase</button>";
    //button.addEventListener("click", purchase(cost));
    //button.addEventListener("click", deleteItem);
    li.innerHTML = "Reward: " + name + ", Costs: " + cost + button
    li.addEventListener("mouseover", headerChange);
    li.addEventListener("mouseout", restoreHead);
    var ol = document.getElementById("rewards");
    ol.appendChild(li);
}

var deleteItem = function(e){
    var li = this;
    this.remove();
}


var listItems = document.getElementsByTagName("li");

for (i = 0; i < listItems.length; i++){
    listItems[i].addEventListener("mouseover", headerChange);
    listItems[i].addEventListener("mouseout", restoreHead);
    listItems[i].addEventListener("click", deleteItem);
}

var button = document.getElementById("add");
button.addEventListener("click", addItem);
