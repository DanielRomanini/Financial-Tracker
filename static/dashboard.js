
let groctot = document.querySelector("#tot_groc")
groctot.addEventListener('click',function(event){
    window.location.href = '/transactions/groceries'
})

let gastot = document.querySelector("#tot_gas")
gastot.addEventListener('click',function(event){
    window.location.href = '/transactions/gas'
})

let resttot = document.querySelector("#tot_rest")
resttot.addEventListener('click',function(event){
    window.location.href = '/transactions/restaurants'
})

let fooddeltot = document.querySelector("#tot_food_del")
fooddeltot.addEventListener('click',function(event){
    window.location.href = '/transactions/food_delivery'
})

let transporttot = document.querySelector("#tot_transport")
transporttot.addEventListener('click',function(event){
    window.location.href = '/transactions/transportation'
})

let substot = document.querySelector("#tot_subs")
substot.addEventListener('click',function(event){
    window.location.href = '/transactions/subscriptions'
})

let enttot = document.querySelector("#tot_ent")
enttot.addEventListener('click',function(event){
    window.location.href = '/transactions/entertainment'
})

let incometot = document.querySelector("#tot_income")
incometot.addEventListener('click',function(event){
    window.location.href = '/transactions/income'
})

let healthtot = document.querySelector("#tot_health")
healthtot.addEventListener('click',function(event){
    window.location.href = '/transactions/health_personal'
})

let traveltot = document.querySelector("#tot_travel")
traveltot.addEventListener('click',function(event){
    window.location.href = '/transactions/travel'
})

let transferstot = document.querySelector("#tot_transfers")
transferstot.addEventListener('click',function(event){
    window.location.href = '/transactions/transfers'
})

let othertot = document.querySelector("#tot_other")
othertot.addEventListener('click',function(event){
    window.location.href = '/transactions/other'
})