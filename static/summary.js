async function getSummary() {
    let response = await fetch('/api/summary')
    let summary = await response.json()
    let grid = document.getElementById('summaryGrid')
    for (entry of summary) {
        let label = Object.keys(entry)[0]
        let value = entry[label]
        let card = document.createElement('div')
        card.className = 'summary-card'
        card.innerHTML = `<p class="summary-label">${label}</p><p class="summary-value">$${value.toFixed(2)}</p>`
        grid.appendChild(card)
    }
}

getSummary()
