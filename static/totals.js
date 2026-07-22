const typeToId = {
    groceries: "tot_groc",
    gas: "tot_gas",
    restaurants: "tot_rest",
    food_delivery: "tot_food_del",
    transportation: "tot_transport",
    subscriptions: "tot_subs",
    entertainment: "tot_ent",
    income: "tot_income",
    health_personal: "tot_health",
    travel: "tot_travel",
    transfers: "tot_transfers",
    other: "tot_other",
    Total: "tot_all"
}

async function getTotals() {
    let response = await fetch('/api/totals')
    let totals = await response.json()
    for (row of totals) {
        let id = typeToId[row.Type]
        if (!id) continue
        let cell = document.getElementById(id)
        cell.textContent = `$${row.Total.toFixed(2)}`
    }
}

getTotals()
