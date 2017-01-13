var headerChange = function(e){
    var h = document.getElementById('h');
    h.innerHTML = this.innerHTML;
}

var restoreHead = function(e){
    var h = document.getElementById('h');
    h.innerHTML = "Hello World!";
}

var addItem = function(e){
    var li = document.createElement("li");
    li.innerHTML = "New thing";
    li.addEventListener("mouseover", headerChange);
    li.addEventListener("mouseout", restoreHead);
    li.addEventListener("click", deleteItem);
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
