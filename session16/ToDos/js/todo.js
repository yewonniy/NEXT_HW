const todoForm = document.getElementById("todo-form");
const todoList = document.getElementById("todo-list");
const submitBtn = document.querySelector(".submitBtn");
const todothings = document.querySelector(".todo-content");
const items = JSON.parse(window.localStorage.getItem("TODO"));

for (i = 0; i < items.length; i++) {
  let item = items.slice(i, i + 1);
  paintTodo(item);
}

function submitAddTodo(event) {
  event.preventDefault();
  let TODO = window.localStorage.getItem("TODO");
  if (!TODO) {
    TODO = JSON.stringify([]);
  }
  let New_TODO = JSON.parse(TODO);
  New_TODO.push(todothings.value);
  window.localStorage.setItem("TODO", JSON.stringify(New_TODO));

  paintTodo(todothings.value);
  todothings.value = "";
}

todoForm.addEventListener("submit", submitAddTodo);

function paintTodo(item) {
  let li1 = document.createElement("li");
  li1.innerHTML = item;
  let button1 = document.createElement("button");
  button1.innerHTML = "삭제";
  todoList.appendChild(li1);
  li1.appendChild(button1);
  button1.addEventListener("click", () => deleteTodo(li1));
}

function deleteTodo(li) {
  li.remove();
  let innertext = li.innerHTML;
  let value = innertext.slice(0, -19);
  let k = 0;
  let array = JSON.parse(window.localStorage.getItem("TODO"));
  let new_array = array.filter((e) => e !== value);
  console.log(new_array);
  window.localStorage.setItem("TODO", JSON.stringify(new_array));
}
