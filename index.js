window.addEventListener('DOMContentLoaded', fetchData)

const adviceId = document.getElementById('advice-id')
const adviceBody = document.getElementById('advice-body')
const dice = document.getElementById('dice')


// functions
async function fetchData () {
  let response = await fetch('https://api.adviceslip.com/advice')
  let data = await response.json()
  let dataObj = data.slip

  adviceId.innerText = `ADVICE #${dataObj.id}`
  adviceBody.innerText = `"${dataObj.advice}"`
}

dice.addEventListener ('click', fetchData)


