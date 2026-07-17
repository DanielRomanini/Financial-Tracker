


async function getTransactions() {
    let url = '/api' + window.location.pathname
    let response = await fetch(url)
    let transactions = await response.json()
    for (dict of transactions){
        let row = document.createElement('tr') //creates row
        for (keyword in dict){
            let cell = document.createElement('td') //creates cell
            cell.textContent = dict[keyword] //adds value to cell
            row.appendChild(cell) //actually adds the cell to the row
        }
        let temp = document.getElementById('transrows') 
        temp.appendChild(row)// actually adds row to table
    }
}
    getTransactions()
