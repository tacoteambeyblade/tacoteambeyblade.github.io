import BLADERS from "../data/bladers.json" with { type: "json"}

function sortRanking(){
    // ... spread operator to not modify the original values
    // uses - due sort only uses positive and negative values not booleans
    const bladers = BLADERS["bladers"]
    const ranking = [...bladers].sort((a,b) => b.score_tr - a.score_tr)

    const container = document.getElementById("ranking");

    ranking.forEach((blader, index) =>{
        console.log(`${index+1}. ${blader.names[0]} -> ${blader.score_tr}`)
    })

    let shared_ranking = []
    let curent = 1
    let past = null 

    ranking.forEach((blader, index) => {
        // Validation to avoid bladers with 0pts (0pts means blader not registered) 
        if(blader.score_tr <= 0) return

        if(blader.score_tr !== past){
            curent = index+1
            past = blader.score_tr
        }

        shared_ranking.push({curent, ...blader})

        // Creates the dom elements
        const item = document.createElement("div");
        item.classList.add("blader");

        item.innerHTML = `
            <strong>${curent}. ${blader.names[0].toUpperCase()}</strong>
            <span>${blader.score_tr} pts</span>
        `;

        container.appendChild(item);
    })

    
}

sortRanking()