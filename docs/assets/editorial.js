/* Progressive enhancements: the complete source content remains readable without JS. */
const sections = [...document.querySelectorAll('h2[id]')];
if ('IntersectionObserver' in window) {
  const observer = new IntersectionObserver(entries => {
    for (const entry of entries) if (entry.isIntersecting) {
      document.querySelectorAll('.chapter-nav a').forEach(a => {
        const active = a.hash === '#' + entry.target.id;
        a.classList.toggle('active', active);
        if (active) a.setAttribute('aria-current', 'location');
        else a.removeAttribute('aria-current');
      });
    }
  }, { rootMargin: '-5% 0px -65% 0px' });
  sections.forEach(h => observer.observe(h));
}
const isCatalog = document.title.includes('道具属性');
document.querySelectorAll('table').forEach(table => {
  if (isCatalog && table.tHead) {
    const headers = [...table.tHead.querySelectorAll('th')].map(h => h.textContent.trim());
    const catalog = document.createElement('div'); catalog.className = 'item-catalog';
    [...table.tBodies].flatMap(body => [...body.rows]).forEach(row => {
      const card = document.createElement('article'); card.className = 'item-card';
      const title = document.createElement('h4'); title.innerHTML = row.cells[0].innerHTML;
      const list = document.createElement('dl');
      [...row.cells].slice(1).forEach((cell, i) => {
        const term = document.createElement('dt'); term.textContent = headers[i + 1] || '说明';
        const value = document.createElement('dd'); value.innerHTML = cell.innerHTML;
        list.append(term, value);
      });
      card.append(title, list); catalog.append(card);
    });
    table.replaceWith(catalog);
  } else {
    const wrapper = document.createElement('div'); wrapper.className = 'table-scroll';
    wrapper.tabIndex = 0; wrapper.setAttribute('role', 'region');
    wrapper.setAttribute('aria-label', '资料表格，可横向滚动');
    table.before(wrapper); wrapper.append(table);
  }
});
// Group adjacent topical blocks into a spread instead of a single text column.
if (!isCatalog) document.querySelectorAll('.research .band > .page').forEach(page => {
  const blocks = [...page.children].filter(el => el.matches('.section, .sec'));
  if (blocks.length >= 2 && blocks.every(el => !el.querySelector('table'))) {
    const grid = document.createElement('div'); grid.className = 'topic-grid';
    blocks[0].before(grid); blocks.forEach(el => grid.append(el));
  }
});
if (isCatalog) {
  const tools = document.createElement('div'); tools.className = 'catalog-tools';
  const input = document.createElement('input'); input.type = 'search';
  input.placeholder = '搜索道具、功能或获取方式…'; input.setAttribute('aria-label', '搜索道具资料');
  const output = document.createElement('output'); output.setAttribute('aria-live', 'polite');
  const empty = document.createElement('p'); empty.className = 'empty-results';
  empty.textContent = '没有匹配的资料，试试其他关键词。'; empty.hidden = true;
  tools.append(input, output); document.querySelector('.hero').append(tools, empty);
  const cards = [...document.querySelectorAll('.item-card')];
  const filter = () => {
    const query = input.value.trim().toLocaleLowerCase(); let count = 0;
    cards.forEach(card => { card.hidden = !card.textContent.toLocaleLowerCase().includes(query); if (!card.hidden) count++; });
    output.textContent = `${count} / ${cards.length} 条资料`; empty.hidden = count !== 0;
  };
  input.addEventListener('input', filter); filter();
}
