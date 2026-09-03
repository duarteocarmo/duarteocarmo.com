(() => {
  const toc = document.querySelector(".article-toc");
  const prose = document.querySelector("article .prose");
  const headings = [...(prose?.querySelectorAll("h2") ?? [])];

  for (const table of prose?.querySelectorAll("table") ?? []) {
    if (table.parentElement.classList.contains("table-scroll")) continue;
    const wrapper = document.createElement("div");
    wrapper.className = "table-scroll";
    table.parentElement.insertBefore(wrapper, table);
    wrapper.append(table);
  }

  for (const [index, wrapper] of [
    ...(prose?.querySelectorAll(".table-scroll") ?? []),
  ].entries()) {
    const firstHeader = wrapper.querySelector("th")?.textContent.trim();
    wrapper.tabIndex = 0;
    wrapper.setAttribute("role", "region");
    wrapper.setAttribute(
      "aria-label",
      firstHeader ? `${firstHeader} table` : `Data table ${index + 1}`,
    );
  }

  if (!toc || headings.length < 2) return;

  const list = toc.querySelector("ol");
  const links = new Map();

  headings.forEach((heading, index) => {
    heading.id ||= `section-${index + 1}`;
    const item = document.createElement("li");
    const link = document.createElement("a");
    link.href = `#${heading.id}`;
    link.textContent = heading.textContent;
    item.append(link);
    list.append(item);
    links.set(heading, link);
  });

  const updateActiveLink = () => {
    let activeHeading = headings[0];
    for (const heading of headings) {
      if (heading.getBoundingClientRect().top > 160) break;
      activeHeading = heading;
    }

    for (const [heading, link] of links) {
      const isActive = heading === activeHeading;
      link.classList.toggle("active", isActive);
      if (isActive) link.setAttribute("aria-current", "location");
      else link.removeAttribute("aria-current");
    }
  };

  toc.hidden = false;
  updateActiveLink();
  window.addEventListener("scroll", updateActiveLink, { passive: true });
})();
