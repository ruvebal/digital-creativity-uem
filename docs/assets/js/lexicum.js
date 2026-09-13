(() => {
  const root = document.querySelector("[data-lexicum]");
  if (!root) return;

  const search = root.querySelector("[data-lexicum-search]");
  const filters = [...root.querySelectorAll("[data-lexicum-filter]")];
  const concepts = [...root.querySelectorAll("[data-lexicum-concept]")];
  const empty = root.querySelector("[data-lexicum-empty]");
  let activeScheme = "all";

  const normalize = (value) =>
    (value || "")
      .toString()
      .normalize("NFD")
      .replace(/[\u0300-\u036f]/g, "")
      .toLowerCase();

  const apply = () => {
    const q = normalize(search ? search.value : "");
    let visible = 0;
    for (const card of concepts) {
      const scheme = card.getAttribute("data-scheme") || "";
      const hay = normalize(card.getAttribute("data-search") || card.textContent);
      const schemeOk = activeScheme === "all" || scheme === activeScheme;
      const queryOk = !q || hay.includes(q);
      const show = schemeOk && queryOk;
      card.classList.toggle("is-hidden", !show);
      if (show) visible += 1;
    }
    if (empty) empty.classList.toggle("is-visible", visible === 0);
  };

  for (const btn of filters) {
    btn.addEventListener("click", () => {
      activeScheme = btn.getAttribute("data-lexicum-filter") || "all";
      for (const other of filters) {
        other.setAttribute(
          "aria-pressed",
          other === btn ? "true" : "false"
        );
      }
      apply();
    });
  }

  if (search) {
    search.addEventListener("input", apply);
  }

  apply();
})();
