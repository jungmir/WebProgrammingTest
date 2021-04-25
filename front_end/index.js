function createForm(priorityNumber, taskName) {
    var dom = document.createElement('tr');
    var checkBoxTh = document.createElement('th');
    var checkBox = document.createElement('input')
    var priority = document.createElement('th');
    var task = document.createElement('th');

    dom.setAttribute('name', 'items[]');
    checkBox.type = 'checkbox';
    checkBox.name = "selectBox[]";
    checkBox.setAttribute("class", "select");
    priority.innerHTML = priorityNumber;
    task.innerHTML = taskName;
    checkBoxTh.scope = "row";

    checkBoxTh.appendChild(checkBox);
    dom.appendChild(checkBoxTh);
    dom.appendChild(priority);
    dom.appendChild(task);

    return dom;
}

function allCheck() {
    var control = document.getElementById('selectAll');
    var checkBoxList = document.getElementsByName('selectBox[]');
    if (control.checked) {
        checkBoxList.forEach((item, index) => {
            item.checked = true;
        })
    } else {
        checkBoxList.forEach((item, index) => {
            item.checked = false;
        })
    }
}

function addItem() {
    var currentPriority = document.getElementsByName('selectBox[]').length + 1;
    var taskName = document.getElementById('task').value;
    document.getElementById('task').value = "";

    if (taskName == "") {
        alert("Please Input Task");
        return;
    }

    var taskForm = createForm(currentPriority, taskName);
    var tableBody = document.getElementById('taskList');
    tableBody.appendChild(taskForm);
}

function deleteItem() {
    var control = document.getElementById('selectAll');
    var tableBody = document.getElementById('taskList');
    tableBody.querySelectorAll("input:checked").forEach(item => item.parentNode.parentNode.remove());
    control.checked = false;
    arrangePriority();
}

function arrangePriority() {
    var taskList = document.getElementsByName('items[]');
    taskList.forEach((item, index) => {
        var thList = item.getElementsByTagName('th');
        thList[1].innerHTML = index + 1;
    })
}

function moveItem(direction) {
    var taskList = document.getElementsByName('items[]');
    if (direction == -1) {
        taskList = [].slice.call(document.getElementsByName('items[]'), 0).reverse();
    }
    taskList.forEach((item, index) => {
        var checkBox = item.getElementsByClassName('select');
        if (checkBox[0].checked) {
            if (index > 0) {
                var source = taskList[index - 1].getElementsByTagName('th')[2];
                var target = item.getElementsByTagName('th')[2];
                swapName(source, target);
            }
        }
        checkBox[0].checked = false;
    })
    arrangePriority();
}

function swapName(source, target) {
    var temp = source.innerHTML;
    source.innerHTML = target.innerHTML;
    target.innerHTML = temp;
}