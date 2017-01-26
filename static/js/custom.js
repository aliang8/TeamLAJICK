$('#myTabs a').click(function(e) {
    e.preventDefault();
    $(this).tab('show');
})

var sMoney = document.getElementById("sMoney");

var sLevel = document.getElementById("sLevel");

var sEvents = document.getElementById("sEvents");


var purchase = function(e) {
    var balance = document.getElementById("balance");
    var initial = parseInt(balance.innerHTML);
    var price = this.parentNode.childNodes;
    price = parseInt(price[1].innerHTML);
    if (price > balance) {
        alert("This Reward Is Too Expensive");
    }
    else {
        var transaction = initial - price;
        balance.innerHTML = transaction.toString();
        this.parentNode.remove();
    }
};

var buy = function(e) {
    var button = this;
    var price = parseInt(button.innerHTML);
    $.ajax({
        url: "/buy",
        type: 'POST',
        data: {
            "price": price
        }
    }).done(function(result) {
        var balance = document.getElementById("balance");
        var initial = parseInt(balance.innerHTML);
        balance.innerHTML = initial - price;

        button.parentElement.parentElement.remove();

    }).fail(function() {
        console.log("Ooops");
    });
}

var addReward = function(e) {
    var name = document.getElementById("reward_name");
    name = name.value;
    var price = document.getElementById("reward_cost");
    price = parseInt(price.value);
    if (name.length == 0) {
        alert("Reward Must Have Name");
    }
    if (isNaN(price)) {
        alert("Price Must Be A Number");
    }
    if (name.length > 0 && !isNaN(price)) {
        var li = document.createElement("li");
        li.setAttribute("id", "reward")
        li.innerHTML = "<p id='reward'>Reward: " + name + "</p><p id='price'>" + price + "</p><button class='purchase'>Purchase</button>";
        var ol = document.getElementById("rewards");
        ol.appendChild(li);
        var reward_list = document.getElementById("rewards");
        var rewards = reward_list.getElementsByClassName("purchase");
        for (var i = 0; i < rewards.length; i++) {
            rewards[i].addEventListener("click", purchase);

        }
    }
}

$.fn.serializeObject = function(e) {
    var o = {};
    var a = this.serializeArray();
    $.each(a, function() {
        if (o[this.name]) {
            if (!o[this.name].push) {
                o[this.name] = [o[this.name]];
            }
            o[this.name].push(this.value || '');
        }
        else {
            o[this.name] = this.value || '';
        }
    });
    return o;
};

// Format a string
String.prototype.format = function() {
    var args = arguments;
    return this.replace(/{(\d+)}/g, function(match, number) {
        return typeof args[number] != 'undefined' 
        ? args[number]
        : match;
    });
};

var taskTemplate = `
<li class="task color-neutral">
<div class="task-meta-controls">
    <form>
        <button class="glyphicon glyphicon-pencil edittask"></button>
        <button class="glyphicon glyphicon-trash deletetask"></button>
        <div class="task-controls">
            <div class="complete">
                <button class="glyphicon glyphicon-plus completetask"></button>
            </div>
        </div>
        <input type="hidden" value="{0}">
        
    </form>
</div>
<div name="test" class="task-text">
    {1}
</div>
</li>
`;

var createToDo = function(item) {
    $("#todolist").append(taskTemplate.format(
        item["id"],
        item["task"]
    ));

};

var createHabit = function(item) {
    $("#habitlist").append(taskTemplate.format(
        item.id,
        item.task
    ));

};

var createGoal = function(item) {
    $("#goallist").append(taskTemplate.format(
        item["id"],
        item["task"]
    ));

};

var newToDo = function(e) {

    $.ajax({
        url: "/newtodo",
        type: 'POST',
        datatype: 'json',
        data: $("#todoform").serializeObject()
    }).done(function(result) {
        createToDo(result);
    }).fail(function() {
        console.log("Ooops");
    });

};

var newHabit = function(e) {


    $.ajax({
        url: "/newhabit",
        type: 'POST',
        datatype: 'json',
        data: $("#habitform").serializeObject()
    }).done(function(result) {
        createHabit(result);
    }).fail(function() {
        console.log("Oops");
    });


}

var newGoal = function(e) {

    $.ajax({
        url: "/newgoal",
        type: 'POST',
        datatype: 'json',
        data: $("#goalform").serializeObject()
    }).done(function(result) {
        createGoal(result);
    }).fail(function() {
        console.log("oops");
    });
};

var todo = document.getElementById("newtodo");
todo.addEventListener("click", newToDo);

var habit = document.getElementById("newhabit");
habit.addEventListener("click", newHabit);

var goal = document.getElementById("newgoal");
goal.addEventListener("click", newGoal);

var shop = document.getElementsByClassName("buy");
for (var i = 0; i < shop.length; i++) {
    shop[i].addEventListener("click", buy);
}


var del = function(e){
    this.parentNode.parentNode.remove();
    
}

var todoitems = document.getElementsByClassName("deletetask");
for (var i = 0; i < shop.length; i++) {
    todoitems[i].addEventListener("click", del);
}