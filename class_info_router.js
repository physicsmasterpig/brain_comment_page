// index.js
import createRouter from "./router.js";

const container = document.querySelector("main")
const pages = {
 class1: () => document.getElementById("asdf").innerText = "class1",
 class2: () => document.getElementById("asdf").innerText  = "class2",
}

const router = createRouter();

router.addRoute("#/class1", pages.class1)
     .addRoute("#/class2", pages.class2)
     .start();

window.addEventListener("click", event => {
   if(event.target.matches("[data-navigate]")) {
      router.navigate(event.target.dataset.navigate);
    }  });
