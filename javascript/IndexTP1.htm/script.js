const container = document.getElementById("container");

      function createComposant() {
        const composant = document.createElement("div");
        composant.classList.add("composant");

        const head = document.createElement("div");
        head.classList.add("composant_head");

        const corbeille = document.createElement("button");
        corbeille.id = "Corbeille";
        corbeille.innerHTML = "<i class='fas fa-trash-alt'></i>Corbeille";
        head.appendChild(corbeille);

        const editeur = document.createElement("button");
        editeur.id = "Editeur";
        editeur.innerHTML = "<i class='fas fa-edit'></i>Editeur";
        head.appendChild(editeur);

        const body = document.createElement("div");
        body.classList.add("composant_body");
        body.setAttribute("contenteditable", "true");

        composant.appendChild(head);
        composant.appendChild(body);
        container.appendChild(composant);

        corbeille.addEventListener("click", () => {
        container.textContent = "";
        });

        editeur.addEventListener("click", () => {
          const isEditable = body.getAttribute("contenteditable") === "true";
          body.setAttribute("contenteditable", !isEditable);
        });
      }

      const addNew = document.createElement("button");
      addNew.innerHTML = "AddNew";
      addNew.style.margin = "1rem";
      addNew.addEventListener("click", createComposant);

      container.insertAdjacentElement("beforebegin", addNew);